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
import re
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H    = 1080, 1920
RACINE  = "/home/claude/niveaux"
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

def largeur_signature(corps=30, espace=7):
    d = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    p = inter(corps, "SemiBold")
    t = int(corps * 0.52) * 2 + 2
    l = t + corps * 0.75
    for c in "BRING MEDINA HOME":
        l += d.textlength(c, font=p) + espace
    return l - espace + 4 + d.textlength("\u00ae", font=inter(int(corps * 0.55), "Medium"))

def poser_signature_centree(img, y, couleur, corps=36, espace=8):
    """La signature posee au milieu, a cheval sur la couture des deux
    photos. Daoud : le petit trait de separation « casse » l'image ; c'est
    la marque qui doit tenir les deux moities ensemble, pas une ligne."""
    poser_signature(img, (W - largeur_signature(corps, espace)) / 2, y,
                    couleur, corps, espace)

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

#  OU SE TROUVE LE FLACON DANS CHAQUE SCENE, en fraction de la largeur.
#  Le style des scenes BMH met les accessoires a gauche et le flacon a
#  DROITE, vers 0,62 a 0,72. Un demi-ecran ne garde que 54 % de la largeur :
#  si on recadre au milieu, le flacon est coupe. Releve a l'oeil le 12/11,
#  parce que la detection automatique attrapait le bois seche, qui est net
#  lui aussi.
CENTRE = {
 "6290171002338": 0.707,  # Afnan 9pm
 "6290171002345": 0.626,  # Afnan 9am
 "6291106066890": 0.688,  # Ana Abiyedh
 "6291107454412": 0.677,  # Ana Abiyedh Rouge
 "6291100139668": 0.668,  # Al Haramain L'aventure (cube argent)
 "6291100137565": 0.616,  # Al Haramain Aventure Femme (cube or)
 "6290360378053": 0.677,  # French Avenue Vulcan Feu
 "6290360378060": 0.668,  # French Avenue Vulcan Sable
 "6290362162629": 0.640,  # Gulf Orchid Mango Ice
 "6290362162643": 0.710,  # Gulf Orchid Creme Caramel
 "6085010044712": 0.710,  # Armaf Club de Nuit Intense Man
 "6294015164152": 0.730,  # Armaf Club de Nuit Iconic
}

#  A quelle hauteur vit le flacon, en fraction de la hauteur de la scene.
#  La plupart sont des flacons hauts, centres vers 0,30. Les deux Aventure
#  sont des CUBES, plus bas et plus larges : il faut descendre la fenetre,
#  sinon on leur coupe le pied.
HAUTEUR = {
 "6291100139668": 0.668,  # Al Haramain L'aventure (cube argent)
 "6291100137565": 0.616,  # Al Haramain Aventure Femme (cube or)
}

def panneau(ean, largeur, hauteur, cible=0.5):
    """Un demi-ecran a partir d'une scene produit, RECADRE SUR LE FLACON.
    `cible` dit ou le flacon doit tomber dans le panneau : 0,5 au milieu.
    Sur le panneau de droite on vise un peu plus a gauche, pour que le
    flacon ne finisse pas sous la pile de boutons de TikTok."""
    im = Image.open(os.path.join(SCENES, ean + "c.jpg")).convert("RGB")
    # ZOOM : sans lui le flacon ne fait qu'un tiers de la hauteur et se lit
    # mal sur un telephone. 1,25 le rapproche sans sortir du decor.
    ech = max(largeur / im.width, hauteur / im.height) * 1.25
    im = im.resize((max(int(im.width * ech) + 1, largeur),
                    max(int(im.height * ech) + 1, hauteur)), Image.LANCZOS)
    x = int(CENTRE.get(ean, 0.68) * im.width - cible * largeur)
    x = max(0, min(x, im.width - largeur))
    # le flacon vit vers le tiers haut de la scene : on le pose au tiers
    # haut du panneau plutot que de couper au milieu.
    y = int(HAUTEUR.get(ean, 0.30) * im.height - 0.36 * hauteur)
    y = max(0, min(y, im.height - hauteur))
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
#  Les familles viennent des etiquettes des fiches Shopify, relevees le
#  13/11. On ne dit jamais lequel est le meilleur.

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
 # ajoutees le 13/11 pour le carrousel des niveaux, relevees sur les fiches
 "safran":  {"fr": "Safran et épices du Golfe", "en": "Saffron and Gulf spices",
             "nl": "Saffraan en Golfspecerijen", "de": "Safran und Golfgewürze"},
 "cuir":    {"fr": "Cuir et miel", "en": "Leather and honey",
             "nl": "Leer en honing", "de": "Leder und Honig"},
}


