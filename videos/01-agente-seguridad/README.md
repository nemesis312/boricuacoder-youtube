# 01: Agente de seguridad antes del commit / Security agent before the commit

## Español

Un subagente de Claude Code (`security-reviewer`) y un hook `pre-commit` de Git que le pasa el diff en staged. El agente busca secretos, inyecciones y otros problemas de seguridad, explica lo que encuentra y la última línea de su respuesta es `VERDICT: PASS` o `VERDICT: BLOCK`. Si es `BLOCK`, el commit se detiene.

- Video: https://youtu.be/Cmw1km8dR5U
- Artículo: https://blog.boricuacoder.dev/es/blog/first-ai-agent-security-reviewer-es/

### Requisitos

- `git`
- Claude Code CLI instalado y con sesión iniciada (el hook ejecuta `claude -p`)

### Contenido

| Archivo | Para qué sirve |
|---|---|
| `.claude/agents/reviewer.md` | Definición del subagente `security-reviewer` |
| `hooks/pre-commit` | Hook de Git que envía el diff en staged al agente |
| `example/app.py` | Ejemplo vulnerable (key ficticia y consulta SQL concatenada) |
| `example/app_fixed.py` | Versión corregida (key desde `os.environ` y consulta parametrizada) |

### Instalación

Desde la raíz de tu repositorio:

```bash
mkdir -p .claude/agents
cp /ruta/a/boricuacoder-youtube/videos/01-agente-seguridad/.claude/agents/reviewer.md .claude/agents/reviewer.md
cp /ruta/a/boricuacoder-youtube/videos/01-agente-seguridad/hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

El agente se llama `security-reviewer` (campo `name` del archivo); el hook lo invoca con `--agent security-reviewer`.

### Cómo probarlo

1. En un repo de prueba, instala el agente y el hook como se indica arriba.
2. Copia `example/app.py` a la raíz del repo de prueba.
3. Ejecuta `git add app.py && git commit -m "add payments"`.
4. El agente debería reportar la API key en el código y la inyección SQL, y terminar con `VERDICT: BLOCK`, lo que detiene el commit.
5. Reemplaza el contenido de `app.py` por el de `example/app_fixed.py`, vuelve a hacer `git add` y `git commit`. Debería terminar con `VERDICT: PASS`. Para que el código corra, define antes la variable de entorno `STRIPE_KEY`.

La key de `example/app.py` es ficticia (`sk_live_FAKE_...`). Nunca pongas una key real en un ejemplo.

### Limitaciones

- Un modelo de lenguaje puede pasar por alto problemas o marcar falsos positivos. No es una garantía. Úsalo junto con una herramienta dedicada como [gitleaks](https://github.com/gitleaks/gitleaks).
- `git commit --no-verify` salta el hook por completo.
- El diff en staged se envía a la API del modelo. No lo uses con código que no puedas compartir con ese servicio.
- Cada commit con cambios tarda lo que tarde la revisión y consume uso del modelo (tiempo y costo).
- El archivo del agente lista `Bash` en `tools`, mientras que el hook solo permite `Read,Grep,Glob` con `--allowedTools`. Se publican tal cual salen en el video.

---

## English

A Claude Code subagent (`security-reviewer`) and a Git `pre-commit` hook that feeds it the staged diff. The agent looks for secrets, injections and other security problems, explains what it finds, and the last line of its answer is `VERDICT: PASS` or `VERDICT: BLOCK`. On `BLOCK`, the commit is stopped.

- Video (in Spanish): https://youtu.be/Cmw1km8dR5U
- Article: https://blog.boricuacoder.dev/blog/first-ai-agent-security-reviewer-en/

### Requirements

- `git`
- Claude Code CLI installed and logged in (the hook runs `claude -p`)

### Contents

| File | Purpose |
|---|---|
| `.claude/agents/reviewer.md` | Definition of the `security-reviewer` subagent |
| `hooks/pre-commit` | Git hook that sends the staged diff to the agent |
| `example/app.py` | Vulnerable example (fake key and concatenated SQL query) |
| `example/app_fixed.py` | Fixed version (key from `os.environ` and parameterized query) |

### Install

From the root of your repository:

```bash
mkdir -p .claude/agents
cp /path/to/boricuacoder-youtube/videos/01-agente-seguridad/.claude/agents/reviewer.md .claude/agents/reviewer.md
cp /path/to/boricuacoder-youtube/videos/01-agente-seguridad/hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

The agent is named `security-reviewer` (the `name` field in the file); the hook calls it with `--agent security-reviewer`.

### How to test it

1. In a scratch repo, install the agent and the hook as above.
2. Copy `example/app.py` to the root of the scratch repo.
3. Run `git add app.py && git commit -m "add payments"`.
4. The agent should report the API key in the code and the SQL injection, and end with `VERDICT: BLOCK`, which stops the commit.
5. Replace the contents of `app.py` with `example/app_fixed.py`, then `git add` and `git commit` again. It should end with `VERDICT: PASS`. To run the code, set the `STRIPE_KEY` environment variable first.

The key in `example/app.py` is fake (`sk_live_FAKE_...`). Never put a real key in an example.

### Limitations

- A language model can miss issues or raise false positives. It is not a guarantee. Use it alongside a dedicated tool such as [gitleaks](https://github.com/gitleaks/gitleaks).
- `git commit --no-verify` skips the hook entirely.
- The staged diff is sent to the model API. Do not use it on code you cannot share with that service.
- Each commit with changes waits for the review and uses model quota (time and cost).
- The agent file lists `Bash` in `tools`, while the hook only allows `Read,Grep,Glob` through `--allowedTools`. They are published exactly as shown in the video.
