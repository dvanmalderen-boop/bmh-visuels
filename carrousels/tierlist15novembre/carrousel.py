# -*- coding: utf-8 -*-
"""
BMH - carrousel du 15 novembre 2026.  FORMAT TIKTOK 1080 x 1920.

MECANIQUE : LA TIER LIST.  « La seule tier list que je peux faire. »

DEUXIEME VERSION. La premiere a ete jetee, et c'est Daoud qui avait raison :
« moi, la verite, je comprends rien du tout a ce carrousel ». Elle posait un
tableau VIDE sur la couverture et onze parfums a la file : aucune image ne
montrait de classement. Une tier list qu'on ne lit pas en une seconde n'est
pas une tier list. Ici la PREMIERE DIAPO EST LE TABLEAU, les onze flacons
deja poses dans leurs bandes.

POURQUOI CE FORMAT
Balayage du 14/11, chiffres releves a la main dans Chrome :
  @zpch_perfumes  « BEST ARAB FRAGRANCES FOR WINTER »
                  30 800 likes · 666 commentaires · 7 713 enregistrements
  @paviafragrances « Best of Lattafa »
                  10 400 likes · 182 commentaires · 1 595 enregistrements
Les deux font 17 secondes et quatre a cinq paliers. Le second n'a PAS de
palier « trash » et marche quand meme : c'est ce qui rend le format jouable
pour un vendeur.

LE PROBLEME DU VENDEUR, ET SA SOLUTION
Un vendeur qui classe ses propres parfums se tire une balle dans le pied :
tout ce qu'il met en bas, il ne le vend plus. Donc le tableau est range par
la SEULE chose qui ne se discute pas — LE PRIX. Quatre bandes, des bornes
nettes, onze flacons dedans. Le classement par le gout, c'est le lecteur qui
le fait, et c'est ce qu'on lui demande a la fin.

RIEN N'EST INVENTE.
Les onze familles sont les etiquettes des fiches Shopify. Les prix et les
stocks ont ete releves en live le 14/11 par l'API. Les marges viennent de
bts/rapports/marges.json du 13/11. A cote d'un flacon on ecrit sa famille,
sa maison, son nom et son prix. AUCUNE note, AUCUNE tenue, AUCUN avis.

ONZE MAISONS DIFFERENTES, une par famille. Le garde-fou le verifie.
Aucun parfum des 10, 11, 12, 13 et 14 novembre n'est repris.

ZONES TIKTOK : 150 px en haut, 480 px en bas, 120 px a droite sont manges
par l'interface. Tout le contenu vit entre y=200 et y=1400.
"""

import os
import re
import sys
from PIL import Image, ImageDraw, ImageFont

W, H    = 1080, 1920
RACINE  = "/home/claude/tierlist"
SCENES  = os.path.join(RACINE, "scenes")
POLICES = "/home/claude/polices"
SORTIE  = os.path.join(RACINE, "carrousel")

CREME    = (240, 228, 206)
ENCRE    = (46, 33, 23)
ENCRE_D  = (92, 70, 51)
OCRE     = (181, 85, 31)
BLANC    = (255, 255, 255)

LIEN = "shop.bringmedinahome.com"

MARGE_G, MARGE_D = 96, 180
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


def bloc(d, x, y, texte, police, couleur, lmax, interligne=1.26):
    pas = int(police.size * interligne)
    for l in couper(d, texte, police, lmax):
        d.text((x, y), l, font=police, fill=couleur)
        y += pas
    return y


def bloc_ajuste(d, x, y, textes, corps, couleur, lmax, y_max,
                interligne=1.22, poids=430, ital=False, mini=24):
    """Retrecit jusqu'a tenir au-dessus de y_max. Sans ca, l'allemand et le
    neerlandais poussent le texte hors de la zone sure de TikTok."""
    if isinstance(textes, str):
        textes = [textes]
    for c in range(corps, mini - 1, -2):
        p = serif(c, poids, 72, ital)
        h = sum(len(couper(d, t, p, lmax)) * int(p.size * interligne)
                for t in textes)
        if y + h <= y_max:
            break
    for t in textes:
        y = bloc(d, x, y, t, p, couleur, lmax, interligne)
    return y


def lettrage(d, y, texte, police, couleur, espace=6, x=MARGE_G):
    for c in texte:
        d.text((x, y), c, font=police, fill=couleur, anchor="lm")
        x += d.textlength(c, font=police) + espace