# ---------------------------------------------------------------------------
#  LA MECANIQUE DU 14/11 : DEBUTANT / CONNAISSEUR / EXPERT
#
#  Pourquoi ce format : c'est celui qui porte le plus gros chiffre du
#  balayage des quatre agents — 1,4 M de vues sur @the_swan_nose. Et il
#  respecte la regle de variation : le 12/11 c'etait « l'endroit ou on le
#  met », le 13/11 le duel. Trois mecaniques, trois jours.
#
#  LA REGLE QUI REND CE CARROUSEL HONNETE : le niveau parle du PARFUM, pas
#  du prix. C'est pour ca que le palier Expert est le MOINS CHER des trois
#  (26,90 et 31,90 contre 48,90 et 50,90 chez les Debutants). Si on avait
#  range les parfums par prix croissant, ce serait une vente deguisee en
#  conseil, et ca se verrait.
#
#  CHAQUE PHRASE DE NIVEAU VIENT DE LA FICHE PRODUIT, pas de mon avis :
#  « le bon flacon pour quelqu'un qui n'a jamais porte d'oud » est ecrit
#  dans la fiche du Shaghaf, « le cumin n'est pas une note consensuelle »
#  dans celle du Glacier Gold. On ne reclasse pas un parfum pour les
#  besoins du carrousel.
# ---------------------------------------------------------------------------

NIVEAUX = [
    {"cle": "debutant",
     "titre": {"fr": "Débutant", "en": "Beginner",
               "nl": "Beginner", "de": "Einsteiger"},
     "sous": {"fr": "On ne se trompe pas",
              "en": "You cannot go wrong",
              "nl": "Je zit altijd goed",
              "de": "Hier liegen Sie nie falsch"}},
    {"cle": "connaisseur",
     "titre": {"fr": "Connaisseur", "en": "Connoisseur",
               "nl": "Kenner", "de": "Kenner"},
     "sous": {"fr": "Un parti pris assumé",
              "en": "A deliberate stance",
              "nl": "Een bewuste keuze",
              "de": "Eine bewusste Entscheidung"}},
    {"cle": "expert",
     "titre": {"fr": "Expert", "en": "Expert",
               "nl": "Expert", "de": "Experte"},
     "sous": {"fr": "Il faut s'y faire",
              "en": "It takes getting used to",
              "nl": "Je moet eraan wennen",
              "de": "Daran muss man sich gewöhnen"}},
]

