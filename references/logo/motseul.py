# -*- coding: utf-8 -*-
"""
BMH - le logo « BRING MEDINA HOME » SEUL, sans le sigle.

C'est ce que Daoud a demande le 10/11 : le meme cadre dore, mais uniquement le
mot de marque, et assez grand pour etre lisible sur un telephone.

POURQUOI CA MARCHE MIEUX QUE D'AGRANDIR LE MOT DANS LE LOGO COMPLET : dans
l'original, BMH et sa barre mangeaient 120 des 336 px de plaque, soit plus du
tiers. En les retirant, toute la largeur revient au mot de marque. Il passe de
9 px de hauteur de capitale a 17, dans une plaque de meme proportion.

TOUT LE CADRE EST RELEVE SUR L'ORIGINAL AU PIXEL, RIEN N'EST REINVENTE :
  plaque      336 x 66, soit un rapport de 5,09
  cadre       3 px, rayon 6 px
  fond        (7, 13, 13)
  or          degrade horizontal, sombre (160,120,62) aux deux bouts,
              clair (245,221,153) au milieu ; le bord bas un peu plus mat
  mot         (165, 154, 127)

LA POLICE DU MOT EST BIEN INTER. Verifie le 10/11 en superposant le mot de
l'original et plusieurs graisses d'Inter a hauteur de capitale egale : les
formes du G, du R et du M correspondent. C'est l'Inter Medium qui colle, avec
un interlettre d'environ 0,19 de la hauteur de capitale.
(Le serif du sigle BMH, lui, n'a PAS ete identifie - mais il ne sert plus ici.)

Sortie en PNG a fond transparent, a six fois la taille, pour rester net sur un
ecran a haute densite.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ICI = "/home/claude/logo"
INTER = "/usr/share/fonts/opentype/inter/Inter-%s.otf"

H_PLAQUE  = 66
L_PLAQUE  = 336          # on garde le rapport de l'original : il se pose au
CADRE     = 3            # meme endroit, rien d'autre ne bouge dans la page
RAYON     = 6
FOND      = (7, 13, 13)
OR_SOMBRE = (160, 120, 62)
OR_CLAIR  = (245, 221, 153)
MOT       = (165, 154, 127)

MARGE       = 26         # de chaque cote, le mot est centre
INTERLETTRE = 0.16       # fraction de la hauteur de capitale
ECHELLE     = 6

TEXTE = "BRING MEDINA HOME"


def sans(cap, graisse="Medium"):
    """Inter regle pour que la hauteur de capitale tombe juste."""
    corps = max(4, int(cap * 1.38))
    f = ImageFont.truetype(INTER % graisse, corps)
    for _ in range(40):
        h = f.getbbox("H")[3] - f.getbbox("H")[1]
        if abs(h - cap) <= 0.6:
            break
        corps = max(4, int(round(corps * cap / max(h, 1))))
        f = ImageFont.truetype(INTER % graisse, corps)
    return f


def largeur(d, texte, police, inter):
    l = 0.0
    for i, c in enumerate(texte):
        l += d.textlength(c, font=police)
        if i < len(texte) - 1:
            l += inter
    return l


def poser(d, x, base, texte, police, couleur, inter):
    haut = police.getbbox("H")[1]
    for i, c in enumerate(texte):
        d.text((x, base - (police.getbbox("H")[3] - haut) - haut), c,
               font=police, fill=couleur)
        x += d.textlength(c, font=police)
        if i < len(texte) - 1:
            x += inter


def or_degrade(L, H, mat=0.0):
    bande = Image.new("RGB", (L, 1))
    p = bande.load()
    for x in range(L):
        q = (abs(x / max(L - 1, 1) - 0.5) * 2) ** 1.25
        c = tuple(int(OR_CLAIR[i] + (OR_SOMBRE[i] - OR_CLAIR[i]) * q) for i in range(3))
        if mat:
            c = tuple(int(v * (1 - mat) + 150 * mat) for v in c)
        p[x, 0] = c
    return bande.resize((L, H), Image.NEAREST)


def construire(echelle=ECHELLE, l_plaque=L_PLAQUE):
    E = echelle
    L, H = l_plaque * E, H_PLAQUE * E
    dispo = (l_plaque - 2 * MARGE) * E

    # --- chercher la plus grande capitale qui tienne dans la largeur ------
    sonde = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    cap = 1
    while True:
        f = sans(cap + 1)
        if largeur(sonde, TEXTE, f, (cap + 1) * INTERLETTRE) > dispo:
            break
        cap += 1
        if cap > H_PLAQUE * E:
            break
    f = sans(cap)
    inter = cap * INTERLETTRE
    l_mot = largeur(sonde, TEXTE, f, inter)

    img = Image.new("RGBA", (L, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    masque = Image.new("L", (L, H), 0)
    ImageDraw.Draw(masque).rounded_rectangle([0, 0, L - 1, H - 1],
                                             radius=RAYON * E, fill=255)
    plaque = Image.new("RGBA", (L, H), (0, 0, 0, 0))
    plaque.paste(or_degrade(L, H), (0, 0))
    plaque.paste(or_degrade(L, H // 2, mat=0.12), (0, H // 2))
    plaque.putalpha(masque)
    img.alpha_composite(plaque)

    c = CADRE * E
    inte = Image.new("L", (L, H), 0)
    ImageDraw.Draw(inte).rounded_rectangle([c, c, L - 1 - c, H - 1 - c],
                                           radius=max(RAYON * E - c, 1), fill=255)
    noir = Image.new("RGBA", (L, H), FOND + (255,))
    noir.putalpha(inte)
    img.alpha_composite(noir)

    # centre horizontalement et optiquement a la verticale
    x = (L - l_mot) / 2
    base = (H + cap) / 2
    poser(d, x, base, TEXTE, f, MOT, inter)

    return img, cap / E


def main():
    os.makedirs(ICI, exist_ok=True)
    img, cap = construire()
    chemin = os.path.join(ICI, "bmhlogo-mot-seul.png")
    img.save(chemin)
    print("  %s  %dx%d  rapport %.2f" % (chemin, img.size[0], img.size[1],
                                         img.size[0] / img.size[1]))
    print("  capitale : %.1f sur une plaque de %d, soit %.3f de la hauteur"
          % (cap, H_PLAQUE, cap / H_PLAQUE))
    print("  l'original etait a 9 sur 66, soit 0,136 - gain de %.0f %%"
          % ((cap / 9 - 1) * 100))
    return img


if __name__ == "__main__":
    main()
