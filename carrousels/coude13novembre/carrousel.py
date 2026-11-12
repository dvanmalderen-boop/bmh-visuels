# -*- coding: utf-8 -*-
"""
BMH - carrousel du 13 novembre 2026.  FORMAT TIKTOK 1080 x 1920.

MECANIQUE : L'ENDROIT OU ON LE MET.  Pas le parfum : le geste.
Diapo 1 accuse, diapo 2 donne la raison, six diapos posent six endroits
AU-DESSUS DU COUDE, puis l'offre, puis la demande d'enregistrement.

POURQUOI CETTE MECANIQUE ET PAS UNE AUTRE
05 et 06/11 l'elimination, 07/11 « le nom ment », 08/11 l'echelle du sucre,
09/11 la plaque constante, 10/11 la coupure en deux, 11/11 les heures.
La regle de la variation interdit de reprendre l'une des six. Ici ce n'est ni
un classement ni une progression : c'est une ACCUSATION suivie d'un remede.

RIEN N'EST INVENTE.
- Le woudou lave les bras jusqu'aux coudes. C'est le fait qui porte tout le
  carrousel, et c'est Daoud qui l'a apporte le 12/11.
- Les six familles olfactives sortent des fiches francaises, relevees sur
  Shopify et deja utilisees dans les carrousels des 09, 10 et 11/11. Aucune
  note, aucune tenue, aucun chiffre de longevite n'est avance ici.
- Les six endroits sont des ENDROITS, pas des promesses. On ne dit nulle part
  qu'un parfum tient plus longtemps a tel endroit : on dit ou le poser pour
  qu'il survive au woudou. C'est verifiable, ca.

LE STOCK ET LES MARGES ONT ETE VERIFIES, ET LES DEUX, le 12/11 sur
bts/rapports/marges.json : les six sont in_stock, marges 9,75 a 12,42 EUR.
SIX MAISONS DIFFERENTES ET SIX FAMILLES DIFFERENTES. Le garde-fou le verifie.

AUCUN DES CINQ PARFUMS DU 11/11 N'EST REPRIS.

ZONES TIKTOK : l'interface mange 150 px en haut, 480 px en bas, 120 px a
droite. Tout le texte vit entre y=200 et y=1400, et s'arrete a x=900.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H    = 1080, 1920
RACINE  = "/home/claude/coude"
SCENES  = os.path.join(RACINE, "scenes")
POLICES = "/home/claude/polices"
SORTIE  = os.path.join(RACINE, "carrousel")

CREME    = (240, 228, 206)
ENCRE    = (46, 33, 23)
ENCRE_D  = (92, 70, 51)
ORANGE   = (234, 88, 12)
OCRE     = (181, 85, 31)
BLANC    = (255, 255, 255)

LIEN = "shop.bringmedinahome.com"

HAUT_SUR  = 200    # sous la barre haute de TikTok
BAS_SUR   = 1400   # au-dessus du pseudo, de la legende et de la progression
MARGE_G   = 96
MARGE_D   = 180    # la pile de boutons de TikTok mange la droite
LARGE     = W - MARGE_G - MARGE_D

# --------------------------------------------------------------- polices

def serif(corps, poids=600, opsz=72, ital=False):
    chemin = os.path.join(POLICES,
                          "Newsreader-Italic.ttf" if ital else "Newsreader.ttf")
    f = ImageFont.truetype(chemin, corps)
    f.set_variation_by_axes([poids, opsz])
    return f

def inter(corps, graisse="Medium"):
    return ImageFont.truetype(
        "/usr/share/fonts/opentype/inter/Inter-%s.otf" % graisse, corps)

def couper(d, texte, police, lmax):
    mots, lignes, courante = texte.split(), [], ""
    for m in mots:
        essai = (courante + " " + m).strip()
        if d.textlength(essai, font=police) <= lmax:
            courante = essai
        else:
            if courante:
                lignes.append(courante)
            courante = m
    if courante:
        lignes.append(courante)
    return lignes

def bloc(d, x, y, texte, police, couleur, lmax, interligne=1.18, centre=False):
    """Pose un paragraphe et rend l'ordonnee de sortie."""
    lignes = couper(d, texte, police, lmax)
    pas = int(police.size * interligne)
    for l in lignes:
        if centre:
            d.text((x + lmax / 2, y), l, font=police, fill=couleur, anchor="ma")
        else:
            d.text((x, y), l, font=police, fill=couleur, anchor="la")
        y += pas
    return y

