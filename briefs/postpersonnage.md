# Brief — le post quotidien avec le personnage BMH

Pour Claude Code, sur la machine de Daoud. À faire **après la vidéo du jour**,
pas avant.

Ce document est le gabarit. Le livrable de chaque journée, ce sont trois images
et trois publications programmées.

---

## 1. L'idée, et pourquoi

Chaque jour, **un post par langue** : le personnage BMH dans une petite scène,
avec un parfum du catalogue, son prix, et la marque. Pittoresque, un peu
drôle. Pas une fiche produit.

Trois raisons mesurées, pas des impressions :

**Le public décroche sur le commercial, pas sur le produit.** Une étude parue
dans la *Revue d'économie RAND* en 2025 (618 influenceurs allemands, 560
espagnols, 67 235 observations) mesure qu'une publication portant un marqueur
commercial visible reçoit **0,39 à 0,55 fois** les likes d'une publication
normale. Mais une étude d'avril 2026 (286 vidéos courtes, 48 créatrices)
montre que **vendre son propre produit ne porte aucune pénalité
significative** (β = 0,057, p = 0,607) — à condition que ce soit cadré comme
une scène et non comme une annonce. Un personnage dans une situation, c'est
une scène. Un flacon avec un prix, c'est une annonce.

**La duplication est pénalisée.** Meta a étendu le 30 avril 2026 son
déclassement du contenu non original **aux photos et aux carrousels**. Trois
personnages différents pour les trois langues donnent trois images réellement
différentes. C'est exactement ce qu'il faut.

**Le personnage tient la première seconde.** Le public froid zappe sur le
premier plan, et un personnage dessiné ne déclenche pas ce réflexe comme un
visage. Une série récurrente construit de la reconnaissance.

---

## 2. Les trois personnages — un par langue

Les planches de référence sont dans ce dépôt, dossier `personnages/` :

| Langue | Fichier | Le personnage |
|---|---|---|
| **FR** | `personnages/personnagefr.jpg` | thobe **blanc**, crâne dégarni, barbe grise fournie, **yeux clairs** |
| **EN** | `personnages/personnageen.jpg` | thobe blanc + **keffieh rouge et blanc avec agal noir** |
| **NL** | `personnages/personnagenl.jpg` | thobe **bleu**, crâne dégarni, barbe grise |

**Ce qui ne change jamais, quelle que soit la scène :** le visage, la barbe
grise, le crâne dégarni, **les yeux clairs**, les chaussures brunes, le style
de rendu 3D doux à fond crème uni. Un rendu précédent lui avait donné des
**yeux marrons** — c'est faux, et c'est le genre d'erreur qui tue une série.

**La règle qui fait tout le travail : on joint TOUJOURS la planche du
personnage en image de référence.** Le modèle tient un style qu'on lui montre,
pas un style qu'on lui décrit. Ne jamais générer le personnage depuis le texte
seul, même avec une très bonne description.

### Les poses, et ce que chacune raconte

Les planches contiennent déjà un jeu de poses. S'en servir comme d'un
vocabulaire : une pose = un type de message. Ça donne de la variété sans
inventer un personnage différent chaque jour.

| Pose sur la planche | Ce qu'elle sert à dire |
|---|---|
| debout, neutre | la présentation simple |
| qui sent une touche à parfum, yeux fermés | le test, la découverte |
| pouce levé | la validation, « celui-là, oui » |
| mains sur la tête, bouche ouverte | la surprise — une odeur inattendue |
| doigt sur la bouche, chut | le secret, la bonne affaire |
| qui salue de la main | l'accueil, une nouvelle maison |
| qui tient un colis | la livraison, la commande arrivée |

Le ton : **chaleureux et léger**. Jamais de moquerie, jamais de gag aux dépens
de quelqu'un. Le personnage représente Daoud — il garde sa dignité.

---

## 3. La méthode — et elle est en DEUX temps

C'est le point le plus important du document.

