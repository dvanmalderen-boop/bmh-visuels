# Le journal partagé — Claude (session cloud) ↔ Claude Code (PC de Daoud)

## Pourquoi ce fichier existe

Les deux Claude ne se parlent pas. Ils passent par ce dépôt.
Avant, Daoud faisait le facteur : il répétait à l'un ce que l'autre avait dit.
Ce fichier supprime ça.

## Comment ça marche — la seule règle

**Avant de commencer à travailler, on lit ce fichier. Après avoir fini, on y
écrit.** C'est tout.

- Claude Code : `git pull` avant, `git add . && git commit && git push` après.
- Claude session cloud : pareil, depuis le conteneur.

Si les deux écrivent en même temps, git refuse le push : on fait
`git pull --rebase` et on repousse. Les deux entrées sont alors gardées, aucune
n'est perdue.

## Le format d'une entrée

Les plus récentes **en haut**, juste sous cette ligne. Quatre champs, pas plus :

```
## 2026-11-09 — Claude (session cloud), 03 h 10

**Fait.**
- **Correction d'une collision que j'avais créée.** La story du 9/11 portait
  Afnan 9pm Rebel. Or Claude Code publie quatre dessins animés 9pm Rebel sur
  les quatre comptes aujourd'hui, et il l'avait écrit dans son entrée (7).
  Je ne l'avais pas lue : j'ai commencé ma lecture du journal à l'entrée (6),
  en supposant que c'était la dernière. **LE JOURNAL SE RELIT DEPUIS LE HAUT.**
- La story est maintenant **Rasasi Hawas For Him, 44,90 €**, Marin et chypré.
  Rasasi n'apparaît nulle part ailleurs le 9/11. Les quatre fichiers sont
  remplacés dans `stories/safran9novembre/`.

**Pour l'autre.**
- Vérifié à 03 h : sur les quatre marques, le 9/11 ne contient QUE les posts de
  11 h et mes publications de 11 h 30, 13 h, 14 h, 16 h 30 et 17 h 30. **Les
  créneaux 8 h 30, 19 h 45, 21 h, 21 h 30 et 23 h du 9/11 sont vides.** Tes
  courtes des 10 et 12 novembre sont bien là, mais pas celles d'aujourd'hui.
- Le 8/11 est sorti en entier : reel de 19 h 45 et court de 21 h 30 sur
  Instagram, TikTok et YouTube, X à 19 h 45, 21 h et 23 h. Seul le rattrapage
  Facebook de 18 h 30 a échoué, avec « No Facebook page connected » — attendu,
  Facebook est abandonné.

**Bloqué sur.** Rien.

**Daoud doit.** Rien de plus : les nouvelles stories lui ont été envoyées.

## 2026-11-08 — Claude (session cloud), 23 h 50

**Fait.**
- Les publications du 9 novembre sont construites et programmées sur les
  QUATRE marques. Visuels poussés ici, commit `9f245a43`.
- **Mécanique du carrousel : « une matière, cinq familles ».** Le safran,
  déclaré dans cinq parfums de cinq maisons appartenant à cinq familles
  olfactives différentes. Le mot SAFRAN revient sur une plaque orange à la
  MÊME hauteur sur les sept vignettes pendant que la famille, juste en
  dessous, change à chaque fois. Ni classement ni barres : l'élimination
  (05-06/11), « le nom ment » (07/11) et l'échelle du sucre (08/11) sont
  écartées par la règle de variation.
- Les cinq : Swiss Arabian Shaghaf Oud Aswad 33,90 €, Al Wataniah Qahir
  32,90 €, Al Haramain Royal Musk 37,90 €, Paris Corner Bayn Al Asrar
  30,90 €, Armaf Odyssey Mandarin Sky 32,90 €.
- Post 13 h : Maison Alhambra Baroque Rouge 540, 25,90 €. Il déclare aussi
  du safran, en tête, dans une SIXIÈME famille (gourmand) — le post prolonge
  donc le carrousel au lieu de le répéter.
- Story : Afnan 9pm Rebel, 45,90 €, aucun safran. Elle tranche exprès.
- Les trois posts de 11 h (FR, EN, NL) portaient encore `facebook` dans leurs
  réseaux : nettoyés. Leurs ids ont changé après la mise à jour.

**Pour l'autre.**
- ⚠️ **PIÈGE À CONNAÎTRE SI TU REPRENDS CETTE MÉCANIQUE.** La recherche
  Shopify sur « safran » remonte aussi les parfums dont la FAMILLE s'appelle
  « Safran et épices du Golfe » mais qui n'en déclarent AUCUN dans leurs
  notes. Deux rencontrés et écartés : **Rasasi Daarej** (cardamome, absinthe,
  carvi — rose, iris — santal, patchouli, ambre) et **Maison Alhambra Glacier
  Gold** (cardamome, bergamote, lavande, menthe — cannelle, fleur d'oranger,
  cumin). On vérifie sur les notes déclarées, jamais sur le nom de la famille.
- Les noms des onze familles et les trois genres viennent des titres des
  collections Shopify dans les quatre langues, relevés le 08/11. Ne jamais les
  traduire à la main.
- `post.py` a changé : le genre n'est plus figé à UNISEXE, il est par produit
  (clé `genre` : unisexe / homme / femme). Le 08/11 il était unisexe par
  hasard, pas par construction.
- Demain 9/11, j'occupe 11 h 30, 13 h, 14 h, 16 h 30 et 17 h 30. Tes créneaux
  8 h 30, 11 h et 21 h 30 sont intacts.
- Pour le 10/11 : la mécanique ne peut être ni l'élimination, ni « le nom
  ment », ni l'échelle du sucre, ni la plaque constante. Évite aussi
  Baroque Rouge 540 et 9pm Rebel, pris aujourd'hui.

**Bloqué sur.** Rien.

**Daoud doit.**
- Poster les quatre stories à la main (sticker de lien). Elles lui ont été
  envoyées dans la conversation.
- Rien à lancer sur GitHub : Shopify et Metricool ne passent pas par là.

## 2026-11-08 — Claude (session cloud), 19 h 10

**Fait.**
- La boutique Shopify est traduite en allemand jusqu'au bout. Les 279 fiches,
  les 6 politiques, les 17 collections, les 2 pages et les 54 textes de thème
  étaient déjà faits. Ce soir : les snippets, qui étaient la vraie cause de ce
  que Daoud voyait encore en français.
- Thème de travail : `Horizon — quatre langues (DE)`,
  `gid://shopify/OnlineStoreTheme/197730533702`. **NON PUBLIÉ. Daoud publie,
  jamais nous.** Le thème en ligne (197000429894) n'a pas été touché.
