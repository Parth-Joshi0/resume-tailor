import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()

client = genai.Client()

def generate_jd_parsing_prompt(jobDescription: str) -> str:
    prompt = f"""You are a senior NLP engineer specializing in job-description parsing and schema-accurate JSON extraction.
    Objective:
    Given a single job description (JD) as raw text, extract the requested hiring signals and output ONLY a valid JSON object that matches the schema below exactly. No extra keys. No comments. No markdown. No surrounding text.
    Output schema (must match exactly):
    {{
      "core_skills": [],
      "domains": [],
      "seniority": "unknown",
      "keywords": [],
      "type": "unknown"
    }}
    
    Hard requirements:
    - Output must be strictly valid JSON (double quotes, no trailing commas).
    - Output must contain exactly these 5 keys and no others.
    - If you output anything other than JSON, the answer is invalid.
    
    Extraction rules:
    1) Key order must match the schema order shown.
    2) All array items must be lowercase strings, deduplicated, and ordered by relevance (most important first).
    3) If not explicitly supported by the JD: use [] for arrays and "unknown" for strings. Never guess.
    4) core_skills: only concrete technical skills/tools/languages/frameworks explicitly mentioned or clearly required (e.g., python, sql, react, aws, docker). Exclude soft skills.
    5) domains: industry areas (e.g., healthcare, fintech, ecommerce) and/or functional areas (e.g., analytics, machine learning, security) only if clearly indicated.
    6) seniority: choose ONE of: "intern","junior","mid","senior","staff","principal","lead","manager","director","vp","cxo","unknown".
       Map cues: "new grad"->"junior", "co-op"->"intern", "entry level"->"junior".
    7) keywords: 2–4 word noun phrases capturing responsibilities/themes (e.g., data pipelines, unit testing, api design, cloud migration).
       Avoid repeating core_skills unless part of a larger phrase (e.g., "python data pipelines" is ok).
    8) type: choose ONE of: "swe","data","ml","devops","security","product","design","qa","analyst","unknown".
       Base on the primary role described (not secondary nice-to-haves).
    
    Input JD (between triple quotes):
    \"\"\"
    {jobDescription}
    \"\"\"
    """

    return prompt

def get_signals(jobDescription: str) -> dict:
    '''
    Generates the key signals from the jobDescription in this format
    {
    "core_skills": ["java", "ruby", "javascript", "scala", "go", "testing"],
    "domains": ["fintech", "payments", "infrastructure"],
    "seniority": "intern",
    "keywords": ["production software", "financial infrastructure", "service discovery", "systems design"],
    "type": "swe"
    }
    param: jobDescription
    :return: Json String of key signals
    '''
    prompt = generate_jd_parsing_prompt(jobDescription)
    resp = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    print(resp.text)
    return json.loads(resp.text)
