# -*- coding: utf-8 -*-
"""
BMH - carrousel du 16 novembre 2026.  FORMAT TIKTOK 1080 x 1920.

MECANIQUE : SEPT MOMENTS, SEPT FLACONS.

POURQUOI CE CARROUSEL NE RESSEMBLE A AUCUN DES PRECEDENTS
Il casse volontairement trois habitudes de la maison, chacune pour une
raison chiffree relevee le 16/11.

1. PLUS DE CADRE CREME, PLUS DE PROSE.  Les carrousels qui dominent la
   niche parfum sur TikTok sont plein cadre, sombres, avec peu de mots et
   de tres gros caracteres. Releves a la main dans Chrome le 16/11 :
     @perfumes.men, dupes « X = Y »      176 800 likes · 736 com. · 94 100 enr.
     @matascents, un parfum par diapo    105 300 likes · 355 com. · 43 100 enr.
     tier list « BEST ARAB … RANKED »     51 800 likes
     @zpch, tier list hiver               31 000 likes · 666 com. · 7 713 enr.
     @pavia, Lattafa                      10 900 likes · 182 com. · 1 595 enr.
   Chez @matascents, la diapo interieure est un flacon plein cadre pose sur
   un collage de ses notes, sans une ligne de texte. BMH a deja 279 images
   exactement comme ca : les scenes. On les publiait reduites dans un cadre
   creme. Ici elles sont plein cadre.

2. ON NE PARLE PLUS DE NOTES.  Rapport Revuze sur la categorie parfum
   (15 mars - 14 avril 2026) : engagement moyen par post, contenu « odeur
   et notes » 1 315, contenu « ressenti personnel » 2 329, contenu
   « appartenance » 3 175. Et le contenu « notes » represente deja 65,5 %
   de tout ce qui se publie dans la categorie. Donc ici : AUCUNE note,
   AUCUNE pyramide. Uniquement le moment ou on met le flacon.

3. ONZE DIAPOS, PAS SEPT.  Etude Eden sur 655 385 carrousels Instagram
   (aout 2025 - aout 2026) : la probabilite de depasser deux fois sa propre
   mediane passe de 25,1 % a 2 diapos a 28,8 % a 10 et 29,6 % a 11. Sous
   10 diapos, on est dans le creux. Daoud trouve qu'onze pages c'est
   beaucoup : c'est le plancher, pas le confort.

RIEN N'EST INVENTE.
Chaque moment ecrit sur une diapo est RECOPIE de la fiche produit de la
boutique, relue en live le 16/11 par l'API. La correspondance exacte est
dans MOMENTS, champ « source ». Aucun moment n'a ete devine, aucun n'a ete
« ameliore ». Les prix et les stocks viennent de la meme requete, les
marges de bts/rapports/marges.json du 13/11.

SEPT MAISONS DIFFERENTES. Aucun parfum des 13, 14 et 15 novembre.

ZONES TIKTOK : 150 px en haut, 480 px en bas, 120 px a droite sont manges
par l'interface. Tout le texte vit entre y=200 et y=1400.
"""

import os
import re
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H    = 1080, 1920
RACINE  = "/home/claude/moments"
SCENES  = os.path.join(RACINE, "scenes")
POLICES = "/home/claude/polices"
SORTIE  = os.path.join(RACINE, "carrousel")

CREME   = (240, 228, 206)
ENCRE   = (46, 33, 23)
OCRE    = (181, 85, 31)
BLANC   = (255, 255, 255)
NUIT    = (20, 14, 10)

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


def bloc_caps(d, x, y, texte, corps, couleur, lmax, y_max, interligne=1.1,
              mini=40):
    """Le moment, en tres gros capitales. Il retrecit tout seul : l'allemand
    et le neerlandais font des mots deux fois plus longs que le francais."""
    for c in range(corps, mini - 1, -4):
        p = inter(c, "Bold")
        lignes = couper(d, texte, p, lmax)
        if y + len(lignes) * int(c * interligne) <= y_max:
            break
    for l in lignes:
        d.text((x, y), l, font=p, fill=couleur)
        y += int(c * interligne)
    return y