PARFUMS = [
 # --- DEBUTANT ---------------------------------------------------------
 {"niveau": "debutant", "ean": "6295124042836",
  "maison": "SWISS ARABIAN", "nom": "Shaghaf Oud Ahmar",
  "prix": 48.90, "famille": "oud", "stock": 132,
  "mot": {"fr": "Pour qui n'a jamais porté d'oud et a peur que ce soit trop.",
          "en": "For anyone who has never worn oud and fears it is too much.",
          "nl": "Voor wie nog nooit oud droeg en bang is dat het te veel is.",
          "de": "Für alle, die nie Oud trugen und fürchten, es sei zu viel."}},
 {"niveau": "debutant", "ean": "0614514555125",
  "maison": "RASASI", "nom": "Hawas Atlantis",
  "prix": 50.90, "famille": "marin", "stock": 47,
  "mot": {"fr": "Fruité et frais, de jour. Il ne demande rien à personne.",
          "en": "Fruity and fresh, for daytime. It asks nothing of anyone.",
          "nl": "Fruitig en fris, overdag. Het vraagt niemand iets.",
          "de": "Fruchtig und frisch, für den Tag. Er fordert nichts."}},
 # --- CONNAISSEUR ------------------------------------------------------
 {"niveau": "connaisseur", "ean": "6290361911570",
  "maison": "ARABIYAT PRESTIGE", "nom": "Nyla Suede",
  "prix": 33.90, "famille": "gourmand", "stock": 50,
  "mot": {"fr": "Commence en dessert, finit en cuir. Le quart d'heure du début est long.",
          "en": "Starts as dessert, ends as leather. The first quarter hour is long.",
          "nl": "Begint als dessert, eindigt als leer. Het eerste kwartier duurt lang.",
          "de": "Beginnt als Dessert, endet als Leder. Die erste Viertelstunde zieht sich."}},
 {"niveau": "connaisseur", "ean": "6295124036811",
  "maison": "SWISS ARABIAN", "nom": "Oud 01",
  "prix": 52.90, "famille": "oud", "stock": 50,
  "mot": {"fr": "Framboise et carvi pour ouvrir un parfum qui s'appelle Oud.",
          "en": "Raspberry and caraway to open a fragrance called Oud.",
          "nl": "Framboos en karwij om een geur te openen die Oud heet.",
          "de": "Himbeere und Kümmel als Auftakt eines Duftes namens Oud."}},
 # --- EXPERT -----------------------------------------------------------
 {"niveau": "expert", "ean": "6290362344094",
  "maison": "MAISON ALHAMBRA", "nom": "Glacier Gold",
  "prix": 31.90, "famille": "safran", "stock": 42,
  "mot": {"fr": "Le cumin au cœur. Ce n'est pas une note consensuelle.",
          "en": "Cumin at its heart. That is not a consensual note.",
          "nl": "Komijn in het hart. Dat is geen note die iedereen ligt.",
          "de": "Kreuzkümmel im Herzen. Keine Note für jedermann."}},
 {"niveau": "expert", "ean": "6298141927940",
  "maison": "EMIR", "nom": "Frenetic Tobacco Honey",
  "prix": 26.90, "famille": "cuir", "stock": 11,
  "mot": {"fr": "Une boîte à cigares ouverte, enrobée de miel.",
          "en": "An open cigar box, wrapped in honey.",
          "nl": "Een open sigarendoos, omhuld met honing.",
          "de": "Eine offene Zigarrenkiste, in Honig gehüllt."}},
]

LANGUES = ("fr", "en", "nl", "de")


def par_niveau(cle):
    return [x for x in PARFUMS if x["niveau"] == cle]


def garde_fou():
    """On verifie AVANT de dessiner, pas apres.

    Les trois choses qui rendraient ce carrousel malhonnete ou faux :
    un parfum deja passe les jours precedents, une scene manquante, et
    surtout un palier Expert plus cher que le palier Debutant — ce qui
    transformerait le conseil en argumentaire de vente.
    """
    deja = set()
    for f in ("coude12novembre", "duel13novembre"):
        c = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f, "carrousel.py")
        if os.path.exists(c):
            deja |= set(re.findall(r'"(\d{13})"', open(c, encoding="utf-8").read()))
    for pf in PARFUMS:
        assert pf["ean"] not in deja, "%s est deja passe cette semaine" % pf["nom"]
        chemin = os.path.join(SCENES, pf["ean"] + "c.jpg")
        assert os.path.exists(chemin), "scene manquante : " + chemin
        assert pf["stock"] >= 10, "%s n a que %d en stock" % (pf["nom"], pf["stock"])
        for lg in LANGUES:
            assert pf["mot"].get(lg), "%s : pas de phrase en %s" % (pf["nom"], lg)
        assert pf["famille"] in F, "famille inconnue : " + pf["famille"]
    assert len({pf["ean"] for pf in PARFUMS}) == 6, "six parfums distincts attendus"
    for n in NIVEAUX:
        assert len(par_niveau(n["cle"])) == 2, "deux parfums par niveau"
    exp = max(x["prix"] for x in par_niveau("expert"))
    deb = min(x["prix"] for x in par_niveau("debutant"))
    assert exp < deb, ("LE PALIER EXPERT DOIT RESTER LE MOINS CHER — sinon le "
                       "carrousel devient une montee en gamme deguisee en conseil "
                       "(expert %.2f, debutant %.2f)" % (exp, deb))
    print("garde-fou : 6 parfums, aucun deja passe, expert %.2f < debutant %.2f"
          % (exp, deb))