# ---------------------------------------------------------------- marque


def largeur_signature(corps=30, espace=7):
    d = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    p = inter(corps, "SemiBold")
    t = int(corps * 0.52) * 2 + 2
    l = t + corps * 0.75
    for c in "BRING MEDINA HOME":
        l += d.textlength(c, font=p) + espace
    return l - espace + 4 + d.textlength(
        "®", font=inter(int(corps * 0.55), "Medium"))


def poser_signature(img, x, y, couleur, corps=30, espace=7):
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

# --------------------------------------------------------------- vignettes
#
#  OU VIT LE FLACON DANS CHAQUE SCENE, en fraction de la largeur et de la
#  hauteur, plus la part de largeur que prend la fenetre carree. Releve a
#  l'oeil le 14/11 sur une planche contact, pas calcule : la detection
#  automatique attrape le bois seche et les fleurs, nets eux aussi.

CADRE = {
 "6290360590585": (0.68, 0.45, 0.70),  # Maison Alhambra Infini Elixir
 "6290361916896": (0.68, 0.45, 0.70),  # Arabiyat Sugar Mango Affogato
 "6298042000926": (0.68, 0.45, 0.70),  # French Avenue Vulcan Baie
 "5061042410214": (0.68, 0.45, 0.70),  # Ayat Jumrah Coffee
 "6294015163513": (0.68, 0.45, 0.70),  # Armaf Club de Nuit Urban Man Elixir
 "6291100130979": (0.63, 0.45, 0.70),  # Al Haramain Royal Musk
 "6290171072829": (0.60, 0.45, 0.70),  # Zimaya Treasure
 "6294879841183": (0.68, 0.45, 0.70),  # Paris Corner Khair Felicity
 "0614514204092": (0.68, 0.45, 0.70),  # Rasasi La Yuqawam Jasmine Wisp
 "6298141926707": (0.65, 0.45, 0.70),  # Emir Voux Violette
 "6290171075288": (0.65, 0.45, 0.70),  # Afnan 9pm Rebel
}


def vignette(ean, cote):
    im = Image.open(os.path.join(SCENES, ean + "c.jpg")).convert("RGB")
    cx, cy, fen = CADRE[ean]
    f = int(im.width * fen)
    x = max(0, min(int(cx * im.width - f / 2), im.width - f))
    y = max(0, min(int(cy * im.height - f / 2), im.height - f))
    return im.crop((x, y, x + f, y + f)).resize((cote, cote), Image.LANCZOS)


def prix(v, lg):
    e, c = ("%.2f" % v).split(".")
    if lg in ("fr", "de"):
        return "%s,%s €" % (e, c)
    if lg == "nl":
        return "€ %s,%s" % (e, c)
    return "€%s.%s" % (e, c)

# --------------------------------------------------------------- contenu
#
#  Les familles sont les etiquettes des fiches Shopify, relevees le 14/11.
#  On ne dit jamais quelle famille vaut mieux qu'une autre.

F = {
 "oud":      {"fr": "Oud et bois précieux", "en": "Oud and precious woods",
              "nl": "Oud en edelhout", "de": "Oud und Edelhölzer"},
 "gourmand": {"fr": "Gourmand praliné et sucré",
              "en": "Gourmand, praline and sweet",
              "nl": "Gourmand, praline en zoet",
              "de": "Gourmand, Praline und süß"},
 "fruits":   {"fr": "Fruits rouges et fruits mûrs",
              "en": "Red and ripe fruits", "nl": "Rood en rijp fruit",
              "de": "Rote und reife Früchte"},
 "tabac":    {"fr": "Tabac et café", "en": "Tobacco and coffee",
              "nl": "Tabak en koffie", "de": "Tabak und Kaffee"},
 "encens":   {"fr": "Encens et résines", "en": "Incense and resins",
              "nl": "Wierook en harsen", "de": "Weihrauch und Harze"},
 "cuir":     {"fr": "Cuir et miel", "en": "Leather and honey",
              "nl": "Leer en honing", "de": "Leder und Honig"},
 "safran":   {"fr": "Safran et épices du Golfe",
              "en": "Saffron and Gulf spices",
              "nl": "Saffraan en Golfspecerijen", "de": "Safran und Golfgewürze"},
 "rose":     {"fr": "Rose", "en": "Rose", "nl": "Roos", "de": "Rose"},
 "agrumes":  {"fr": "Agrumes et aromates", "en": "Citrus and aromatics",
              "nl": "Citrus en aromaten", "de": "Zitrus und Aromaten"},
 "iris":     {"fr": "Iris et fleurs blanches", "en": "Iris and white flowers",
              "nl": "Iris en witte bloemen", "de": "Iris und weiße Blüten"},
 "marin":    {"fr": "Marin et chypré", "en": "Marine and chypre",
              "nl": "Marine en chypre", "de": "Marine und Chypre"},
}

