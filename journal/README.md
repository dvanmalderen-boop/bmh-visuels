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
- Le seul défaut : le nom gravé sur le flacon sort tordu. La parade est dans le
  brief — plaque vierge dans le prompt, ou incrustation du vrai flacon.
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