# ------------------------------------------------------------------ diapos

TITRES = {
 "couverture": {"fr": "Débutant,\nconnaisseur,\nexpert", "en": "Beginner,\nconnoisseur,\nexpert",
                "nl": "Beginner,\nkenner,\nexpert",      "de": "Einsteiger,\nKenner,\nExperte"},
 "ou":   {"fr": "Tu es où ?", "en": "Where do you sit?",
          "nl": "Waar sta jij?", "de": "Wo stehen Sie?"},
 "regle_t": {"fr": "Le niveau parle du parfum.\nPas du prix.",
             "en": "The level is about the scent.\nNot the price.",
             "nl": "Het niveau gaat over de geur.\nNiet over de prijs.",
             "de": "Die Stufe betrifft den Duft.\nNicht den Preis."},
 "regle_s": {"fr": "Les deux parfums les moins chers de ce carrousel sont dans le "
                   "palier Expert. Ce n'est pas une erreur, c'est la preuve.",
             "en": "The two cheapest fragrances here sit in the Expert tier. "
                   "That is not a mistake, it is the proof.",
             "nl": "De twee goedkoopste geuren hier staan in de Expert-rij. "
                   "Dat is geen vergissing, dat is het bewijs.",
             "de": "Die beiden günstigsten Düfte hier stehen in der Experten-Stufe. "
                   "Das ist kein Fehler, das ist der Beweis."},
 "preuve_t": {"fr": "La preuve, en euros", "en": "The proof, in euros",
              "nl": "Het bewijs, in euro", "de": "Der Beweis, in Euro"},
 "fin_t": {"fr": "Alors, tu es où ?", "en": "So, where do you sit?",
           "nl": "En, waar sta jij?", "de": "Und, wo stehen Sie?"},
 "fin_s": {"fr": "Dis-le en commentaire. Les vingt-sept maisons sont sur la boutique.",
           "en": "Say it in the comments. All twenty-seven houses are in the shop.",
           "nl": "Zeg het in de reacties. Alle zevenentwintig huizen staan in de winkel.",
           "de": "Schreiben Sie es in die Kommentare. Alle siebenundzwanzig Häuser im Shop."},
}


def fond(lg):
    img = Image.new("RGB", (W, H), CREME)
    return img, ImageDraw.Draw(img)


# Les deux images de Claude Code, livrees le 13/11 a 20h40. Il a mesure les
# positions dans le journal, je m en sers pour choisir les decalages :
#   niveaux1  — tete y 350-660, flacon en main y 750-890, flacons de table
#               y 1350-1570
#   niveaux10 — flacons y 965-1565, mur nu au-dessus
# Le bandeau de la couverture s arrete AVANT les flacons de la table : on
# garde le visage et le flacon en main, le reste serait coupe par le fondu.
HAUT_1 = 860          # hauteur du bandeau de couverture
DEC_1 = 300           # on entre dans l image juste au-dessus de la tete
HAUT_10 = 1060        # le bandeau du bas, qui contient les trois flacons
DEC_10 = 860          # 965 - 105 : un peu d air au-dessus des bouchons