def hauteur_bloc(d, texte, police, lmax, interligne):
    return len(couper(d, texte, police, lmax)) * int(police.size * interligne)

def bloc_ajuste(d, x, y, textes, corps, couleur, lmax, y_max,
                interligne=1.28, poids=430, ital=False, mini=26):
    """Pose une ou plusieurs lignes en reduisant le corps jusqu'a ce que
    l'ensemble tienne au-dessus de y_max. C'est ce qui empeche l'allemand
    de pousser le texte dans le filet du pied."""
    if isinstance(textes, str):
        textes = [(textes, couleur)]
    elif textes and isinstance(textes[0], str):
        textes = [(t, couleur) for t in textes]
    for c in range(corps, mini - 1, -2):
        p = serif(c, poids, 72, ital)
        h = sum(hauteur_bloc(d, t, p, lmax, interligne) for t, _ in textes)
        if y + h <= y_max:
            break
    for t, coul in textes:
        y = bloc(d, x, y, t, p, coul, lmax, interligne)
    return y

def lettrage(d, y, texte, police, couleur, espace=6, x=MARGE_G):
    for c in texte:
        d.text((x, y), c, font=police, fill=couleur, anchor="lm")
        x += d.textlength(c, font=police) + espace

# ---------------------------------------------------------------- marque

def poser_signature(img, x, y, couleur, corps=30, espace=7):
    r = int(corps * 0.52)
    taille = r * 2 + 2
    lune = Image.new("L", (taille * 4, taille * 4), 0)
    dl = ImageDraw.Draw(lune)
    R = r * 4
    dl.ellipse([2, 2, 2 + R * 2, 2 + R * 2], fill=255)
    dec = int(R * 0.52)
    dl.ellipse([2 + dec, 2 - R * 0.06, 2 + dec + R * 2, 2 - R * 0.06 + R * 2],
               fill=0)
    lune = lune.resize((taille, taille), Image.LANCZOS)
    teinte = Image.new("RGB", (taille, taille), couleur)
    img.paste(teinte, (int(x), int(y - taille / 2)), lune)

    d = ImageDraw.Draw(img)
    cx = x + taille + corps * 0.75
    p = inter(corps, "SemiBold")
    for c in "BRING MEDINA HOME":
        d.text((cx, y), c, font=p, fill=couleur, anchor="lm")
        cx += d.textlength(c, font=p) + espace
    pr = inter(int(corps * 0.55), "Medium")
    d.text((cx - espace + 4, y - corps * 0.42), "®", font=pr,
           fill=couleur, anchor="lm")

# ---------------------------------------------------------------- decors

