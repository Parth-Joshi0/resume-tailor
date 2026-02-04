import json
from xml.sax.handler import property_encoding

from jinja2 import Environment, FileSystemLoader
import subprocess
from pathlib import Path

def getPersonalInfo(path: str = "../data/personal.json") -> dict:
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def getProjectsData(path: str = "../data/projects", selected_projects: list = []) -> dict:
    path = Path(path)
    projects = []

    for file in path.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            project = json.load(f)
            if project['project_id'] in selected_projects:
                projects.append(project)

    return {'projects': projects}

def getExperienceDate(path: str = "../data/experience") -> dict:
    path = Path(path)
    experiences = []

    for file in path.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            experience = json.load(f)
            experiences.append(experience)

    return {'experience': experiences}

def generateLatexJson(selected_projects: list) -> dict:
    return getPersonalInfo() | getExperienceDate() | getProjectsData(selected_projects=selected_projects)

def renderLatex(selected_projects: list, template_file: str = "../templates/resume.j2", output_file: str = "resume.tex"):
    data = generateLatexJson(selected_projects)
    template_path = Path(template_file)
    env = Environment(
        loader = FileSystemLoader(template_path.parent if template_path.parent.exists() else '.'),
        trim_blocks = True,
        lstrip_blocks = True,
        block_start_string="((*",
        block_end_string="*))",
        variable_start_string="(((",
        variable_end_string=")))",
        comment_start_string="((#",
        comment_end_string="#))",
    )
    template = env.get_template(template_path.name)
    rendered = template.render(**data)

    output_path = Path("../data/resumes/" + output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered)

    return output_path
