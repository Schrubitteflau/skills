# skills

Skills Claude Code personnels, installables avec [`npx skills`](https://github.com/vercel-labs/skills).

| Skill | Description |
| --- | --- |
| `end-grilling` | Clôt une session de grilling : écrit chaque décision de l'humain, avec ses propres mots, dans le journal de décisions (hors du repo). |
| `ship` | Livre les tickets d'une spec sur une branche d'intégration : chaque ticket implémenté, revu jusqu'à être propre, puis mergé. |

## Installation

Le repo est privé : `npx skills` le clone via git, donc il faut être authentifié auprès de GitHub (`gh auth login` / `gh auth setup-git`).

```bash
# Tous les skills, au niveau utilisateur
npx skills add Schrubitteflau/skills -g

# Un seul skill
npx skills add Schrubitteflau/skills -g --skill ship
```

Mise à jour :

```bash
npx skills update -g
```

## Ajouter un skill

Créer `skills/<nom>/SKILL.md` (frontmatter `name` + `description`) avec ses fichiers annexes à côté.