def diapo_1(lg):
    img = Image.new("RGB", (W, H), CREME)
    img.paste(photo("niveaux1.jpg", HAUT_1, DEC_1), (0, 0))
    fondu(img, HAUT_1 - 200, 200)
    d = ImageDraw.Draw(img)
    lettrage(d, HAUT_1 + 60, TITRES["ou"][lg].upper(), inter(34, "SemiBold"),
             OCRE, 10)
    bloc_ajuste(d, MARGE_G, HAUT_1 + 150, TITRES["couverture"][lg].split("\n"),
                116, ENCRE, LARGE, 1520)
    d.line([(MARGE_G, 1580), (MARGE_G + 180, 1580)], fill=OCRE, width=4)
    bloc(d, MARGE_G, 1630, TITRES["regle_s"][lg], serif(34, 400, 34, True),
         ENCRE_D, LARGE)
    poser_signature(img, MARGE_G, 1830, ENCRE_D, 30, 7)
    return img


def diapo_2(lg):
    img, d = fond(lg)
    lettrage(d, 300, "01", inter(34, "SemiBold"), OCRE, 10)
    bloc_ajuste(d, MARGE_G, 400, TITRES["regle_t"][lg].split("\n"),
                96, ENCRE, LARGE, 900)
    y = 980
    for n in NIVEAUX:
        lots = par_niveau(n["cle"])
        lettrage(d, y, n["titre"][lg].upper(), inter(30, "SemiBold"), OCRE, 8)
        # La fourchette de prix est calee A DROITE, et le sous-titre ne peut
        # pas empieter dessus : en allemand, « Daran muss man sich gewöhnen »
        # passait par-dessus « 26,90 € ». On mesure, on reduit le corps tant
        # que ca ne tient pas, et on garde 40 px de respiration.
        texte_prix = "%s — %s" % (prix(min(x["prix"] for x in lots), lg),
                                  prix(max(x["prix"] for x in lots), lg))
        pf_prix = inter(38, "Medium")
        l_prix = d.textlength(texte_prix, font=pf_prix)
        x_prix = W - MARGE_D - l_prix
        d.text((x_prix, y + 56), texte_prix, font=pf_prix, fill=ENCRE_D)
        place = x_prix - MARGE_G - 40
        corps = 44
        while corps > 26 and d.textlength(n["sous"][lg],
                                          font=serif(corps, 400, corps, True)) > place:
            corps -= 2
        d.text((MARGE_G, y + 52), n["sous"][lg],
               font=serif(corps, 400, corps, True), fill=ENCRE)
        y += 150
    poser_signature(img, MARGE_G, 1760, ENCRE_D, 32, 8)
    return img


def diapo_parfum(pf, rang, lg):
    img = Image.new("RGB", (W, H), CREME)
    sc = Image.open(os.path.join(SCENES, pf["ean"] + "c.jpg")).convert("RGB")
    ech = W / sc.width
    sc = sc.resize((W, int(sc.height * ech)), Image.LANCZOS)
    haut = 980
    img.paste(sc.crop((0, 0, W, min(haut, sc.height))), (0, 0))
    fondu(img, haut - 220, 220)
    d = ImageDraw.Draw(img)
    niv = next(n for n in NIVEAUX if n["cle"] == pf["niveau"])
    lettrage(d, haut + 60, niv["titre"][lg].upper(), inter(32, "SemiBold"), OCRE, 10)
    d.text((MARGE_G, haut + 120), pf["maison"], font=inter(30, "Medium"), fill=ENCRE_D)
    bloc_ajuste(d, MARGE_G, haut + 176, [pf["nom"]], 76, ENCRE, LARGE, haut + 330)
    d.line([(MARGE_G, haut + 360), (MARGE_G + 120, haut + 360)], fill=OCRE, width=3)
    bloc(d, MARGE_G, haut + 400, pf["mot"][lg], serif(44, 400, 44, True),
         ENCRE, LARGE)
    d.text((MARGE_G, 1700), F[pf["famille"]][lg], font=inter(28, "Medium"),
           fill=ENCRE_D)
    d.text((MARGE_G, 1748), prix(pf["prix"], lg), font=inter(44, "SemiBold"),
           fill=ENCRE)
    poser_signature(img, W - MARGE_D - largeur_signature(30, 7), 1760, ENCRE_D, 30, 7)
    return img


