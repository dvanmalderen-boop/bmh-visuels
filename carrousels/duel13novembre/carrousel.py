# -*- coding: utf-8 -*-
"""
BMH - carrousel du 13 novembre 2026.  FORMAT TIKTOK 1080 x 1920.

MECANIQUE : LE DUEL.  « Lequel tu mets ? »
Deux flacons par diapo, cote a cote, le lecteur choisit et commente.

POURQUOI CETTE MECANIQUE
Le 12/11 c'etait une ACCUSATION (« tu te trompes d'endroit ») : on glisse
pour savoir ou le mettre. Reprendre la meme chose le lendemain userait le
gabarit. Ici le moteur du glissement est autre : la COMPARAISON. Et surtout
le duel fait COMMENTER — c'est le signal le moins cher pour l'algorithme, et
c'est ce qui manque le plus aux comptes de Daoud.
Format verifie par les agents : « Reef 33 VS Gissah Imperial Valley »,
166 800 vues.
Mecaniques deja employees, a ne pas reprendre : elimination (05-06/11),
« le nom ment » (07/11), echelle du sucre (08/11), plaque constante (09/11),
coupure en deux (10/11), les heures (11/11), les endroits (12/11).

RIEN N'EST INVENTE.
Chaque duel oppose DEUX PARFUMS DE LA MEME MAISON, souvent de la meme ligne.
La seule chose qu'on dit d'un parfum, c'est SA FAMILLE OLFACTIVE, relevee le
12/11 sur les etiquettes des fiches Shopify (le tag « Oud et bois precieux »,
« Agrumes et aromates », etc.). Aucune note, aucune tenue, aucune comparaison
de qualite. On ne dit jamais lequel est le meilleur : c'est le lecteur qui
tranche, et c'est tout l'interet du format.

LE STOCK ET LES MARGES ONT ETE VERIFIES, ET LES DEUX, le 12/11 :
les douze sont in_stock, marges de 9,65 a 16,02 EUR.
SIX MAISONS DIFFERENTES, une par duel. Le garde-fou le verifie.
Aucun parfum du 11/11 ni du 12/11 n'est repris.

ZONES TIKTOK : 150 px en haut, 480 px en bas, 120 px a droite sont manges
par l'interface. Tout le texte vit entre y=200 et y=1400, et s'arrete a x=900.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H    = 1080, 1920
RACINE  = "/home/claude/duel"
SCENES  = os.path.join(RACINE, "scenes")
PHOTOS  = os.path.join(RACINE, "photos")     # images generees par Claude Code
POLICES = "/home/claude/polices"
SORTIE  = os.path.join(RACINE, "carrousel")

CREME    = (240, 228, 206)
ENCRE    = (46, 33, 23)
ENCRE_D  = (92, 70, 51)
ORANGE   = (234, 88, 12)
OCRE     = (181, 85, 31)
BLANC    = (255, 255, 255)

LIEN = "shop.bringmedinahome.com"

HAUT_SUR, BAS_SUR = 200, 1400
MARGE_G, MARGE_D  = 96, 180
LARGE = W - MARGE_G - MARGE_D

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

def bloc(d, x, y, texte, police, couleur, lmax, interligne=1.26, centre=False):
    pas = int(police.size * interligne)
    for l in couper(d, texte, police, lmax):
        d.text((x + lmax / 2 if centre else x, y), l, font=police,
               fill=couleur, anchor="ma" if centre else "la")
        y += pas
    return y

def bloc_ajuste(d, x, y, textes, corps, couleur, lmax, y_max,
                interligne=1.26, poids=430, ital=False, mini=26, centre=False):
    """Retrecit jusqu'a tenir au-dessus de y_max. Sans ca, l'allemand et le
    neerlandais poussent le texte dans le filet du pied."""
    if isinstance(textes, str):
        textes = [(textes, couleur)]
    elif textes and isinstance(textes[0], str):
        textes = [(t, couleur) for t in textes]
    for c in range(corps, mini - 1, -2):
        p = serif(c, poids, 72, ital)
        h = sum(len(couper(d, t, p, lmax)) * int(p.size * interligne)
                for t, _ in textes)
        if y + h <= y_max:
            break
    for t, coul in textes:
        y = bloc(d, x, y, t, p, coul, lmax, interligne, centre)
    return y

def lettrage(d, y, texte, police, couleur, espace=6, x=MARGE_G):
    for c in texte:
        d.text((x, y), c, font=police, fill=couleur, anchor="lm")
        x += d.textlength(c, font=police) + espace

# ---------------------------------------------------------------- marque

def couleur_signature(img, x, y, largeur=560, hauteur=60):
    zone = img.crop((int(x), int(y - hauteur / 2),
                     int(min(W, x + largeur)), int(y + hauteur / 2)))
    px = list(zone.resize((16, 4), Image.LANCZOS).getdata())
    clarte = sum(0.299 * r + 0.587 * g + 0.114 * b for r, g, b in px) / len(px)
    return ENCRE if clarte > 150 else BLANC

def poser_signature(img, x, y, couleur, corps=30, espace=7):
    r = int(corps * 0.52)
    t = r * 2 + 2
    lune = Image.new("L", (t * 4, t * 4), 0)
    dl = ImageDraw.Draw(lune)
    R = r * 4
    dl.ellipse([2, 2, 2 + R * 2, 2 + R * 2], fill=255)
    dec = int(R * 0.52)
    dl.ellipse([2 + dec, 2 - R * 0.06, 2 + dec + R * 2, 2 - R * 0.06 + R * 2], fill=0)
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

# ---------------------------------------------------------------- decors

def panneau(ean, largeur, hauteur, biais=0.5):
    """Un demi-ecran a partir d'une scene produit. `biais` decide quelle part
    de la scene on garde : a droite on recadre vers la gauche, pour que le
    flacon ne finisse pas sous la pile de boutons de TikTok."""
    im = Image.open(os.path.join(SCENES, ean + "c.jpg")).convert("RGB")
    ech = max(largeur / im.width, hauteur / im.height)
    im = im.resize((int(im.width * ech) + 1, int(im.height * ech) + 1),
                   Image.LANCZOS)
    x = int((im.width - largeur) * biais)
    y = int((im.height - hauteur) * 0.42)
    return im.crop((x, y, x + largeur, y + hauteur))

def photo(nom, hauteur, decalage):
    im = Image.open(os.path.join(PHOTOS, nom)).convert("RGB")
    if im.width != W:
        im = im.resize((W, int(im.height * W / im.width)), Image.LANCZOS)
    decalage = max(0, min(decalage, im.height - hauteur))
    return im.crop((0, decalage, W, decalage + hauteur))

def fondu(img, depart, hauteur, vers=CREME):
    voile = Image.new("RGBA", (W, hauteur), vers + (0,))
    d = ImageDraw.Draw(voile)
    for i in range(hauteur):
        d.line([(0, i), (W, i)],
               fill=vers + (int(((i / max(hauteur - 1, 1)) ** 1.6) * 255),))
    img.paste(voile, (0, depart), voile)

def prix(v, lg):
    e, c = ("%.2f" % v).split(".")
    if lg in ("fr", "de"):
        return "%s,%s €" % (e, c)
    if lg == "nl":
        return "€ %s,%s" % (e, c)
    return "€%s.%s" % (e, c)

# --------------------------------------------------------------- contenu
#
#  Six duels, six maisons. Les familles viennent des etiquettes des fiches
#  Shopify, relevees le 12/11. On ne dit jamais lequel est le meilleur.

F = {  # les familles, telles qu'elles sont ecrites sur les fiches
 "iris":    {"fr": "Iris et fleurs blanches", "en": "Iris and white flowers",
             "nl": "Iris en witte bloemen",   "de": "Iris und weiße Blüten"},
 "agrumes": {"fr": "Agrumes et aromates", "en": "Citrus and aromatics",
             "nl": "Citrus en aromaten",  "de": "Zitrus und Aromaten"},
 "oud":     {"fr": "Oud et bois précieux", "en": "Oud and precious woods",
             "nl": "Oud en edelhout",       "de": "Oud und Edelhölzer"},
 "marin":   {"fr": "Marin et chypré", "en": "Marine and chypre",
             "nl": "Marine en chypre", "de": "Marine und Chypre"},
 "rose":    {"fr": "Rose", "en": "Rose", "nl": "Roos", "de": "Rose"},
 "encens":  {"fr": "Encens et résines", "en": "Incense and resins",
             "nl": "Wierook en harsen",   "de": "Weihrauch und Harze"},
 "gourmand":{"fr": "Gourmand praliné et sucré", "en": "Gourmand, praline and sweet",
             "nl": "Gourmand, praline en zoet",    "de": "Gourmand, Praline und süß"},
 "fruits":  {"fr": "Fruits rouges et fruits mûrs", "en": "Red and ripe fruits",
             "nl": "Rood en rijp fruit",            "de": "Rote und reife Früchte"},
}

DUELS = [
 dict(maison="AFNAN",
      a=dict(ean="6290171002338", nom="9pm", ml="100 ML", p=40.90, f="iris"),
      b=dict(ean="6290171002345", nom="9am", ml="100 ML", p=36.90, f="agrumes"),
      mot={"fr": "Le nom dit l'heure.", "en": "The name tells you the hour.",
           "nl": "De naam zegt het uur.", "de": "Der Name nennt die Stunde."}),
 dict(maison="LATTAFA",
      a=dict(ean="6291106066890", nom="Ana Abiyedh", ml="60 ML", p=25.90, f="oud"),
      b=dict(ean="6291107454412", nom="Ana Abiyedh Rouge", ml="60 ML", p=24.90, f="marin"),
      mot={"fr": "Le blanc ou le rouge.", "en": "The white or the red.",
           "nl": "De witte of de rode.", "de": "Das wei\u00dfe oder das rote."}),
 dict(maison="AL HARAMAIN",
      a=dict(ean="6291100139668", nom="L'aventure", ml="100 ML", p=38.90, f="iris"),
      b=dict(ean="6291100137565", nom="Aventure Femme", ml="100 ML", p=43.90, f="rose"),
      mot={"fr": "La m\u00eame aventure, deux chemins.",
           "en": "The same adventure, two roads.",
           "nl": "Hetzelfde avontuur, twee wegen.",
           "de": "Dasselbe Abenteuer, zwei Wege."}),
 dict(maison="FRENCH AVENUE",
      a=dict(ean="6290360378053", nom="Vulcan Feu", ml="100 ML", p=48.90, f="oud"),
      b=dict(ean="6290360378060", nom="Vulcan Sable", ml="100 ML", p=39.90, f="encens"),
      mot={"fr": "Le feu ou le sable.", "en": "The fire or the sand.",
           "nl": "Het vuur of het zand.", "de": "Das Feuer oder der Sand."}),
 dict(maison="GULF ORCHID",
      a=dict(ean="6290362162629", nom="Mango Ice", ml="100 ML", p=36.90, f="gourmand"),
      b=dict(ean="6290362162643", nom="Creme Caramel", ml="100 ML", p=36.90, f="agrumes"),
      mot={"fr": "Tu choisis au nez.",
           "en": "You choose with your nose.",
           "nl": "Je kiest met je neus.",
           "de": "Sie wählen mit der Nase."}),
 dict(maison="ARMAF",
      a=dict(ean="6085010044712", nom="Club de Nuit Intense Man", ml="105 ML", p=40.90, f="fruits"),
      b=dict(ean="6294015164152", nom="Club de Nuit Iconic", ml="105 ML", p=53.90, f="agrumes"),
      mot={"fr": "La m\u00eame Club de Nuit.", "en": "The same Club de Nuit.",
           "nl": "Dezelfde Club de Nuit.", "de": "Dieselbe Club de Nuit."}),
]

# ALLEMAND : vouvoiement (Sie). NEERLANDAIS : tutoiement sur les reseaux.
T = {
 "fr": dict(t1a="Lequel tu mets ?", t1s="Six duels. Six fois deux parfums de la "
                 "même maison. À toi de trancher.",
            t1p="DIS-LE EN COMMENTAIRE",
            t2a="On ne choisit pas", t2b="un parfum au prix.",
            t2c="Dans chaque duel, les deux sortent de la même maison, souvent "
                "de la même ligne. Ce qui change, c'est la famille.",
            t2d="Ça ne se discute pas. Ça se sent.",
            t2p="PREMIER DUEL", ou="OU",
            o1="Avant de partir.",
            o=[("2 flacons", "la livraison est offerte"),
               ("3 flacons", "livraison offerte et −5 %"),
               ("10 %", "du bénéfice part en sadaqa")],
            f1="Tu as choisi", f2="lequel ?",
            f3="Écris-le en commentaire. Et enregistre le carrousel pour "
               "le jour où tu commandes."),
 "en": dict(t1a="Which one do you wear?", t1s="Six duels. Six times two perfumes "
                 "from the same house. You decide.",
            t1p="SAY IT IN THE COMMENTS",
            t2a="You don't pick a perfume", t2b="by its price.",
            t2c="In every duel, both come from the same house, often from the "
                "same line. What changes is the family.",
            t2d="That isn't up for debate. You smell it.",
            t2p="FIRST DUEL", ou="OR",
            o1="Before you go.",
            o=[("2 bottles", "delivery is free"),
               ("3 bottles", "free delivery and −5%"),
               ("10%", "of the profit goes to sadaqa")],
            f1="Which one", f2="did you pick?",
            f3="Tell me in the comments. And save the carousel for the day "
               "you order."),
 "nl": dict(t1a="Welke draag jij?", t1s="Zes duels. Zes keer twee parfums van "
                 "hetzelfde huis. Jij kiest.",
            t1p="ZEG HET IN DE REACTIES",
            t2a="Je kiest een parfum", t2b="niet op de prijs.",
            t2c="In elk duel komen ze allebei van hetzelfde huis, vaak uit "
                "dezelfde lijn. Wat verschilt, is de familie.",
            t2d="Daar valt niet over te praten. Dat ruik je.",
            t2p="EERSTE DUEL", ou="OF",
            o1="Voor je weggaat.",
            o=[("2 flacons", "gratis levering"),
               ("3 flacons", "gratis levering en −5 %"),
               ("10 %", "van de winst gaat naar sadaqa")],
            f1="Welke heb jij", f2="gekozen?",
            f3="Zet het in de reacties. En bewaar het carrousel voor de dag "
               "dat je bestelt."),
 "de": dict(t1a="Welches tragen Sie?", t1s="Sechs Duelle. Sechsmal zwei Parfums "
                 "aus demselben Haus. Sie entscheiden.",
            t1p="SCHREIBEN SIE ES IN DIE KOMMENTARE",
            t2a="Ein Parfum wählt man", t2b="nicht nach dem Preis.",
            t2c="In jedem Duell stammen beide aus demselben Haus, oft aus "
                "derselben Linie. Was sich ändert, ist die Familie.",
            t2d="Darüber lässt sich nicht streiten. Das riecht man.",
            t2p="ERSTES DUELL", ou="ODER",
            o1="Bevor Sie gehen.",
            o=[("2 Flakons", "Versand kostenlos"),
               ("3 Flakons", "Versand kostenlos und −5 %"),
               ("10 %", "des Gewinns gehen als Sadaqa")],
            f1="Welches haben Sie", f2="gewählt?",
            f3="Schreiben Sie es in die Kommentare. Und speichern Sie das "
               "Karussell für den Tag Ihrer Bestellung."),
}

ECART = {
 "fr": ("Exactement le m\u00eame prix.", "%s d'\u00e9cart."),
 "en": ("Exactly the same price.",        "%s apart."),
 "nl": ("Precies dezelfde prijs.",        "%s verschil."),
 "de": ("Genau derselbe Preis.",          "%s Unterschied."),
}

def ligne_ecart(duel, lg):
    """L'ecart se CALCULE. Comme ca il ne peut pas etre faux."""
    e = abs(round(duel["a"]["p"] - duel["b"]["p"], 2))
    pareil, modele = ECART[lg]
    tete = pareil if e < 0.005 else modele % prix(e, lg)
    return "%s %s" % (tete, duel["mot"][lg])

