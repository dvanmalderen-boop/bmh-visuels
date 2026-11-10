# Le logo Bring Medina Home

## Le fichier à utiliser

`bmhlogo-mot-seul.png` — 2016 × 396 px, fond transparent, rapport 5,09.

Le mot de marque seul, sans le sigle BMH, dans le cadre doré d'origine.
C'est le logo du site depuis le 10/11/2026.

## Pourquoi celui-là et pas l'ancien

`ancien-logo-bmh-512x135.png` est l'ancien, gardé pour mémoire. Deux défauts,
et ce sont eux qui ont motivé le changement :

1. **Une grosse marge transparente.** Le fichier fait 512 × 135 mais la plaque
   noire n'occupe que 336 × 66 dedans : 92 px de vide à gauche, 84 à droite,
   35 en haut, 34 en bas. Shopify aligne le FICHIER, pas le dessin — donc le
   logo paraissait centré dans sa colonne et impossible à coller à gauche,
   alors que le fichier, lui, était déjà à gauche. Et la moitié de la hauteur
   réglée partait en vide : 200 px de réglage ne donnaient que 98 px de plaque.
2. **Trop petit pour un écran moderne.** 512 px de large à afficher sur 500 à
   760 px, sur un écran qui compte deux à trois pixels réels par pixel de page :
   le navigateur agrandissait, et ça bavait sur mobile.

Le mot de marque y faisait aussi 9 px de capitale sur une plaque de 66, soit
0,136 de la hauteur — illisible en petit. Dans le nouveau il est à 0,25.

## Les règles à respecter si on le refait

- **Aucune marge transparente.** La plaque touche les quatre bords du fichier.
- **Au moins quatre fois la taille d'affichage.** Ici six fois.
- **Police du mot de marque : Inter Medium**, vérifié le 10/11 en superposant
  l'original et plusieurs graisses à hauteur de capitale égale.
- **Le serif du sigle BMH n'a jamais été identifié.** Aucune des polices
  disponibles ne correspond à ses empattements plats et épais. Si un jour on
  doit redessiner le sigle, il faut demander à Daoud le fichier source ou le
  nom de la police — ne pas improviser.
- Relevé du cadre, au pixel : 3 px d'épaisseur, rayon 6, fond (7, 13, 13),
  or en dégradé horizontal de (160,120,62) aux deux bouts à (245,221,153) au
  milieu, bord bas un peu plus mat. Mot de marque (165, 154, 127).

`motseul.py` régénère le fichier. Tout y est commenté.

## Où il est posé

- Shopify, réglage « Logo » du thème — en-tête et barre de navigation.
- Pied de page : le bloc Logo doit avoir **« Utiliser le logo inversé »
  DÉCOCHÉ**, sinon il retombe sur l'ancien fichier, qui est encore dans
  l'emplacement « Logo inversé ».
