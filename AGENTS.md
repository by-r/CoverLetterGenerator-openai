# CoverLetterGenerator

Flask app that uses the OpenAI API (legacy completion) to generate tailored cover letters based on job title and company name.

## Project

- **Stack**: Python 3.10, Flask 2.3, OpenAI (v0.27 legacy `openai.Completion`), Tailwind CSS, Jinja2
- **Entry point**: `app.py` — runs `app.run(debug=True)` when executed directly
- **Config**: `.env` file with `API_KEY=<OpenAI key>` (copy from `.env.template`)
- **Dependencies managed via**: both `Pipfile` (pipenv) and `requirements.txt`

## Commands

| Purpose | Command |
|---------|---------|
| Activate env | `pipenv shell` |
| Run app | `python app.py` (serves on `http://127.0.0.1:5000`) |
| Build Tailwind CSS | `tailwindcss -i static/src/style.css -o static/css/main.css --watch` |
| Lint templates | `djlint templates/` |

## Architecture

- **`app.py`** — single Flask module: routes (`/` GET+POST, `/gotohome`), OpenAI prompt construction, text formatting (`format_text`)
- **`templates/`** — Jinja2 templates:
  - `base.html` — layout shell with Tailwind CSS link
  - `index.html` — form with Job + Company inputs
  - `coverletter.html` — renders generated cover letter in `<pre>` tag
- **`static/`** — Tailwind source (`src/style.css`) and compiled output (`css/main.css`)
- **`test.py`** — standalone CLI script to test the OpenAI completion call

## Conventions

- **Flask**: standard route decorators, `render_template`, `redirect`/`url_for`
- **Jinja2**: `{% extends %}`, `{% block %}`, `{% endblock %}` with named blocks (`title`, `content`)
- **CSS**: Tailwind utility classes throughout; config in `tailwind.config.js` scoped to `templates/index.html`
- **OpenAI**: uses legacy `openai.Completion.create` with `text-curie-001` model (NOT the newer ChatCompletion API)
- **Error handling**: minimal — no try/except around OpenAI calls
- **Naming**: snake_case for Python variables/functions, lowercase with hyphens for CSS classes
- **Testing**: no test framework; `test.py` is a manual CLI script

## Notes

- Legacy OpenAI v0.27 API (not the v1+ client). Uses Completion (not ChatCompletion).
- Cover letter prompt is static: `"Write a cover letter for {job} role at {company}"`.
- The `format_text` helper uses `textwrap.wrap` (width=80) for paragraph formatting.
- Both `Pipfile` and `requirements.txt` are kept in sync — use either.
