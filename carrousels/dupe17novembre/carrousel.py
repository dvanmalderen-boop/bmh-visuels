# -*- coding: utf-8 -*-
"""
BMH - carrousel du 17 novembre 2026.  FORMAT TIKTOK 1080 x 1920.

MECANIQUE : LA COMPARAISON DE NOTES DECLAREES.

CE QU'ON FAIT, ET CE QU'ON NE FAIT PAS
Le format qui ecrase la niche parfum est le « dupe » : un flacon arabe, un
signe egal, un parfum de luxe. Releve a la main dans Chrome le 16/11 :
@perfumes.men, 176 800 likes, 736 commentaires, 94 100 enregistrements, soit
53 % d'enregistrements. C'est le plus gros du secteur, de loin.

MAIS ON N'ECRIT JAMAIS « = ». Cette equivalence, aucune maison ne la declare,
et elle nomme des marques de luxe. Daoud a tranche le 16/11 : on compare les
NOTES PUBLIEES par les deux marques, sur leurs propres sites, avec les deux
prix, et une diapo dit noir sur blanc que memes notes ne veut pas dire meme
parfum. Chaque mot est verifiable par qui veut.

LES DEUX SOURCES, RELEVEES LE 16/11/2026
  Mugler A*Men Eau de Toilette, sur mugler.fr :
    notes de tete  : grains de cafe arabica
    notes de coeur : patchouli
    notes de fond  : vanille bourbon
    100 ml rechargeable, prix catalogue 105,00 EUR
    (78,75 EUR en promo Black Week le jour du releve ; on affiche le prix
     catalogue, une promo passe)
  Maison Alhambra Kismet for Men, sur la fiche de la boutique :
    tete  : muscade, epices orientales, bois precieux
    coeur : cafe, cacao, bois de santal
    fond  : vanille, patchouli, vetiver
    100 ml, 26,90 EUR
  Notes communes aux deux listes : CAFE, PATCHOULI, VANILLE.

LA DIAPO 1 EST UNE VIDEO — et c'est la premiere fois.
Etude Socialinsider sur 2,96 M de carrousels : un carrousel 100 % images fait
7 commentaires medians, un carrousel mixte image+video en fait 16, et
l'engagement passe de 1,80 % a 2,33 %. Daoud a filme le flacon qu'il a chez
lui, 3 secondes, un seul geste. TIKTOK N'ACCEPTE PAS DE VIDEO DANS UN
CARROUSEL PHOTO : la version TikTok part sans elle, et c'est exactement la
comparaison qu'on veut mesurer.

SON VISAGE est sur la diapo de couverture, comme depuis le 16/11.

ZONES TIKTOK : 150 px en haut, 480 px en bas, 120 px a droite sont manges
par l'interface. Tout le texte vit entre y=200 et y=1400.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

W, H    = 1080, 1920
RACINE  = "/home/claude/dupe"
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


def bloc_caps(d, x, y, texte, corps, couleur, lmax, interligne=1.1, mini=36):
    for c in range(corps, mini - 1, -4):
        p = inter(c, "Bold")
        lignes = couper(d, texte, p, lmax)
        if len(lignes) == len(texte.split("\n")) or c == mini:
            break
    for l in lignes:
        d.text((x, y), l, font=p, fill=couleur)
        y += int(c * interligne)
    return y


def caps_multi(d, x, y, texte, corps, couleur, lmax, interligne=1.08):
    """Un bloc en capitales dont les retours a la ligne sont ecrits a la main.
    Chaque ligne garde la meme taille : sinon le bloc part en escalier."""
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

CX = {
 "6291107459257": 0.66,  # Maison Alhambra Kismet for Men
 "6290064558416": 0.66,  # Paris Corner Eternal Coffee
 "5055810030094": 0.63,  # Al Wataniah Qahir
 "6291100132171": 0.65,  # Al Haramain Amber Oud Tobacco Edition
}

VOILE_HAUT = [(0, 225), (380, 205), (700, 95), (980, 0)]
VOILE_BAS  = [(960, 0), (1130, 120), (1290, 205), (1420, 232), (1920, 238)]
VOILE_COUV = [(0, 232), (560, 226), (900, 160), (1260, 0)]


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


def prix(v, lg, ml=None):
    e, c = ("%.2f" % v).split(".")
    if lg in ("fr", "de"):
        p = "%s,%s €" % (e, c)
    elif lg == "nl":
        p = "€ %s,%s" % (e, c)
    else:
        p = "€%s.%s" % (e, c)
    return "%s · %d ml" % (p, ml) if ml else p

# --------------------------------------------------------------- contenu

LUX = {
 "nom": "Mugler A*Men",
 "prix": "105,00 €",
 "notes": {
   "fr": ["Tête — grains de café arabica", "Cœur — patchouli",
          "Fond — vanille bourbon"],
   "en": ["Top — arabica coffee beans", "Heart — patchouli",
          "Base — bourbon vanilla"],
   "nl": ["Kop — arabica koffiebonen", "Hart — patchoeli",
          "Basis — bourbonvanille"],
   "de": ["Kopf — Arabica-Kaffeebohnen", "Herz — Patschuli",
          "Basis — Bourbon-Vanille"]},
}

BMH = {
 "ean": "6291107459257",
 "maison": "MAISON ALHAMBRA",
 "nom": "Kismet for Men",
 "prix": 26.90, "ml": 100, "stock": 22, "marge": 10.06,
 "notes": {
   "fr": ["Tête — muscade, épices, bois précieux",
          "Cœur — café, cacao, bois de santal",
          "Fond — vanille, patchouli, vétiver"],
   "en": ["Top — nutmeg, spices, precious woods",
          "Heart — coffee, cocoa, sandalwood",
          "Base — vanilla, patchouli, vetiver"],
   "nl": ["Kop — nootmuskaat, specerijen, edelhout",
          "Hart — koffie, cacao, sandelhout",
          "Basis — vanille, patchoeli, vetiver"],
   "de": ["Kopf — Muskatnuss, Gewürze, Edelhölzer",
          "Herz — Kaffee, Kakao, Sandelholz",
          "Basis — Vanille, Patschuli, Vetiver"]},
}

#  Les trois autres cafes. La phrase vient de la fiche, mot pour mot.
AUTRES = [
 {"ean": "6290064558416", "maison": "PARIS CORNER", "nom": "Eternal Coffee",
  "prix": 25.90, "ml": 85, "stock": 120, "marge": 10.03,
  "source": "un café au lait, en parfum",
  "l": {"fr": "Un café au lait, en parfum.",
        "en": "A café au lait, as a fragrance.",
        "nl": "Een koffie verkeerd, als geur.",
        "de": "Ein Milchkaffee, als Duft."}},
 {"ean": "5055810030094", "maison": "AL WATANIAH", "nom": "Qahir",
  "prix": 32.90, "ml": 100, "stock": 9, "marge": 9.75,
  "source": "un oriental construit autour du tabac et du café",
  "l": {"fr": "Un oriental construit autour du tabac et du café.",
        "en": "An oriental built around tobacco and coffee.",
        "nl": "Een oosterse geur rond tabak en koffie.",
        "de": "Ein Orientale, gebaut um Tabak und Kaffee."}},
 {"ean": "6291100132171", "maison": "AL HARAMAIN",
  "nom": "Amber Oud Tobacco Edition",
  "prix": 50.90, "ml": 60, "stock": 23, "marge": 10.68,
  "source": "le plus chaleureux de la gamme Amber Oud",
  "l": {"fr": "Le plus chaleureux de la gamme Amber Oud.",
        "en": "The warmest of the Amber Oud range.",
        "nl": "De warmste van de Amber Oud-reeks.",
        "de": "Der wärmste der Amber-Oud-Reihe."}},
]

T = {
 "sup": {"fr": "CAFÉ", "en": "COFFEE", "nl": "KOFFIE", "de": "KAFFEE"},
 "couv_t": {"fr": "105 €\nET 26,90 €", "en": "€105\nAND €26.90",
            "nl": "€ 105\nEN € 26,90", "de": "105 €\nUND 26,90 €"},
 "couv_s": {
   "fr": "Les deux déclarent café, patchouli et vanille. Je te montre les "
         "deux fiches.",
   "en": "Both declare coffee, patchouli and vanilla. Here are both listings.",
   "nl": "Allebei vermelden ze koffie, patchoeli en vanille. Ik laat je beide "
         "productpagina's zien.",
   "de": "Beide nennen Kaffee, Patschuli und Vanille. Ich zeige Ihnen beide "
         "Produktseiten."},
 "lux_lab": {"fr": "LE PARFUM À 105 €", "en": "THE €105 FRAGRANCE",
             "nl": "DE GEUR VAN € 105", "de": "DER DUFT FÜR 105 €"},
 "lux_fmt": {"fr": "Eau de Toilette · 100 ml", "en": "Eau de Toilette · 100 ml",
             "nl": "Eau de Toilette · 100 ml", "de": "Eau de Toilette · 100 ml"},
 "lux_src": {
   "fr": "Notes et prix catalogue publiés par Mugler sur mugler.fr, "
         "relevés le 16 novembre 2026.",
   "en": "Notes and list price published by Mugler on mugler.fr, checked on "
         "16 November 2026.",
   "nl": "Noten en catalogusprijs gepubliceerd door Mugler op mugler.fr, "
         "gecontroleerd op 16 november 2026.",
   "de": "Noten und Listenpreis von Mugler auf mugler.fr veröffentlicht, "
         "geprüft am 16. November 2026."},
 "bmh_lab": {"fr": "LE PARFUM À 26,90 €", "en": "THE €26.90 FRAGRANCE",
             "nl": "DE GEUR VAN € 26,90", "de": "DER DUFT FÜR 26,90 €"},
 "bmh_src": {
   "fr": "Notes et prix publiés sur la fiche de la boutique.",
   "en": "Notes and price published on the shop's own product page.",
   "nl": "Noten en prijs van onze eigen productpagina.",
   "de": "Noten und Preis von unserer eigenen Produktseite."},
 "com_t": {"fr": "CAFÉ\nPATCHOULI\nVANILLE", "en": "COFFEE\nPATCHOULI\nVANILLA",
           "nl": "KOFFIE\nPATCHOELI\nVANILLE", "de": "KAFFEE\nPATSCHULI\nVANILLE"},
 "com_s": {
   "fr": "Trois notes déclarées par les deux marques, chacune sur son "
         "propre site.",
   "en": "Three notes declared by both brands, each on its own website.",
   "nl": "Drie noten die beide merken zelf vermelden, elk op hun eigen site.",
   "de": "Drei Noten, die beide Marken selbst nennen, jede auf ihrer eigenen "
         "Website."},
 "hon_t": {"fr": "MÊMES NOTES,\nPAS MÊME\nPARFUM.",
           "en": "SAME NOTES,\nNOT THE SAME\nFRAGRANCE.",
           "nl": "ZELFDE NOTEN,\nNIET DEZELFDE\nGEUR.",
           "de": "GLEICHE NOTEN,\nNICHT DERSELBE\nDUFT."},
 "hon_c": {
   "fr": "Une liste de notes ne dit rien de la qualité des matières, ni de "
         "la tenue, ni de ce que ça donne sur ta peau. Je te donne les deux "
         "listes et les deux prix. Le reste, c'est ton nez.",
   "en": "A list of notes says nothing about the quality of the materials, "
         "the longevity, or what it does on your skin. I give you both lists "
         "and both prices. The rest is your nose.",
   "nl": "Een lijst noten zegt niets over de kwaliteit van de grondstoffen, "
         "de houdbaarheid, of wat het op jouw huid doet. Ik geef je beide "
         "lijsten en beide prijzen. De rest is jouw neus.",
   "de": "Eine Notenliste sagt nichts über die Qualität der Rohstoffe, die "
         "Haltbarkeit oder die Wirkung auf Ihrer Haut. Ich gebe Ihnen beide "
         "Listen und beide Preise. Der Rest ist Ihre Nase."},
 "tr_t": {"fr": "ET SI C'EST LE CAFÉ\nQUE TU CHERCHES",
          "en": "AND IF COFFEE\nIS WHAT YOU WANT",
          "nl": "EN ALS JE KOFFIE\nZOEKT",
          "de": "UND WENN SIE KAFFEE\nSUCHEN"},
 "tr_s": {"fr": "Trois autres, tous en stock.",
          "en": "Three more, all in stock.",
          "nl": "Nog drie, allemaal op voorraad.",
          "de": "Drei weitere, alle auf Lager."},
 "recap_t": {"fr": "LES QUATRE CAFÉS", "en": "THE FOUR COFFEES",
             "nl": "DE VIER KOFFIES", "de": "DIE VIER KAFFEES"},
 "fin_t": {"fr": "LEQUEL JE\nDÉCORTIQUE ?", "en": "WHICH ONE\nSHOULD I BREAK DOWN?",
           "nl": "WELKE PLUIS\nIK UIT?", "de": "WELCHEN NEHME\nICH AUSEINANDER?"},
 "fin_s": {
   "fr": "Dis-moi le nom en commentaire et je te fais la même chose : les "
         "deux listes, les deux prix, rien d'inventé.",
   "en": "Give me a name in the comments and I will do the same: both lists, "
         "both prices, nothing made up.",
   "nl": "Geef me een naam in de reacties en ik doe hetzelfde: beide lijsten, "
         "beide prijzen, niets verzonnen.",
   "de": "Nennen Sie mir einen Namen in den Kommentaren, und ich mache "
         "dasselbe: beide Listen, beide Preise, nichts erfunden."},
}

# ------------------------------------------------------------- garde-fou


def garde_fou():
    """Ici le controle qui compte n'est pas le stock, c'est la SOURCE.

    Une seule affirmation non verifiable dans ce carrousel et tout l'edifice
    tombe, parce que son seul argument c'est qu'il est verifiable.
    """
    assert LUX["notes"]["fr"] and LUX["prix"], "les notes Mugler sont la source"
    for pf in [BMH] + AUTRES:
        assert os.path.exists(os.path.join(SCENES, pf["ean"] + "c.jpg")), \
            "scene manquante : " + pf["ean"]
        assert pf["ean"] in CX, "cadrage non releve : " + pf["ean"]
        assert pf["stock"] >= 5, "%s n'a que %d" % (pf["nom"], pf["stock"])
        net = pf["marge"] - 4.85
        assert net >= 4.00, ("%s sous le plancher : %.2f" % (pf["nom"], net))
    for pf in AUTRES:
        assert pf["source"], "phrase sans source : " + pf["nom"]
    #  Les trois notes annoncees comme communes doivent vraiment etre dans
    #  les deux listes. C'est tout le carrousel qui tient a ca.
    lux = " ".join(LUX["notes"]["fr"]).lower()
    bmh = " ".join(BMH["notes"]["fr"]).lower()
    for mot in ("café", "patchouli", "vanille"):
        assert mot in lux, "%s absent des notes Mugler" % mot
        assert mot in bmh, "%s absent des notes Kismet" % mot
    assert len({p["maison"] for p in [BMH] + AUTRES}) == 4, "quatre maisons"
    faible = [p["nom"] for p in [BMH] + AUTRES if p["stock"] < 10]
    print("garde-fou : 4 maisons, 3 notes communes verifiees dans les deux "
          "listes, net de %.2f a %.2f EUR"
          % (min(p["marge"] for p in [BMH] + AUTRES) - 4.85,
             max(p["marge"] for p in [BMH] + AUTRES) - 4.85))
    if faible:
        print("   ! stock sous 10 : " + ", ".join(faible))

# ------------------------------------------------------------------ diapos


def diapo_couverture(lg):
    img = voile(plein_cadre(BMH["ean"]), haut=VOILE_COUV)
    d = ImageDraw.Draw(img)
    lettrage(d, 262, T["sup"][lg], inter(32, "SemiBold"), OCRE, 10)
    y = caps_multi(d, MARGE_G, 420, T["couv_t"][lg], 104, BLANC, LARGE)
    d.line([(MARGE_G, y + 40), (MARGE_G + 180, y + 40)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 86, [T["couv_s"][lg]], 42, CREME, LARGE,
                1240, ital=True)
    poser_visage(img)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_fiche(lab, nom, fmt, notes, src, lg, numero, fond_ean=None):
    """Une fiche : l'etiquette, le nom, le format, les trois lignes de notes,
    et la source en bas. Celle de Mugler est sur fond noir et sans image —
    on ne se sert pas du visuel d'une autre marque."""
    if fond_ean:
        img = voile(plein_cadre(fond_ean), haut=VOILE_COUV)
        d = ImageDraw.Draw(img)
    else:
        img, d = nuit()
    d.text((W - MARGE_D, 250), numero, font=inter(30, "SemiBold"),
           fill=GRIS, anchor="rm")
    lettrage(d, 250, lab, inter(30, "SemiBold"), OCRE, 8)
    y = bloc_ajuste(d, MARGE_G, 320, [nom], 76, BLANC, LARGE, 560, poids=600)
    d.text((MARGE_G, y + 16), fmt, font=inter(32, "Medium"), fill=GRIS)
    y += 110
    d.line([(MARGE_G, y), (MARGE_G + 120, y)], fill=OCRE, width=3)
    y += 46
    for l in notes:
        y = bloc_ajuste(d, MARGE_G, y, [l], 46, CREME, LARGE, y + 130) + 18
    assert y <= 1260, "les notes debordent (%d)" % y
    bloc_ajuste(d, MARGE_G, 1300, [src], 28, GRIS, LARGE, 1430, ital=True)
    poser_signature(img, MARGE_G, 1830, CREME if fond_ean else CREME)
    return img