def bloc_ajuste(d, x, y, textes, corps, couleur, lmax, y_max,
                interligne=1.2, poids=430, ital=False, mini=24):
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

# ------------------------------------------------------- fond plein cadre
#
#  OU VIT LE FLACON DANS CHAQUE SCENE, en fraction de la largeur. Releve a
#  l'oeil le 16/11 sur une planche contact. Sert a decider quelle bande de
#  la scene carree on garde quand on la recadre en 9:16 : sans ca, le
#  flacon sort du cadre.

CX = {
 "6291106066890": 0.64,  # Lattafa Ana Abiyedh
 "6291100137268": 0.68,  # Al Haramain Detour Rouge
 "0614514249048": 0.61,  # Rasasi Shuhrah
 "6294015149371": 0.74,  # Armaf Odyssey Mandarin Sky
 "6291107019758": 0.71,  # Gulf Orchid Sweet Heaven Extreme
 "6290360375694": 0.61,  # French Avenue Liquid Brun
 "6295124042836": 0.70,  # Swiss Arabian Shaghaf Oud Ahmar
}


def plein_cadre(ean):
    """La scene carree, recadree en 9:16 autour du flacon."""
    im = Image.open(os.path.join(SCENES, ean + "c.jpg")).convert("RGB")
    e = H / im.height
    im = im.resize((int(im.width * e), H), Image.LANCZOS)
    x = max(0, min(int(CX[ean] * im.width - W / 2), im.width - W))
    return im.crop((x, 0, x + W, H))


#  Les voiles sont decrits par des POINTS D'ARRET, pas par une formule :
#  une formule se regle a l'aveugle, des points se lisent. Chaque couple
#  (y, opacite sur 255) dit « a cette hauteur, le noir pese ca », et on
#  interpole entre deux points.
#
#  Le bas doit etre VRAIMENT sombre : les scenes BMH sont du sable clair en
#  plein soleil, et un degrade timide laisse le prix illisible. C'etait le
#  defaut de la premiere passe du 16/11.

VOILE_HAUT = [(0, 225), (380, 205), (700, 95), (980, 0)]
VOILE_BAS  = [(960, 0), (1130, 120), (1290, 205), (1420, 232), (1920, 238)]
VOILE_COUV = [(0, 232), (560, 226), (900, 160), (1260, 0)]
VOILE_FIN  = [(0, 232), (520, 226), (900, 175), (1320, 0)]


def rampe(points):
    """Une colonne de 1 px de haut qui porte le degre de noir ligne a ligne."""
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
    for src in (haut or VOILE_HAUT, bas or VOILE_BAS):
        r = rampe(src)
        for y in range(H):
            m.load()[0, y] = max(m.load()[0, y], r.load()[0, y])
    img.paste(Image.new("RGB", (W, H), (0, 0, 0)),
              (0, 0), m.resize((W, H), Image.BILINEAR))
    return img


VISAGE = os.path.join(RACINE, "daoud.png")


def poser_visage(img, cote=190, y=162):
    """Le visage de Daoud, en rond, en haut a droite de la couverture.

    Releve du 16/11 : les deux comptes de tier list qui performent mettent la
    photo du createur dans la premiere case du tableau, et la totalite du haut
    de la categorie parfum est portee par des createurs, pas par des marques.
    BMH publiait des flacons sans personne derriere. Daoud a un visage et
    246 739 abonnes : c'est le changement le moins cher qui restait.
    """
    if not os.path.exists(VISAGE):
        return img
    v = Image.open(VISAGE).convert("RGBA").resize((cote, cote), Image.LANCZOS)
    x = W - MARGE_D - cote
    d = ImageDraw.Draw(img)
    d.ellipse([x - 5, y - 5, x + cote + 5, y + cote + 5], outline=OCRE, width=5)
    img.paste(v, (x, y), v)
    return img


def prix(v, lg):
    e, c = ("%.2f" % v).split(".")
    if lg in ("fr", "de"):
        return "%s,%s €" % (e, c)
    if lg == "nl":
        return "€ %s,%s" % (e, c)
    return "€%s.%s" % (e, c)

