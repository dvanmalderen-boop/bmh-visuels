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

Les plus récentes **en haut**, juste sous le trait `---` qui ferme cette
notice — **pas sous le bloc d'exemple ci-dessous**, sinon l'entrée se
retrouve enfermée dedans et tout le journal s'affiche comme du code.
C'est arrivé le 10/11, réparé le 11/11. Quatre champs, pas plus :

```
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

## 2026-11-12 — Claude (session cloud), 04 h 50

**Fait :** le carrousel du **13/11**, premier au format **TikTok 1080 × 1920**,
en **quatre langues**. Mécanique : *« Tu mets ton parfum au mauvais endroit »*
→ le woudou lave jusqu'au coude → six endroits que l'eau n'atteint pas, six
parfums à y poser → l'offre → « enregistre-le pour vendredi ».
Dix diapos, pas cinq. Tout est dans `carrousels/coude13novembre/` avec le
script `carrousel.py` et le brief d'images `brief-visages.md`.
**Programmé sur TikTok, les quatre marques, 13/11 à 15 h 45.**

**Pour l'autre :** trois choses.

1. **Les horaires sont séparés, on ne se marche pas dessus.**
   Toi : **11 h 00**, le post personnage, comme d'habitude — je n'y touche pas.
   Moi : **15 h 45**, le carrousel. Daoud : **19 h 45**, la vidéo.
   Si tu dois bouger quelque chose, préviens ici avant.

2. **`brief-visages.md` est pour toi.** Sept images à générer sur fal.ai (je ne
   peux pas : le réseau de mon conteneur ne sort que vers GitHub et les dépôts
   de paquets, fal.ai répond 000). **La règle est en tête du fichier et elle
   n'est pas négociable : des hommes ; si une femme apparaît, elle est voilée,
   de profil, visage non lisible ; dans le doute, les mains seules.**
   Priorité absolue : `coude1`, la couverture.

3. **Ce que quatre agents ont mesuré hier soir, et qui change la fabrication.**
   - Dix diapos dépassent 2 % d'engagement ; seulement 6 % des carrousels y vont.
   - La **diapo 2 doit tenir seule** : Mosseri a dit qu'un carrousel ignoré peut
     être re-servi en commençant par elle.
   - Un **visage** vaut +38 % de likes et +32 % de commentaires (1,1 M de photos).
     Sur TikTok, un visage sous **20 %** du cadre bat un gros plan de +31 %.
   - **5 à 10 mots par seconde** affichés : sur une vignette, **5 à 15 mots max**.
   - Contraste texte/fond **4,5:1** minimum. Le crème sur crème flouté ne le
     passe pas. Ça se mesure, ce n'est pas un avis.
   - **Carrousel → Instagram** (4,7× les vues du carrousel TikTok, sur 24 M de
     posts). **Vidéo → TikTok** (5,6× un post photo).
   - Le format le plus sous-exploité du créneau : **la routine du vendredi**.
     @akhifragrance, **9 669 abonnés**, a fait **389 000 vues** avec
     « Jummah Fragrance Routine ». En vidéo, parce que le geste est le contenu.

**Bloqué sur :** rien.

**Daoud doit :** rien. Les quatre posts sont programmés, les images sont en
ligne sur le dépôt public.

---

## 2026-11-12 — Claude (session cloud), 02 h 40

# ⚠️ LIS CETTE ENTRÉE AVANT TOUTE AUTRE. LA STRATÉGIE A CHANGÉ.

**Daoud a posé son échéance : fin décembre.** Après, les charges deviennent
impayables. ~550 €/mois contre 295 € de chiffre d'affaires **depuis le
18 octobre**. Cinq commandes. Zéro budget publicitaire, et il n'y en aura pas.

Il a demandé une analyse complète, sans complaisance. Ses mots : *« ne viens
pas me dire que mes vidéos c'est un succès, parce que ça c'est des conneries.
1000 views sur Instagram c'est du pipeau. »* Il a raison. Deux audits ont
tourné — Metricool sur les quatre comptes, et une recherche sur les leviers de
trafic sans budget. Voici ce qu'ils disent.

---

## 1. LE CHIFFRE QUI CADRE TOUT

**390 000 vues sur 30 jours, toutes plateformes. 38 sessions sur la boutique.**

Une session pour 10 000 vues. **0,01 %.** Un compte sain est entre 0,5 et 2 %.

Et le détail qui tue : **les clics sur lien ne sont mesurables sur aucun
réseau** sauf X, où ils valent zéro. Instagram a déprécié la métrique, TikTok
et YouTube ne l'ont jamais eue. **Toute attribution part de Shopify, jamais de
Metricool.** Ne jamais raisonner sur une statistique de clic venue d'ailleurs.

## 2. L'ÉQUATION, ET C'EST ELLE LE VRAI SUJET

Le port est un coût **par commande**, pas par flacon. Donc :

| Flacons par commande | Net pour Daoud | Commandes/mois pour 550 € |
|---|---|---|
| 1 | ~4,50 € | **122** |
| 2 | ~14 € | **39** |
| 3 | ~23,50 € | **23** |

**Faire passer le panier de 1 à 2 flacons divise l'objectif par trois.** Ce
n'est pas du marketing, c'est de l'arithmétique, et **ça ne demande pas un
visiteur de plus**.

C'est la conclusion commune des deux audits : **les sept semaines ne se jouent
pas sur le trafic, elles se jouent sur le panier.** 122 flacons à l'unité est
hors de portée en organique. 39 commandes à deux flacons ne l'est pas.

Le seuil de livraison offerte à 90 € est **52 % au-dessus du panier moyen**,
quand la pratique documentée est 20 à 30 %. Personne ne l'atteint jamais.
**Proposition à soumettre à Daoud, pas à appliquer :** descendre vers 75 €, et
construire des duos explicites de deux flacons.
⚠️ Les prix des flacons restent **figés** depuis le 03/11. On ne touche pas aux
prix. Le seuil de port et les duos sont autre chose.

## 3. CE QUI MARCHE — UNE SEULE CHOSE, ET ELLE EST CLAIRE

Trois publications sont sorties du lot sur toute la période :

| Date | Sujet | Résultat |
|---|---|---|
| 29/10 | « Un an de travail, la boutique est en ligne » | 114 328 vues — ⛔ **PAYÉE EN ADS TIKTOK, à ne pas compter** |
| 06/11 | « Pourquoi Bring Medina Home » — hijra, Foundation, marge minime | **13,9 %** TikTok, **14,4 %** Instagram |
| 27/10 | Un rappel, avant le lancement | 24 935 vues, **388 enregistrements, 248 partages** |

**Point commun : aucune ne vend un flacon.** Daoud qui parle, le soir, d'un
engagement personnel, avec un enjeu que le spectateur peut relayer.

Face à ça, les vidéos produit font **0,81 %**. Et **zéro partage sur
27 publications feed Instagram**. Aucune fiche produit n'a jamais été partagée.

**👉 LA RÈGLE QUI EN SORT : on ne vend pas le parfum, on raconte pourquoi il
existe.** Le parfum est la conséquence, pas le sujet.

## 3 bis. ⚠️ CORRECTION DU 12/11 — L'AUDIT MESURAIT LA MAUVAISE CHOSE

Daoud a corrigé deux choses, et il a raison sur les deux.

**1. La vidéo du 29/10 à 114 328 vues était POUSSÉE EN ADS TIKTOK.** Ce
n'est pas une réussite organique. Elle tombe de la liste des exemples.

**2. Un taux d'interaction sur une base minuscule ne veut rien dire.** Les
13,9 % et 14,4 % de la vidéo du 6/11 portent sur **580 et 1 048 vues**. Ses
mots : *« 1 000 ou 2 000 vues, c'est rien. Ce qui fait venir les gens, c'est
20, 30, 100, 300 000 vues. »* Il a raison. Un bon pourcentage sur 580
personnes n'amène personne sur une boutique.

**Donc la conclusion « le format qui marche, c'est la vidéo parlée » est à
jeter.** Ce format est le moins mauvais, pas un format qui marche. Aucun
format ne marche aujourd'hui, parce que **rien ne sort du compte**.

**LA BONNE QUESTION N'EST PAS QUOI PUBLIER. C'EST POURQUOI RIEN NE SORT.**

TikTok FR : **246 739 abonnés, 304 vues médianes. 0,12 % des abonnés.**
Un compte sain distribue à 5-15 % de ses abonnés, soit **12 000 à 37 000
vues** pour ce compte. Il en fait 300.

Écrire un meilleur script ne change rien à ça : aucune vidéo ne sort d'un
compte qui ne distribue plus. **Si ce compte remontait seulement à 2 %, il
ferait 5 000 vues par publication au lieu de 300 — seize fois plus, sans un
euro et sans un créateur.** C'est le plus gros levier du dossier, et aucune
collaboration ne peut apporter 246 000 personnes.

Une recherche est en cours sur ce seul sujet : causes documentées
d'effondrement de portée, effet d'un changement de thématique, comment
vérifier une restriction de compte, et s'il faut récupérer ce compte ou en
ouvrir un autre.

---

## 4. LA CASSURE DU 30/10, ET C'EST LE FAIT STRUCTURANT

TikTok FR, vues médianes par publication :
**avant le lancement 834 · après 315. −62 %, du jour au lendemain.**
Instagram : 1 550 avant le 29/10, 406 après.

246 739 abonnés sur TikTok FR, **304 vues médianes**. Un abonné sur huit cents.

L'explication : le compte vivait de contenu d'affiliation et de rappels. **Son
audience ne s'est pas abonnée pour une boutique de parfum.** En basculant sur
le produit, l'engagement est tombé et la distribution avec. L'audience n'est
pas perdue — l'accord entre le contenu et la raison de l'abonnement l'est.

## 5. CE QU'IL FAUT ARRÊTER

- **X** — 82 abonnés, ~65 publications en 12 jours, **0 impression, 0 clic**, et
  10 €/mois. Ce n'est pas une économie, c'est un canal mort qui consomme du
  temps de production.
- **Les 4 posts photo/jour sur TikTok** — 27 publications, **8 208 vues en
  tout**, 7 interactions médianes, portée renvoyée à 0 depuis le 10/11.
- **Threads** — 12 740 abonnés, **44 vues médianes**.
- **Instagram EN** — portée médiane de **2 à 7 personnes** par publication.
  Inutile d'alimenter tant que personne n'y amène d'audience.
- **TikTok EN et NL** — ~760 vues par publication, écart-type sous 140 sur
  38 publications, moins de 1 % de likes. **Ce ne sont pas des spectateurs**,
  c'est de la distribution de pool. **Ne jamais compter ces vues comme de la
  portée.**
- **Le post personnage** : 15 publications, 24 interactions au total,
  2 abonnés gagnés. ⚠️ **DAOUD A TRANCHÉ LE 10/11 : ON N'Y TOUCHE PAS.** Le
  chiffre est noté pour l'honnêteté, pas pour rouvrir la décision.

## 6. LES HEURES — le test du 11/11 va dans le bon sens

`getBestTimeToPostByNetwork` confirme : Instagram, **10 h est le pic absolu**
tous les jours de semaine (4 942 à 6 734) contre 3 326-4 641 à 13 h, soit
**+40 à +50 %**. TikTok : 10 h et 18 h sont les pics, **13 h est le pire
créneau de la journée active**. Et les trois publications qui ont marché sont
toutes entre **17 h et 19 h 30**. Un seul jour de test exploitable pour
l'instant, aucune conclusion, mais la direction est bonne.

## 7. CE QUI EST FERMÉ, VÉRIFIÉ, À NE PAS REPROPOSER

- **r/fragrance** : *« Discussion of selling fragrances is not permitted »*.
- **bol.com** : **interdit explicitement le dropshipping**. Amazon : parfum sous
  gating de marque. Les places de marché sont fermées.
- **L'affiliation** : elle est la **conséquence** d'un seeding réussi, jamais
  son point d'entrée. Daoud l'a fermée le 03/11, elle reste fermée.
  Et à 4,50 € de net, une commission de 15 % laisse 0,70 € — ça n'achète
  personne.
- **Shopify Collabs** : la place de marché créateurs exigerait 10 000 $ de
  ventes et une boutique US/CA. *(source tierce, à confirmer dans son admin)*
- **Pinterest** : 4 à 12 semaines de latence entre le clic et l'achat. Trop
  lent pour l'échéance.

## 8. CE QUE JE DEMANDE À CLAUDE CODE

Dans l'ordre, et le premier est de loin le plus important.

**1. Les visuels du duo.** Deux flacons dans le même cadre, pas un. C'est le
levier n°1 de tout le dossier et il n'existe aucun visuel pour ça aujourd'hui.
Il faut de quoi montrer « deux flacons, livraison offerte » sur tous les
formats. **La règle de la main validée le 10/11 s'applique : la main SOULÈVE,
sans appui visible, main nue, flacon réel.**

**2. Les vidéos « pourquoi », pas « quoi ».** C'est le seul format qui marche :
14 % contre 0,8 %. Le sujet n'est pas le parfum, c'est **la hijra, la
Foundation, les 10 % réservés, pourquoi la marge est mince**. Daoud parle. Le
soir. Si tu peux générer ou monter quoi que ce soit qui serve ce format,
c'est là qu'il faut mettre l'énergie — pas sur une 28ᵉ fiche produit animée.

**3. Rien pour X, rien pour Threads, rien pour Instagram EN** tant que la
situation n'a pas changé. Le temps de production qui y va est perdu.

## 9. CE QUE JE N'AI PAS VÉRIFIÉ, ET QU'IL NE FAUT PAS PRÉSENTER COMME ACQUIS

- **Le taux de conversion de 6 %** (5 commandes / 76 sessions externes) **n'a
  aucune valeur statistique.** Je m'en suis servi dans un message à Daoud ce
  matin, j'ai eu tort. Sur du trafic froid, tabler sur 2 à 2,5 %.
- **Les 692 sessions « direct »** : je suppose que ce sont surtout celles de
  Daoud et de son éditeur de thème. **Non vérifié.** S'il est premier sur
  Google pour sa marque, une partie du trafic social arrive en direct et les
  38 sessions sous-estiment la réalité.
- **Y a-t-il un lien cliquable en bio** sur TikTok et Instagram, dans les
  quatre langues ? **Question posée à Daoud, sans réponse à cette heure.**
  C'est le premier maillon de toute la chaîne.
- **Khalid crée en anglais et en néerlandais, pas en français.** Son audience
  de 165 000 ne nourrit donc **pas** le marché francophone. Elle peut en
  revanche faire exister les comptes EN et NL, qui sont à 89 et 3 392 abonnés
  avec 2 à 7 personnes touchées. J'avais présenté Khalid comme « l'opération du
  trimestre » sans avoir vu ça.
- **Le seul canal dont on ait une preuve de conversion est le Facebook
  personnel de Daoud (~45 000 abonnés)** : sa première commande à deux flacons
  en vient. ⚠️ À ne pas confondre avec la page Facebook BMH, abandonnée le
  08/11. Le compte personnel, lui, est le canal le plus efficace du dossier.

**Bloqué sur :** la réponse de Daoud sur les liens en bio.

**Daoud doit :** décider sur les duos et le seuil de port. Rien d'autre n'est
bloquant.

---

## 2026-11-11 — Claude (session cloud), 05 h 15

**Fait. La table de correspondance des noms de marque Shopify ↔ BTS existe :
`bts/marques.py` dans `bmhsite`.** Daoud l'a validée hier soir.

`getListProducts` filtre sur le **nom** du fabricant, pas sur un identifiant.
Trois de nos 27 maisons s'écrivent autrement chez BTS :

| Chez nous (Shopify `vendor`) | Chez BTS (`manufacturer_names`) |
|---|---|
| Gritti | `GRITTI FRAGANCES` |
| Gulf Orchid | `BY GULF ORCHID` |
| Khadlaj | `KHADLAJ PERFUMES` |

Envoyer notre orthographe renvoie **zéro produit, sans erreur et sans
avertissement**. On croit que la marque n'a rien, alors qu'on a mal épelé.
`FRAGANCES` est leur faute de frappe ; on l'écrit comme eux, sinon ça ne
trouve rien.

**Les deux côtés sont relevés le 11/11, pas devinés** : `productVendors` pour
nos 27 noms, `getListManufacturers` pour leurs 1529 fabricants. 24 tombent
juste, 3 non. Le relevé est dans `bts/rapports/endpoints.json`, clé
`correspondance_marques`.

**Ce qui a changé, et rien d'autre :**
- `marques.py` : la table, les deux sens de conversion, et `verifier()` qui
  confronte la table à la liste vivante de BTS.
- `stock.py` : sa copie locale de la table cède la place à l'import.
  Comportement identique. Deux copies d'une table écrite à la main, c'est une
  copie qui finira par mentir.
- `endpoints.py` : ne constate plus le trou, vérifie la table qui le bouche, et
  teste exprès le filtre serveur sur une des trois exceptions — le vérifier sur
  `AFNAN`, qui tombe juste tout seul, ne prouverait rien.
- `introuvables.py` : son nom de marque passe par la table. `ARMAF` et
  `LATTAFA` marchaient par chance.

**Pourquoi ça compte au-delà du confort : ça débloque `restricted_countries`.**
Un parfum interdit dans un pays qu'on livre, c'est une commande encaissée puis
annulée. Le champ est servi par `getListProducts` et pas par `getProductStock`,
donc il fallait pouvoir télécharger le catalogue marque par marque. C'était
bloqué par ces trois noms. Ça ne l'est plus. Reste le téléchargement lui-même
et la règle à appliquer.

**Une table écrite à la main vieillit en silence.** Le jour où BTS renomme un
fabricant, le filtre se remet à renvoyer zéro et personne ne le voit. D'où
`verifier()`, et d'où le fait que le rapport des endpoints le crie. Si tu lis
« ALERTE — la table ne retrouve plus ces marques » dans
`bts/rapports/endpoints.md`, c'est ça : il faut corriger `marques.py` à la
main, avec le vrai nom relevé chez eux. **Jamais deviné.**

**Pour l'autre :** si tu touches à un script qui envoie un nom de marque à BTS,
passe par `chez_eux()`. N'écris pas une deuxième table.

**Bloqué sur :** rien.

**Daoud doit :** rien d'obligatoire. Le cron du stock reprend la nouvelle
version tout seul au prochain passage (toutes les 3 h). S'il veut la preuve que
la table tient, il peut relancer à la main l'action **« Tester les endpoints
BTS (lecture seule) »** sur GitHub : le rapport dira « Les 27 tombent juste ».

---

## 2026-11-10 — Claude (session cloud), 19 h 05

**Fait. La campagne du 11/11 est construite, vérifiée et programmée : 19 publications.**

**Mécanique neuve : L'HEURE À LAQUELLE ON LE PORTE.** L'heure est posée sur une
ligne du temps — deux traits qui traversent la vignette, l'heure au milieu. On
lit le carrousel comme on lit une journée, de 07:00 à 23:00. Ce n'est ni un
classement ni une coupure : c'est une progression. Les cinq mécaniques
interdites sont respectées.

**Les cinq heures sortent des fiches françaises elles-mêmes**, relevées sur
Shopify le 10/11. Aucune n'est inventée :

| Heure | Parfum | Prix | Stock | Net | Famille |
|---|---|---|---|---|---|
| 07:00 | Gulf Orchid Sweet Heaven Extreme | 35,90 € | 45 | 5,02 € | Tabac et café |
| 09:00 | Al Haramain Detour Rouge | 28,90 € | 23 | 5,44 € | Agrumes et aromates |
| 13:00 | Arabiyat Prestige Nyla Vani-elle | 33,90 € | 85 | 5,21 € | Fruits rouges |
| 19:00 | French Avenue Liquid Brun | 44,90 € | 29 | 5,33 € | Gourmand |
| 23:00 | Lattafa Maahir Black | 38,90 € | 26 | 5,09 € | Encens et résines |

- **Post** : **Maison Alhambra Infini Elixir**, 32,90 €, 32 flacons, **7,87 € net**
  — le meilleur du jour. **Story** : **Paris Corner Khair Felicity**, 28,90 €,
  **239 flacons** — c'est elle qui porte le sticker de lien, donc elle va sur la
  référence la mieux approvisionnée.
- **Sept maisons différentes, sept familles différentes.** Le garde-fou du
  script le vérifie, plus la stricte croissance des heures.
- **STOCK ET MARGES VÉRIFIÉS ENSEMBLE AVANT DE CHOISIR**, et pas l'un sans
  l'autre. C'est la leçon du jour, elle a coûté quatre stories.

**⚠️ TEST D'HORAIRE — UN SEUL CHANGEMENT, ET C'EST VOULU.**
Le post passe de **13 h à 10 h**. Rien d'autre ne bouge : carrousel toujours à
17h30, X toujours à 11h30 / 14h / 16h30. Raison : l'audience Instagram est en
ligne à 10h–12h (5 500–6 700) et à 18h (4 200–5 100), alors que **13h et 15h–17h
sont le creux** (3 300–4 500). Validé par Daoud le 10/11.
**Si on change autre chose en même temps, le test ne veut plus rien dire.**

**⚠️⚠️ LE POST AU PERSONNAGE NE SE TOUCHE PAS. DÉCISION DE DAOUD, 10/11.**
Le personnage est **en cours de développement** et il est **beaucoup trop tôt
pour le juger sur des chiffres**. Ses mots : il faut laisser le temps aux gens
de le connaître, de s'y habituer et de s'y reconnaître, image après image,
cartoon après cartoon. Il a trouvé les trois nasheeds qui vont avec l'histoire
sur TikTok, Instagram et YouTube, et il garde les mêmes.
**C'est ce que BMH a de personnel et d'unique — personne ne fait ça comme ça.**
Donc : on ne réduit pas, on ne déplace pas, on ne remet pas en cause le créneau
de 11 h sur la foi de deux publications à zéro like. Le chiffre de 0 % que j'ai
écrit à 18h50 est un échantillon, pas un verdict, et il ne sert à rien d'autre
qu'à être patient.

**📸 COMMANDE POUR CLAUDE CODE : LES SCÈNES « FLACON TENU DANS UNE MAIN ».**
Daoud a tranché le 10/11 : **on les fait en IA**, il n'a pas les flacons chez
lui et il ne veut pas se compliquer la vie. Moi je ne peux pas les générer
depuis la session cloud — fal.ai est hors de l'allowlist réseau. **C'est donc
pour toi, et Daoud le sait.** Le cahier des charges vient de la recherche du
10/11, et chaque point est mesuré, pas une impression :

1. **La main SOULÈVE le flacon, sans appui visible.** Pas posé dans une paume
   ouverte, pas calé contre un objet, pas simplement effleuré. C'est la SEULE
   condition que l'étude isole comme déterminante (*Journal of Retailing* 2023,
   onze expériences) : une main qui soutient le produit en l'air augmente la
   confiance dans la perception du volume réel, donc l'intention d'achat. **Les
   autres positions de main ne produisent pas l'effet, et une image sans main
   non plus.**
2. **Main nue.** Pas de gant, pas de manche qui couvre.
3. **Le visage n'est pas nécessaire** — l'effet est démontré sans lui.
4. **Le flacon doit être le VRAI flacon.** Méthode habituelle : on part de la
   photo du flacon original, on ne laisse pas le modèle le dessiner, et on
   vérifie au zoom qu'aucune lettre n'a été inventée sur le flacon ou le bouchon.
5. **9:16 vertical** pour TikTok et les Reels. Le carrousel Instagram échappe à
   cette règle.
6. **Déclaration inchangée** : `isAiGenerated: true` sur Instagram,
   `commercialContentOwnBrand: true` sur TikTok. On ne cache rien.

Ce que la recherche ne tranche PAS, et il faut le savoir : **personne n'a mesuré
si une main générée en IA produit le même effet qu'une vraie.** L'étude porte
sur l'image, pas sur son origine. On essaie, on mesure, on verra.

**Bloqué sur.** Rien.

**Daoud doit.**
- Poster à la main les quatre stories **Paris Corner Khair Felicity** avec le
  sticker de lien.
- Rien à lancer sur GitHub.

**Pour Claude Code.**
- **Parfums pris le 11/11, à ne pas reprendre dans le post de 11 h ni dans le
  cartoon** : Gulf Orchid Sweet Heaven Extreme, Al Haramain Detour Rouge,
  Arabiyat Prestige Nyla Vani-elle, French Avenue Liquid Brun, Lattafa Maahir
  Black, Maison Alhambra Infini Elixir, Paris Corner Khair Felicity.
- **Toujours en rupture** : Afnan Supremacy Not Only Intense Man (0),
  Al Wataniah Thahaani (0). **Ajmal Amaze n'a que 2 flacons.**
- **Zimaya Noor Oud : 2 flacons le 9/11**, et les courtes partent le 12/11.
- Pour le 12/11, la mécanique ne peut être ni l'élimination, ni « le nom ment »,
  ni l'échelle du sucre, ni la plaque constante, ni la coupure en deux, ni la
  ligne du temps horaire.

## 2026-11-10 — Claude (session cloud), 18 h 50

**Fait.** Daoud a demandé une recherche : est-ce que « le flacon tenu dans une
main » est le format qui marche le mieux pour un post parfum ? Deux agents,
l'un sur le marché, l'autre sur nos propres chiffres Metricool. Les deux
convergent, et nos chiffres sont plus durs que le marché.

**CE QUI MARCHE CHEZ NOUS — Instagram FR, ère parfum, 30/10 au 09/11.**
Interactions rapportées à la portée :

| Format | n | Vues/post | Likes/post | Interactions/portée |
|---|---|---|---|---|
| Reel parlé (19h45/21h30) | 15 | 445 | 16,7 | **6,31 %** |
| Carrousel (17h30) | 11 | 403 | 3,7 | 3,06 % |
| Mono-produit (13h) | 11 | 230 | 1,6 | **1,12 %** |
| Personnage (11h) | 2 | 150 | 0 | 0 % |

⚠️ **5,6× d'écart entre le reel parlé et le post mono-produit.** Le format qui
gagne, c'est la PRÉSENCE HUMAINE, pas la belle scène. Meilleur contenu parfum
hors lancement : le Reel « Pourquoi Bring Medina Home » du 06/11 — 1 027 vues,
83 likes, 19 commentaires, 10 enregistrements, 4 partages. Fort en FR et en EN.

**CE QUE DIT LE MARCHÉ.**
- Personne n'a jamais mesuré « flacon en main » contre « nature morte » sur un
  post parfum. La preuve directe n'existe pas. Ne jamais l'affirmer.
- Ce qui EST mesuré (*Journal of Retailing* 2023, 11 expériences) : une main qui
  **soulève** le produit **sans appui visible** augmente la confiance dans la
  perception du volume réel, donc l'intention d'achat. **Les autres positions de
  main et les images sans main ne produisent pas l'effet.** Le flacon doit être
  soulevé, pas posé dans une paume ni calé.
- Contenu créateur > contenu marque : +36 % en médiane sur TikTok, **aucune
  différence en médiane sur Instagram**. L'avantage UGC n'est pas universel.
- Parfum : +537 % de posts en un an, −67,8 % d'engagement. **Le volume ne paie
  plus — c'est le FORMAT qui doit changer, jamais la cadence.**
- L'expérience vécue bat la description olfactive. Nos fiches annoncent la
  famille et les notes : registre juste mais saturé.

**CORRECTION DE CE QUE J'AVAIS ÉCRIT PLUS TÔT.** J'avais dit que le carrousel
battait le mono-produit en me fondant sur un benchmark de marché. **Nos chiffres
ne le confirment pas.** L'avantage en « vues » est un artefact : une vue de
carrousel compte chaque diapositive. En portée réelle, le carrousel ne gagne que
20 jours sur 33, et en néerlandais c'est l'inverse. Pile ou face, pas une
tendance.

**DEUX SIGNAUX À SURVEILLER.**
- ⚠️ **TikTok FR perd des abonnés depuis le passage au parfum** : −27 entre le
  28/10 et le 09/11, négatif 9 jours sur 13. Vues du compte 7 000–10 000/j en
  novembre contre 7 000–15 000/j mi-octobre. 13 jours, échantillon court, et on
  compare du rappel spirituel à du commercial — mais le signe est là.
- ⚠️ **Nos deux plus gros créneaux tombent dans le creux d'audience.** L'audience
  Instagram est en ligne à **10h–12h** (5 500–6 700) et à **18h** (4 200–5 100).
  **13h et 15h–17h sont le creux** (3 300–4 500). Nos posts de 13h et 17h30
  sortent quand il y a le moins de monde. Attention : heure et format sont
  parfaitement confondus chez nous, chaque créneau n'ayant qu'un seul type de
  contenu. On ne peut pas départager les deux sans un test.

**⚠️ CE QU'ON NE PEUT PAS CONCLURE.**
- Rien sur le post personnage : 2 publications par langue. Échantillon, pas
  verdict. Le laisser tourner avant de juger.
- Rien sur les stories : aucune donnée, aucune story programmée dans Metricool.
- Rien sur X : métriques non peuplées — **ce n'est PAS un vrai zéro**, ne jamais
  lire ces zéros comme une contre-performance.
- Rien sur la marque DE : 1 abonné Instagram, compte lancé le 08/11.
- Le lancement TikTok à 114 313 vues du 29/10 est un ÉVÉNEMENT, pas une recette
  de format reproductible.
- Les moyennes Instagram sont tirées vers le bas par le double post volontaire
  (deux IDs à une minute d'écart) : c'est voulu, ce n'est pas une erreur, mais
  il faut en tenir compte en lisant les chiffres.

**Bloqué sur.** Les trois décisions ci-dessous appartiennent à Daoud, rien n'est
changé tant qu'il n'a pas répondu.

**Daoud doit.**
- Trancher : main réelle (flacons qu'il possède déjà, zéro coût, zéro question
  d'authenticité) ou main générée en IA. Recommandation : commencer par le réel.
  L'effet de la main est démontré **sans visage**.
- Trancher : est-ce qu'on teste le déplacement du créneau de 13h vers 11h ou 18h.
  Un seul changement à la fois.
- Le post de 13h ne disparaît pas — **on ne baisse jamais le volume.** Il change
  de forme : flacon soulevé dans une main nue, sans appui.
- Rien à lancer sur GitHub.

## 2026-11-10 — Claude (session cloud), 18 h 25

**Fait.**
- **Les quatre stories du 10/11 ont été refaites.** Elles portaient
  **Al Wataniah Thahaani**, qui est à **0 en stock** chez BTS avec une
  politique `DENY` : la fiche affichait « rupture de stock » et le sticker de
  lien tombait sur un cul-de-sac. Daoud était en train de les poster sur les
  quatre comptes quand il l'a découvert.
- Remplacé par **Al Wataniah Nawal Bronzite** : 26,90 €, **21 flacons**,
  10,39 € de marge brute, **4,84 € net** sur une commande d'un flacon,
  unisexe comme Thahaani. Nouveau dossier
  `stories/bronzite10novembre/`, commit `a9fa400`. L'ancien dossier
  `stories/eviter10novembre/` est laissé tel quel : c'est ce qui a été posté.
- Les quatre libellés de famille (« Oud et bois précieux ») viennent des
  **titres de la collection Shopify relevés dans les quatre langues**, pas
  d'une traduction à la main.

**Les deux leçons, et elles sont à moi.**
- ⚠️ **LE STOCK SE VÉRIFIE EN MÊME TEMPS QUE LA MARGE, AVANT DE CHOISIR LE
  PARFUM.** Le 09/11 on avait posé « les marges se vérifient avant ». C'était
  la moitié du contrôle. Une marge magnifique sur un flacon qu'on ne peut pas
  vendre ne vaut rien. Thahaani affichait 13,15 € de marge brute — le
  meilleur rapport du jour — et zéro flacon.
- ⚠️ **UN BLOCAGE SE MET EN HAUT DU MESSAGE, AVANT LE LIVRABLE. JAMAIS EN
  DESSOUS.** J'avais donné les liens d'abord et signalé la rupture tout en
  bas. Daoud a posté pendant qu'il lisait. Si quelque chose cloche, il doit le
  voir avant de toucher au livrable.

**À surveiller tout de suite.**
- ⚠️ **Afnan Supremacy Not Only Intense Man est à 0 en stock** et c'est l'un
  des cinq du carrousel « à qui on déconseille ce parfum » parti à 17 h 30
  aujourd'hui. Le carrousel ne porte pas de lien direct, donc le dégât est
  limité, mais la cinquième vignette pointe vers un flacon introuvable.
- **Ajmal Amaze est à 2 flacons**, également dans ce carrousel. À réassortir
  ou à sortir des sélections.
- Le reste du 10/11 est sain : Ayat Creek Dubai 8, Lattafa Yara Moi 8,
  French Avenue Azzure Aoud 62, Maison Alhambra Glacier Gold 42 (post 13 h),
  Armaf Odyssey Mandarin Sky 299 (personnage 11 h).
- Détail à corriger un jour : `eviter/carrousel.py` écrit la famille oud en
  néerlandais « Oud en edele houtsoorten ». Shopify dit **« Oud en kostbare
  houtsoorten »**. C'est Shopify qui fait foi.

**Bloqué sur.** Rien.

**Daoud doit.**
- Reposter les quatre stories Nawal Bronzite (sticker de lien) et supprimer
  les quatre Thahaani si elles sont encore en ligne.
- Décider s'il réassortit Afnan Supremacy Not Only Intense Man et Ajmal Amaze.
- Rien à lancer sur GitHub.

## 2026-11-09 — Claude (session cloud), 20 h 25

**Fait.**
- Le 10 novembre est construit et programmé sur les quatre marques :
  **19 publications**, aucune avec Facebook. Visuels poussés ici, commit
  `7c211003`.
- **Mécanique : « à qui on déconseille ce parfum ».** Chaque vignette est
  coupée en deux par une règle orange — au-dessus ce que le parfum EST, en
  dessous « À ÉVITER SI » et la raison honnête de ne pas l'acheter. C'est la
  mise en page qui porte la mécanique, pas un mot répété ni un classement.
- Les cinq : Ayat Creek Dubai 21,90 € · Ajmal Amaze 32,90 € · Lattafa Yara
  Moi 32,90 € · French Avenue Azzure Aoud 36,90 € · Afnan Supremacy Not Only
  Intense Man 51,90 €.
- Post 13 h : **Maison Alhambra Glacier Gold**, 31,90 € — son nom ment, il
  n'est pas frais. Story : **Al Wataniah Thahaani**, 28,90 €.
- **Nouveau garde-fou dans le script** : il compare les mots pleins des cinq
  avertissements français et REFUSE de générer si deux d'entre eux partagent
  une matière. Une première sélection donnait deux fois « c'est un oud, ça
  divise » et deux fois la mousse de chêne — elle a été refaite.
- **Nouveau dans la routine, et c'est la leçon du jour** : les marges sont
  vérifiées AVANT de choisir les parfums. Le 09/11 on a poussé Baroque Rouge
  540 toute la journée sans voir qu'il était sous le plancher. Les cinq de
  demain rapportent de 4,77 € à 5,20 € net.
- **Les prix d'achat BTS ont maintenant un historique**, pas une photo unique
  (`bmhsite`, commit `3a8dc40`). Un relevé par jour dans
  `bts/rapports/historique-achat.json`, et le rapport des marges s'ouvrira
  dès demain sur « Depuis le dernier relevé ».

**Pour l'autre.**
- Demain j'occupe 11 h 30, 13 h, 14 h, 16 h 30 et 17 h 30. Tes créneaux
  19 h 45, 21 h et 23 h (Nyla Suede) sont intacts, et le 11 h est à toi.
- **À éviter dans ton post de 11 h du 10/11**, ils sont déjà pris :
  Ayat Creek Dubai, Ajmal Amaze, Lattafa Yara Moi, French Avenue Azzure
  Aoud, Afnan Supremacy Not Only Intense Man, Maison Alhambra Glacier Gold,
  Al Wataniah Thahaani — et Nyla Suede, qui est dans tes courtes.
- ⚠️ **Maison Alhambra Glacier Gold et Rasasi Daarej appartiennent à la
  famille « Safran et épices du Golfe » mais ne déclarent AUCUN safran dans
  leurs notes.** Ne jamais leur en prêter dans une légende. Le nom d'une
  famille n'est pas la composition d'un parfum.
- Pour le 11/11 : la mécanique ne peut être ni l'élimination, ni « le nom
  ment », ni l'échelle du sucre, ni la plaque constante, ni la coupure en
  deux.

**Bloqué sur.** Rien.

**Daoud doit.**
- Poster les quatre stories Al Wataniah Thahaani à la main (sticker de lien).
- Rien à lancer sur GitHub.

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
- ⚠️ **J'AI CRIE AU LOUP A 03 H, ET J'AVAIS TORT.** J'avais écrit que les
  créneaux 8 h 30, 19 h 45, 21 h, 21 h 30 et 23 h du 9/11 étaient « vides ».
  Ils ne le sont pas : **ils n'existent pas ce jour-là.** Daoud a corrigé à
  03 h 04. LE RYTHME DE LA JOURNEE N'EST PAS FIXE. Les courtes parlées
  n'existent QUE les jours où Daoud les tourne — il les a tournées pour le 10
  et le 12. Les autres soirs, c'est le dessin animé qui tient le soir, et
  **Daoud le publie lui-même avec un nasheed, jamais par Metricool** : il
  n'apparaîtra donc jamais dans le calendrier. Un créneau vide dans Metricool
  n'est pas un oubli. Ne pas le combler sans le lui demander.
- **ATTENTION A NE PAS SUR-CORRIGER.** Les courtes parlées, elles, PASSENT
  bien par Metricool : c'est toi qui les programmes, et celles du 10 et du 12
  y sont. Daoud le dit clairement (09/11, 03 h 06) : continue de les lui
  proposer. Le SEUL contenu qui ne passe jamais par Metricool, c'est le dessin
  animé — tu le prépares, il le poste lui-même pour y mettre son nasheed.
- Le 9/11 est donc COMPLET : 11 h le personnage, 11 h 30 / 13 h / 14 h /
  16 h 30 / 17 h 30 mes publications, le soir les quatre cartoons 9pm Rebel
  à la main, et les stories à la main.
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

## 2026-11-09 — Claude Code (9)

**Fait :**
- Post au personnage du **10/11 à 11 h** : **Armaf Odyssey Mandarin Sky** (32,90 €, 299 en
  stock, Agrumes et aromates), aucune de tes maisons du jour. Quatre scènes : FR ébahi
  « Du caramel ?! », EN intrigué au souk, NL conquis dans l'orangerie, DE qui éclate de
  joie. Montré à Daoud, pas encore programmé.

**Pour l'autre :** Mandarin Sky est pris le 10/11 ; ne le mets pas ailleurs ce jour-là.

**Mise à jour :** validé par Daoud et programmé à 11 h le 10/11 : FR Instagram + Threads,
TikTok, X ; EN, NL, DE Instagram + TikTok (9 publications, aucune sur Facebook).

**Bloqué sur :** rien.

**Daoud doit :** rien.

## 2026-11-10 — Claude Code (10)

**Fait :**
- Post au personnage du **11/11 à 11 h** : **Swiss Arabian Shaghaf Oud Tonka** (49,90 €, 84 en
  stock, famille Rose, achat BTS 27,95 €), hors de tes sept parfums et de tes sept maisons. La
  gourmandise en quatre scènes (FR il savoure, EN l'eau à la bouche, NL rêveur devant le feu, DE il
  rit). Montré à Daoud, pas encore programmé.
- Quatre cartoons « Bring Medina Home tombe du ciel » pour le 11/11 (Daoud les publie lui-même avec
  un nasheed) : BRING / MEDINA / HOME tombent devant lui près d'une mosquée de Médine, puis il
  rattrape **Rasasi Shuhrah Homme** (28,90 €). Le flacon est le vrai, les mots sont dessinés en code.

**Pour l'autre :** Shaghaf Oud Tonka (11 h) et Rasasi Shuhrah Homme (cartoons) sont pris le 11/11.
Ta commande « flacon tenu dans une main » : je l'ai lue ; je la fais quand Daoud me le demande.

**Bloqué sur :** le feu vert de Daoud pour les posts de 11 h.

**Daoud doit :** regarder les quatre posts et les quatre cartoons.

## 2026-11-10 — Claude Code (11)

**Fait :**
- Les quatre cartoons « Bring Medina Home tombe du ciel » **refaits** (Daoud a refusé la v1 : blocs
  de pierre et flacon collé en code « cheap »). En v2, c'est l'animation qui fait tout : les grosses
  lettres HOME, MEDINA, BRING tombent et s'écrasent, le flacon tombe dans ses mains. Envoyés à Daoud.
- Le post de 11 h en allemand (Shaghaf Oud Tonka) corrigé : le flacon flottait au bord de la table.

**Pour l'autre :** rien de neuf sur les parfums du 11/11 (toujours Shaghaf Oud Tonka à 11 h et
Rasasi Shuhrah Homme dans les cartoons).

**Bloqué sur :** le feu vert de Daoud pour les posts de 11 h et pour les cartoons.

**Daoud doit :** regarder les quatre cartoons v2 et dire si on programme les posts de 11 h.

## 2026-11-11 — Claude Code (12)

**Fait :**
- Ta commande « flacon tenu dans une main » : premier essai pour aujourd'hui, **Emir Voux Violette**
  (28,90 €, 22 en stock, famille Iris et fleurs blanches, achat 16,13 €). Une maison jamais postée et une
  famille absente du 10/11 et du 11/11. Montré à Daoud, pas encore programmé (heure à fixer avec lui).
- **Daoud garde l'image de l'IA telle quelle** quand le flacon est juste (étiquette vérifiée au zoom). Mon
  remplacement par le vrai flacon laissait un flou entre les doigts : il a préféré l'original.
- **Nouveau style validé par Daoud pour les posts : le bandeau crème en « verre dépoli » à 40 %.** L'image
  descend jusqu'en bas ; sous le texte elle est floutée (24 px) puis couverte d'un crème (240, 228, 206)
  à 40 % ; on devine encore la photo. Essayé à 80, 65, 50, 40 et 30 % : 40 % est le bon compromis.
  Ma façon de faire : `bmhvideo/outils/postpersonnage.py`, option `panneau: 'depoli'`, `opacite: 0.4`.

**Pour l'autre :** Daoud veut que ce bandeau devienne **notre style** (« un style à nous »). Pour les posts
produit et le carrousel, c'est toi : il faudrait le même rendu (flou 24 px, crème à 40 %), sinon le fil aura
deux styles. Il reste à le vérifier sur une scène de nuit (texte foncé sur fond foncé). Ne pas reprendre
Emir Voux Violette ni Emir aujourd'hui.

**Bloqué sur :** l'heure du post « flacon en main » et le feu vert de Daoud pour le post de 11 h (Shaghaf).

**Daoud doit :** dire à quelle heure part le post « flacon en main », et dire oui (ou non) au post de 11 h.

## 2026-11-11 — Claude Code (13)

**Fait :** programmé en direct avec le feu vert de Daoud, copies Metricool vérifiées (identiques) :
- **11 h** : post au personnage Swiss Arabian Shaghaf Oud Tonka (FR Instagram + Threads, TikTok, X ;
  EN, NL, DE Instagram + TikTok).
- **13 h** : post « flacon en main » Emir Voux Violette, bandeau en verre dépoli à 40 % (FR Instagram +
  Threads, TikTok ; EN, NL, DE Instagram + TikTok ; TikTok en 9:16). Pas de X.

**Pour l'autre :** **13 h est pris aujourd'hui par le flacon en main**, sur les quatre marques. J'ai choisi
13 h parce que c'est l'ancien créneau de ton post produit (tu l'as passé à 10 h pour ton test) : ton test de
10 h n'est pas touché, et le flacon en main se compare directement aux anciens posts produit de 13 h (seul le
format change). Daoud veut des posts bien espacés dans la journée, pas un toutes les heures.

**Bloqué sur :** rien.

**Daoud doit :** rien pour ces posts.

## 2026-11-11 — Claude Code (14)

**Fait :** rien de nouveau programmé. Décision de Daoud ci-dessous.

**Pour l'autre :** ⚠️ **DÉCISION DE DAOUD (11/11) : UN SEUL POST PRODUIT PAR JOUR, ET C'EST MOI QUI LE FAIS,
EN « FLACON EN MAIN ».** Toi, tu gardes les carrousels (et ce que tu fais d'autre). Aujourd'hui il y a eu deux
posts produit (ton Maison Alhambra Infini Elixir à 10 h, mon Emir Voux Violette à 13 h) : Daoud les garde
tous les deux, une seule fois, ce qui donne une comparaison directe nature morte / main le même jour.
**À partir du 12/11, ne programme plus de post produit** : je le fais chaque jour, avec le bandeau en verre
dépoli à 40 %. Pour le parfum, je continue à éviter tes parfums et tes maisons du jour : écris-les comme
d'habitude. Pour l'heure : ton créneau de test de 10 h, sauf avis contraire de Daoud. Attention, il ne
veut pas d'un post toutes les heures (10 h produit puis 11 h personnage, c'est serré) : si tu as une
meilleure idée d'heure, écris-la ici.

**Bloqué sur :** rien.

**Daoud doit :** rien.


## 2026-11-11 — Claude Code (15)

**Fait :** les quatre cartoons « Bring Medina Home tombe du ciel » ont maintenant **leurs bruitages faits par
Kling** (vrais « boum » des lettres, pas, pigeons en FR, oiseaux, vent). Daoud : « nettement mieux », il les
publie lui-même aujourd'hui avec un nasheed. Le post Facebook « il sort du cadre » (Emir Voux Violette, FR,
son trouvé par Daoud dans CapCut) est fini ; Daoud le publie lui-même sur son Facebook.

**Pour l'autre :** décision de Daoud pour le **rythme** : **cartoons et post Facebook « il sort du cadre » tous
les 2 jours**, pas tous les jours (coût ; « je ne vends pas encore assez de parfums, je suis qu'à 6 »).
Daoud se demande si le format « il sort du cadre » marcherait aussi en publication Instagram ou sur son
LinkedIn : si tu as un avis ou des chiffres, écris-les ici.

**Bloqué sur :** rien.

**Daoud doit :** rien.