**Temps 1 — générer la scène, SANS AUCUN TEXTE.**
Les modèles d'image écrivent mal. Un prix ou un nom généré dans l'image sort
tordu une fois sur trois, et c'est invisible tant qu'on ne regarde pas de
près.

**Temps 2 — poser la typographie en code**, par-dessus, avec Pillow. Le nom,
le format, le prix, l'adresse, la signature. C'est net, c'est exact, et c'est
la typo de marque.

Le gabarit existe déjà : **`post.py` de la campagne du jour** (par exemple
`/home/claude/arabiyat/post.py` côté session cloud) contient la mise en page
du post 1080 × 1350 — scène nette en haut sur 755 px, fondu de 150 px vers le
crème, signature au croissant en blanc à (70, 95), en-tête en capitales
espacées à 855, titre à 935, famille olfactive en italique orange à 1063, prix
en Inter SemiBold orange à 1163, « Le lien est dans la bio » à 1253, adresse à
1300. Reprendre cette mise en page telle quelle : le post au personnage doit
ressembler aux autres posts BMH, c'est la même marque.

### ⚠️ Le flacon : le piège vérifié le 08/11

J'ai testé la génération avec la photo réelle du flacon jointe en référence.
**Le modèle a quand même inventé un flacon arrondi** à la place du Liquid
Brun, qui est une colonne carrée à bouchon rectangulaire.

C'est inacceptable : la règle de Daoud est qu'**un flacon réinventé est un
faux produit**. On ne publie pas ça.

Donc, dans cet ordre :

1. **Joindre la photo réelle du flacon** en deuxième référence (les scènes
   produit sont dans les fichiers du projet, nommées `<ean>c.jpg`), et écrire
   dans le prompt de copier ce flacon exactement — forme, bouchon, plaque,
   couleur.
2. **Regarder le résultat** et comparer au vrai flacon. Si la forme ne
   correspond pas, ne pas publier.
3. **Si le modèle s'obstine** — et il s'obstine : générer la scène **avec le
   personnage et une table vide**, puis **incruster le vrai flacon détouré**
   par-dessus, en code. C'est plus fiable que de négocier avec le modèle, et
   le flacon est alors exact à 100 %.

La solution 3 est probablement la bonne par défaut. Elle a un autre avantage :
une seule génération de personnage peut resservir pour plusieurs parfums.

---

## 4. Le gabarit de prompt de génération

À adapter par parfum. Les deux premiers paragraphes ne changent jamais.

```
Garde EXACTEMENT le personnage de la première image de référence : même
visage, même crâne dégarni, même barbe grise, mêmes YEUX CLAIRS, même tenue,
mêmes chaussures brunes, même style de rendu 3D doux. Ne redessine pas le
visage.

Garde EXACTEMENT le flacon de la deuxième image de référence : même forme,
même bouchon, même plaque, même couleur. Ne redessine pas le flacon, ne
l'arrondis pas, ne change pas ses proportions.

[LA SCÈNE — voir le tableau ci-dessous]

Lumière rasante de fin d'après-midi, ombres longues et douces, palette miel et
ambre, mur crème chaud en arrière-plan, rendu 3D doux et chaleureux.

AUCUN TEXTE, aucune étiquette lisible, aucun logo, aucun chiffre nulle part
dans l'image. Format portrait 4:5.
```

### Les scènes, par famille olfactive

La scène illustre **la famille**, pas la pyramide du parfum. C'est une règle
posée pour les visuels produit et elle vaut ici aussi.

| Famille | La scène |
|---|---|
| Gourmand praliné et sucré | le personnage à une table basse, éclats de chocolat, noisettes, gousse de vanille |
| Fruits rouges et fruits mûrs | cagettes de fruits sombres, figues ouvertes, cerises |
| Oud et bois précieux | copeaux de bois sombre, encensoir en laiton, fumée légère |
| Marin et chypré | bois flotté gris, galets, un filet de corde |
| Iris et fleurs blanches | fleurs blanches, voile de lin, poudre claire |
| Agrumes et aromates | agrumes coupés, branches de romarin |
| Encens et résines | résines ambrées, brûleur, tissus lourds |
| Rose | roses fraîches, pétales, cuivre |
| Tabac et café | grains de café, cuir patiné, tasse en terre |