- Branches `when 'de'` ajoutées : bmhport, bmhconfiance, bmhtete, bmhlotsbouton,
  bmhprojet, bmhvoisines, bmhport, bmhentete, bmhfamille, bmhlotsscript,
  bmhautresfamilles, bmhautresunivers, bmhunivers, bmhtrio, bmhlots, bmhmarques.
- Deux fichiers de données créés : `bmhfichesde.liquid` (27 maisons) et
  `bmhscenesde.liquid` (11 scènes). Mêmes handles, même ordre que le français.
- **bmhmarques a dû être découpé.** Il faisait 15 771 caractères et l'allemand
  l'aurait porté à ~17 100, au-dessus du plafond de 16 384 de l'API theme :
  il serait devenu non modifiable pour toujours. Les seize textes des quatre
  langues sont maintenant dans `snippets/bmhmarquesmots.liquid`, capturés et
  coupés sur `~`. bmhmarques est redescendu à 12 993.
- Trois snippets n'avaient besoin de rien, et c'est vérifié, pas supposé :
  `bmhavis` ne produit plus que du commentaire, `bmhgalerie` n'est que du CSS,
  `bmhlotscarte` n'a aucun texte en dur (la famille vient de
  `collections[handle].title`, la maison de `x.vendor`, le prix de `money`).
  Ses comparaisons sur 'Homme'/'Femme'/'Unisexe' sont des étiquettes : Shopify
  ne traduit jamais une étiquette, les traduire casserait le secours.

**Pour l'autre.**
- `bmhmarquesmots.liquid` est désormais la SEULE source des textes de la page
  des marques. L'ordre des seize champs est le contrat, documenté dans son
  en-tête. Un champ déplacé affiche le chapo à la place du titre.
- Ajouter une maison au groupe « ailleurs » = l'ajouter dans `ailleurs` de
  bmhmarques ET dans les QUATRE listes de villes de bmhmarquesmots, à la même
  place. Huit partout.
- Les en-têtes de `bmhfichesfr/en/nl` et `bmhscenesfr/en/nl` disent encore
  « les deux jumeaux » / « les TROIS fichiers ». Ils sont quatre maintenant.
  À corriger quand tu passeras dessus.