#  Un parfum par famille, onze maisons differentes. Stock et prix releves
#  en live le 14/11 ; marge nette = marge brute du 13/11 moins 4,85 EUR de
#  port sur une commande d'un seul flacon.

PARFUMS = [
 {"f": "oud",      "ean": "6290360590585", "maison": "MAISON ALHAMBRA",
  "nom": "Infini Elixir",            "prix": 32.90, "stock": 32,  "marge": 13.42},
 {"f": "gourmand", "ean": "6290361916896", "maison": "ARABIYAT",
  "nom": "Sugar Mango Affogato",     "prix": 34.90, "stock": 23,  "marge": 10.11},
 {"f": "fruits",   "ean": "6298042000926", "maison": "FRENCH AVENUE",
  "nom": "Vulcan Baie",              "prix": 40.90, "stock": 368, "marge": 9.99},
 {"f": "tabac",    "ean": "5061042410214", "maison": "AYAT",
  "nom": "Jumrah Coffee",            "prix": 33.90, "stock": 23,  "marge": 9.84},
 {"f": "encens",   "ean": "6294015163513", "maison": "ARMAF",
  "nom": "Club de Nuit Urban Man Elixir", "prix": 43.90, "stock": 23, "marge": 10.05},
 {"f": "cuir",     "ean": "6291100130979", "maison": "AL HARAMAIN",
  "nom": "Royal Musk",               "prix": 37.90, "stock": 6,   "marge": 10.07},
 {"f": "safran",   "ean": "6290171072829", "maison": "ZIMAYA",
  "nom": "Treasure",                 "prix": 27.90, "stock": 8,   "marge": 10.42},
 {"f": "rose",     "ean": "6294879841183", "maison": "PARIS CORNER",
  "nom": "Khair Felicity",           "prix": 28.90, "stock": 230, "marge": 10.99},
 {"f": "agrumes",  "ean": "0614514204092", "maison": "RASASI",
  "nom": "La Yuqawam Jasmine Wisp",  "prix": 41.90, "stock": 32,  "marge": 10.41},
 {"f": "iris",     "ean": "6298141926707", "maison": "EMIR",
  "nom": "Voux Violette",            "prix": 28.90, "stock": 22,  "marge": 9.95},
 {"f": "marin",    "ean": "6290171075288", "maison": "AFNAN",
  "nom": "9pm Rebel",                "prix": 45.90, "stock": 23,  "marge": 10.61},
]

#  LES QUATRE BANDES. Les bornes sont choisies pour que les onze se
#  repartissent 3 / 3 / 3 / 2 sans qu'aucune bande soit vide ou surchargee.
#  Un parfum tombe dans une bande par son prix, point. Il n'y a rien a
#  discuter la-dedans, et c'est exactement pour ca que c'est honnete.

BANDES = [
 {"max": 30.00, "l": {"fr": "MOINS\nDE 30 €", "en": "UNDER\n€30",
                      "nl": "ONDER\n€ 30",  "de": "UNTER\n30 €"}},
 {"max": 35.00, "l": {"fr": "30 À\n35 €", "en": "€30 TO\n€35",
                      "nl": "€ 30 TOT\n€ 35", "de": "30 BIS\n35 €"}},
 {"max": 42.00, "l": {"fr": "35 À\n42 €", "en": "€35 TO\n€42",
                      "nl": "€ 35 TOT\n€ 42", "de": "35 BIS\n42 €"}},
 {"max": 999.0, "l": {"fr": "PLUS\nDE 42 €", "en": "OVER\n€42",
                      "nl": "BOVEN\n€ 42",   "de": "ÜBER\n42 €"}},
]


def par_bande(i):
    bas = 0.0 if i == 0 else BANDES[i - 1]["max"]
    return [p for p in sorted(PARFUMS, key=lambda x: x["prix"])
            if bas < p["prix"] <= BANDES[i]["max"]]