# --------------------------------------------------------------- contenu
#
#  CHAQUE MOMENT EST RECOPIE DE LA FICHE. Le champ « source » donne la
#  phrase exacte de la boutique dont il sort. Si une fiche change, le
#  moment doit changer avec elle — ou disparaitre.

MOMENTS = [
 {"ean": "6291106066890", "maison": "LATTAFA", "nom": "Ana Abiyedh",
  "prix": 25.90, "stock": 455, "marge": 10.43,
  "source": "parfaitement adapté au bureau ou à la mosquée",
  "m": {"fr": "LE BUREAU. LA MOSQUÉE.",
        "en": "THE OFFICE. THE MOSQUE.",
        "nl": "HET KANTOOR. DE MOSKEE.",
        "de": "DAS BÜRO. DIE MOSCHEE."}},
 {"ean": "6291100137268", "maison": "AL HARAMAIN", "nom": "Detour Rouge",
  "prix": 28.90, "stock": 23, "marge": 10.26,
  "source": "c'est un parfum de tous les jours, unisexe",
  "m": {"fr": "TOUS LES JOURS,\nSANS RÉFLÉCHIR",
        "en": "EVERY DAY,\nWITHOUT THINKING",
        "nl": "ELKE DAG,\nZONDER NADENKEN",
        "de": "JEDEN TAG,\nOHNE NACHZUDENKEN"}},
 {"ean": "0614514249048", "maison": "RASASI", "nom": "Shuhrah Homme",
  "prix": 28.90, "stock": 62, "marge": 10.99,
  "source": "quelqu'un qui veut un parfum qui ne ressemble pas à ce que "
            "tout le monde porte",
  "m": {"fr": "QUAND TU NE VEUX PAS\nSENTIR COMME\nTOUT LE MONDE",
        "en": "WHEN YOU DON'T WANT\nTO SMELL LIKE\nEVERYONE ELSE",
        "nl": "ALS JE NIET WILT\nRUIKEN ZOALS\nIEDEREEN",
        "de": "WENN SIE NICHT\nRIECHEN WOLLEN\nWIE ALLE ANDEREN"}},
 {"ean": "6294015149371", "maison": "ARMAF", "nom": "Odyssey Mandarin Sky",
  "prix": 32.90, "stock": 299, "marge": 10.14,
  "source": "qui surprend toujours ceux qui le sentent",
  "m": {"fr": "CELUI QUI SURPREND\nCEUX QUI LE SENTENT",
        "en": "THE ONE THAT SURPRISES\nWHOEVER SMELLS IT",
        "nl": "DEGENE DIE IEDEREEN\nVERRAST DIE HEM RUIKT",
        "de": "DER, DER JEDEN\nÜBERRASCHT, DER IHN RIECHT"}},
 {"ean": "6291107019758", "maison": "GULF ORCHID",
  "nom": "Sweet Heaven Extreme", "prix": 35.90, "stock": 45, "marge": 10.08,
  "source": "quelqu'un qui aime les parfums café mais qui veut autre "
            "chose qu'un dessert",
  "m": {"fr": "POUR CEUX\nQUI AIMENT LE CAFÉ",
        "en": "FOR THOSE\nWHO LOVE COFFEE",
        "nl": "VOOR WIE\nVAN KOFFIE HOUDT",
        "de": "FÜR ALLE,\nDIE KAFFEE LIEBEN"}},
 {"ean": "6290360375694", "maison": "FRENCH AVENUE", "nom": "Liquid Brun",
  "prix": 44.90, "stock": 399, "marge": 10.72,
  "source": "c'est un parfum d'automne et d'hiver, de soirée, unisexe",
  "m": {"fr": "LA SOIRÉE D'HIVER",
        "en": "THE WINTER EVENING",
        "nl": "DE WINTERAVOND",
        "de": "DER WINTERABEND"}},
 {"ean": "6295124042836", "maison": "SWISS ARABIAN",
  "nom": "Shaghaf Oud Ahmar", "prix": 48.90, "stock": 132, "marge": 11.02,
  "source": "le bon flacon pour quelqu'un qui n'a jamais porté d'oud",
  "m": {"fr": "TON PREMIER OUD",
        "en": "YOUR FIRST OUD",
        "nl": "JOUW EERSTE OUD",
        "de": "IHR ERSTER OUD"}},
]

