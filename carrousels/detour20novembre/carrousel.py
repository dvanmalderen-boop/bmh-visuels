# -*- coding: utf-8 -*-
"""
BMH - carrousel du 20 novembre 2026.  FORMAT TIKTOK 1080 x 1920.

UN SEUL PARFUM : AL HARAMAIN DETOUR NOIR INTENSE.

Demande de Daoud le 20/11 : « un carrousel comme tu as fait avec Bring
Medina Home en grand, 4-5 diapos, tu choisis la bouteille. »

POURQUOI CELUI-LA
Sa propre fiche le dit : « le meilleur rapport qualite-prix de toute la
selection Al Haramain ». 31,90 EUR, 23 en stock, parfaitement unisexe, et
c'est un parfum d'automne et d'hiver — on est le 20 novembre. Tout le texte
des diapos est repris de la fiche de la boutique, pas invente.

CINQ DIAPOS : couverture, les notes, pourquoi celui-la, la carte de marque,
le prix. Largement sous la limite de 10 de l'API Instagram.
"""

from socle import *            # noqa
from socle import (W, H, CREME, OCRE, BLANC, LIEN, MARGE_G, MARGE_D, LARGE,
                   LANGUES, MAX_DIAPOS, serif, inter, couper, caps_multi,
                   caps_auto, bloc_ajuste, lettrage, poser_signature,
                   poser_visage, voile, plein_cadre, VOILE_COUV, SORTIE)
import os
import sys
from PIL import ImageDraw

EAN = "6291106813838"

#  Releve dans Shopify le 20/11/2026 : prix, stock et fiche.
PRIX = 31.90
ML = 100
STOCK = 23

#  Les notes sont celles publiees sur la fiche, dans l'ordre de la fiche.
#  On ne les reecrit pas, on ne les resume pas.
NOTES = {
 "fr": [("TÊTE", "Cardamome, héliotrope, poivre rose"),
        ("CŒUR", "Amande amère, lavande, géranium, jasmin"),
        ("FOND", "Vanille, bois de gaïac, oud, bois de santal, ambre")],
 "en": [("TOP", "Cardamom, heliotrope, pink pepper"),
        ("HEART", "Bitter almond, lavender, geranium, jasmine"),
        ("BASE", "Vanilla, guaiac wood, oud, sandalwood, amber")],
 "nl": [("KOP", "Kardemom, heliotroop, roze peper"),
        ("HART", "Bittere amandel, lavendel, geranium, jasmijn"),
        ("BASIS", "Vanille, guajakhout, oud, sandelhout, amber")],
 "de": [("KOPF", "Kardamom, Heliotrop, rosa Pfeffer"),
        ("HERZ", "Bittermandel, Lavendel, Geranie, Jasmin"),
        ("BASIS", "Vanille, Guajakholz, Oud, Sandelholz, Amber")],
}