def diapo_commun(lg):
    img, d = nuit()
    d.text((W - MARGE_D, 250), "04", font=inter(30, "SemiBold"), fill=GRIS,
           anchor="rm")
    y = caps_multi(d, MARGE_G, 420, T["com_t"][lg], 112, OCRE, LARGE)
    d.line([(MARGE_G, y + 50), (MARGE_G + 180, y + 50)], fill=CREME, width=4)
    bloc_ajuste(d, MARGE_G, y + 96, [T["com_s"][lg]], 44, CREME, LARGE, 1400,
                ital=True)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_honnete(lg):
    img, d = nuit()
    d.text((W - MARGE_D, 250), "05", font=inter(30, "SemiBold"), fill=GRIS,
           anchor="rm")
    y = caps_multi(d, MARGE_G, 340, T["hon_t"][lg], 84, BLANC, LARGE)
    d.line([(MARGE_G, y + 44), (MARGE_G + 120, y + 44)], fill=OCRE, width=4)
    bloc_ajuste(d, MARGE_G, y + 100, [T["hon_c"][lg]], 46, CREME, LARGE, 1400)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_transition(lg):
    img, d = nuit()
    d.text((W - MARGE_D, 250), "06", font=inter(30, "SemiBold"), fill=GRIS,
           anchor="rm")
    y = caps_multi(d, MARGE_G, 420, T["tr_t"][lg], 82, BLANC, LARGE)
    d.line([(MARGE_G, y + 44), (MARGE_G + 180, y + 44)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 96, [T["tr_s"][lg]], 46, OCRE, LARGE, 1400,
                ital=True)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_autre(pf, numero, lg):
    img = voile(plein_cadre(pf["ean"]))
    d = ImageDraw.Draw(img)
    d.text((W - MARGE_D, 250), numero, font=inter(30, "SemiBold"), fill=CREME,
           anchor="rm")
    y = bloc_ajuste(d, MARGE_G, 300, [pf["l"][lg]], 76, BLANC, LARGE, 700,
                    poids=600)
    d.text((MARGE_G, 1150), pf["maison"], font=inter(28, "SemiBold"), fill=OCRE)
    yy = bloc_ajuste(d, MARGE_G, 1196, [pf["nom"]], 60, BLANC, LARGE, 1330)
    d.text((MARGE_G, yy + 16), prix(pf["prix"], lg, pf["ml"]),
           font=inter(44, "Bold"), fill=CREME)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_recap(lg):
    img, d = nuit()
    lettrage(d, 250, T["recap_t"][lg], inter(30, "SemiBold"), OCRE, 8)
    y = 340
    cote = 150
    for pf in sorted([BMH] + AUTRES, key=lambda p: p["prix"]):
        img.paste(plein_cadre(pf["ean"]).resize(
            (cote, int(cote * H / W)), Image.LANCZOS).crop((0, 44, cote, 44 + cote)),
            (MARGE_G, y))
        x = MARGE_G + cote + 30
        d.text((x, y + 14), pf["maison"], font=inter(23, "SemiBold"), fill=OCRE)
        bloc_ajuste(d, x, y + 52, [pf["nom"]], 42, BLANC,
                    W - MARGE_D - x - 20, y + cote - 34)
        d.text((x, y + cote - 34), prix(pf["prix"], lg, pf["ml"]),
               font=inter(30, "Bold"), fill=CREME)
        y += cote + 26
    assert y <= 1430, "le recapitulatif deborde (%d)" % y
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_fin(lg):
    img = voile(plein_cadre(AUTRES[0]["ean"]), haut=VOILE_COUV)
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
    pages = [
        diapo_couverture(lg),
        diapo_fiche(T["lux_lab"][lg], LUX["nom"], T["lux_fmt"][lg],
                    LUX["notes"][lg], T["lux_src"][lg], lg, "02"),
        diapo_fiche(T["bmh_lab"][lg], BMH["maison"].title() + " " + BMH["nom"],
                    "Eau de Parfum · 100 ml", BMH["notes"][lg],
                    T["bmh_src"][lg], lg, "03", fond_ean=BMH["ean"]),
        diapo_commun(lg),
        diapo_honnete(lg),
        diapo_transition(lg),
    ]
    pages += [diapo_autre(pf, "%02d" % (i + 7), lg)
              for i, pf in enumerate(AUTRES)]
    pages += [diapo_recap(lg), diapo_fin(lg)]
    assert len(pages) == 11, "onze diapos attendues, %d" % len(pages)
    for i, im in enumerate(pages, 1):
        im.save(os.path.join(dossier, "%02d.jpg" % i), quality=90,
                optimize=True)
    print("%s : %d diapos ecrites dans %s" % (lg, len(pages), dossier))


if __name__ == "__main__":
    main()