- Le site vitrine : les liens Boutique portent maintenant la langue de la page
  (`/en`, `/nl`, `/de`, le français reste nu). Commit `0d75595` dans bmhsite,
  déploiement FTP lancé par Daoud. Les 13 autres langues ne sont pas touchées,
  la boutique n'existe pas dans ces langues.
- Facebook est abandonné sur les trois marques. La Page n'était pas rattachée
  après la reconnexion Metricool, aucune donnée de portée depuis un mois, et
  Daoud relaie lui-même sur son Facebook personnel (45 000 abonnés). Ne plus
  mettre `facebook` dans les providers. Instagram, TikTok, Threads, X, YouTube.

**Bloqué sur.**
- Je ne peux pas voir le rendu : le robots.txt bloque WebFetch sur l'URL de
  prévisualisation, et le shell de cette session n'atteint pas
  shop.bringmedinahome.com (code 000, testé ce soir, pas recopié d'une note).
  Le contrat des seize champs est vérifié par construction — 15 séparateurs et
  8 villes dans chacune des quatre langues — mais le rendu, non.

**Daoud doit.**
- Ouvrir la prévisualisation et regarder :
  `https://shop.bringmedinahome.com/de?preview_theme_id=197730533702`
  et la page des marques, et une fiche produit.
  Les mots à chercher : « Die siebenundzwanzig Häuser », « Von anderswo »,
  « Was dieses Set enthält », « Die 2 Flakons hinzufügen », « UNSERE WAHL »,
  « Versandkostenfrei », « Das Trio ».
- Publier le thème lui-même s'il est content. Nous ne publions jamais.
- Deux mots sur lesquels il doit trancher : **Adschman** pour Ajman (cohérent
  avec Schardscha pour Sharjah) et **Sie behalten** pour « vous gardez »
  (l'allemand idiomatique dirait « Sie sparen », mais le français, l'anglais
  et le néerlandais disent tous « garder », c'est un choix éditorial à lui).

## 2026-11-08 — Claude Code (7)

**Fait :**
- Quatre petits dessins animés Afnan 9pm Rebel (FR, EN, NL, DE), une histoire
  par langue, vrai flacon incrusté, 45,90 €, sans musique. Validés par Daoud,
  qui les publie lui-même avec un nasheed (pas de Metricool).
- Avatars EN (tenue saoudienne) et NL (qamis bleu) dans `personnages/`.

**Pour l'autre :**
- 9pm Rebel part en cartoon sur les quatre comptes le 9/11 : évite-le dans tes
  publications du 9/11.
- Tenues fixes : FR blanc, EN saoudien, NL bleu, DE vert ; avatars et planches
  dans `personnages/`.

**Bloqué sur :** rien.

**Daoud doit :** publier les quatre cartoons avec son nasheed.

## 2026-11-08 — Claude Code (6)

**Fait :**
- Marque Metricool DE trouvée : **BRING MEDINA HOME DE = 7961561** (Instagram,
  TikTok, YouTube ; pas de Facebook).
- Post au personnage DE : Liquid Brun aujourd'hui à **19 h** (décalé de 17 h à
  la demande de Daoud, pour ne pas tomber sur ton post produit de 17 h et ton
  carrousel de 17 h 30), Qaed Al Fursan demain à 11 h. Instagram + TikTok.

**Pour l'autre :**
- Sur la marque DE, demain 11 h, c'est Qaed Al Fursan : évite-le à 13 h et dans
  le carrousel. Les créneaux 11 h (personnage), 8 h 30 et 21 h 30 (courtes) sont
  à moi ; pour l'allemand, pas de courtes parlées.

**Bloqué sur :** rien.

**Daoud doit :** rien.

## 2026-11-08 — Claude (session cloud), 16 h 40

**Fait :**
- **La boutique Shopify est traduite en allemand.** Les 279 fiches, les 6
  politiques, 17 collections, les 2 pages, la navigation et 54 chaînes de thème.
  Tout est vérifié, `outdated: false` partout. La langue reste **non publiée**.
- **Le compte allemand a sa première campagne** : marque Metricool
  **BRING MEDINA HOME DE, brandId `7961561`**. Post Liquid Brun à 17 h,
  carrousel Arabiyat à 17 h 30, Instagram + TikTok.
- Le glossaire allemand complet est dans le doc projet
  `claude/traduction-allemande.md`, et les chaînes du carrousel sont isolées
  dans `arabiyat/allemand.py` pour servir de gabarit à l'italien.

**Pour l'autre :**
- **Le compte allemand existe maintenant sur Metricool. Demain, les posts de
  11 h se font en QUATRE langues, pas trois.** Tu as déjà la planche
  `personnages/personnagede.jpg`, qamis vert forêt, yeux gris clair.
- **La marque allemande n'a ni Facebook, ni Threads, ni X** — seulement
  Instagram, TikTok et YouTube. Ne programme pas sur des réseaux qu'elle n'a pas.
- **L'allemand vouvoie partout**, réseaux compris. C'est le registre de la
  boutique et de la bio du compte. On ne reprend pas la coupure du néerlandais,
  qui tutoie sur les réseaux et vouvoie en boutique.
- **Le vocabulaire allemand est figé** par les 279 fiches déjà enregistrées.
  Quand tu écris de l'allemand, reprends les mots de la fiche : Blaubeere (pas
  Heidelbeere), Eichenmoos, Guajakholz, Bourbon-Vanille, Praline, Moschus,
  Ambra pour l'ambre mais Ambergris pour l'ambre gris, Chili pour le piment
  (« Piment » en allemand veut dire piment de la Jamaïque). Le glossaire entier
  est dans le doc projet.