---

## 5. Les interdits — tous déjà posés par Daoud

1. **Ne jamais inventer une information sur l'origine ou la fabrication** d'un
   parfum.
2. **Ne jamais recréer le flacon d'une autre maison** de mémoire ou par
   description. Voir la section 3.
3. **Aucune imagerie de boisson.** « Vanille Bourbon » est un cultivar, pas un
   alcool. Pas de verre, pas de bouteille de boisson, pas de bar.
4. **Aucun texte arabe généré par IA** — il sort systématiquement déformé.
5. **Aucun texte généré dans l'image**, voir la méthode en deux temps.
6. **Ne jamais publier de soi-même.** Claude Code produit les fichiers et
   programme ; Daoud décide. En cas de doute sur un rendu, il le montre.
7. **Rien de payant sans demander**, avec le chiffre en euros.
8. **Les clés jamais dans la conversation ni dans le code** — variable
   d'environnement en local, secret GitHub en CI, nommée `FAL_KEY`.
9. **Nommage des fichiers : minuscules, aucun tiret, aucun souligné, aucun
   espace.** Par exemple `<ean>persofr.jpg`, `<ean>persoen.jpg`,
   `<ean>personl.jpg`.
10. **Pas de Noël, pas de Black Friday, pas de fêtes de fin d'année**, ni sous
    ce nom ni sous un autre. Daoud est musulman et ne les célèbre pas.

---

## 6. La programmation sur Metricool

Les trois marques :

| Marque | brandId | Comptes |
|---|---|---|
| deenwithdaoud (FR) | `7711673` | Facebook, Instagram, Threads, TikTok, X |
| BRING MEDINA HOME (EN) | `7714813` | Facebook, Instagram, TikTok |
| BMH NL | `7715503` | Facebook, Instagram, TikTok |

Les créneaux déjà pris : le post produit à **13 h 00**, le carrousel à
**17 h 30**. Le post au personnage a besoin de son propre créneau — **10 h 30
semble libre, à confirmer avec Daoud** avant de l'inscrire dans la routine.

Les règles de publication, toutes déjà en vigueur :

- **Règle de la ligne 2** : `shop.bringmedinahome.com` est la **deuxième ligne
  de la légende**, juste sous le titre. Seule exception : TikTok.
- **TikTok** : la légende, c'est **les trois hashtags et rien d'autre**. Le
  titre va dans `tiktokData.title`.
- **Trois hashtags, jamais plus.** FR `#parfum #bringmedinahome
  #parfumsorientaux` · EN `#fragrance #bringmedinahome #orientalfragrances`
  · NL `#parfum #bringmedinahome #oosterseparfums`.
- **Threads** coupe à 500 caractères, viser 470. **X refuse au-dessus de 280.**
- **Threads seulement en français** : sur les marques EN et NL, Meta renvoie
  toujours sur le Threads de deenwithdaoud.
- **Déclarations obligatoires**, et elles sont vraies ici puisque l'image est
  générée : `tiktokData.commercialContentOwnBrand: true` sur chaque TikTok, et
  `instagramData.isAiGenerated: true` sur chaque image Instagram. Ne jamais
  les décocher — vérifié le 08/11 sur les pages officielles, c'est la
  **non-déclaration** qui coûte de la distribution, pas la déclaration.
- **Ne jamais réactiver `tiktokData.autoAddMusic`.**

---

## 7. À vérifier avant de programmer

- Le parfum est **réellement en stock** sur Shopify, et le prix est celui de
  la fiche. Ne jamais chercher un produit par `query: "barcode:..."` — ça
  renvoie les mauvais produits. Passer par le handle ou l'identifiant.
- Les **yeux du personnage sont clairs**.
- Le **flacon correspond au vrai**, forme et bouchon compris.
- **Aucun texte parasite** généré dans l'image.
- Les trois images sont **réellement différentes** entre elles, pas la même
  scène recolorée.