T = {
 "sup": {"fr": "TIER LIST", "en": "TIER LIST", "nl": "TIER LIST",
         "de": "TIER LIST"},
 "couv": {
   "fr": ["La seule tier list", "que je peux faire"],
   "en": ["The only tier list", "I can make"],
   "nl": ["De enige tier list", "die ik kan maken"],
   "de": ["Die einzige Tier List,", "die ich machen kann"]},
 "couv_s": {
   "fr": "Par le prix. Par le goût, c'est toi qui ranges.",
   "en": "By price. By taste, you do the ranking.",
   "nl": "Op prijs. Op smaak rangschik jij.",
   "de": "Nach Preis. Nach Geschmack ordnen Sie."},
 "regle_t": {
   "fr": ["Pourquoi par", "le prix"],
   "en": ["Why by price"],
   "nl": ["Waarom op prijs"],
   "de": ["Warum nach Preis"]},
 "regle_c": {
   "fr": "Je vends les onze familles. Si j'en mets une en bas, je ne la vends "
         "plus — donc je ne peux pas te dire laquelle est la meilleure. Le "
         "prix, lui, ne se discute pas. C'est le seul classement que j'ai le "
         "droit d'afficher.",
   "en": "I sell all eleven families. If I put one at the bottom, I stop "
         "selling it — so I cannot tell you which is best. Price, on the "
         "other hand, is not up for debate. It is the only ranking I am "
         "entitled to show.",
   "nl": "Ik verkoop alle elf families. Zet ik er één onderaan, dan verkoop "
         "ik hem niet meer — dus ik kan je niet zeggen welke de beste is. "
         "Over de prijs valt niet te discussiëren. Dat is de enige ranglijst "
         "die ik mag tonen.",
   "de": "Ich verkaufe alle elf Familien. Setze ich eine nach unten, verkaufe "
         "ich sie nicht mehr — ich kann Ihnen also nicht sagen, welche die "
         "beste ist. Über den Preis lässt sich nicht streiten. Das ist die "
         "einzige Rangliste, die ich zeigen darf."},
 "regle_p": {
   "fr": "Le tien, mets-le en commentaire : quelle famille en S ?",
   "en": "Yours goes in the comments: which family is your S?",
   "nl": "De jouwe zet je in de reacties: welke familie is jouw S?",
   "de": "Ihre gehört in die Kommentare: welche Familie ist Ihr S?"},
 "fin_t": {
   "fr": ["Ta famille en S ?"], "en": ["Your S family?"],
   "nl": ["Jouw familie in S?"], "de": ["Ihre Familie auf S?"]},
 "fin_s": {
   "fr": "Dis-la en commentaire. Je te sors trois flacons de cette famille, "
         "dans ton budget.",
   "en": "Say it in the comments. I will pull three bottles from that family, "
         "in your budget.",
   "nl": "Zeg het in de reacties. Ik haal er drie flacons uit die familie bij, "
         "binnen jouw budget.",
   "de": "Schreiben Sie es in die Kommentare. Ich suche Ihnen drei Flakons aus "
         "dieser Familie, in Ihrem Budget."},
}

# ------------------------------------------------------------- garde-fou