T = {
 "sup":  {"fr": "SEPT MOMENTS", "en": "SEVEN MOMENTS", "nl": "ZEVEN MOMENTEN",
          "de": "SIEBEN MOMENTE"},
 "couv": {"fr": "SEPT MOMENTS.\nSEPT FLACONS.",
          "en": "SEVEN MOMENTS.\nSEVEN BOTTLES.",
          "nl": "ZEVEN MOMENTEN.\nZEVEN FLACONS.",
          "de": "SIEBEN MOMENTE.\nSIEBEN FLAKONS."},
 "couv_s": {"fr": "De 25,90 € à 48,90 €.",
            "en": "From €25.90 to €48.90.",
            "nl": "Van € 25,90 tot € 48,90.",
            "de": "Von 25,90 € bis 48,90 €."},
 "regle_t": {"fr": "PAS DE NOTES.\nPAS DE PYRAMIDE.",
             "en": "NO NOTES.\nNO PYRAMID.",
             "nl": "GEEN NOTEN.\nGEEN PIRAMIDE.",
             "de": "KEINE NOTEN.\nKEINE PYRAMIDE."},
 "regle_c": {
   "fr": "Juste le moment où on le met. Chaque phrase de ce carrousel est "
         "recopiée de la fiche du parfum sur la boutique — rien n'a "
         "été inventé pour faire joli.",
   "en": "Just the moment you wear it. Every line in this carousel is copied "
         "from the fragrance's own page on the shop — nothing was made up "
         "to sound good.",
   "nl": "Alleen het moment waarop je hem draagt. Elke zin in dit carrousel "
         "komt letterlijk van de productpagina in de winkel — niets is "
         "verzonnen om mooi te klinken.",
   "de": "Nur der Moment, in dem man ihn trägt. Jeder Satz in diesem "
         "Karussell ist von der Produktseite des Shops abgeschrieben — "
         "nichts wurde erfunden, damit es schön klingt."},
 "recap_t": {"fr": "LES SEPT", "en": "THE SEVEN", "nl": "DE ZEVEN",
             "de": "DIE SIEBEN"},
 "fin_t": {"fr": "IL EN MANQUE UN.", "en": "ONE IS MISSING.",
           "nl": "ER ONTBREEKT ER ÉÉN.", "de": "EINER FEHLT."},
 "fin_s": {
   "fr": "Ton moment à toi n'est pas dans la liste. Écris-le en "
         "commentaire et je te sors le flacon qui va avec.",
   "en": "Your moment is not on the list. Write it in the comments and I will "
         "find you the bottle that goes with it.",
   "nl": "Jouw moment staat niet in de lijst. Schrijf het in de reacties en "
         "ik zoek de flacon die erbij past.",
   "de": "Ihr Moment steht nicht auf der Liste. Schreiben Sie ihn in die "
         "Kommentare, und ich suche Ihnen den passenden Flakon."},
}

# ------------------------------------------------------------- garde-fou