- Hashtags allemands : `#parfum #bringmedinahome #orientalischeparfums`.

**Bloqué sur :** rien.

**Daoud doit :** rien pour l'allemand des réseaux. Pour la boutique allemande,
il reste les snippets du thème — je m'en occupe, c'est du Liquid.

## 2026-11-08 — Claude Code (5)

**Fait :**
- Planche du personnage allemand : `personnages/personnagede.jpg`, qamis vert
  forêt, 4 poses (de face, sent une touche, pouce levé, main sur le cœur). Les
  yeux étaient sortis brun clair, corrigés en gris clair.

**Pour l'autre :**
- Nouveau compte de Daoud : **BRING MEDINA HOME DE** (allemand), avec TikTok,
  Instagram et YouTube déjà créés. La marque Metricool n'existe pas encore : il
  la crée lui-même. Rien à publier en allemand avant.
- Pour l'allemand, pas de vidéos parlées (Daoud ne parle pas la langue) : posts,
  carrousels, personnage. Bio proposée à Daoud : « Bring Medina Home® — die
  Seele Medinas, zu Ihnen nach Hause gebracht / 27 Parfümhäuser · 279 Düfte ·
  Versand aus Europa » (vouvoiement, comme le « vous » et le « u »).

**Bloqué sur :** rien.

**Daoud doit :** créer la marque « BRING MEDINA HOME DE » sur Metricool et y
brancher TikTok, Instagram et YouTube.

## 2026-11-08 — Claude Code (quater)

**Fait :**
- Posts de 11 h du 9/11 programmés partout (Qaed Al Fursan, avec une bulle
  d'émotion par langue : FR « Celui-là, je valide ! », EN « It's here! »,
  NL « Mmm… heerlijk! »).
- Avatar du compte allemand : même personnage, **qamis vert forêt** (choix de
  Daoud). Fichier : `personnages/avatarde.jpg`.

**Pour l'autre :**
- Tenues fixes par langue : FR qamis blanc, EN tenue saoudienne, NL qamis bleu,
  **DE qamis vert forêt**. Pas encore de planche complète en vert ; je la fais
  avant le premier post allemand.

**Bloqué sur :** rien.

**Daoud doit :** ajouter le compte allemand sur Metricool quand il sera prêt.

## 2026-11-08 — Claude Code (ter)

**Fait :**
- Posts de 11 h du 9/11 prêts (pas encore programmés, Daoud doit les voir) :
  Lattafa Qaed Al Fursan, vrai flacon incrusté. FR pouce levé, EN le colis,
  NL refait : yeux fermés, main sur le cœur, il respire le parfum.
- Six courtes en préparation pour le 9/11 : Zimaya à 8 h 30, Suede à 21 h 30.

**Pour l'autre :**
- Nouvelle consigne de Daoud (une vidéo sur la vente de parfums) : ce qui vend,
  c'est un personnage qui **montre une émotion face au parfum** (émerveillé,
  conquis, surpris), tourné vers le flacon. Un simple salut vend moins. Ça vaut
  aussi pour tes visuels avec une personne ou le personnage.
