# -*- coding: utf-8 -*-
"""
BMH - socle commun du 22 novembre 2026.  FORMAT TIKTOK 1080 x 1920.

Repris tel quel du carrousel du 19/11 (detour/socle.py) : polices, decoupe de
texte, capitales ajustees, voiles en rampe, plein cadre, signature de marque.
Seuls RACINE et la table CX changent.

⚠️ DIX DIAPOS MAXIMUM — L'API INSTAGRAM COUPE AU-DELA, EN SILENCE.
La derniere diapo n'est JAMAIS la variable d'ajustement : c'est la seule qui
porte l'adresse de la boutique.

ZONES TIKTOK : 150 px en haut, 480 px en bas, 120 px a droite sont manges
par l'interface. Tout le texte vit entre y=200 et y=1400.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

W, H    = 1080, 1920
RACINE = "/home/claude/maison"
SCENES  = os.path.join(RACINE, "scenes")
POLICES = "/home/claude/polices"
SORTIE  = os.path.join(RACINE, "carrousel")
VISAGE  = os.path.join(RACINE, "daoud.png")

CREME   = (240, 228, 206)
OCRE    = (181, 85, 31)
BLANC   = (255, 255, 255)
NUIT    = (20, 14, 10)

LIEN = "shop.bringmedinahome.com"

MARGE_G, MARGE_D = 88, 180
LARGE = W - MARGE_G - MARGE_D

LANGUES = ("fr", "en", "nl", "de")
MAX_DIAPOS = 10          # limite dure de l'API Instagram

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


def caps_auto(d, x, y, texte, corps, couleur, lmax, interligne=1.10):
    """Capitales dont les retours a la ligne sont calcules. Sert aux titres
    de conseil, dont la longueur change beaucoup d'une langue a l'autre :
    « NE FROTTE PAS » contre « ZIELEN SIE AUF DIE WARMEN STELLEN »."""
    for c in range(corps, 29, -3):
        p = inter(c, "Bold")
        lignes = couper(d, texte, p, lmax)
        if len(lignes) <= 3:
            break
    for l in lignes:
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


def poser_signature(img, x, y, couleur, corps=38, espace=8):
    #  38 px, pas 28. Daoud, le 19/11 : « toutes les grandes marques, leur
    #  marque c'est en lettres capitales, tout gros. Quand tu l'ecris
    #  toujours petit, ca ne reste pas dans la tete. » Il a raison : a 28 px
    #  sur une image de 1920, c'etait une mention legale, pas une marque.
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

#  Position horizontale du flacon, relevee a l'oeil le 18/11 sur une
#  planche-contact des huit scenes. Jamais devinee a partir du numero.
CX = {
 #  Releve a l'oeil le 22/11/2026 sur deux planches-contact, jamais devine.
 "6291107454412": 0.66,   # Lattafa Ana Abiyedh Rouge
 "6290360598963": 0.695,  # Lattafa Mayar Cherry Intense
 "6291107456058": 0.69,   # Lattafa Fakhar Men
 "6290360591421": 0.69,   # Lattafa Yara Moi
 "6290360593661": 0.655,  # Lattafa Khamrah Qahwa
 "6291107458328": 0.69,   # Lattafa Badee Al Oud For Glory
 "0614514331026": 0.66,   # Rasasi Hawas For Him
}

VOILE_HAUT = [(0, 232), (420, 222), (720, 110), (1000, 0)]
VOILE_BAS  = [(900, 0), (1060, 150), (1180, 214), (1320, 242), (1920, 248)]
VOILE_COUV = [(0, 234), (580, 228), (920, 160), (1280, 0)]
#  Sur les diapos de conseil, le texte occupe tout le haut et il n'y a rien
#  en bas : un seul voile, long et profond.
VOILE_CONSEIL = [(0, 236), (700, 230), (1020, 150), (1380, 0)]


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
    sources = [haut if haut is not None else VOILE_HAUT]
    if bas is not None:
        sources.append(bas)
    for src in sources:
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

