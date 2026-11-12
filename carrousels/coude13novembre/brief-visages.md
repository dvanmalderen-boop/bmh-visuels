# Brief pour Claude Code — les images « l'endroit où on le met »

Pour la machine de Daoud. Génération fal.ai. Je ne peux pas générer depuis
mon côté : le réseau de mon bac à sable ne sort que vers GitHub et les
dépôts de paquets. Testé le 12/11 : fal.ai répond 000.

---

## LES HORAIRES — ON NE SE MARCHE PAS DESSUS

- **11 h 00 — Claude Code** : le post personnage, comme d'habitude. Inchangé.
- **15 h 45 — session cloud** : le carrousel. Déjà programmé pour le 13/11.
- **19 h 45 — Daoud** : la vidéo du jour.

Ce brief ne demande **aucune publication** : seulement de générer sept images
et de les déposer dans le dépôt. La publication reste sur le créneau de 15 h 45.

---

## LES RÈGLES, AVANT TOUT LE RESTE

**1. Les visages.** Des **hommes**. Si une femme apparaît, elle est
**voilée**, vue **de profil ou de trois quarts dos**, et **son visage n'est
pas lisible**. Aucune exception, aucune interprétation large. Dans le doute :
pas de personne du tout, seulement les mains et les avant-bras.

**2. La main.** La main **soulève** le flacon, elle ne le pose pas sur un
support. Aucun support visible. **Main nue** — pas de gant, pas de bijou
clinquant. Le flacon est un **vrai flacon**, pas une invention.

**3. Le cadre.** 1080 × 1920, **9:16**. Le visage, s'il y en a un, occupe
**moins de 20 %** du cadre (mesuré par TikTok : +31 % de considération
contre un visage plus gros).

**4. Les zones mortes de TikTok.** L'interface mange 150 px en haut,
480 px en bas, 120 px à droite. **Le sujet vit dans le tiers central
gauche.** Rien d'important à droite ni dans les 480 px du bas.

**5. Pas de texte dans l'image générée.** Le texte est gravé après, par
`carrousel.py`. Une image qui arrive avec du faux texte est à refaire.

**6. Style.** Lumière chaude et rasante, fond crème ou bois sombre,
rendu photographique. Le même étalonnage que les scènes produit
existantes du dépôt `bmh-visuels`.

---

## LES SEPT IMAGES

Toutes en 1080 × 1920. Nommées `coude1.jpg` … `coude7.jpg`.

**coude1 — la couverture.**
> Close-up photograph, warm raking light. A man's bare forearm, sleeve of a
> white qamis pushed up above the elbow. His other hand lifts a small amber
> glass perfume bottle toward the upper arm, finger on the atomiser. The
> bottle is fully held in the air, no surface under it. Skin texture
> visible, no jewellery. Cream linen background, soft shadows. Vertical
> 9:16, subject in the centre-left third, upper two thirds of the frame.
> No text, no logo, no watermark.

**coude2 — le haut du bras.**
> Same man, same qamis, photographed from the side. He sprays perfume onto
> his upper arm, just above the elbow, sleeve lifted. The bottle is held in
> the air. Fine mist visible in the raking light. Face out of frame — the
> crop stops at the shoulder. Cream background. Vertical 9:16. No text.

**coude3 — la nuque.**
> A man seen from behind, three-quarter back view, wearing a white qamis.
> He lifts a perfume bottle to the back of his neck, below the hairline.
> His face is not visible. Warm light from the left. Cream wall background.
> Vertical 9:16, subject centre-left. No text.

**coude4 — le col.**
> Close-up of the collar of a white qamis on a man, cropped at the chin so
> no face is visible. A bare hand holds a perfume bottle against the fabric
> of the collar, nozzle toward the cloth. Fabric weave visible. Warm light.
> Vertical 9:16. No text.

**coude5 — derrière l'oreille.**
> Profile view of a bearded man, cropped tightly: only the jaw, ear and
> neck are in frame, the eyes are above the crop. A bare hand lifts a dark
> oud perfume bottle behind the ear. Warm raking light, dark wood
> background. Vertical 9:16, the head occupying less than a fifth of the
> frame. No text.

**coude6 — l'épaule.**
> A man's shoulder in a white qamis, photographed from above and behind, no
> face in frame. A bare hand lifts a perfume bottle just above the shoulder
> seam. Soft mist in the air. Cream and sand tones. Vertical 9:16. No text.

**coude7 — le revers, en sortant.**
> A man's hand, cropped at the wrist, slipping a small 30 ml roll-on
> perfume bottle into the inside pocket of a dark jacket. Only the hand and
> the jacket are in frame. Warm evening light, dark background with a
> single warm highlight. Vertical 9:16. No text.

---

## CE QU'ON EN FAIT

Les sept images se déposent dans `/home/claude/coude/scenes/` sous ces noms,
puis on remplace dans `carrousel.py` la clé `ean=` par `fichier=` pour les
diapos concernées. Les scènes produit actuelles restent le repli : le
carrousel tourne déjà sans ces images.

**Ordre de priorité si une seule image est générée : `coude1`.**
C'est la couverture, c'est elle qui décide si quelqu'un scrolle.