def garde_fou():
    """On verifie AVANT de dessiner, pas apres.

    Ce qui rendrait ce carrousel faux ou malhonnete : un parfum deja passe
    cette semaine, une scene manquante, un flacon en rupture, une marge sous
    le plancher de 4 EUR net, deux parfums de la meme maison. Et une bande
    vide ou a quatre flacons, qui ferait deborder le tableau.
    """
    deja = set()
    base = "/home/claude/bmh-visuels/carrousels"
    for f in ("eviter10novembre", "heures11novembre", "coude12novembre",
              "duel13novembre", "niveaux14novembre"):
        c = os.path.join(base, f, "carrousel.py")
        if os.path.exists(c):
            deja |= set(re.findall(r'"(\d{13})"',
                                   open(c, encoding="utf-8").read()))
    for pf in PARFUMS:
        assert pf["ean"] not in deja, "%s est deja passe cette semaine" % pf["nom"]
        assert os.path.exists(os.path.join(SCENES, pf["ean"] + "c.jpg")), \
            "scene manquante : " + pf["ean"]
        assert pf["ean"] in CADRE, "cadrage non releve : " + pf["ean"]
        assert pf["stock"] >= 5, "%s n'a que %d en stock" % (pf["nom"], pf["stock"])
        net = pf["marge"] - 4.85
        assert net >= 4.00, ("%s tombe sous le plancher : %.2f EUR net"
                             % (pf["nom"], net))
        assert pf["f"] in F, "famille inconnue : " + pf["f"]
    assert len(PARFUMS) == 11, "onze parfums attendus, %d" % len(PARFUMS)
    assert len({p["f"] for p in PARFUMS}) == 11, "une famille par parfum"
    assert len({p["maison"] for p in PARFUMS}) == 11, "onze maisons differentes"
    compte = [len(par_bande(i)) for i in range(len(BANDES))]
    assert sum(compte) == 11, "des parfums tombent hors des bandes : %s" % compte
    for n in compte:
        assert 1 <= n <= 3, ("une bande a %d flacons : le tableau deborde "
                             "ou sonne creux (%s)" % (n, compte))
    faible = [p["nom"] for p in PARFUMS if p["stock"] < 10]
    print("garde-fou : 11 familles, 11 maisons, bandes %s, net de %.2f a %.2f EUR"
          % (compte, min(p["marge"] for p in PARFUMS) - 4.85,
             max(p["marge"] for p in PARFUMS) - 4.85))
    if faible:
        print("   ! stock sous 10 : " + ", ".join(faible))

# ------------------------------------------------------------------ diapos

#  LE TABLEAU. C'est la premiere diapo, et c'est tout le carrousel.
#  ETIQ = largeur de la case du palier, COTE = cote d'une vignette.
#  Trois vignettes au plus par bande : ETIQ + ECART + 3 x COTE doit rester
#  sous 864 px, la largeur utile une fois la colonne de boutons de TikTok
#  retiree a droite.

ETIQ, ECART, COTE, SAUT = 190, 12, 220, 12
HAUT_TABLEAU = 4 * COTE + 3 * SAUT
assert ETIQ + ECART + 3 * COTE <= W - MARGE_G - 120, "le tableau est trop large"


def fond():
    img = Image.new("RGB", (W, H), CREME)
    return img, ImageDraw.Draw(img)


def tableau(img, d, y0, lg, cote=COTE, etiq=ETIQ, ecart=ECART, saut=SAUT,
            corps=34):
    """Le tableau lui-meme : une case de palier en ocre, puis les flacons de
    la bande poses a la suite. Il sert deux fois, en grand sur la premiere
    diapo et en petit sur la derniere."""
    y = y0
    for i, b in enumerate(BANDES):
        d.rectangle([MARGE_G, y, MARGE_G + etiq, y + cote], fill=OCRE)
        lignes = b["l"][lg].split("\n")
        p = inter(corps, "SemiBold")
        ht = len(lignes) * int(p.size * 1.22)
        yy = y + (cote - ht) / 2
        for l in lignes:
            d.text((MARGE_G + etiq / 2, yy), l, font=p, fill=CREME, anchor="ma")
            yy += int(p.size * 1.22)
        x = MARGE_G + etiq + ecart
        for pf in par_bande(i):
            img.paste(vignette(pf["ean"], cote), (int(x), int(y)))
            x += cote
        y += cote + saut
    return y - saut          # le bas reel du tableau, sans l'ecart final


def diapo_tableau(lg):
    img, d = fond()
    lettrage(d, 250, T["sup"][lg], inter(34, "SemiBold"), OCRE, 10)
    y = bloc_ajuste(d, MARGE_G, 306, T["couv"][lg], 74, ENCRE, LARGE, 452)
    bloc_ajuste(d, MARGE_G, y + 18, [T["couv_s"][lg]], 36, ENCRE_D, LARGE,
                516, ital=True)
    bas = tableau(img, d, 508, lg)
    assert bas <= 1430, "le tableau deborde de la zone sure (%d)" % bas
    poser_signature(img, MARGE_G, 1830, ENCRE_D, 30, 7)
    return img