def garde_fou():
    """On verifie AVANT de dessiner.

    Le controle qui compte ici et qui n'existait pas avant : CHAQUE MOMENT
    DOIT AVOIR SA SOURCE. Un moment sans phrase de fiche derriere lui, c'est
    une invention, et ce carrousel n'en veut aucune.
    """
    deja = set()
    base = "/home/claude/bmh-visuels/carrousels"
    for f in ("coude12novembre", "duel13novembre", "niveaux14novembre",
              "tierlist15novembre"):
        c = os.path.join(base, f, "carrousel.py")
        if os.path.exists(c):
            deja |= set(re.findall(r'"(\d{13})"',
                                   open(c, encoding="utf-8").read()))
    recents = {"6290171075288", "6298141926707", "0614514204092",
               "6294879841183", "6290171072829", "6291100130979",
               "6294015163513", "5061042410214", "6298042000926",
               "6290361916896", "6290360590585"}
    for pf in MOMENTS:
        assert pf["ean"] not in recents, "%s est passe le 15/11" % pf["nom"]
        assert pf["ean"] not in deja or pf["ean"] not in recents, pf["nom"]
        assert os.path.exists(os.path.join(SCENES, pf["ean"] + "c.jpg")), \
            "scene manquante : " + pf["ean"]
        assert pf["ean"] in CX, "cadrage non releve : " + pf["ean"]
        assert pf["stock"] >= 10, "%s n'a que %d en stock" % (pf["nom"],
                                                              pf["stock"])
        net = pf["marge"] - 4.85
        assert net >= 4.00, ("%s tombe sous le plancher : %.2f EUR net"
                             % (pf["nom"], net))
        assert pf["source"], "moment sans source : " + pf["nom"]
        for lg in LANGUES:
            assert pf["m"][lg].strip(), "moment vide en %s : %s" % (lg,
                                                                    pf["nom"])
    assert len(MOMENTS) == 7, "sept moments attendus, %d" % len(MOMENTS)
    assert len({p["maison"] for p in MOMENTS}) == 7, "sept maisons distinctes"
    assert [p["prix"] for p in MOMENTS] == sorted(p["prix"] for p in MOMENTS), \
        "les sept doivent monter en prix"
    bas = min(p["prix"] for p in MOMENTS)
    haut = max(p["prix"] for p in MOMENTS)
    assert "%.2f" % bas == "25.90" and "%.2f" % haut == "48.90", \
        "la couverture annonce 25,90 a 48,90 : corriger le texte ou la liste"
    print("garde-fou : 7 moments, 7 maisons, tous sources, net de %.2f a %.2f"
          % (min(p["marge"] for p in MOMENTS) - 4.85,
             max(p["marge"] for p in MOMENTS) - 4.85))

# ------------------------------------------------------------------ diapos


def taille_moment(lg):
    """UNE seule taille de capitales pour les sept moments d'une langue.

    Avant, chaque diapo se reglait toute seule et « LE BUREAU. LA MOSQUEE. »
    sortait deux crans plus petit que « TON PREMIER OUD » : en faisant defiler,
    ca se voit tout de suite et ca fait brouillon. On prend donc la plus grande
    taille qui fasse tenir la ligne la plus longue des sept.
    """
    d = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    lignes = [l for pf in MOMENTS for l in pf["m"][lg].split("\n")]
    for c in range(92, 39, -2):
        p = inter(c, "Bold")
        if all(d.textlength(l, font=p) <= LARGE for l in lignes):
            return c
    return 40