def diapo_preuve(lg):
    img, d = fond(lg)
    lettrage(d, 300, "09", inter(34, "SemiBold"), OCRE, 10)
    bloc_ajuste(d, MARGE_G, 400, TITRES["preuve_t"][lg].split("\n"),
                96, ENCRE, LARGE, 700)
    y = 820
    for n in NIVEAUX:
        lots = sorted(par_niveau(n["cle"]), key=lambda x: x["prix"])
        lettrage(d, y, n["titre"][lg].upper(), inter(30, "SemiBold"), OCRE, 8)
        yy = y + 54
        for x in lots:
            d.text((MARGE_G, yy), "%s %s" % (x["maison"].title(), x["nom"]),
                   font=serif(38, 400, 38, True), fill=ENCRE)
            d.text((W - MARGE_D - 170, yy), prix(x["prix"], lg),
                   font=inter(36, "Medium"), fill=ENCRE_D)
            yy += 56
        y = yy + 46
    bloc(d, MARGE_G, y + 10, TITRES["regle_s"][lg], serif(36, 400, 36, True),
         ENCRE_D, LARGE)
    poser_signature(img, MARGE_G, 1800, ENCRE_D, 30, 7)
    return img


def diapo_fin(lg):
    img = Image.new("RGB", (W, H), CREME)
    img.paste(photo("niveaux10.jpg", HAUT_10, DEC_10), (0, H - HAUT_10))
    # PAS DE FONDU ICI, et c est voulu. fondu() va du transparent vers le
    # creme EN DESCENDANT : sur un bandeau bas il voilerait le haut des
    # flacons, dont les bouchons dores commencent 105 px sous la couture.
    # Le haut du bandeau tombe sur le mur nu de l image, donc la coupe
    # franche se lit comme un choix et non comme un accident.
    d = ImageDraw.Draw(img)
    bloc_ajuste(d, MARGE_G, 280, TITRES["fin_t"][lg].split("\n"),
                104, ENCRE, LARGE, 560)
    d.line([(MARGE_G, 620), (MARGE_G + 180, 620)], fill=OCRE, width=4)
    bloc(d, MARGE_G, 670, TITRES["fin_s"][lg], serif(40, 400, 40, True),
         ENCRE_D, LARGE)
    # Le lien doit finir AVANT la couture de la photo (y = H - HAUT_10 = 860).
    # A 850 il tombait pile dessus et devenait illisible : ocre sur photo.
    d.text((MARGE_G, 772), LIEN, font=inter(38, "SemiBold"), fill=OCRE)
    assert 772 + 46 < H - HAUT_10, "le lien mord sur la photo"
    poser_signature(img, MARGE_G, 120, ENCRE_D, 30, 7)
    return img


def main():
    garde_fou()
    lg = (sys.argv[1] if len(sys.argv) > 1 else "fr").lower()
    assert lg in LANGUES, "langue inconnue : " + lg
    dossier = os.path.join(SORTIE, lg)
    os.makedirs(dossier, exist_ok=True)
    pages = [diapo_1(lg), diapo_2(lg)]
    for i, pf in enumerate(PARFUMS):
        pages.append(diapo_parfum(pf, i, lg))
    pages += [diapo_preuve(lg), diapo_fin(lg)]
    assert len(pages) == 10, "dix diapos attendues, %d produites" % len(pages)
    for i, im in enumerate(pages, 1):
        im.save(os.path.join(dossier, "%02d.jpg" % i), quality=92, optimize=True)
    print("%s : %d diapos ecrites dans %s" % (lg, len(pages), dossier))


if __name__ == "__main__":
    main()