T = {
 "maison": "AL HARAMAIN",
 "nom": "Détour Noir Intense",
 "couv_s": {
   "fr": "Un boisé gourmand construit comme un parfum beaucoup plus cher.",
   "en": "A gourmand woody built like a far more expensive fragrance.",
   "nl": "Een gourmand houtgeur, gebouwd als een veel duurder parfum.",
   "de": "Ein gourmandiger Holzduft, gebaut wie ein viel teurerer Duft."},
 "notes_t": {"fr": "LES NOTES", "en": "THE NOTES",
             "nl": "DE NOTEN", "de": "DIE NOTEN"},
 "notes_sup": {"fr": "OUD ET BOIS PRÉCIEUX", "en": "OUD AND PRECIOUS WOODS",
               "nl": "OUD EN KOSTBARE HOUTSOORTEN",
               "de": "OUD UND EDELHÖLZER"},
 "pq_t": {"fr": "LE MEILLEUR\nRAPPORT\nQUALITÉ-PRIX\nDE LA MAISON",
          "en": "THE BEST\nVALUE IN\nTHE WHOLE\nHOUSE",
          "nl": "DE BESTE\nPRIJS-KWALITEIT\nVAN HET\nHELE HUIS",
          "de": "DAS BESTE\nPREIS-LEISTUNGS-\nVERHÄLTNIS\nDES HAUSES"},
 "pq_c": {
   "fr": "L'amande amère et la lavande ensemble, c'est l'accord qui signe "
         "les grands masculins modernes — posé ici sur un fond d'oud et de "
         "bois de gaïac. Soirée, automne et hiver, parfaitement unisexe. "
         "Deux pulvérisations suffisent largement.",
   "en": "Bitter almond and lavender together is the accord behind the great "
         "modern masculines — set here on a base of oud and guaiac wood. "
         "Evening, autumn and winter, perfectly unisex. Two sprays are "
         "plenty.",
   "nl": "Bittere amandel en lavendel samen is het akkoord achter de grote "
         "moderne herengeuren — hier op een basis van oud en guajakhout. "
         "Avond, herfst en winter, volledig uniseks. Twee sprays zijn ruim "
         "voldoende.",
   "de": "Bittermandel und Lavendel zusammen sind der Akkord der großen "
         "modernen Herrendüfte — hier auf einer Basis aus Oud und "
         "Guajakholz. Abend, Herbst und Winter, vollkommen unisex. Zwei "
         "Sprühstöße genügen völlig."},
 "prix_sup": {"fr": "EAU DE PARFUM · 100 ML", "en": "EAU DE PARFUM · 100 ML",
              "nl": "EAU DE PARFUM · 100 ML", "de": "EAU DE PARFUM · 100 ML"},
 "prix_s": {
   "fr": "Expédié depuis l'Union européenne. Livraison 4,95 €, offerte dès "
         "70 €.",
   "en": "Shipped from the European Union. Delivery €4.95, free from €70.",
   "nl": "Verzonden vanuit de Europese Unie. Verzending € 4,95, gratis vanaf "
         "€ 70.",
   "de": "Versand aus der Europäischen Union. Lieferung 4,95 €, ab 70 € "
         "kostenlos."},
}


def euro(v, lg):
    e, c = ("%.2f" % v).split(".")
    if lg in ("fr", "de"):
        return "%s,%s €" % (e, c)
    if lg == "nl":
        return "€ %s,%s" % (e, c)
    return "€%s.%s" % (e, c)


def garde_fou():
    assert os.path.exists(os.path.join(RACINE, "scenes", EAN + "c.jpg")), \
        "scene manquante"
    assert STOCK >= 5, "stock trop bas pour mettre un parfum en avant"
    for lg in LANGUES:
        assert len(NOTES[lg]) == 3, "trois etages de notes attendus en " + lg
    #  Les notes publiees par la maison ne se reecrivent pas : on verifie que
    #  les matieres citees dans la diapo « pourquoi » existent bien dans les
    #  notes de la fiche.
    bas = " ".join(n for _, n in NOTES["fr"]).lower()
    for mot in ("amande amère", "lavande", "oud", "bois de gaïac"):
        assert mot in bas, "« %s » n'est pas dans les notes de la fiche" % mot
    print("garde-fou : %s %s, %.2f EUR, %d en stock, notes conformes a la "
          "fiche" % (T["maison"], T["nom"], PRIX, STOCK))