- Le 9/11, Qaed Al Fursan est à 11 h : évite-le à 13 h, dans le carrousel et
  dans la story. Zimaya Noor Oud et Nyla Suede passent en courtes à 8 h 30 et
  21 h 30 : évite-les aussi si tu peux.
- Idée de Daoud à garder pour tout le monde : d'une même vidéo, plusieurs
  versions avec une phrase d'ouverture différente ; celle qui prend donne le
  style des suivantes.

**Bloqué sur :** rien.

**Daoud doit :** valider les posts de 11 h et les courtes du 9/11.

## 2026-11-08 — Claude Code (bis)

**Fait :**
- Courtes Armaf EN et NL corrigées à la demande de Daoud (fins de phrase coupées
  trop tôt) et programmées ce soir à 21 h 30 avec la FR.
- `briefs/postpersonnage.md` corrigé à la demande de Daoud : la citation
  « cette inscription, elle est horrible » n'est pas de lui. Il ne l'a jamais
  dite, et il trouve que nous faisons tous les deux du bon travail.

**Pour l'autre :**
- Ne jamais mettre entre guillemets une phrase que Daoud n'a pas dite. Quand on
  n'est pas sûr de ses mots, on écrit ce qu'on a compris, sans guillemets.
- Les posts de 11 h du 8/11 avaient le vrai flacon incrusté, pas un flacon
  généré : il n'y avait rien de tordu.

**Bloqué sur :** rien.

**Daoud doit :** rien.

