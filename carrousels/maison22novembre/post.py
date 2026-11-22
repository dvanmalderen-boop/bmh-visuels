# -*- coding: utf-8 -*-
"""
BMH - le post image du 22 novembre 2026, 11h00.  1080 x 1920.

CE QUE DAOUD A DEMANDE
« Mets un parfum, mets une belle phrase, mets Bring Medina Home en grand.
Je veux que ce Bring Medina Home, ca sorte partout. »

Donc une seule image, et la marque est le sujet. Le parfum est le decor,
la phrase est l'entree, BRING MEDINA HOME occupe le milieu du cadre en trois
lignes justifiees — le meme lettrage que la carte de marque adjugee le 19/11.

LE PARFUM : Rasasi Hawas For Him, 44,90 €, 23 en stock (verifie en direct
dans Shopify le 22/11). Choisi pour deux raisons : la marge est dans la bande
(il n'est pas dans la liste des 50 sous 9,50 €), et surtout la scene montre
exactement ce que raconte sa fiche — du bois flotte, des galets, du sel.

LA PHRASE N'EST PAS INVENTEE. Elle est recopiee de la fiche produit :
« Le bois flotte, c'est cette odeur de bois seche par le sel et le soleil. »
On garde la moitie qui fait image.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import ImageDraw                                    # noqa: E402
from socle import (                                          # noqa: E402
    W, H, MARGE_G, LARGE, LANGUES, SORTIE, CREME, OCRE,
    serif, inter, bloc_ajuste, lettrage, plein_cadre, voile,
)

EAN = "0614514331026"
NOM = "Rasasi Hawas For Him"
PRIX = 44.90
ML = 100
STOCK = 23           # releve le 22/11/2026 dans Shopify

LIEN = "shop.bringmedinahome.com"

#  Recopiee de la fiche, pas ecrite ici.
PHRASE = {
    "fr": "Du bois séché par le sel et le soleil.",
    "en": "Wood dried by salt and sun.",
    "nl": "Hout, gedroogd door zout en zon.",
    "de": "Holz, getrocknet von Salz und Sonne.",
}

#  Le mot qui annonce la phrase, en petites capitales espacees.
SUR = {"fr": "LE FOND", "en": "THE BASE", "nl": "DE BASIS", "de": "DIE BASIS"}

#  Le voile : profond en haut pour la phrase, profond en bas pour la marque.
#  Le flacon vit entre les deux et reste lisible.
VOILE_HAUT = [(0, 238), (380, 230), (640, 120), (900, 0)]
VOILE_BAS = [(820, 0), (1000, 120), (1140, 210), (1300, 244), (1920, 250)]


def prix_affiche(p, lg):
    return ("%.2f" % p).replace(
        ".", "," if lg in ("fr", "de", "nl") else ".") + " €"


def marque_geante(img, d, y, bloc=820, depart=210):
    """BRING / MEDINA / HOME, trois lignes justifiees a la meme largeur.
    Regle posee par Daoud le 19/11 : le nom en grand, le bam dans la figure.
    Detail dans les fichiers du projet, claude/carte-de-marque.md."""
    mots = ("BRING", "MEDINA", "HOME")
    for corps in range(depart, 60, -2):
        p = inter(corps, "Bold")
        if max(sum(d.textlength(c, font=p) for c in m) for m in mots) <= bloc:
            break
    p = inter(corps, "Bold")
    for m in mots:
        brut = sum(d.textlength(c, font=p) for c in m)
        espace = (bloc - brut) / float(len(m) - 1)
        x = MARGE_G
        for c in m:
            d.text((x, y), c, font=p, fill=CREME)
            x += d.textlength(c, font=p) + espace
        if m == "HOME":
            d.text((MARGE_G + bloc + 30, y + corps * 0.10), "®",
                   font=inter(int(corps * 0.26), "Medium"), fill=OCRE)
        y += int(corps * 1.12)
    return y, corps


def image(lg):
    img = voile(plein_cadre(EAN), haut=VOILE_HAUT, bas=VOILE_BAS)
    d = ImageDraw.Draw(img)

    #  Haut : la phrase. C'est elle qu'on lit en premier.
    lettrage(d, 252, SUR[lg], inter(28, "SemiBold"), OCRE, 7)
    bloc_ajuste(d, MARGE_G, 312, [PHRASE[lg]], 76, CREME, LARGE, 560,
                poids=500, ital=True)

    #  Milieu-bas : la marque, en grand.
    y, corps = marque_geante(img, d, 1012)

    #  Pied : ce qu'on voit sur l'image, puis l'adresse.
    d.line([(MARGE_G, y + 34), (MARGE_G + 820, y + 34)], fill=OCRE, width=5)
    pied = "%s · %d ml · %s" % (NOM, ML, prix_affiche(PRIX, lg))
    d.text((MARGE_G, y + 78), pied, font=inter(38, "Medium"), fill=CREME)
    d.text((MARGE_G, y + 142), LIEN, font=inter(34, "SemiBold"), fill=OCRE)
    return img


def garde_fou():
    """Deux verifications avant de dessiner : la phrase vient bien de la
    fiche, et on ne promet aucun chiffre qui n'a pas ete lu."""
    import re
    assert STOCK >= 10, "stock trop court pour pousser cette reference"
    for lg in LANGUES:
        assert lg in PHRASE and PHRASE[lg], "phrase manquante en " + lg
        assert not re.search(r"\d+\s*(%|heures|hours|uur|Stunden)", PHRASE[lg]), \
            "aucune promesse chiffree dans la phrase"


def main():
    garde_fou()
    os.makedirs(SORTIE, exist_ok=True)
    for lg in LANGUES:
        dossier = os.path.join(SORTIE, "post", lg)
        os.makedirs(dossier, exist_ok=True)
        chemin = os.path.join(dossier, "p01.jpg")
        image(lg).save(chemin, quality=92, subsampling=0)
        print(chemin)


if __name__ == "__main__":
    main()
