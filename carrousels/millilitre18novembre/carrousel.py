# -*- coding: utf-8 -*-
"""
BMH - carrousel du 18 novembre 2026.  FORMAT TIKTOK 1080 x 1920.

MECANIQUE : LE PRIX AU MILLILITRE.

POURQUOI CELUI-LA
Releve Metricool du 18/11 sur les quatre comptes : les vues s'ecroulent de
moitie chaque nuit (FR 376 -> 256 -> 197 -> 122). UNE SEULE chose est montee :
le taux d'engagement du 17/11, 9,4 % sur la portee, contre 2,5 % et 3,0 % les
deux soirs d'avant, et c'est le seul post qui ait recolte des
enregistrements. Ce qui a change ce soir-la : DEUX NOMBRES opposes des la
couverture. On garde le crochet, on change la mecanique.

CE QU'ON NE REFAIT PAS : le dupe. Regle de variation, et surtout le dupe
depend d'une source exterieure qu'il faut aller chercher. Ici tout vient de
la boutique : rien a verifier ailleurs, rien a inventer.

LE CROCHET
Le flacon le moins cher de la liste, Ayat Creek Dubai a 21,90 EUR, est le
parfum LE PLUS CHER des huit au millilitre : 0,73 EUR. Et le flacon le plus
gros, Armaf Le Parfait a 33,90 EUR, est le moins cher : 0,17 EUR. C'est vrai,
c'est verifiable par le lecteur sur la boutique, et ca lui sert.

L'HONNETETE DU FORMAT
Comparer des EUR/ml entre concentrations differentes n'a pas de sens : un
extrait est plus concentre, donc plus cher au millilitre, et c'est normal.
LES HUIT SONT DONC TOUS DES EAUX DE PARFUM, et la diapo 2 le dit. Huit
maisons differentes, aucune citee deux fois.

PRIX ET STOCKS RELEVES EN DIRECT DANS SHOPIFY LE 18/11/2026.

ZONES TIKTOK : 150 px en haut, 480 px en bas, 120 px a droite sont manges
par l'interface. Tout le texte vit entre y=200 et y=1400.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

W, H    = 1080, 1920
RACINE  = "/home/claude/millilitre"
SCENES  = os.path.join(RACINE, "scenes")
POLICES = "/home/claude/polices"
SORTIE  = os.path.join(RACINE, "carrousel")
VISAGE  = os.path.join(RACINE, "daoud.png")

CREME   = (240, 228, 206)
OCRE    = (181, 85, 31)
BLANC   = (255, 255, 255)
NUIT    = (20, 14, 10)
GRIS    = (168, 152, 130)

LIEN = "shop.bringmedinahome.com"

MARGE_G, MARGE_D = 88, 180
LARGE = W - MARGE_G - MARGE_D

LANGUES = ("fr", "en", "nl", "de")

# --------------------------------------------------------------- polices


def serif(corps, poids=600, opsz=72, ital=False):
    f = ImageFont.truetype(os.path.join(
        POLICES, "Newsreader-Italic.ttf" if ital else "Newsreader.ttf"), corps)
    f.set_variation_by_axes([poids, opsz])
    return f


def inter(corps, graisse="Medium"):
    return ImageFont.truetype(
        "/usr/share/fonts/opentype/inter/Inter-%s.otf" % graisse, corps)


def couper(d, texte, police, lmax):
    mots, lignes, cour = texte.split(), [], ""
    for m in mots:
        essai = (cour + " " + m).strip()
        if d.textlength(essai, font=police) <= lmax:
            cour = essai
        else:
            if cour:
                lignes.append(cour)
            cour = m
    if cour:
        lignes.append(cour)
    return lignes


def caps_multi(d, x, y, texte, corps, couleur, lmax, interligne=1.08):
    """Capitales dont les retours a la ligne sont ecrits a la main.
    Toutes les lignes gardent la meme taille, sinon le bloc part en
    escalier."""
    for c in range(corps, 35, -4):
        p = inter(c, "Bold")
        if all(d.textlength(l, font=p) <= lmax for l in texte.split("\n")):
            break
    for l in texte.split("\n"):
        d.text((x, y), l, font=p, fill=couleur)
        y += int(c * interligne)
    return y


def bloc_ajuste(d, x, y, textes, corps, couleur, lmax, y_max,
                interligne=1.22, poids=430, ital=False, mini=22):
    if isinstance(textes, str):
        textes = [textes]
    for c in range(corps, mini - 1, -2):
        p = serif(c, poids, 72, ital)
        h = sum(len(couper(d, t, p, lmax)) * int(p.size * interligne)
                for t in textes)
        if y + h <= y_max:
            break
    for t in textes:
        for l in couper(d, t, p, lmax):
            d.text((x, y), l, font=p, fill=couleur)
            y += int(p.size * interligne)
    return y


def lettrage(d, y, texte, police, couleur, espace=6, x=MARGE_G):
    for c in texte:
        d.text((x, y), c, font=police, fill=couleur, anchor="lm")
        x += d.textlength(c, font=police) + espace

# ---------------------------------------------------------------- marque


def poser_signature(img, x, y, couleur, corps=28, espace=6):
    r = int(corps * 0.52)
    t = r * 2 + 2
    lune = Image.new("L", (t * 4, t * 4), 0)
    dl = ImageDraw.Draw(lune)
    R = r * 4
    dl.ellipse([2, 2, 2 + R * 2, 2 + R * 2], fill=255)
    dec = int(R * 0.52)
    dl.ellipse([2 + dec, 2 - R * 0.06, 2 + dec + R * 2, 2 - R * 0.06 + R * 2],
               fill=0)
    lune = lune.resize((t, t), Image.LANCZOS)
    img.paste(Image.new("RGB", (t, t), couleur), (int(x), int(y - t / 2)), lune)
    d = ImageDraw.Draw(img)
    cx = x + t + corps * 0.75
    p = inter(corps, "SemiBold")
    for c in "BRING MEDINA HOME":
        d.text((cx, y), c, font=p, fill=couleur, anchor="lm")
        cx += d.textlength(c, font=p) + espace
    d.text((cx - espace + 4, y - corps * 0.42), "®",
           font=inter(int(corps * 0.55), "Medium"), fill=couleur, anchor="lm")


def poser_visage(img, cote=190, y=162):
    if not os.path.exists(VISAGE):
        return img
    v = Image.open(VISAGE).convert("RGBA").resize((cote, cote), Image.LANCZOS)
    x = W - MARGE_D - cote
    ImageDraw.Draw(img).ellipse([x - 5, y - 5, x + cote + 5, y + cote + 5],
                                outline=OCRE, width=5)
    img.paste(v, (x, y), v)
    return img

# ------------------------------------------------------- fond plein cadre

#  Position horizontale du flacon, relevee a l'oeil sur une planche-contact
#  des huit scenes (18/11). Jamais devinee a partir du numero.
CX = {
 "6294015163988": 0.62,  # Armaf Le Parfait
 "6290171002079": 0.58,  # Afnan Inara
 "5055810038991": 0.63,  # Al Wataniah Muheeb
 "6290360379128": 0.75,  # Fragrance World Elysia Pista Sundae
 "6298141926707": 0.62,  # Emir Voux Violette
 "6291106813838": 0.60,  # Al Haramain Detour Noir Intense
 "6290360375687": 0.58,  # French Avenue Azzure Aoud
 "5060908999146": 0.63,  # Ayat Creek Dubai
}

#  Voiles : des points d'arret releves a l'oeil, pas une formule. Le haut
#  porte le nombre, le bas porte la maison et le prix ; entre les deux on
#  laisse le flacon respirer.
VOILE_HAUT = [(0, 232), (420, 222), (720, 110), (1000, 0)]
VOILE_BAS  = [(900, 0), (1060, 150), (1180, 214), (1320, 242), (1920, 248)]
VOILE_COUV = [(0, 234), (580, 228), (920, 160), (1280, 0)]


def rampe(points):
    m = Image.new("L", (1, H), 0)
    px = m.load()
    for i in range(len(points) - 1):
        (y0, v0), (y1, v1) = points[i], points[i + 1]
        for y in range(max(0, y0), min(H, y1)):
            t = (y - y0) / float(y1 - y0)
            px[0, y] = max(px[0, y], int(v0 + (v1 - v0) * t))
    for y in range(points[-1][0], H):
        px[0, y] = max(px[0, y], points[-1][1])
    return m


def voile(img, haut=None, bas=None):
    m = Image.new("L", (1, H), 0)
    mp = m.load()
    for src in (haut or VOILE_HAUT, bas or VOILE_BAS):
        rp = rampe(src).load()
        for y in range(H):
            mp[0, y] = max(mp[0, y], rp[0, y])
    img.paste(Image.new("RGB", (W, H), (0, 0, 0)),
              (0, 0), m.resize((W, H), Image.BILINEAR))
    return img


def plein_cadre(ean):
    im = Image.open(os.path.join(SCENES, ean + "c.jpg")).convert("RGB")
    e = H / im.height
    im = im.resize((int(im.width * e), H), Image.LANCZOS)
    x = max(0, min(int(CX[ean] * im.width - W / 2), im.width - W))
    return im.crop((x, 0, x + W, H))


def nuit():
    img = Image.new("RGB", (W, H), NUIT)
    return img, ImageDraw.Draw(img)

# ------------------------------------------------------------- les nombres


def euro(v, lg, dec=2):
    s = ("%." + str(dec) + "f") % v
    e, c = s.split(".")
    if lg in ("fr", "de"):
        return "%s,%s €" % (e, c)
    if lg == "nl":
        return "€ %s,%s" % (e, c)
    return "€%s.%s" % (e, c)


def format_flacon(pf, lg):
    return "%s · %d ml" % (euro(pf["prix"], lg), pf["ml"])

# --------------------------------------------------------------- contenu
#
#  Prix, volumes et stocks RELEVES EN DIRECT DANS SHOPIFY LE 18/11/2026.
#  marge = marge brute du garde-fou ; net sur une commande d'un flacon =
#  marge - 4,85 EUR.

PARFUMS = [
 {"ean": "6294015163988", "maison": "ARMAF", "nom": "Le Parfait",
  "prix": 33.90, "ml": 200, "stock": 5, "marge": 10.35},
 {"ean": "6290171002079", "maison": "AFNAN", "nom": "Inara",
  "prix": 22.90, "ml": 100, "stock": 17, "marge": 10.05},
 {"ean": "5055810038991", "maison": "AL WATANIAH", "nom": "Muheeb",
  "prix": 24.90, "ml": 100, "stock": 23, "marge": 10.26},
 {"ean": "6290360379128", "maison": "FRAGRANCE WORLD",
  "nom": "Elysia Pista Sundae",
  "prix": 25.90, "ml": 100, "stock": 11, "marge": 9.89},
 {"ean": "6298141926707", "maison": "EMIR", "nom": "Voux Violette",
  "prix": 28.90, "ml": 100, "stock": 22, "marge": 9.95},
 {"ean": "6291106813838", "maison": "AL HARAMAIN",
  "nom": "Détour Noir Intense",
  "prix": 31.90, "ml": 100, "stock": 23, "marge": 9.94},
 {"ean": "6290360375687", "maison": "FRENCH AVENUE", "nom": "Azzure Aoud",
  "prix": 36.90, "ml": 100, "stock": 85, "marge": 10.08},
 {"ean": "5060908999146", "maison": "AYAT", "nom": "Creek Dubai",
  "prix": 21.90, "ml": 30, "stock": 8, "marge": 10.24},
]

for _p in PARFUMS:
    _p["ml_prix"] = _p["prix"] / _p["ml"]

#  Une phrase seulement sur les deux extremes. Au milieu, le nombre parle
#  tout seul.
PHRASES = {
 "6294015163988": {
   "fr": "Le moins cher au millilitre de nos 279 parfums.",
   "en": "The lowest price per millilitre of our 279 fragrances.",
   "nl": "De laagste prijs per milliliter van onze 279 geuren.",
   "de": "Der niedrigste Preis pro Milliliter unserer 279 Düfte."},
 "5060908999146": {
   "fr": "Le flacon le moins cher de la liste. Un 30 ml sert à essayer, "
         "pas à durer.",
   "en": "The cheapest bottle on the list. A 30 ml is for trying, "
         "not for lasting.",
   "nl": "Het goedkoopste flesje van de lijst. Een 30 ml is om te proberen, "
         "niet om lang mee te doen.",
   "de": "Der günstigste Flakon der Liste. Ein 30 ml ist zum Ausprobieren, "
         "nicht für die Dauer."},
}

T = {
 "sup": {"fr": "LE PRIX AU MILLILITRE", "en": "THE PRICE PER MILLILITRE",
         "nl": "DE PRIJS PER MILLILITER", "de": "DER PREIS PRO MILLILITER"},
 "couv_t": {"fr": "21,90 €\nC'EST LE\nPLUS CHER",
            "en": "€21.90\nIS THE MOST\nEXPENSIVE",
            "nl": "€ 21,90\nIS DE\nDUURSTE",
            "de": "21,90 €\nIST DER\nTEUERSTE"},
 "couv_s": {
   "fr": "C'est le flacon le moins cher de cette liste. Et c'est le parfum "
         "le plus cher des huit. Je te montre pourquoi.",
   "en": "It is the cheapest bottle on this list. And the most expensive "
         "fragrance of the eight. Let me show you why.",
   "nl": "Het is het goedkoopste flesje van deze lijst. En de duurste geur "
         "van de acht. Ik laat je zien waarom.",
   "de": "Es ist der günstigste Flakon dieser Liste. Und der teuerste Duft "
         "der acht. Ich zeige Ihnen, warum."},
 "regle_t": {"fr": "ON REGARDE\nLE FLACON.\nJAMAIS LE\nMILLILITRE.",
             "en": "WE LOOK AT\nTHE BOTTLE.\nNEVER AT THE\nMILLILITRE.",
             "nl": "WE KIJKEN NAAR\nHET FLESJE.\nNOOIT NAAR DE\nMILLILITER.",
             "de": "WIR SCHAUEN AUF\nDEN FLAKON.\nNIE AUF DEN\nMILLILITER."},
 "regle_c": {
   "fr": "Le prix divisé par le volume. Les huit sont des eaux de parfum, "
         "même concentration, donc comparables entre elles. Les prix sont "
         "ceux de la boutique aujourd'hui, le 18 novembre 2026, arrondis au "
         "centime. Huit maisons, aucune deux fois.",
   "en": "The price divided by the volume. All eight are eaux de parfum, "
         "the same concentration, so they can be compared. The prices are "
         "the shop's prices today, 18 November 2026, rounded to the cent. "
         "Eight houses, none of them twice.",
   "nl": "De prijs gedeeld door de inhoud. Alle acht zijn eaux de parfum, "
         "dezelfde concentratie, dus onderling vergelijkbaar. De prijzen "
         "zijn die van de winkel vandaag, 18 november 2026, afgerond op de "
         "cent. Acht huizen, geen enkel twee keer.",
   "de": "Der Preis geteilt durch den Inhalt. Alle acht sind Eaux de Parfum, "
         "gleiche Konzentration, also untereinander vergleichbar. Die Preise "
         "sind die des Shops heute, 18. November 2026, auf den Cent "
         "gerundet. Acht Häuser, keines zweimal."},
 "le_ml": {"fr": "LE MILLILITRE", "en": "PER MILLILITRE",
           "nl": "PER MILLILITER", "de": "PRO MILLILITER"},
 "recap_t": {"fr": "DU MOINS CHER\nAU PLUS CHER",
             "en": "FROM CHEAPEST\nTO DEAREST",
             "nl": "VAN GOEDKOOPST\nNAAR DUURST",
             "de": "VOM GÜNSTIGSTEN\nZUM TEUERSTEN"},
 "recap_s": {"fr": "Au millilitre. Les huit, en stock aujourd'hui.",
             "en": "Per millilitre. All eight, in stock today.",
             "nl": "Per milliliter. Alle acht, vandaag op voorraad.",
             "de": "Pro Milliliter. Alle acht, heute auf Lager."},
 "fin_t": {"fr": "ET LE TIEN,\nIL COÛTE\nCOMBIEN ?",
           "en": "AND YOURS,\nWHAT DOES\nIT COST?",
           "nl": "EN DE JOUWE,\nWAT KOST\nDIE?",
           "de": "UND IHRER,\nWAS KOSTET\nER?"},
 "fin_s": {
   "fr": "Prends ton flacon, divise le prix par le nombre de millilitres. "
         "Dis-moi ce que ça donne en commentaire.",
   "en": "Take your bottle, divide the price by the number of millilitres. "
         "Tell me what you get in the comments.",
   "nl": "Pak je flesje, deel de prijs door het aantal milliliter. Zeg me in "
         "de reacties wat eruit komt.",
   "de": "Nehmen Sie Ihren Flakon, teilen Sie den Preis durch die Milliliter. "
         "Schreiben Sie mir Ihr Ergebnis in die Kommentare."},
}

# ------------------------------------------------------------- garde-fou


def garde_fou():
    """Ce carrousel n'a qu'un argument : chaque nombre est verifiable sur la
    boutique. Un seul faux et tout tombe."""
    import json
    import re
    assert len(PARFUMS) == 8, "huit flacons attendus"
    assert len({p["maison"] for p in PARFUMS}) == 8, "huit maisons distinctes"
    for pf in PARFUMS:
        assert os.path.exists(os.path.join(SCENES, pf["ean"] + "c.jpg")), \
            "scene manquante : " + pf["ean"]
        assert pf["ean"] in CX, "cadrage non releve : " + pf["ean"]
        assert pf["stock"] >= 5, "%s n'a que %d" % (pf["nom"], pf["stock"])
        net = pf["marge"] - 4.85
        assert net >= 4.00, "%s sous le plancher : %.2f" % (pf["nom"], net)

    #  Le classement doit etre strictement croissant, sinon le carrousel
    #  raconte n'importe quoi.
    v = [p["ml_prix"] for p in PARFUMS]
    assert v == sorted(v), "les huit ne sont pas dans l'ordre croissant"

    #  Les deux affirmations de la couverture, verifiees sur les donnees.
    moins_cher = min(PARFUMS, key=lambda p: p["prix"])
    assert moins_cher["ean"] == "5060908999146", "le flacon le moins cher a change"
    assert moins_cher is PARFUMS[-1], "le flacon le moins cher n'est plus le plus cher au ml"
    assert abs(moins_cher["prix"] - 21.90) < 0.001, "21,90 EUR n'est plus le bon prix"

    #  « le moins cher au millilitre de nos 279 » : on le verifie sur tout le
    #  catalogue, pas sur les huit.
    chemin = "/home/claude/bmhsite/bts/rapports/marges.json"
    if os.path.exists(chemin):
        cat = json.load(open(chemin))
        pire = None
        for ean, p in cat.items():
            m = re.search(r"—\s*(.+?)\s+(\d+(?:[.,]\d+)?)\s*ml$", p.get("nom", ""))
            if not m or p.get("disponibilite") != "in_stock":
                continue
            r = p["vente"] / float(m.group(2).replace(",", "."))
            if pire is None or r < pire[0]:
                pire = (r, ean, p["nom"])
        assert pire and pire[1] == "6294015163988", \
            "Le Parfait n'est plus le moins cher au ml : " + str(pire)
        assert len(cat) >= 279, "le catalogue n'a plus 279 references"
        print("garde-fou : Le Parfait confirme le moins cher au ml sur "
              "%d references du catalogue" % len(cat))

    print("garde-fou : 8 maisons, ordre croissant de %s a %s, net de "
          "%.2f a %.2f EUR"
          % (euro(PARFUMS[0]["ml_prix"], "fr"), euro(PARFUMS[-1]["ml_prix"], "fr"),
             min(p["marge"] for p in PARFUMS) - 4.85,
             max(p["marge"] for p in PARFUMS) - 4.85))
    faible = [p["nom"] for p in PARFUMS if p["stock"] < 10]
    if faible:
        print("   ! stock sous 10 : " + ", ".join(faible))

# ------------------------------------------------------------------ diapos


def diapo_couverture(lg):
    img = voile(plein_cadre("5060908999146"), haut=VOILE_COUV)
    d = ImageDraw.Draw(img)
    lettrage(d, 262, T["sup"][lg], inter(30, "SemiBold"), OCRE, 8)
    y = caps_multi(d, MARGE_G, 420, T["couv_t"][lg], 100, BLANC, LARGE)
    d.line([(MARGE_G, y + 40), (MARGE_G + 180, y + 40)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 86, [T["couv_s"][lg]], 42, CREME, LARGE,
                1260, ital=True)
    poser_visage(img)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_regle(lg):
    img, d = nuit()
    d.text((W - MARGE_D, 250), "02", font=inter(30, "SemiBold"), fill=GRIS,
           anchor="rm")
    y = caps_multi(d, MARGE_G, 360, T["regle_t"][lg], 86, BLANC, LARGE)
    d.line([(MARGE_G, y + 46), (MARGE_G + 180, y + 46)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 104, [T["regle_c"][lg]], 44, CREME, LARGE,
                1400)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_parfum(pf, rang, lg):
    """Le nombre en haut, le flacon au milieu, la fiche en bas.
    La phrase n'existe que pour les deux extremes."""
    img = voile(plein_cadre(pf["ean"]))
    d = ImageDraw.Draw(img)
    d.text((W - MARGE_D, 250), "%02d" % rang, font=inter(30, "SemiBold"),
           fill=CREME, anchor="rm")
    lettrage(d, 250, T["le_ml"][lg], inter(30, "SemiBold"), OCRE, 8)

    #  Le nombre. C'est lui qu'on vient lire.
    d.text((MARGE_G, 318), euro(pf["ml_prix"], lg), font=inter(132, "Bold"),
           fill=BLANC)

    phr = PHRASES.get(pf["ean"])
    if phr:
        d.line([(MARGE_G, 500), (MARGE_G + 160, 500)], fill=OCRE, width=5)
        fin = bloc_ajuste(d, MARGE_G, 546, [phr[lg]], 44, CREME, LARGE, 760,
                          ital=True)
        assert fin <= 790, "la phrase descend sur le flacon (%d)" % fin

    d.text((MARGE_G, 1148), pf["maison"], font=inter(31, "SemiBold"), fill=OCRE)
    y = bloc_ajuste(d, MARGE_G, 1196, [pf["nom"]], 60, BLANC, LARGE, 1330)
    d.text((MARGE_G, y + 16), format_flacon(pf, lg), font=inter(44, "Bold"),
           fill=CREME)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_recap(lg):
    img, d = nuit()
    d.text((W - MARGE_D, 250), "11", font=inter(30, "SemiBold"), fill=GRIS,
           anchor="rm")
    y = caps_multi(d, MARGE_G, 318, T["recap_t"][lg], 76, BLANC, LARGE)
    d.line([(MARGE_G, y + 36), (MARGE_G + 160, y + 36)], fill=OCRE, width=4)
    y = bloc_ajuste(d, MARGE_G, y + 80, [T["recap_s"][lg]], 36, OCRE, LARGE,
                    y + 190, ital=True) + 40

    #  Deux colonnes : le nombre a gauche, le parfum a droite, aligne sur une
    #  largeur fixe pour que la colonne des noms ne danse pas.
    pn = inter(46, "Bold")
    colonne = max(d.textlength(euro(p["ml_prix"], lg), font=pn)
                  for p in PARFUMS) + 34
    for pf in PARFUMS:
        d.text((MARGE_G, y), euro(pf["ml_prix"], lg), font=pn, fill=OCRE)
        x = MARGE_G + colonne
        nom = pf["maison"].title() + " " + pf["nom"]
        for c in range(38, 23, -2):
            ps = serif(c, 500)
            if d.textlength(nom, font=ps) <= W - MARGE_D - x:
                break
        d.text((x, y + 6), nom, font=ps, fill=CREME)
        y += 86
    assert y <= 1440, "le recapitulatif deborde (%d)" % y
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_fin(lg):
    img = voile(plein_cadre("6294015163988"), haut=VOILE_COUV)
    d = ImageDraw.Draw(img)
    y = caps_multi(d, MARGE_G, 340, T["fin_t"][lg], 92, BLANC, LARGE)
    d.line([(MARGE_G, y + 44), (MARGE_G + 180, y + 44)], fill=OCRE, width=5)
    y = bloc_ajuste(d, MARGE_G, y + 96, [T["fin_s"][lg]], 44, CREME, LARGE,
                    1280, ital=True)
    d.text((MARGE_G, y + 40), LIEN, font=inter(38, "Bold"), fill=CREME)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def main():
    garde_fou()
    lg = (sys.argv[1] if len(sys.argv) > 1 else "fr").lower()
    assert lg in LANGUES, "langue inconnue : " + lg
    dossier = os.path.join(SORTIE, lg)
    os.makedirs(dossier, exist_ok=True)
    pages = [diapo_couverture(lg), diapo_regle(lg)]
    pages += [diapo_parfum(pf, i + 3, lg) for i, pf in enumerate(PARFUMS)]
    pages += [diapo_recap(lg), diapo_fin(lg)]
    assert len(pages) == 12, "douze diapos attendues, %d" % len(pages)
    for i, im in enumerate(pages, 1):
        im.save(os.path.join(dossier, "%02d.jpg" % i), quality=90,
                optimize=True)
    print("%s : %d diapos ecrites dans %s" % (lg, len(pages), dossier))


if __name__ == "__main__":
    main()