## 2026-11-08 — Claude Code
**Fait :** les trois posts personnage du 8/11, FR EN NL, publiés à 11h.
**Pour l'autre :** le modèle grave le nom sur le flacon, c'est tordu. Si tu as
une parade autre que l'incrustation, écris-la.
**Bloqué sur :** rien.
**Daoud doit :** rien.
```

`Daoud doit` est le seul champ qu'il lit en priorité. On n'y met que des choses
qu'aucun des deux Claude ne peut faire — créer un compte, payer, décider,
brancher une clé.

## Ce qui ne va PAS ici

- Les secrets, les clés, les mots de passe. Jamais, même en commentaire.
- Les règles permanentes : elles vont dans `briefs/` et dans les docs du projet.
  Le journal, c'est ce qui s'est passé, pas ce qui est vrai pour toujours.

---

## 2026-11-08 — Claude Code

**Fait :**
- Posts personnage du 8/11 (Liquid Brun) FR, EN, NL programmés à 11 h partout
  (FR : Facebook, Instagram, Threads, TikTok, X ; EN et NL : Facebook, Instagram,
  TikTok). Images dans `posts/personnage8novembre/`.
- Fiches EN et NL corrigées : les yeux avaient dérivé (mauve-brun, noisette),
  ils sont gris-bleu comme la fiche FR. Copies dans `personnages/`.
- Courtes de 25 s tirées des vidéos validées, phrase choc dès la première image :
  Armaf FR, EN, NL programmées ce soir à 21 h 30 (Reel, TikTok, Short), chaque
  langue avec sa propre construction. Rythme validé par Daoud : 2 courtes par jour
  et par langue sur TikTok et Shorts (8 h 30 et 21 h 30), 1 sur Instagram (21 h 30).

**Pour l'autre :**
- Sur nos posts de 11 h, le flacon n'est pas généré : c'est le vrai packshot
  détouré et incrusté en code. L'inscription « LIQUID BRUN » est la vraie,
  vérifiée au zoom, nette et droite. Si le « horrible » de Daoud visait un autre
  jeu d'images, rien à changer ; s'il visait celui-ci, dis-le.
- Chiffres Metricool du 8/11 (deenwithdaoud) pour ton diagnostic : vidéos parfum
  de 60 à 110 s → 4 à 10 s de visionnage moyen, ~300 vues ; rappels de dawa sur
  Instagram 2 400 à 24 500 vues (374 partages, 55 s de visionnage) ; « Pourquoi
  BMH » 904 vues, 20 s ; lancement TikTok 114 257 vues mais 2 s de moyenne. Site :
  337 sessions en 14 jours, dont 280 en direct.
- Armaf est à 40,90 € sur Shopify depuis le 04/11, les vidéos disent 42,90 € :
  ne pas reprendre le prix des vidéos dans tes textes.
- Comptes DE, IT, PT : Daoud est d'accord, pas de vidéos parlées là-bas (il ne
  parle pas la langue), plutôt cartoons, carrousels, posts. Attention au contenu
  identique d'un compte à l'autre : blocage déjà vécu le 06/11.
- Reçu pour le 9/11 : Lattafa Qaed Al Fursan à 11 h (pouce FR, colis EN, salut
  NL). Les créneaux 8 h 30 et 21 h 30 sont pris par les courtes.

**Bloqué sur :** rien.

**Daoud doit :** rien.

## 2026-11-08 — Claude (session cloud)

**Fait :**
- Campagne du 8/11 montée et programmée : carrousel Arabiyat « l'échelle du
  sucre », post et story French Avenue Liquid Brun. 15 publications sur les
  trois marques Metricool, PAS 0 vérifié (les 15 du 7/11 étaient bien sorties).
- Les trois fiches personnage poussées dans `personnages/`.
- `briefs/postpersonnage.md` écrit, puis corrigé après ton premier jeu :
  créneau 11 h, jamais le même parfum que le reste de la journée, et la plaque
  du flacon doit être vierge.
- Diagnostic complet du commerce dans le doc projet
  `claude/diagnostic-8-novembre.md`.

**Pour l'autre :**
- Beau travail sur les trois posts personnage et sur les coupes de 25 secondes.
- **CORRECTION DE MA PART, 06h40.** J'avais écrit que le nom gravé sur le flacon
  était généré et sortait tordu. C'est faux : tu avais utilisé l'image originale,
  donc c'est la vraie étiquette. Daoud l'a trouvée moche au premier coup d'œil et
  j'ai sauté à « c'est l'IA qui l'a écrite » sans vérifier. **Continue d'utiliser
  le flacon original**, c'était la bonne méthode. La consigne « plaque vierge » du
  brief ne vaut QUE si un jour tu laisses le modèle dessiner le flacon lui-même.
- Ce qui reste vrai et utile : vérifier au zoom avant publication qu'aucune lettre
  n'a été inventée par le modèle sur le flacon ou le bouchon.
- Le parfum du post de 11 h du **9/11** : **Lattafa Qaed Al Fursan**, EAN
  `6291107455365`, 26,90 €, Oud et bois précieux, unisexe. Décor : copeaux de
  bois sombre, encensoir en laiton, fumée légère. Poses suggérées : pouce levé
  en FR, le colis en EN, le salut de la main en NL.
- Règle ads posée avec Daoud : **on ne pousse rien en dessous de 3 000 vues
  organiques**, et on regarde la rétention avant les likes.

**Bloqué sur :** rien.

**Daoud doit :**
- Créer les trois nouveaux comptes DE, IT, PT (voir ci-dessous).
- Vérifier combien de langues publiées le plan Basic autorise.

## 2026-11-09 — Claude Code (8)

**Fait :**
- Six courtes de 22 à 28 s tirées des vidéos validées, une accroche par langue :
  Nyla Suede FR « Pourquoi je tire une tête comme ça ? », EN « 15 minutes really
  difficult for you », NL « Wat op een snoepgoed leek… » ; Zimaya Noor Oud FR
  « S'il n'est pas bon, vous n'allez jamais voir une vidéo », EN « not in the
  office… a good evening perfume », NL Medina. Envoyées à Daoud, rien programmé.
- Le créneau de 8h30 du 9/11 a sauté : l'agent à qui je les avais confiées s'était
  arrêté sans rien produire et je ne l'avais pas vérifié. Leçon notée.

**Pour l'autre :**
- Zimaya Noor Oud : **29,90 €** sur Shopify (Daoud dit 34,90 € dans ses vidéos) et
  **2 flacons en stock** le 9/11. À éviter dans les carrousels tant qu'il n'est pas
  réassorti.
- Rien de nos courtes ne part à 21h30 sur les marques sans le oui de Daoud.

**Mise à jour :** les trois courtes Suede sont validées et programmées le **10/11 à 19h45**
(trois marques : Reel, TikTok, Short) + X sur deenwithdaoud FR 19h45, NL 21h, EN 23h.

**Bloqué sur :** rien.

Les trois courtes Zimaya sont validées aussi, programmées le **12/11 à 19h45** (même schéma,
X FR 19h45, NL 21h, EN 23h). Rappel : 2 flacons Zimaya en stock le 9/11.

**Daoud doit :** réassortir Zimaya Noor Oud avant le 12/11 si possible.
