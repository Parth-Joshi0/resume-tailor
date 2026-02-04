# resume-tailor

A personal tool for managing and generating tailored resumes using structured JSON project data and AI-powered content optimization.

> ⚠️ **Work in Progress** — this project is actively being built out. Structure and tooling may change.

---

## Structure

```
resume-tailor/
├── backend/
│   ├── .env
│   ├── .env.example
│   ├── ai_client.py
│   ├── app.py
│   ├── pdf_pipeline.py
│   └── scoring.py
├── data/
│   ├── experience/
│   │   └── (your experience JSON files)
│   ├── projects/
│   │   └── (your project JSON files)
│   ├── resumes/
│   │   └── (generated resumes will go here)
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

## Quick Start (Current Functionality)

### 1. Configure API Access

Copy `.env.example` to `.env` in the `backend/` directory and add your Gemini API key:

```bash
cd backend
cp .env.example .env
```

Then edit `.env` and add your API key:
```
GEMINI_API_KEY=your_api_key_here
```

### 2. Set Up Your Data

- **Personal Info**: Fill in `data/personal.json` with your name, contact info, education, and skills
- **Projects**: Copy `templates/project.json` for each project into `data/projects/`, rename it, and fill in the fields
- **Experience**: Copy `templates/experience.json` for each job into `data/experience/`, rename it, and fill in the fields

### 3. Add Your Job Description

Open `backend/app.py` and paste your target job description in the designated spot.

### 4. Generate Your Resume

Run the application:

```bash
cd backend
python app.py
```

### 5. Get Your Output

The script will generate two files in `data/resumes/`:
- `first_name last_name.pdf` — Your tailored resume PDF
- `resume.tex` — The LaTeX source file

You can also upload `resume.tex` directly to Overleaf for further customization.

---

## How It Works

1. **Structured Data** — All your experience, projects, and personal info are stored as modular JSON files
2. **AI Optimization** — The tool analyzes the job description and tailors your resume content accordingly
3. **Template Rendering** — Jinja2 templates combine your data into a professional LaTeX resume
4. **PDF Generation** — Automatic compilation to PDF for immediate use

---

## Templates

- **`templates/project.json`** — Base schema for a project entry. Copy this for each new project.
- **`templates/experience.json`** — Base schema for a job experience entry. Copy this for each new job.
- **`templates/personal.json`** — Base schema for personal information, education, and skills.
- **`templates/resume.j2`** — Jinja2 template that renders a complete LaTeX resume. Expects `personal`, `education`, `skills`, `experience`, and `projects` data.

Feel free to customize these templates to match your preferred resume style.

---

## Data Files

All resume content lives in `data/`:

- **`personal.json`** — Your name, contact info, education, and skills categories
- **`projects/`** — One JSON file per project (e.g., `chess_engine.json`, `introspect.json`)
- **`experience/`** — One JSON file per job (e.g., `tetra_tech.json`, `mathnasium.json`)

This modular structure lets you add or remove projects and jobs without touching other files.

---

## Roadmap

- [ ] Frontend interface for easier data management
- [ ] Skills highlighting based on job requirements
- [ ] Experience relevance scoring
- [ ] Cover letter generation
- [ ] Multiple resume templates

---

## License

See `LICENSE` for details.