def diapo_couverture(lg):
    img = voile(plein_cadre(EAN), haut=VOILE_COUV)
    d = ImageDraw.Draw(img)
    lettrage(d, 262, T["maison"], inter(30, "SemiBold"), OCRE, 8)
    y = bloc_ajuste(d, MARGE_G, 400, [T["nom"]], 112, BLANC, LARGE, 760,
                    interligne=1.02, poids=620)
    d.line([(MARGE_G, y + 34), (MARGE_G + 180, y + 34)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 80, [T["couv_s"][lg]], 44, CREME, LARGE,
                1180, ital=True)
    poser_visage(img)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_notes(lg):
    img = voile(plein_cadre(EAN),
                haut=[(0, 240), (1120, 236), (1460, 140), (1800, 0)])
    d = ImageDraw.Draw(img)
    lettrage(d, 250, T["notes_sup"][lg], inter(26, "SemiBold"), OCRE, 6)
    y = caps_multi(d, MARGE_G, 316, T["notes_t"][lg], 86, BLANC, LARGE)
    y += 54
    for etage, liste in NOTES[lg]:
        d.text((MARGE_G, y), etage, font=inter(30, "Bold"), fill=OCRE)
        y = bloc_ajuste(d, MARGE_G, y + 48, [liste], 46, CREME, LARGE,
                        y + 230, ital=True) + 38
    assert y <= 1300, "les notes debordent (%d)" % y
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_pourquoi(lg):
    img = voile(plein_cadre(EAN),
                haut=[(0, 240), (1150, 236), (1500, 140), (1820, 0)])
    d = ImageDraw.Draw(img)
    y = caps_multi(d, MARGE_G, 300, T["pq_t"][lg], 78, BLANC, LARGE)
    d.line([(MARGE_G, y + 40), (MARGE_G + 180, y + 40)], fill=OCRE, width=5)
    fin = bloc_ajuste(d, MARGE_G, y + 90, [T["pq_c"][lg]], 44, CREME, LARGE,
                      1300, ital=True)
    assert fin <= 1340, "le texte deborde (%d)" % fin
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_marque(lg):
    """La carte de marque. Regle posee par Daoud le 19/11 : le nom en grand,
    trois lignes JUSTIFIEES a la meme largeur. Detail dans les fichiers du
    projet, claude/carte-de-marque.md."""
    #  Meme scene que le reste du carrousel. Sur un carrousel mono-produit,
    #  poser la carte de marque sur un AUTRE flacon fait croire a un second
    #  parfum : le flacon bleu d'Azzure Aoud se voyait derriere MEDINA.
    img = voile(plein_cadre(EAN),
                haut=[(0, 246), (1200, 243), (1540, 140), (1830, 0)])
    d = ImageDraw.Draw(img)
    mots = ("BRING", "MEDINA", "HOME")
    bloc = 820
    for corps in range(200, 60, -2):
        p = inter(corps, "Bold")
        if max(sum(d.textlength(c, font=p) for c in m) for m in mots) <= bloc:
            break
    y = 430
    for m in mots:
        p = inter(corps, "Bold")
        brut = sum(d.textlength(c, font=p) for c in m)
        espace = (bloc - brut) / float(len(m) - 1)
        x = MARGE_G
        for c in m:
            d.text((x, y), c, font=p, fill=BLANC)
            x += d.textlength(c, font=p) + espace
        if m == "HOME":
            d.text((MARGE_G + bloc + 14, y + corps * 0.10), "®",
                   font=inter(int(corps * 0.26), "Medium"), fill=OCRE)
        y += int(corps * 1.12)
    d.line([(MARGE_G, y + 40), (MARGE_G + bloc, y + 40)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 92, ["279 parfums · 27 maisons d'Arabie"],
                48, CREME, bloc, y + 220, ital=True)
    return img


def diapo_prix(lg):
    img = voile(plein_cadre(EAN), haut=VOILE_COUV)
    d = ImageDraw.Draw(img)
    lettrage(d, 262, T["prix_sup"][lg], inter(28, "SemiBold"), OCRE, 7)
    y = bloc_ajuste(d, MARGE_G, 340, [T["nom"]], 68, CREME, LARGE, 520,
                    poids=560)
    d.text((MARGE_G, y + 24), euro(PRIX, lg), font=inter(150, "Bold"),
           fill=BLANC)
    y += 24 + 180
    d.line([(MARGE_G, y + 20), (MARGE_G + 180, y + 20)], fill=OCRE, width=5)
    y = bloc_ajuste(d, MARGE_G, y + 66, [T["prix_s"][lg]], 40, CREME, LARGE,
                    1240, ital=True)
    d.text((MARGE_G, y + 40), LIEN, font=inter(42, "Bold"), fill=CREME)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def main():
    garde_fou()
    lg = (sys.argv[1] if len(sys.argv) > 1 else "fr").lower()
    assert lg in LANGUES, "langue inconnue : " + lg
    dossier = os.path.join(SORTIE, lg)
    os.makedirs(dossier, exist_ok=True)
    pages = [diapo_couverture(lg), diapo_notes(lg), diapo_pourquoi(lg),
             diapo_marque(lg), diapo_prix(lg)]
    assert len(pages) <= MAX_DIAPOS, \
        "Instagram coupe au-dela de %d : %d diapos" % (MAX_DIAPOS, len(pages))
    assert len(pages) == 5, "cinq diapos attendues, %d" % len(pages)
    for i, im in enumerate(pages, 1):
        im.save(os.path.join(dossier, "d%02d.jpg" % i), quality=90,
                optimize=True)
    print("%s : %d diapos ecrites dans %s" % (lg, len(pages), dossier))


if __name__ == "__main__":
    main()
