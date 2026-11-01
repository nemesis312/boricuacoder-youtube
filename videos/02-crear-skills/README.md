# 02: Cómo crear una skill / How to create a skill

## Español

Una skill de Claude Code es una carpeta con un archivo `SKILL.md`. El campo `description` es lo que Claude lee para decidir cuándo usarla; el resto del archivo son las instrucciones. También la puedes invocar a mano con `/nombre`. Este video construye dos skills: `hackernews` y `mensaje-commit`.

- Video: https://youtu.be/jkUsPg7dUhc
- Artículo: https://blog.boricuacoder.dev/es/blog/crear-skills-es/

### Requisitos

- Claude Code CLI instalado y con sesión iniciada
- `curl` (para instalar las skills con un comando y para que `hackernews` consulte la API)
- `git` (para `mensaje-commit`)

### Contenido

| Archivo | Para qué sirve |
|---|---|
| `skills/hackernews/SKILL.md` | Busca en Hacker News (portada o por tema) y devuelve las 5 noticias más interesantes: título, puntos y link |
| `skills/mensaje-commit/SKILL.md` | Lee el diff en staged y tus últimos commits, y propone un mensaje de commit en tu estilo antes de hacerlo |

Las skills se publican idénticas a las del video, en español.

### Instalación

Hay dos lugares donde puede vivir una skill:

- `~/.claude/skills/<nombre>/SKILL.md`: personal, disponible en todos tus proyectos.
- `.claude/skills/<nombre>/SKILL.md` dentro de un repo: para compartirla con tu equipo.

Instalación personal, una línea por skill:

```bash
mkdir -p ~/.claude/skills/hackernews && curl -fsSL https://raw.githubusercontent.com/nemesis312/boricuacoder-youtube/main/videos/02-crear-skills/skills/hackernews/SKILL.md -o ~/.claude/skills/hackernews/SKILL.md
mkdir -p ~/.claude/skills/mensaje-commit && curl -fsSL https://raw.githubusercontent.com/nemesis312/boricuacoder-youtube/main/videos/02-crear-skills/skills/mensaje-commit/SKILL.md -o ~/.claude/skills/mensaje-commit/SKILL.md
```

Para compartirlas con tu equipo, ejecuta desde la raíz del repo y cambia `~/.claude/skills` por `.claude/skills`.

### Cómo probarlo

- `hackernews`: pregunta "¿qué hay hoy en Hacker News?" o "busca en HN algo de Rust".
- `mensaje-commit`: haz `git add` de un cambio y escribe `/mensaje-commit`, o pregunta "¿qué pongo en el commit?".

### Las 3 lecciones

1. Una descripción vaga no le dice a Claude cuándo usar la skill. Incluye frases que tú dirías de verdad.
2. Más corta es mejor. Di lo necesario y nada de relleno.
3. Una skill, una tarea.

---

## English

A Claude Code skill is a folder with a `SKILL.md` file. The `description` field is what Claude reads to decide when to use it; the rest of the file holds the instructions. You can also invoke it manually with `/name`. This video builds two skills: `hackernews` and `mensaje-commit`.

- Video (in Spanish): https://youtu.be/jkUsPg7dUhc
- Article: https://blog.boricuacoder.dev/blog/crear-skills-en/

### Requirements

- Claude Code CLI installed and logged in
- `curl` (to install the skills with one command and for `hackernews` to query the API)
- `git` (for `mensaje-commit`)

### Contents

| File | Purpose |
|---|---|
| `skills/hackernews/SKILL.md` | Searches Hacker News (front page or by topic) and returns the 5 most interesting stories: title, points and link |
| `skills/mensaje-commit/SKILL.md` | Reads the staged diff and your recent commits, and proposes a commit message in your style before committing |

The skills are published identical to the ones in the video. Their content stays in Spanish; the skills reply in Spanish.

### Install

A skill can live in two places:

- `~/.claude/skills/<name>/SKILL.md`: personal, available in all your projects.
- `.claude/skills/<name>/SKILL.md` inside a repo: to share it with your team.

Personal install, one line per skill:

```bash
mkdir -p ~/.claude/skills/hackernews && curl -fsSL https://raw.githubusercontent.com/nemesis312/boricuacoder-youtube/main/videos/02-crear-skills/skills/hackernews/SKILL.md -o ~/.claude/skills/hackernews/SKILL.md
mkdir -p ~/.claude/skills/mensaje-commit && curl -fsSL https://raw.githubusercontent.com/nemesis312/boricuacoder-youtube/main/videos/02-crear-skills/skills/mensaje-commit/SKILL.md -o ~/.claude/skills/mensaje-commit/SKILL.md
```

To share them with your team, run from the repo root and replace `~/.claude/skills` with `.claude/skills`.

### How to try them

- `hackernews`: ask "¿qué hay hoy en Hacker News?" or "busca en HN algo de Rust".
- `mensaje-commit`: `git add` a change and type `/mensaje-commit`, or ask "¿qué pongo en el commit?".

### The 3 lessons

1. A vague description does not tell Claude when to use the skill. Include phrases you would actually say.
2. Shorter is better. Say what is needed and no filler.
3. One skill, one task.
