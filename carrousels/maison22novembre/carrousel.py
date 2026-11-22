# -*- coding: utf-8 -*-
"""
BMH - carrousel du 22 novembre 2026, 19h00.  FORMAT TIKTOK 1080 x 1920.

MECANIQUE : LE BALAYAGE D'UNE MAISON.

POURQUOI CELUI-LA
C'est le format n°5 du fichier « ce qui marche » (claude/ce-qui-marche-
carrousels.md) : « j'ai senti +100 parfums X » a fait 389 300 vues. C'est le
seul des formats mesures qu'on n'a jamais essaye, et il se fabrique
entierement avec les donnees de la boutique — rien a inventer.

Regle de variation : le 18/11 c'etait le prix au millilitre, le 19/11 quatre
conseils, le 20/11 un seul parfum en profondeur. Celui-ci ne compare pas deux
produits et ne classe rien : il cartographie une maison.

LE CROCHET EST VERIFIE, PAS DEVINE
« 30 Lattafa, 11 familles » sort d'une requete sur les collections Shopify le
22/11/2026. Trente produits Lattafa actifs, chacun range dans exactement une
collection de famille olfactive, onze familles distinctes au total :

  fruits rouges 6 · gourmand 6 · oud 6 · encens 3 · iris 2 · tabac et cafe 2
  agrumes 1 · cuir et miel 1 · safran 1 · marin 1 · rose 1      = 30

⚠️ ON N'ECRIT PAS « J'AI SENTI LES 30 ». Daoud ne tient pas de stock, il ne
les a pas sentis. Le carrousel dit ce qui est vrai : la maison est chez nous
en entier, voila par ou commencer.

LES CINQ, ET POURQUOI CEUX-LA
Une famille differente chacun, du moins cher au plus cher, tous avec du stock
reel releve le 22/11 et une scene disponible. Les notes et les phrases sont
RECOPIEES des fiches Shopify, jamais reecrites de memoire.

⚠️ DIX DIAPOS MAXIMUM — l'API Instagram coupe au-dela, en silence. On en fait
neuf. La derniere porte l'adresse et n'est jamais la variable d'ajustement.
L'avant-derniere est la carte de marque, adjugee le 19/11.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import ImageDraw                                    # noqa: E402
from socle import (                                          # noqa: E402
    W, H, MARGE_G, MARGE_D, LARGE, LANGUES, SORTIE, MAX_DIAPOS,
    CREME, OCRE, BLANC,
    serif, inter, couper, caps_multi, bloc_ajuste, lettrage,
    poser_signature, plein_cadre, voile,
)

LIEN = "shop.bringmedinahome.com"

MAISON = "Lattafa"
TOTAL = 30            # produits Lattafa actifs, Shopify, 22/11/2026
FAMILLES = 11         # collections de famille distinctes qu'ils occupent

SCENE_COUV = "6291107458328"   # Badee Al Oud For Glory - pas un des cinq

#  --------------------------------------------------------------- les cinq
#  « famille » est le titre exact de la collection Shopify.
#  « coeur » et « phrase » sont recopies de la fiche produit.
CINQ = [
    dict(
        ean="6291107454412", nom="Ana Abiyedh Rouge", ml=60, prix=24.90,
        stock=806,
        famille={"fr": "Marin et chypré", "en": "Marine and chypre",
                 "nl": "Marien en chypre", "de": "Marine und Chypre"},
        coeur={"fr": "Poire nashi, caramel, mousse de chêne",
               "en": "Nashi pear, caramel, oakmoss",
               "nl": "Nashi-peer, karamel, eikenmos",
               "de": "Nashi-Birne, Karamell, Eichenmoos"},
        phrase={"fr": "Un fruité sucré-salé qui s'achève sur la mousse de chêne.",
                "en": "A sweet-salty fruity that ends on oakmoss.",
                "nl": "Een zoet-zoute fruitige die eindigt op eikenmos.",
                "de": "Ein süß-salziger Fruchtduft, der auf Eichenmoos endet."},
    ),
    dict(
        ean="6290360598963", nom="Mayar Cherry Intense", ml=100, prix=30.90,
        stock=1238,
        famille={"fr": "Fruits rouges et fruits mûrs",
                 "en": "Red and ripe fruits",
                 "nl": "Rood en rijp fruit", "de": "Rote und reife Früchte"},
        coeur={"fr": "Confiture de cerise, cacao, vanille",
               "en": "Cherry jam, cocoa, vanilla",
               "nl": "Kersenjam, cacao, vanille",
               "de": "Kirschkonfitüre, Kakao, Vanille"},
        phrase={"fr": "Une cerise enrobée de chocolat. Pas fraîche : cuite, dense.",
                "en": "A chocolate-coated cherry. Not fresh: cooked, dense.",
                "nl": "Een kers in chocolade. Niet vers: gekookt, dicht.",
                "de": "Eine Kirsche in Schokolade. Nicht frisch: gekocht, dicht."},
    ),
    dict(
        ean="6291107456058", nom="Fakhar Men", ml=100, prix=31.90,
        stock=1283,
        famille={"fr": "Oud et bois précieux", "en": "Oud and precious woods",
                 "nl": "Oud en edele houtsoorten",
                 "de": "Oud und edle Hölzer"},
        coeur={"fr": "Cardamome, patchouli, oud, santal",
               "en": "Cardamom, patchouli, oud, sandalwood",
               "nl": "Kardemom, patchoeli, oud, sandelhout",
               "de": "Kardamom, Patschuli, Oud, Sandelholz"},
        phrase={"fr": "Là où le Fakhar classique est fruité, celui-ci est boisé.",
                "en": "Where the classic Fakhar is fruity, this one is woody.",
                "nl": "Waar de klassieke Fakhar fruitig is, is deze houtachtig.",
                "de": "Wo der klassische Fakhar fruchtig ist, ist dieser holzig."},
    ),
    dict(
        ean="6290360591421", nom="Yara Moi", ml=100, prix=32.90,
        stock=1490,
        famille={"fr": "Gourmand praliné et sucré",
                 "en": "Praline and sweet gourmand",
                 "nl": "Praline en zoet gourmand",
                 "de": "Praline und süßer Gourmand"},
        coeur={"fr": "Tubéreuse, amande, vanille, patchouli",
               "en": "Tuberose, almond, vanilla, patchouli",
               "nl": "Tuberoos, amandel, vanille, patchoeli",
               "de": "Tuberose, Mandel, Vanille, Patschuli"},
        phrase={"fr": "La version la plus adulte de toute la gamme Yara.",
                "en": "The most grown-up version of the whole Yara range.",
                "nl": "De meest volwassen versie van de hele Yara-reeks.",
                "de": "Die erwachsenste Version der ganzen Yara-Reihe."},
    ),
    dict(
        ean="6290360593661", nom="Khamrah Qahwa", ml=100, prix=36.90,
        stock=363,
        famille={"fr": "Tabac et café", "en": "Tobacco and coffee",
                 "nl": "Tabak en koffie", "de": "Tabak und Kaffee"},
        coeur={"fr": "Cannelle, praline, café, fève tonka",
               "en": "Cinnamon, praline, coffee, tonka bean",
               "nl": "Kaneel, praline, koffie, tonkaboon",
               "de": "Zimt, Praline, Kaffee, Tonkabohne"},
        phrase={"fr": "Le café vient trancher dans le sucre. Un hiver en bouteille.",
                "en": "The coffee cuts through the sugar. A winter in a bottle.",
                "nl": "De koffie snijdt door de suiker. Een winter in een fles.",
                "de": "Der Kaffee schneidet durch den Zucker. Ein Winter in der Flasche."},
    ),
]

#  ------------------------------------------------------------- les textes

T = {
    "couv_sur": {"fr": "LA MAISON LATTAFA", "en": "THE HOUSE OF LATTAFA",
                 "nl": "HET HUIS LATTAFA", "de": "DAS HAUS LATTAFA"},
    "couv_titre": {"fr": "30 LATTAFA\n11 FAMILLES", "en": "30 LATTAFA\n11 FAMILIES",
                   "nl": "30 LATTAFA\n11 FAMILIES", "de": "30 LATTAFA\n11 FAMILIEN"},
    "couv_bas": {
        "fr": "La maison entière est chez nous. Voilà par où commencer.",
        "en": "The whole house is in our shop. Here is where to start.",
        "nl": "Het hele huis staat bij ons. Hier begin je.",
        "de": "Das ganze Haus steht bei uns. Hier fangen Sie an."},

    "deux_sur": {"fr": "LA QUESTION", "en": "THE QUESTION",
                 "nl": "DE VRAAG", "de": "DIE FRAGE"},
    "deux_titre": {"fr": "PAR OÙ\nCOMMENCER ?", "en": "WHERE DO\nYOU START ?",
                   "nl": "WAAR BEGIN\nJE ?", "de": "WO FANGEN\nSIE AN ?"},
    "deux_bas": {
        "fr": "Cinq flacons, cinq familles différentes. De 24,90 € à 36,90 €.",
        "en": "Five bottles, five different families. From 24.90 € to 36.90 €.",
        "nl": "Vijf flacons, vijf verschillende families. Van 24,90 € tot 36,90 €.",
        "de": "Fünf Flakons, fünf verschiedene Familien. Von 24,90 € bis 36,90 €."},

    "le_coeur": {"fr": "LE CŒUR", "en": "THE HEART",
                 "nl": "HET HART", "de": "DAS HERZ"},

    "fin_sur": {"fr": "LES VINGT-CINQ AUTRES", "en": "THE OTHER TWENTY-FIVE",
                "nl": "DE ANDERE VIJFENTWINTIG", "de": "DIE ANDEREN FÜNFUNDZWANZIG"},
    "fin_titre": {"fr": "LES 30 SONT\nEN BOUTIQUE", "en": "ALL 30 ARE\nIN THE SHOP",
                  "nl": "ALLE 30 STAAN\nIN DE WINKEL",
                  "de": "ALLE 30 SIND\nIM SHOP"},
    "fin_bas": {
        "fr": "Enregistre ce carrousel pour le retrouver quand tu choisiras.",
        "en": "Save this carousel so you can find it when you choose.",
        "nl": "Bewaar dit carrousel zodat je het terugvindt als je kiest.",
        "de": "Speichern Sie diesen Beitrag, damit Sie ihn bei der Wahl wiederfinden."},

    "marque_bas": {"fr": "279 parfums · 27 maisons d'Arabie",
                   "en": "279 perfumes · 27 houses of Arabia",
                   "nl": "279 parfums · 27 huizen uit Arabië",
                   "de": "279 Parfums · 27 Häuser Arabiens"},
}

#  ---------------------------------------------------------------- voiles

VOILE_COUV = [(0, 236), (560, 230), (900, 155), (1270, 0)]
VOILE_HAUT = [(0, 232), (420, 222), (720, 110), (1000, 0)]
VOILE_BAS = [(820, 0), (980, 150), (1120, 220), (1260, 246), (1920, 250)]
VOILE_MARQUE = [(0, 246), (1200, 243), (1540, 140), (1830, 0)]


def prix_affiche(p, lg):
    #  Le neerlandais ecrit la decimale avec une virgule, comme le francais
    #  et l'allemand. Seul l'anglais prend le point.
    return ("%.2f" % p).replace(
        ".", "," if lg in ("fr", "de", "nl") else ".") + " €"


#  ---------------------------------------------------------------- diapos


def diapo_couverture(lg):
    img = voile(plein_cadre(SCENE_COUV), haut=VOILE_COUV, bas=VOILE_BAS)
    d = ImageDraw.Draw(img)
    lettrage(d, 258, T["couv_sur"][lg], inter(28, "SemiBold"), OCRE, 7)
    y = caps_multi(d, MARGE_G, 318, T["couv_titre"][lg], 136, CREME, LARGE)
    d.line([(MARGE_G, y + 34), (MARGE_G + 560, y + 34)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 86, [T["couv_bas"][lg]], 50, CREME, LARGE,
                y + 260, ital=True)
    poser_signature(img, MARGE_G, 1392, CREME)
    return img


def diapo_question(lg):
    """La diapo 2 doit tenir toute seule : Instagram peut re-servir le
    carrousel en commencant par elle. Donc elle redit le chiffre."""
    img = voile(plein_cadre(CINQ[4]["ean"]), haut=VOILE_COUV, bas=VOILE_BAS)
    d = ImageDraw.Draw(img)
    lettrage(d, 258, T["deux_sur"][lg], inter(28, "SemiBold"), OCRE, 7)
    y = caps_multi(d, MARGE_G, 318, T["deux_titre"][lg], 124, CREME, LARGE)
    d.line([(MARGE_G, y + 34), (MARGE_G + 560, y + 34)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 86, [T["deux_bas"][lg]], 50, CREME, LARGE,
                y + 280, ital=True)
    poser_signature(img, MARGE_G, 1392, CREME)
    return img


def diapo_parfum(p, rang, lg):
    """Le texte est coupe en deux blocs, un sous chaque voile, et le flacon
    respire au milieu. Tout tient au-dessus de y=1400 : en dessous, c'est
    l'interface de TikTok qui mange l'image."""
    img = voile(plein_cadre(p["ean"]), haut=VOILE_HAUT, bas=VOILE_BAS)
    d = ImageDraw.Draw(img)

    #  Haut : le rang, la famille — c'est elle l'information — puis le coeur.
    lettrage(d, 252, "%d / 5" % rang, inter(28, "SemiBold"), OCRE, 7)
    y = bloc_ajuste(d, MARGE_G, 300, [p["famille"][lg]], 58, CREME, LARGE,
                    440, poids=560)
    lettrage(d, y + 56, T["le_coeur"][lg], inter(26, "SemiBold"), OCRE, 6)
    bloc_ajuste(d, MARGE_G, y + 86, [p["coeur"][lg]], 42, CREME, LARGE,
                y + 230)

    #  Bas : le nom, le prix, la phrase de la fiche.
    nom = "%s %s" % (MAISON, p["nom"])
    y = bloc_ajuste(d, MARGE_G, 1010, [nom], 68, BLANC, LARGE, 1168,
                    poids=600)
    d.text((MARGE_G, y + 8), "%d ml · %s" % (p["ml"],
           prix_affiche(p["prix"], lg)), font=inter(44, "SemiBold"), fill=OCRE)
    bloc_ajuste(d, MARGE_G, y + 76, [p["phrase"][lg]], 42, CREME, LARGE,
                1348, ital=True)

    poser_signature(img, MARGE_G, 1400, CREME)
    return img


def diapo_marque(lg):
    """La carte de marque, adjugee par Daoud le 19/11 : trois lignes
    JUSTIFIEES a la meme largeur. claude/carte-de-marque.md.
    Pas de signature en pied ici : la marque EST la diapo."""
    img = voile(plein_cadre(SCENE_COUV), haut=VOILE_MARQUE)
    d = ImageDraw.Draw(img)
    mots = ("BRING", "MEDINA", "HOME")
    bloc = 820
    for corps in range(200, 60, -2):
        p = inter(corps, "Bold")
        if max(sum(d.textlength(c, font=p) for c in m) for m in mots) <= bloc:
            break
    p = inter(corps, "Bold")
    y = 430
    for m in mots:
        brut = sum(d.textlength(c, font=p) for c in m)
        espace = (bloc - brut) / float(len(m) - 1)
        x = MARGE_G
        for c in m:
            d.text((x, y), c, font=p, fill=BLANC)
            x += d.textlength(c, font=p) + espace
        if m == "HOME":
            d.text((MARGE_G + bloc + 30, y + corps * 0.10), "®",
                   font=inter(int(corps * 0.26), "Medium"), fill=OCRE)
        y += int(corps * 1.12)
    d.line([(MARGE_G, y + 40), (MARGE_G + bloc, y + 40)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 92, [T["marque_bas"][lg]], 48, CREME, bloc,
                y + 220, ital=True)
    return img


def diapo_fin(lg):
    """La seule diapo qui porte l'adresse. Elle ne demande pas un clic :
    les carrousels produisent des enregistrements, on demande ca."""
    img = voile(plein_cadre(CINQ[1]["ean"]), haut=VOILE_COUV, bas=VOILE_BAS)
    d = ImageDraw.Draw(img)
    lettrage(d, 258, T["fin_sur"][lg], inter(28, "SemiBold"), OCRE, 7)
    y = caps_multi(d, MARGE_G, 318, T["fin_titre"][lg], 118, CREME, LARGE)
    d.line([(MARGE_G, y + 34), (MARGE_G + 560, y + 34)], fill=OCRE, width=5)
    y = bloc_ajuste(d, MARGE_G, y + 86, [T["fin_bas"][lg]], 48, CREME, LARGE,
                    y + 280, ital=True)
    d.text((MARGE_G, 1300), LIEN, font=inter(50, "SemiBold"), fill=OCRE)
    poser_signature(img, MARGE_G, 1430, CREME)
    return img


#  ------------------------------------------------------------- garde-fou


def garde_fou():
    """Ce que ce carrousel affirme doit etre verifiable.
    1. Le compte des familles doit tomber sur le chiffre annonce.
    2. Les cinq doivent etre dans cinq familles differentes.
    3. Aucun des cinq ne doit etre en rupture ou presque.
    4. L'intervalle de prix annonce en diapo 2 doit etre le vrai.
    5. Aucune promesse chiffree de tenue : on n'ecrit pas ce qu'on n'a pas lu.
    """
    assert TOTAL == 30 and FAMILLES == 11

    fam = [p["famille"]["fr"] for p in CINQ]
    assert len(set(fam)) == len(CINQ), "deux parfums dans la meme famille"

    for p in CINQ:
        assert p["stock"] >= 100, "%s : stock trop court" % p["nom"]
        for lg in LANGUES:
            for cle in ("famille", "coeur", "phrase"):
                assert p[cle].get(lg), "%s : %s manquant en %s" % (
                    p["nom"], cle, lg)
                assert not re.search(
                    r"\d+\s*(%|fois|x|heures|hours|uur|Stunden)",
                    p[cle][lg]), "promesse chiffree dans %s" % p["nom"]

    prix = [p["prix"] for p in CINQ]
    assert prix == sorted(prix), "les cinq ne sont pas du moins cher au plus cher"
    for lg in LANGUES:
        bas, haut = prix_affiche(min(prix), lg), prix_affiche(max(prix), lg)
        assert bas in T["deux_bas"][lg] and haut in T["deux_bas"][lg], \
            "l'intervalle de prix annonce est faux en " + lg


def pages(lg):
    p = [diapo_couverture(lg), diapo_question(lg)]
    for i, parfum in enumerate(CINQ, 1):
        p.append(diapo_parfum(parfum, i, lg))
    p.append(diapo_marque(lg))
    p.append(diapo_fin(lg))
    return p


def main():
    garde_fou()
    for lg in LANGUES:
        dossier = os.path.join(SORTIE, lg)
        os.makedirs(dossier, exist_ok=True)
        p = pages(lg)
        assert len(p) <= MAX_DIAPOS, \
            "%d diapos : l'API Instagram coupe au-dela de %d" % (
                len(p), MAX_DIAPOS)
        for i, img in enumerate(p, 1):
            chemin = os.path.join(dossier, "m%02d.jpg" % i)
            img.save(chemin, quality=92, subsampling=0)
        print("%s : %d diapos" % (lg, len(p)))


if __name__ == "__main__":
    main()
