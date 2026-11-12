# Comment on écrit un prompt d'image chez BMH

**Pourquoi ce fichier existe.** Le 12/11, un brief d'images a coûté **3 à 4 €**
pour sept images dont **trois seulement** étaient utilisables. Ce n'est pas le
générateur qui a raté : c'est le brief qui était mauvais. Ce fichier existe
pour que ça ne se reproduise pas.

La règle de fond : **un prompt court ne laisse pas le modèle libre, il le
laisse perdu.** Si on ne dit pas quel flacon, il en invente un. Si on ne dit
pas où s'arrête le cadre, il met un visage. Chaque chose qu'on ne précise pas,
quelqu'un d'autre la décide à notre place.

---

## Les six règles

### 1. Dire ce qu'on veut, jamais ce qu'on ne veut pas

C'est la plus importante et c'est la moins intuitive.

Écrire « **pas** de visage », « **pas** de texte », « **pas** de support » fait
souvent **apparaître** la chose interdite : le modèle lit les mots, pas la
négation.

| À ne plus écrire | À écrire à la place |
|---|---|
| « pas de visage » | « le cadre s'arrête aux épaules » |
| « pas de texte dans l'image » | « surfaces nues, étiquette du flacon seule » |
| « pas de support sous le flacon » | « la main tient le flacon en l'air » |
| « pas de bijoux » | « main nue » |

### 2. Nommer le parfum. Toujours.

Un prompt qui dit « un flacon de parfum » rend un flacon inventé. Il faut
**le nom exact, la maison, la couleur et la matière** :

> *a white and gold Lattafa Yara bottle with its gold ribbon and round medallion*

Si une planche de référence du flacon existe dans le dépôt, **on la joint**.
Le modèle tient un objet qu'on lui montre, pas un objet qu'on lui décrit.

### 3. Raconter une scène, pas cocher une liste

L'ordre qui marche : **sujet → action → lieu → cadrage → lumière → objectif →
matières → style**. Une phrase qui se lit, pas des mots séparés par des virgules.

### 4. Le geste doit être physiquement vrai

On vaporise un parfum **à une quinzaine de centimètres** de la peau. On ne
colle pas un flacon contre une oreille. On ne tient pas un flacon à l'envers.
Un geste faux se voit tout de suite et rend l'image inutilisable, même quand
elle est belle.

### 5. Une seule image d'essai avant la série

On génère **une** image, on la montre à Daoud, **et seulement après** on lance
les six autres. Sept images ratées coûtent sept fois ; une image ratée coûte
une fois.

### 6. Les contraintes BMH, dans tous les prompts

- **Des hommes.** Si une femme apparaît : **voilée**, de profil ou de trois
  quarts dos, **le cadre ne montre pas son visage**. Dans le doute : les mains
  et les avant-bras seuls, c'est toujours sûr.
- **9:16, 1080 × 1920.**
- **Le sujet vit dans le tiers central gauche** et dans les deux tiers du haut.
  L'interface de TikTok mange 150 px en haut, 480 px en bas, 120 px à droite.
- **Aucun texte dans l'image générée.** Le texte est gravé après, par le script
  du carrousel. Dit à l'endroit : *surfaces nues, seule l'étiquette du flacon
  porte des lettres*.
- Lumière chaude et rasante, fond crème ou bois sombre, rendu photographique,
  le même étalonnage que les scènes produit du dépôt.

---

## Un exemple qui a marché

C'est le prompt de `scenes/coude/coude2.jpg` — Lattafa Yara Moi, vaporisé sur
le haut du bras. Image gardée du premier coup.

> A man in a white qamis photographed from the side in warm raking afternoon
> light. He has pushed his sleeve above the elbow and sprays a white and gold
> **Lattafa Yara** bottle — gold cap, gold ribbon, round medallion — onto his
> upper arm, holding the bottle about fifteen centimetres from the skin, a fine
> mist visible in the light. The frame starts at the chin and ends at the waist.
> Cream linen background, soft shadows, 85 mm lens, shallow depth of field.
> Vertical 9:16, the man in the centre-left of the frame, surfaces bare apart
> from the bottle's own label.

Ce qu'il contient et qu'un mauvais prompt n'a pas : **le parfum nommé et
décrit**, **la distance du geste**, **où commence et où finit le cadre**,
**l'objectif**, **la matière du fond**, **la place dans le cadre**.

---

## La liste à cocher avant d'envoyer un brief

1. Chaque image a-t-elle **son parfum nommé** ?
2. Le **geste** est-il physiquement possible ?
3. Ai-je dit **où le cadre commence et finit**, au lieu d'écrire « pas de visage » ?
4. Ai-je donné **lumière, objectif, matières** ?
5. Reste-t-il une seule **négation** dans le texte ? Si oui, la retourner.
6. Ai-je prévu **une image d'essai** avant la série ?

Six cases. Si l'une n'est pas cochée, le brief n'est pas prêt, et on ne lance
rien. Ça coûte de l'argent à chaque fois.