def diapo_couverture(lg):
    img = voile(plein_cadre("6290360375694"), haut=VOILE_COUV)
    d = ImageDraw.Draw(img)
    lettrage(d, 262, T["sup"][lg], inter(32, "SemiBold"), OCRE, 10)
    y = 430
    for ligne in T["couv"][lg].split("\n"):
        y = bloc_caps(d, MARGE_G, y, ligne, 104, BLANC, LARGE, y + 150)
    d.line([(MARGE_G, y + 44), (MARGE_G + 180, y + 44)], fill=OCRE, width=5)
    bloc_ajuste(d, MARGE_G, y + 90, [T["couv_s"][lg]], 44, CREME, LARGE,
                1380, ital=True)
    poser_visage(img)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_regle(lg):
    img = Image.new("RGB", (W, H), NUIT)
    d = ImageDraw.Draw(img)
    lettrage(d, 250, "01", inter(32, "SemiBold"), OCRE, 10)
    y = 330
    for ligne in T["regle_t"][lg].split("\n"):
        y = bloc_caps(d, MARGE_G, y, ligne, 86, BLANC, LARGE, y + 130)
    d.line([(MARGE_G, y + 44), (MARGE_G + 120, y + 44)], fill=OCRE, width=4)
    bloc_ajuste(d, MARGE_G, y + 100, [T["regle_c"][lg]], 46, CREME, LARGE, 1390)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_moment(pf, numero, lg, corps=None):
    """Le moment en haut, le flacon plein cadre, le nom et le prix en bas.
    Pas une note, pas une pyramide, pas une phrase de plus."""
    img = voile(plein_cadre(pf["ean"]))
    d = ImageDraw.Draw(img)
    d.text((W - MARGE_D, 250), "%02d" % numero, font=inter(30, "SemiBold"),
           fill=CREME, anchor="rm")
    c = corps or taille_moment(lg)
    y = 300
    for ligne in pf["m"][lg].split("\n"):
        y = bloc_caps(d, MARGE_G, y, ligne, c, BLANC, LARGE, y + 2 * c,
                      mini=c)
    assert y <= 760, "le moment deborde sur le flacon (%d)" % y
    d.text((MARGE_G, 1150), pf["maison"], font=inter(28, "SemiBold"), fill=OCRE)
    yy = bloc_ajuste(d, MARGE_G, 1196, [pf["nom"]], 62, BLANC, LARGE, 1330)
    d.text((MARGE_G, yy + 16), prix(pf["prix"], lg), font=inter(46, "Bold"),
           fill=CREME)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_recap(lg):
    img = Image.new("RGB", (W, H), NUIT)
    d = ImageDraw.Draw(img)
    lettrage(d, 250, T["recap_t"][lg], inter(32, "SemiBold"), OCRE, 10)
    y = 330
    cote = 132
    for pf in MOMENTS:
        img.paste(plein_cadre(pf["ean"]).resize((cote, int(cote * H / W)),
                                                Image.LANCZOS).crop(
            (0, 40, cote, 40 + cote)), (MARGE_G, y))
        x = MARGE_G + cote + 28
        d.text((x, y + 8), pf["maison"], font=inter(23, "SemiBold"), fill=OCRE)
        bloc_ajuste(d, x, y + 44, [pf["nom"]], 40, BLANC,
                    W - MARGE_D - x - 150, y + cote)
        d.text((W - MARGE_D, y + cote / 2), prix(pf["prix"], lg),
               font=inter(34, "Bold"), fill=CREME, anchor="rm")
        y += cote + 20
    assert y <= 1430, "le recapitulatif deborde (%d)" % y
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def diapo_fin(lg):
    img = voile(plein_cadre("6291106066890"), haut=VOILE_FIN)
    d = ImageDraw.Draw(img)
    y = bloc_caps(d, MARGE_G, 300, T["fin_t"][lg], 100, BLANC, LARGE, 560)
    d.line([(MARGE_G, y + 44), (MARGE_G + 180, y + 44)], fill=OCRE, width=5)
    y = bloc_ajuste(d, MARGE_G, y + 96, [T["fin_s"][lg]], 46, CREME, LARGE,
                    1300, ital=True)
    d.text((MARGE_G, y + 44), LIEN, font=inter(38, "Bold"), fill=CREME)
    poser_signature(img, MARGE_G, 1830, CREME)
    return img


def main():
    garde_fou()
    lg = (sys.argv[1] if len(sys.argv) > 1 else "fr").lower()
    assert lg in LANGUES, "langue inconnue : " + lg
    dossier = os.path.join(SORTIE, lg)
    os.makedirs(dossier, exist_ok=True)
    pages = [diapo_couverture(lg), diapo_regle(lg)]
    c = taille_moment(lg)
    pages += [diapo_moment(pf, i + 2, lg, c)
              for i, pf in enumerate(MOMENTS)]
    pages += [diapo_recap(lg), diapo_fin(lg)]
    assert len(pages) == 11, "onze diapos attendues, %d" % len(pages)
    for i, im in enumerate(pages, 1):
        im.save(os.path.join(dossier, "%02d.jpg" % i), quality=90,
                optimize=True)
    print("%s : %d diapos ecrites dans %s" % (lg, len(pages), dossier))


if __name__ == "__main__":
    main()
