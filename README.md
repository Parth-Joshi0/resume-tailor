# resume-tailor

A personal tool for managing and generating resume content using structured JSON project data and Jinja2 LaTeX templates.

> ⚠️ **Work in Progress** — this project is actively being built out. Structure and tooling may change.

---

## Structure

```
resume-tailor/
├── backend/
│   └── (backend code will go here)
├── data/
│   ├── experience/
│   │   ├── mathnasium.json
│   │   └── tetra_tech.json
│   ├── projects/
│   │   ├── chess_engine.json
│   │   ├── introspect.json
│   │   ├── maple_sap_prediction.json
│   │   └── nurse-ai-followup.json
│   ├── resumes/
│   │   └── (Generate resumes will go here)
│   └── personal.json
├── frontend/
│   └── (frontend code will go here)
├── templates/
│   ├── experience.json
│   ├── personal.json
│   ├── project.json
│   └── resume.j2
├── LICENSE
└── README.md
```

## How It Works

1. **New project?** Copy `templates/project.json` into `data/projects/`, rename it, and fill in the fields.
2. **New job?** Copy `templates/experience_template.json` into `data/experience/`, rename it, and fill in the fields.
3. **Update personal info?** Edit `data/personal.json` with your contact info, education, and skills.
4. **Generate resume?** Feed your data files into `templates/resume.j2` to render the full LaTeX resume. Drop it straight into Overleaf.

## Templates

- **`templates/project.json`** — Base schema for a project entry. Copy this for each new project.
- **`templates/experience_template.json`** — Base schema for a job experience entry. Copy this for each new job.
- **`templates/resume.j2`** — Jinja2 template that renders a complete LaTeX resume. Expects `personal`, `education`, `skills`, `experience`, and `projects` data. Feel free to swap in your own.

## Data Files

All resume content lives in `backend/data/`:
- **`personal.json`** — Your name, contact info, education, and skills categories
- **`projects/`** — One JSON file per project (e.g., `chess_engine.json`, `introspect.json`)
- **`experience/`** — One JSON file per job (e.g., `tetra_tech.json`, `mathnasium.json`)

This structure keeps everything modular — add/remove projects and jobs without touching other files.