def scene(ean, hauteur, flou=0):
    im = Image.open(os.path.join(SCENES, ean + "c.jpg")).convert("RGB")
    im = im.resize((W, W), Image.LANCZOS)
    haut = int((W - hauteur) * 0.42) if hauteur < W else 0
    if hauteur > W:
        im = im.resize((int(W * hauteur / W), hauteur), Image.LANCZOS)
        im = im.crop(((im.width - W) // 2, 0, (im.width - W) // 2 + W, hauteur))
    else:
        im = im.crop((0, haut, W, haut + hauteur))
    if flou:
        im = im.filter(ImageFilter.GaussianBlur(flou))
    return im

def fondu(img, depart, hauteur, vers=CREME):
    voile = Image.new("RGBA", (W, hauteur), vers + (0,))
    d = ImageDraw.Draw(voile)
    for i in range(hauteur):
        p = i / max(hauteur - 1, 1)
        d.line([(0, i), (W, i)], fill=vers + (int((p ** 1.6) * 255),))
    img.paste(voile, (0, depart), voile)

def prix_affiche(v, lg):
    e, c = ("%.2f" % v).split(".")
    if lg in ("fr", "de"):
        return "%s,%s €" % (e, c)
    if lg == "nl":
        return "€ %s,%s" % (e, c)
    return "€%s.%s" % (e, c)

# --------------------------------------------------------------- contenu
#
#  Six maisons, six familles, six endroits. Tous AU-DESSUS DU COUDE.
#  Les familles sont celles des fiches francaises. Les endroits sont des
#  endroits : aucune promesse de tenue n'est faite nulle part.

PRODUITS = [
    dict(ean="6290360591421", titre="Lattafa Yara Moi", ml="100 ML", prix=32.90,
         famille={"fr": "Gourmand pralin\u00e9 et sucr\u00e9",
                  "en": "Gourmand, praline and sweet",
                  "nl": "Gourmand, praline en zoet",
                  "de": "Gourmand, Praline und s\u00fc\u00df"},
         endroit={"fr": "LE HAUT DU BRAS", "en": "THE UPPER ARM",
                  "nl": "DE BOVENARM",     "de": "DER OBERARM"},
         ligne={"fr": "Deux pressions sur le haut du bras, sous la manche. "
                      "L'eau s'arr\u00eate au coude.",
                "en": "Two sprays on the upper arm, under the sleeve. "
                      "The water stops at the elbow.",
                "nl": "Twee keer op je bovenarm, onder de mouw. "
                      "Het water stopt bij de elleboog.",
                "de": "Zwei Spr\u00fchst\u00f6\u00dfe auf den Oberarm, unter dem \u00c4rmel. "
                      "Das Wasser endet am Ellenbogen."}),

    dict(ean="6294015149371", titre="Armaf Odyssey Mandarin Sky", ml="100 ML", prix=32.90,
         famille={"fr": "Agrumes et aromates", "en": "Citrus and aromatics",
                  "nl": "Citrus en aromaten",  "de": "Zitrus und Aromaten"},
         endroit={"fr": "LA NUQUE", "en": "THE NAPE",
                  "nl": "DE NEK",   "de": "DER NACKEN"},
         ligne={"fr": "La nuque ne passe pas sous le robinet. "
                      "Ceux derri\u00e8re toi la re\u00e7oivent.",
                "en": "The nape never goes under the tap. "
                      "The people behind you get it.",
                "nl": "Je nek gaat nooit onder de kraan. "
                      "De mensen achter je ruiken hem.",
                "de": "Der Nacken kommt nie unter den Wasserhahn. "
                      "Die Menschen hinter Ihnen riechen ihn."}),

    dict(ean="5055810030094", titre="Al Wataniah Qahir", ml="100 ML", prix=32.90,
         famille={"fr": "Tabac et caf\u00e9", "en": "Tobacco and coffee",
                  "nl": "Tabak en koffie",  "de": "Tabak und Kaffee"},
         endroit={"fr": "LE COL DU QAMIS", "en": "THE COLLAR",
                  "nl": "DE KRAAG",         "de": "DER KRAGEN"},
         ligne={"fr": "Sur le col, pas sur la peau. Le v\u00eatement, lui, "
                      "ne se lave pas avant la pri\u00e8re.",
                "en": "On the collar, not on the skin. "
                      "The garment is not washed before prayer.",
                "nl": "Op de kraag, niet op de huid. "
                      "Je kleren was je niet voor het gebed.",
                "de": "Auf den Kragen, nicht auf die Haut. "
                      "Die Kleidung wird vor dem Gebet nicht gewaschen."}),

    dict(ean="6290360375687", titre="French Avenue Azzure Aoud", ml="100 ML", prix=36.90,
         famille={"fr": "Oud et bois pr\u00e9cieux", "en": "Oud and precious woods",
                  "nl": "Oud en edelhout",          "de": "Oud und Edelh\u00f6lzer"},
         endroit={"fr": "DERRI\u00c8RE L'OREILLE", "en": "BEHIND THE EAR",
                  "nl": "ACHTER HET OOR",        "de": "HINTER DEM OHR"},
         ligne={"fr": "Un oud se pose haut et une seule fois. "
                      "Derri\u00e8re l'oreille, pas trois pressions.",
                "en": "An oud goes high, and only once. "
                      "Behind the ear, not three sprays.",
                "nl": "Een oud zet je hoog, en \u00e9\u00e9n keer. "
                      "Achter het oor, geen drie keer.",
                "de": "Ein Oud kommt nach oben, und nur einmal. "
                      "Hinter das Ohr, keine drei Spr\u00fchst\u00f6\u00dfe."}),

    dict(ean="6293708015627", titre="Ajmal Amaze", ml="100 ML", prix=32.90,
         famille={"fr": "Cuir et miel", "en": "Leather and honey",
                  "nl": "Leer en honing", "de": "Leder und Honig"},
         endroit={"fr": "L'\u00c9PAULE", "en": "THE SHOULDER",
                  "nl": "DE SCHOUDER",  "de": "DIE SCHULTER"},
         ligne={"fr": "L'\u00e9paule reste s\u00e8che du d\u00e9but \u00e0 la fin. "
                      "Personne n'y pense jamais.",
                "en": "The shoulder stays dry from start to finish. "
                      "Nobody ever thinks of it.",
                "nl": "Je schouder blijft droog van begin tot eind. "
                      "Niemand denkt eraan.",
                "de": "Die Schulter bleibt von Anfang bis Ende trocken. "
                      "Niemand denkt daran."}),

    dict(ean="5060908999146", titre="Ayat Creek Dubai", ml="30 ML", prix=21.90,
         famille={"fr": "Encens et r\u00e9sines", "en": "Incense and resins",
                  "nl": "Wierook en harsen",    "de": "Weihrauch und Harze"},
         endroit={"fr": "LE REVERS DE LA VESTE", "en": "THE INSIDE POCKET",
                  "nl": "DE BINNENZAK",          "de": "DIE INNENTASCHE"},
         ligne={"fr": "Trente millilitres dans la poche. "
                      "Celui-l\u00e0, on le remet en sortant.",
                "en": "Thirty millilitres in your pocket. "
                      "That one you put back on the way out.",
                "nl": "Dertig milliliter in je zak. "
                      "Die doe je er weer op als je buitenkomt.",
                "de": "Drei\u00dfig Milliliter in der Tasche. "
                      "Dieses tragen Sie beim Hinausgehen erneut auf."}),
]

# Les textes fixes des quatre diapos qui ne portent pas de parfum.
# ALLEMAND : vouvoiement (Sie). NEERLANDAIS : tutoiement sur les reseaux.
TEXTES = {
 "fr": dict(
   t1a="Tu mets ton parfum", t1b="au mauvais endroit.",
   t1s="Six endroits que l'eau n'atteint pas, et six parfums \u00e0 y poser.",
   t1p="ON COMMENCE PAR LE COUDE",
   t2a="Le woudou lave", t2b="jusqu'au coude.",
   t2c="Tout ce que tu as mis sous le coude part \u00e0 chaque ablution. "
       "Le poignet, l'avant-bras, le dos de la main : il n'en reste rien.",
   t2d="Au-dessus du coude, l'eau ne passe pas.",
   t2p="SIX ENDROITS, SIX PARFUMS",
   o1="Avant de partir.",
   o=[("2 flacons", "la livraison est offerte"),
      ("3 flacons", "livraison offerte et \u22125 %"),
      ("10 %",      "du b\u00e9n\u00e9fice part en sadaqa")],
   f1="Enregistre-le", f2="pour vendredi.",
   f3="Et envoie-le \u00e0 celui qui met encore son parfum sur les poignets."),
 "en": dict(
   t1a="You put your perfume", t1b="in the wrong place.",
   t1s="Six places the water never reaches, and six perfumes to wear there.",
   t1p="WE START AT THE ELBOW",
   t2a="Wudu washes", t2b="up to the elbow.",
   t2c="Everything you put below the elbow goes with every ablution. "
       "The wrist, the forearm, the back of the hand: nothing is left.",
   t2d="Above the elbow, the water never reaches.",
   t2p="SIX PLACES, SIX PERFUMES",
   o1="Before you go.",
   o=[("2 bottles", "delivery is free"),
      ("3 bottles", "free delivery and \u22125%"),
      ("10%",       "of the profit goes to sadaqa")],
   f1="Save it", f2="for Friday.",
   f3="And send it to the one who still sprays his perfume on his wrists."),
 "nl": dict(
   t1a="Je zet je parfum", t1b="op de verkeerde plek.",
   t1s="Zes plekken waar het water niet komt, en zes parfums om daar te dragen.",
   t1p="WE BEGINNEN BIJ DE ELLEBOOG",
   t2a="Woedoe wast", t2b="tot aan de elleboog.",
   t2c="Alles wat je onder de elleboog zet, gaat weg bij elke wassing. "
       "De pols, de onderarm, de rug van je hand: er blijft niets van over.",
   t2d="Boven de elleboog komt het water niet.",
   t2p="ZES PLEKKEN, ZES PARFUMS",
   o1="Voor je weggaat.",
   o=[("2 flacons", "gratis levering"),
      ("3 flacons", "gratis levering en \u22125 %"),
      ("10 %",      "van de winst gaat naar sadaqa")],
   f1="Bewaar hem", f2="voor vrijdag.",
   f3="En stuur hem door naar wie zijn parfum nog op zijn polsen zet."),
 "de": dict(
   t1a="Sie tragen Ihr Parfum", t1b="an der falschen Stelle.",
   t1s="Sechs Stellen, die das Wasser nicht erreicht, und sechs Parfums daf\u00fcr.",
   t1p="WIR BEGINNEN AM ELLENBOGEN",
   t2a="Wudu w\u00e4scht", t2b="bis zum Ellenbogen.",
   t2c="Alles, was Sie unterhalb des Ellenbogens auftragen, geht bei jeder "
       "Waschung verloren. Handgelenk, Unterarm, Handr\u00fccken: nichts bleibt.",
   t2d="Oberhalb des Ellenbogens kommt das Wasser nicht hin.",
   t2p="SECHS STELLEN, SECHS PARFUMS",
   o1="Bevor Sie gehen.",
   o=[("2 Flakons", "Versand kostenlos"),
      ("3 Flakons", "Versand kostenlos und \u22125 %"),
      ("10 %",      "des Gewinns gehen als Sadaqa")],
   f1="Speichern Sie ihn", f2="f\u00fcr Freitag.",
   f3="Und schicken Sie ihn weiter an den, der sein Parfum noch auf die "
      "Handgelenke spr\u00fcht."),
}

# ------------------------------------------------------------- garde-fou

LANGUES = ("fr", "en", "nl", "de")

def garde_fou():
    maisons = [p["titre"].split()[0] for p in PRODUITS]
    assert len(set(maisons)) == len(PRODUITS), "deux parfums de la meme maison"
    for lg in LANGUES:
        fam = [p["famille"][lg] for p in PRODUITS]
        end = [p["endroit"][lg] for p in PRODUITS]
        assert len(set(fam)) == len(PRODUITS), "deux fois la meme famille en " + lg
        assert len(set(end)) == len(PRODUITS), "deux fois le meme endroit en " + lg
        for cle in ("t1a", "t1b", "t1s", "t2a", "t2b", "t2c", "t2d",
                    "o1", "f1", "f2", "f3"):
            assert TEXTES[lg].get(cle), "texte manquant : %s / %s" % (lg, cle)
        assert len(TEXTES[lg]["o"]) == 3, "il faut trois lignes d'offre en " + lg
    for p in PRODUITS:
        assert os.path.exists(os.path.join(SCENES, p["ean"] + "c.jpg")), \
            "scene manquante : " + p["ean"]
    # le 11/11 a utilise ces cinq-la. La regle de la variation les interdit.
    hier = {"6291107019758", "6291100137268", "6290361911563",
            "6290360375694", "6291108730362"}
    assert not (hier & {p["ean"] for p in PRODUITS}), "parfum repris d'hier"

# ----------------------------------------------------------- les diapos

def diapo_1(lg):
    T = TEXTES[lg]
    img = Image.new("RGB", (W, H), CREME)
    img.paste(scene("6290360591421", 980, flou=3), (0, 0))
    fondu(img, 520, 460)
    poser_signature(img, MARGE_G, HAUT_SUR + 20, BLANC, 30)
    d = ImageDraw.Draw(img)

    y = 980
    y = bloc_ajuste(d, MARGE_G, y, [T["t1a"], T["t1b"]], 76, ENCRE,
                    LARGE, 1200, 1.10, poids=700, mini=44)
    y += 40
    bloc_ajuste(d, MARGE_G, y, T["t1s"], 42, ENCRE_D, LARGE, 1306,
                1.28, poids=430, ital=True)

    d.line([(MARGE_G, 1330), (MARGE_G + 180, 1330)], fill=OCRE, width=4)
    lettrage(d, 1388, T["t1p"], inter(28, "SemiBold"), OCRE, 7)
    return img

def diapo_2(lg):
    T = TEXTES[lg]
    img = Image.new("RGB", (W, H), CREME)
    poser_signature(img, MARGE_G, HAUT_SUR + 20, ENCRE_D, 30)
    d = ImageDraw.Draw(img)

    y = 420
    y = bloc_ajuste(d, MARGE_G, y, [(T["t2a"], ENCRE), (T["t2b"], ORANGE)],
                    92, ENCRE, LARGE + 120, 700, 1.10, poids=700, mini=56)
    y += 64
    y = bloc_ajuste(d, MARGE_G, y, T["t2c"], 50, ENCRE_D, LARGE, 1100,
                    1.32, poids=440)
    y += 40
    bloc_ajuste(d, MARGE_G, y, T["t2d"], 52, ENCRE, LARGE, 1306,
                1.26, poids=620)

    d.line([(MARGE_G, 1330), (MARGE_G + 180, 1330)], fill=OCRE, width=4)
    lettrage(d, 1388, T["t2p"], inter(28, "SemiBold"), OCRE, 7)
    return img

def diapo_produit(p, n, lg):
    img = Image.new("RGB", (W, H), CREME)
    img.paste(scene(p["ean"], 1000), (0, 0))
    fondu(img, 560, 440)
    poser_signature(img, MARGE_G, HAUT_SUR + 20, BLANC, 28)
    d = ImageDraw.Draw(img)

    lettrage(d, 1050, "%d / 6   \u00b7   %s" % (n, p["endroit"][lg]),
             inter(30, "SemiBold"), ORANGE, 6)

    # le titre tient TOUJOURS sur une ligne : sinon il pousse le corps de
    # texte dans le filet du pied. On reduit le corps jusqu'a ce qu'il entre.
    lmax_titre = LARGE + 120
    for corps in range(70, 44, -2):
        pt = serif(corps, 680)
        if d.textlength(p["titre"], font=pt) <= lmax_titre:
            break
    y = 1090 + (70 - corps) // 3
    y = bloc(d, MARGE_G, y, p["titre"], pt, ENCRE, lmax_titre, 1.08)
    y += 18
    bloc_ajuste(d, MARGE_G, y, p["ligne"][lg], 42, ENCRE_D, LARGE, 1300,
                1.26, poids=430)

    d.line([(MARGE_G, 1322), (W - MARGE_D, 1322)], fill=(206, 190, 164), width=2)
    d.text((MARGE_G, 1378), p["famille"][lg], font=serif(38, 500, ital=True),
           fill=ENCRE_D, anchor="lm")
    d.text((W - MARGE_D, 1378),
           "%s \u00b7 %s" % (prix_affiche(p["prix"], lg), p["ml"]),
           font=inter(34, "SemiBold"), fill=ENCRE, anchor="rm")
    return img

def diapo_offre(lg):
    T = TEXTES[lg]
    img = Image.new("RGB", (W, H), ENCRE)
    poser_signature(img, MARGE_G, HAUT_SUR + 20, CREME, 30)
    d = ImageDraw.Draw(img)

    y = 420
    y = bloc(d, MARGE_G, y, T["o1"], serif(90, 700), CREME, LARGE + 160, 1.10)
    y += 70
    for gros, petit in T["o"]:
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
    T = TEXTES[lg]
    img = Image.new("RGB", (W, H), CREME)
    img.paste(scene("6290360375687", 900, flou=6), (0, 0))
    fondu(img, 440, 460)
    poser_signature(img, MARGE_G, HAUT_SUR + 20, BLANC, 30)
    d = ImageDraw.Draw(img)

    y = 980
    y = bloc_ajuste(d, MARGE_G, y, [(T["f1"], ENCRE), (T["f2"], ORANGE)],
                    88, ENCRE, LARGE + 160, 1190, 1.10, poids=700, mini=52)
    y += 40
    bloc_ajuste(d, MARGE_G, y, T["f3"], 42, ENCRE_D, LARGE, 1330,
                1.26, poids=440)

    d.line([(MARGE_G, 1348), (W - MARGE_D, 1348)], fill=(206, 190, 164), width=2)
    lettrage(d, 1400, LIEN.upper(), inter(28, "SemiBold"), OCRE, 6)
    return img

# ----------------------------------------------------------------- sortie

def main():
    garde_fou()
    for lg in LANGUES:
        dossier = os.path.join(SORTIE, lg)
        os.makedirs(dossier, exist_ok=True)
        pages = [diapo_1(lg), diapo_2(lg)]
        for i, p in enumerate(PRODUITS, 1):
            pages.append(diapo_produit(p, i, lg))
        pages.append(diapo_offre(lg))
        pages.append(diapo_fin(lg))
        assert len(pages) == 10, "il faut dix diapos, pas %d" % len(pages)
        for i, im in enumerate(pages, 1):
            im.save(os.path.join(dossier, "%02d.jpg" % i), "JPEG",
                    quality=92, optimize=True)
        print(lg, "->", dossier, len(pages), "diapos")

if __name__ == "__main__":
    main()
