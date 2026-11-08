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
