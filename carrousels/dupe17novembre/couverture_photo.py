# -*- coding: utf-8 -*-
"""La couverture TikTok, faite a partir d'une image de la video de Daoud.

TikTok n'accepte pas de video dans un carrousel photo. Plutot que de perdre
le benefice du visage, on prend une image de la video : Daoud, le flacon
pose devant lui, et le titre au-dessus de sa tete — c'est la seule bande
assez sombre et assez vide pour poser du texte sans manger son visage.
Releve du 16/11 : toute la tete de la categorie parfum est portee par des
createurs, pas par des marques.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageEnhance

sys.path.insert(0, "/home/claude/dupe")
import carrousel as C   # noqa: E402

PHOTO = "/home/claude/dupe/photo.jpg"
VOILE_PHOTO = [(0, 238), (380, 232), (560, 180), (760, 0)]
#  Le bas reste CLAIR : c'est la que se trouve le flacon. Le voile
#  du bas des autres diapos le faisait disparaitre completement.
VOILE_PHOTO_BAS = [(1560, 0), (1920, 95)]


def couverture_photo(lg):
    im = Image.open(PHOTO).convert("RGB")
    e = C.H / im.height
    im = im.resize((int(im.width * e), C.H), Image.LANCZOS)
    x = max(0, min(int(0.5 * im.width - C.W / 2), im.width - C.W))
    im = ImageEnhance.Brightness(im.crop((x, 0, x + C.W, C.H))).enhance(1.22)
    img = C.voile(im, haut=VOILE_PHOTO, bas=VOILE_PHOTO_BAS)
    d = ImageDraw.Draw(img)
    C.lettrage(d, 218, C.T["sup"][lg], C.inter(30, "SemiBold"), C.OCRE, 10)
    titre = C.T["couv_t"][lg].replace("\n", " ")
    y = C.bloc_caps(d, C.MARGE_G, 256, titre, 74, C.BLANC, C.LARGE)
    d.line([(C.MARGE_G, y + 24), (C.MARGE_G + 150, y + 24)], fill=C.OCRE,
           width=4)
    fin = C.bloc_ajuste(d, C.MARGE_G, y + 60, [C.T["couv_s"][lg]], 36,
                        C.CREME, C.LARGE, 700, ital=True)
    assert fin <= 700, "le texte descend sur le visage (%d)" % fin
    C.poser_signature(img, C.MARGE_G, 1830, C.CREME)
    return img


if __name__ == "__main__":
    for lg in C.LANGUES:
        d = os.path.join(C.SORTIE, lg)
        os.makedirs(d, exist_ok=True)
        couverture_photo(lg).save(os.path.join(d, "tk01.jpg"), quality=90,
                                  optimize=True)
        print(lg, "tk01.jpg ecrite")