def diapo_regle(lg):
    img, d = fond()
    lettrage(d, 250, "01", inter(34, "SemiBold"), OCRE, 10)
    y = bloc_ajuste(d, MARGE_G, 320, T["regle_t"][lg], 96, ENCRE, LARGE, 620)
    d.line([(MARGE_G, y + 40), (MARGE_G + 120, y + 40)], fill=OCRE, width=3)
    y = bloc_ajuste(d, MARGE_G, y + 90, [T["regle_c"][lg]], 46, ENCRE, LARGE,
                    1180)
    bloc_ajuste(d, MARGE_G, y + 60, [T["regle_p"][lg]], 46, OCRE, LARGE, 1400,
                ital=True)
    poser_signature(img, MARGE_G, 1830, ENCRE_D, 30, 7)
    return img


def rang(img, d, pf, y, lg, cote=300):
    """Une ligne detaillee : la vignette a gauche, la famille, la maison, le
    nom et le prix a droite. Le nom retrecit tout seul — « Club de Nuit
    Urban Man Elixir » ne tient pas en corps 50."""
    img.paste(vignette(pf["ean"], cote), (MARGE_G, y))
    x = MARGE_G + cote + 36
    l = W - MARGE_D - x
    d.text((x, y + 6), F[pf["f"]][lg].upper(), font=inter(25, "SemiBold"),
           fill=OCRE)
    d.text((x, y + 52), pf["maison"], font=inter(25, "Medium"), fill=ENCRE_D)
    yy = bloc_ajuste(d, x, y + 96, [pf["nom"]], 50, ENCRE, l, y + cote - 64)
    d.text((x, max(yy + 14, y + cote - 56)), prix(pf["prix"], lg),
           font=inter(40, "SemiBold"), fill=ENCRE)
    return y + cote


def diapo_bande(i, lg):
    """Une bande en grand, pour qu'on puisse lire les noms. La case du palier
    est reprise en haut a gauche, a l'identique du tableau : c'est elle qui
    dit au lecteur ou il est."""
    img, d = fond()
    lignes = BANDES[i]["l"][lg].replace("\n", " ")
    d.rectangle([MARGE_G, 214, MARGE_G + 300, 286], fill=OCRE)
    d.text((MARGE_G + 150, 250), lignes, font=inter(32, "SemiBold"),
           fill=CREME, anchor="mm")
    d.text((W - MARGE_D, 250), "%02d" % (i + 2), font=inter(30, "SemiBold"),
           fill=ENCRE_D, anchor="rm")
    y = 340
    for pf in par_bande(i):
        y = rang(img, d, pf, y, lg) + 40
    assert y <= 1430, "les lignes debordent (%d)" % y
    poser_signature(img, MARGE_G, 1830, ENCRE_D, 30, 7)
    return img


def diapo_fin(lg):
    img, d = fond()
    y = bloc_ajuste(d, MARGE_G, 300, T["fin_t"][lg], 104, ENCRE, LARGE, 560)
    d.line([(MARGE_G, y + 40), (MARGE_G + 180, y + 40)], fill=OCRE, width=4)
    y = bloc_ajuste(d, MARGE_G, y + 90, [T["fin_s"][lg]], 44, ENCRE_D, LARGE,
                    900, ital=True)
    d.text((MARGE_G, y + 50), LIEN, font=inter(38, "SemiBold"), fill=OCRE)
    # le tableau revient en petit, cases de palier comprises : la derniere
    # image doit rappeler ce qu'on demande de classer, pas seulement porter
    # du texte. Sans les cases, les vignettes se lisent comme un tas.
    bas = tableau(img, d, 946, lg, cote=112, etiq=112, ecart=10, saut=8,
                  corps=19)
    assert bas <= 1430, "le rappel du tableau deborde (%d)" % bas
    poser_signature(img, MARGE_G, 1830, ENCRE_D, 30, 7)
    return img


def main():
    garde_fou()
    lg = (sys.argv[1] if len(sys.argv) > 1 else "fr").lower()
    assert lg in LANGUES, "langue inconnue : " + lg
    dossier = os.path.join(SORTIE, lg)
    os.makedirs(dossier, exist_ok=True)
    pages = [diapo_tableau(lg), diapo_regle(lg)]
    pages += [diapo_bande(i, lg) for i in range(len(BANDES))]
    pages.append(diapo_fin(lg))
    assert len(pages) == 7, "sept diapos attendues, %d produites" % len(pages)
    for i, im in enumerate(pages, 1):
        im.save(os.path.join(dossier, "%02d.jpg" % i), quality=92, optimize=True)
    print("%s : %d diapos ecrites dans %s" % (lg, len(pages), dossier))


if __name__ == "__main__":
    main()