LANGUES = ("fr", "en", "nl", "de")

# ------------------------------------------------------------- garde-fou

def garde_fou():
    maisons = [d["maison"] for d in DUELS]
    assert len(set(maisons)) == len(DUELS), "deux duels de la meme maison"
    for d in DUELS:
        assert d["a"]["f"] != d["b"]["f"], \
            "duel sans contraste de famille : " + d["maison"]
        for lg in ("fr", "en", "nl", "de"):
            assert d["mot"].get(lg), "phrase manquante : %s / %s" % (d["maison"], lg)
        for c in ("a", "b"):
            e = d[c]["ean"]
            assert os.path.exists(os.path.join(SCENES, e + "c.jpg")), \
                "scene manquante : " + e
    # 11/11 et 12/11. La regle de la variation les interdit.
    deja = {"6291107019758", "6291100137268", "6290361911563",
            "6290360375694", "6291108730362",            # 11/11
            "6290360591421", "6294015149371", "5055810030094",
            "6290360375687", "6293708015627", "5060908999146"}  # 12/11
    pris = {d[c]["ean"] for d in DUELS for c in ("a", "b")}
    assert not (deja & pris), "parfum deja employe : %s" % (deja & pris)
    for lg in LANGUES:
        for cle in ("t1a", "t1s", "t2a", "t2b", "t2c", "t2d", "o1", "f1", "f2", "f3"):
            assert T[lg].get(cle), "texte manquant : %s / %s" % (lg, cle)
        assert len(T[lg]["o"]) == 3

