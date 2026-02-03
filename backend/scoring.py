import json

def score_project_against_jd(project: dict, jd_parsed: dict) -> dict:

    score = {
        "total_score": 0.0,
        "skill_score": 0.0,
        "domain_score": 0.0,
        "keyword_score": 0.0,
        "type_score": 0.0,
        "matches": {
            "skills": [],
            "domains": [],
            "keywords": []
        },
        "missing": {
            "skills": [],
            "domains": [],
            "keywords": []
        }
    }

    # Extracting Project & Job Description Data

    project_skills = set([s.lower() for s in project.get("tech_stack", [])] +
                         [s.lower() for s in project.get("skills", [])])
    project_domains = set([d.lower() for d in project.get("domains", [])])
    project_keywords = set()
    for bp in project.get("bullet_points", []):
        project_keywords.update([k.lower() for k in bp.get("keywords", [])])

    jd_skills = set(s.lower() for s in jd_parsed.get("core_skills", []))
    jd_domains = set(s.lower() for s in jd_parsed.get("domains", []))
    jd_keywords = set(s.lower() for s in jd_parsed.get("keywords", []))

    if jd_skills:
        matched_skills = project_skills & jd_skills
        score["matches"]["skills"] = list(matched_skills)
        score["missing"]["skills"] = list(jd_skills - matched_skills)
        score["skill_score"] = len(matched_skills) / len(jd_skills) * 40

    if jd_domains:
        matched_domains = project_domains & jd_domains
        score["matches"]["domains"] = list(matched_domains)
        score["missing"]["domains"] = list(jd_domains - matched_domains)
        score["domain_score"] = len(matched_domains) / len(jd_domains) * 25

    if jd_keywords:
        matched_keywords = []
        for jd_kw in jd_keywords:
            for proj_kw in project_keywords:
                # Check if any word from JD keyword appears in project keyword
                if any(word in proj_kw for word in jd_kw.split()):
                    matched_keywords.append(jd_kw)
                    break

        score["matches"]["keywords"] = matched_keywords
        score["missing"]["keywords"] = list(jd_keywords - set(matched_keywords))
        score["keyword_score"] = len(matched_keywords) / len(jd_keywords) * 25

    project_type = infer_project_type(project)
    if project_type == jd_parsed.get("type", "unknown"):
        score["type_score"] = 10

    score["total_score"] = (
            score["skill_score"] +
            score["domain_score"] +
            score["keyword_score"] +
            score["type_score"]
    )

    return score

def infer_project_type(project) -> str:
    domains = [d.lower() for d in project.get("domains", [])]
    skills = [s.lower() for s in project.get("skills", [])]

    if any(d in ["machine learning", "ml", "computer vision", "nlp"] for d in domains):
        return "ml"
    if any(d in ["data", "analytics", "data analytics", "business intelligence", "bi"] for d in domains):
        return "data"
    if any("testing" in s or "qa" in s for s in skills):
        return "qa"

    return "swe"

def rank_projects_for_jd(projects: list, jd_parsed: dict) -> list:
    scored_projects = []

    for project in projects:
        score = score_project_against_jd(project, jd_parsed)
        scored_projects.append({
            "project": project,
            "score": score
        })

    # Sort by total score descending
    scored_projects.sort(key=lambda x: x["score"]["total_score"], reverse=True)

    return scored_projects