# ----------------------------------------------------------- les diapos

def ecran_double(a, b, hauteur=1000):
    """Les deux flacons cote a cote. Le panneau de droite est recadre vers la
    gauche pour que le flacon ne finisse pas sous la pile de boutons."""
    img = Image.new("RGB", (W, hauteur), CREME)
    img.paste(panneau(a["ean"], W // 2, hauteur, 0.52), (0, 0))
    img.paste(panneau(b["ean"], W // 2, hauteur, 0.38), (W // 2, 0))
    d = ImageDraw.Draw(img)
    d.line([(W // 2, 0), (W // 2, hauteur)], fill=CREME, width=4)
    return img

def diapo_1(lg):
    t = T[lg]
    img = Image.new("RGB", (W, H), CREME)
    nom = os.path.join(PHOTOS, "duel1.jpg")
    if os.path.exists(nom):
        # 45 et pas 90 : a 90 la signature touche les cheveux et « HOME » se
        # perd dans le noir. Valeur testee par Claude Code le 12/11.
        img.paste(photo("duel1.jpg", 1060, 45), (0, 0))
        fondu(img, 880, 180)
    else:
        img.paste(ecran_double(DUELS[0]["a"], DUELS[0]["b"], 1060), (0, 0))
        fondu(img, 880, 180)
    poser_signature(img, MARGE_G, HAUT_SUR + 20,
                    couleur_signature(img, MARGE_G, HAUT_SUR + 20), 30)
    d = ImageDraw.Draw(img)
    y = bloc_ajuste(d, MARGE_G, 1082, t["t1a"], 76, ENCRE, LARGE, 1240,
                    1.10, poids=700, mini=50)
    y += 32
    bloc_ajuste(d, MARGE_G, y, t["t1s"], 40, ENCRE_D, LARGE, 1366,
                1.26, poids=430, ital=True)
    d.line([(MARGE_G, 1390), (MARGE_G + 180, 1390)], fill=OCRE, width=4)
    lettrage(d, 1428, t["t1p"], inter(24, "SemiBold"), OCRE, 6)
    return img

def diapo_2(lg):
    t = T[lg]
    img = Image.new("RGB", (W, H), CREME)
    poser_signature(img, MARGE_G, HAUT_SUR + 20, ENCRE_D, 30)
    d = ImageDraw.Draw(img)
    y = bloc_ajuste(d, MARGE_G, 420, [(t["t2a"], ENCRE), (t["t2b"], ORANGE)],
                    88, ENCRE, LARGE + 120, 700, 1.10, poids=700, mini=54)
    y += 64
    y = bloc_ajuste(d, MARGE_G, y, t["t2c"], 50, ENCRE_D, LARGE, 1100,
                    1.32, poids=440)
    y += 40
    bloc_ajuste(d, MARGE_G, y, t["t2d"], 52, ENCRE, LARGE, 1306, 1.26, poids=620)
    d.line([(MARGE_G, 1330), (MARGE_G + 180, 1330)], fill=OCRE, width=4)
    lettrage(d, 1388, t["t2p"], inter(26, "SemiBold"), OCRE, 6)
    return img

def ligne_parfum(img, d, y, c, lg, couleur_nom):
    """Un cote du duel : le nom, puis la famille a gauche et le prix a droite."""
    lmax = LARGE + 120
    for corps in range(54, 32, -2):
        pn = serif(corps, 680)
        if d.textlength(c["nom"], font=pn) <= lmax:
            break
    d.text((MARGE_G, y), c["nom"], font=pn, fill=couleur_nom, anchor="la")
    y2 = y + int(corps * 1.12)
    d.text((MARGE_G, y2), F[c["f"]][lg], font=serif(32, 500, ital=True),
           fill=ENCRE_D, anchor="la")
    d.text((W - MARGE_D, y2 + 6), "%s · %s" % (prix(c["p"], lg), c["ml"]),
           font=inter(30, "SemiBold"), fill=ENCRE, anchor="ra")
    return y2 + 54

def diapo_duel(duel, n, lg):
    img = Image.new("RGB", (W, H), CREME)
    # duel1.jpg est la COUVERTURE : on ne la remet pas en diapo 3, sinon les
    # deux premieres vignettes du profil sont la meme image.
    nom = "duel%d.jpg" % n
    if n != 1 and os.path.exists(os.path.join(PHOTOS, nom)):
        # duel6 a son petit texte « club de nuit » plus bas : on descend un
        # peu plus la fenetre pour qu'il reste net. Note de Claude Code.
        img.paste(photo(nom, 1040, 220 if n == 6 else 150), (0, 0))
    else:
        img.paste(ecran_double(duel["a"], duel["b"], 1040), (0, 0))
    fondu(img, 840, 200)
    poser_signature(img, MARGE_G, HAUT_SUR + 20,
                    couleur_signature(img, MARGE_G, HAUT_SUR + 20), 28)
    d = ImageDraw.Draw(img)

    lettrage(d, 1052, "%d / 6   ·   %s" % (n, duel["maison"]),
             inter(28, "SemiBold"), ORANGE, 6)
    y = ligne_parfum(img, d, 1086, duel["a"], lg, ENCRE)

    # le trait avec « OU » pose dessus
    p = inter(26, "SemiBold")
    mot = T[lg]["ou"]
    larg = d.textlength(mot, font=p) + 28
    d.line([(MARGE_G, y + 14), (W - MARGE_D, y + 14)], fill=(206, 190, 164), width=2)
    d.rectangle([MARGE_G + 60, y - 4, MARGE_G + 60 + larg, y + 32], fill=CREME)
    d.text((MARGE_G + 60 + larg / 2, y + 14), mot, font=p, fill=OCRE, anchor="mm")

    ligne_parfum(img, d, y + 52, duel["b"], lg, ENCRE)

    d.line([(MARGE_G, 1364), (W - MARGE_D, 1364)], fill=(206, 190, 164), width=2)
    bloc_ajuste(d, MARGE_G, 1392, ligne_ecart(duel, lg), 36, ENCRE_D,
                LARGE, 1444, 1.20, poids=480, ital=True)
    return img

def diapo_offre(lg):
    t = T[lg]
    img = Image.new("RGB", (W, H), ENCRE)
    poser_signature(img, MARGE_G, HAUT_SUR + 20, CREME, 30)
    d = ImageDraw.Draw(img)
    y = bloc_ajuste(d, MARGE_G, 420, t["o1"], 90, CREME, LARGE + 160, 620,
                    1.10, poids=700, mini=58)
    y += 70
    for gros, petit in t["o"]:
        d.text((MARGE_G, y), gros, font=serif(70, 680), fill=(226, 176, 120),
               anchor="la")
        y += 86
        y = bloc_ajuste(d, MARGE_G, y, petit, 44, CREME, LARGE, y + 120,
                        1.20, poids=430, mini=32)
        y += 44
    d.line([(MARGE_G, 1330), (MARGE_G + 180, 1330)], fill=(226, 176, 120), width=4)
    lettrage(d, 1388, LIEN.upper(), inter(28, "SemiBold"), (226, 176, 120), 6)
    return img

def diapo_fin(lg):
    t = T[lg]
    img = Image.new("RGB", (W, H), CREME)
    img.paste(ecran_double(DUELS[4]["a"], DUELS[4]["b"], 900), (0, 0))
    fondu(img, 560, 340)
    poser_signature(img, MARGE_G, HAUT_SUR + 20,
                    couleur_signature(img, MARGE_G, HAUT_SUR + 20), 30)
    d = ImageDraw.Draw(img)
    y = bloc_ajuste(d, MARGE_G, 980, [(t["f1"], ENCRE), (t["f2"], ORANGE)],
                    86, ENCRE, LARGE + 160, 1190, 1.10, poids=700, mini=50)
    y += 40
    bloc_ajuste(d, MARGE_G, y, t["f3"], 42, ENCRE_D, LARGE, 1330, 1.26, poids=440)
    d.line([(MARGE_G, 1348), (W - MARGE_D, 1348)], fill=(206, 190, 164), width=2)
    lettrage(d, 1400, LIEN.upper(), inter(28, "SemiBold"), OCRE, 6)
    return img

def main():
    garde_fou()
    for lg in LANGUES:
        dossier = os.path.join(SORTIE, lg)
        os.makedirs(dossier, exist_ok=True)
        pages = [diapo_1(lg), diapo_2(lg)]
        for i, duel in enumerate(DUELS, 1):
            pages.append(diapo_duel(duel, i, lg))
        pages += [diapo_offre(lg), diapo_fin(lg)]
        assert len(pages) == 10, "il faut dix diapos, pas %d" % len(pages)
        for i, im in enumerate(pages, 1):
            im.save(os.path.join(dossier, "%02d.jpg" % i), "JPEG",
                    quality=92, optimize=True)
        print(lg, "->", len(pages), "diapos")

if __name__ == "__main__":
    main()
