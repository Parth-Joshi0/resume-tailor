from backend.ai_client import get_signals, generate_jd_parsing_prompt
import json
from pathlib import Path

from backend.pdf_pipeline import renderLatex, generatePdffromLatex
from backend.scoring import rank_projects_for_jd

def load_projects(projects_dir: str = "../data/projects") -> list[dict]:
    projects = []
    projects_path = Path(projects_dir)

    for file in projects_path.glob("*.json"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                project = json.load(f)
                projects.append(project)
        except Exception as e:
            print(f"⚠️ Failed to load {file.name}: {e}")

    return projects

jd = '''As a Data Analyst Intern, you’ll have the opportunity to work alongside our experienced data analytics professionals, gaining hands-on experience in data collection, analysis and reporting.

About the Role
Assist in the collection, organization, and cleaning of data from various sources
Perform data analysis using tools such as SQL, Excel, and data visualization software
Develop and maintain dashboards and reports to present insights to stakeholders
Collaborate with cross-functional teams to understand business requirements and translate them into data-driven solutions
Participate in data-related projects and initiatives, contributing to the development of data-driven strategies
Identify trends, patterns, and anomalies in data to support decision-making processes
Continuously learn and stay up-to-date with the latest data analysis techniques and technologies

About You
Minimum Qualifications:
Currently pursuing a degree in Data Science, Statistics, Computer Science, or a related field
Proficiency in SQL and data manipulation tools (e.g., Excel, Tableau, Power BI)
Excellent communication and collaboration skills
Ability to work independently and as part of a team
Passion for data-driven insights and a desire to learn and grow

Preferred Qualifications:
Experience with programming languages such as Python or R
Strong analytical and problem-solving skills
What you’ll get
Our team members fuel our strategy, innovation and growth, so we ensure the health and well-being of not just you, but your family, too! We go above and beyond to give you the support you need on an individual level and offer all sorts of ways to help you live your best life. We are proud to offer eligible team members perks and health benefits that will help you have peace of mind. Simply put: We’ve got your back. Check out our full list of Benefits and Perks.
About us
Rocket Innovation Studio (RIS) launched in 2019 and has gone on to make its mark in the Canadian fintech industry. Headquartered at 156 Chatham Street in Windsor, Ontario, the company renovated the historic building which began as an auto showroom and garage before becoming a furniture store, the Old Fish Market, the Coach and Horses Pub, and the Loop.
 
With the backing of Rocket Companies®, RIS is able to capitalize on the creativity and growth of a startup environment with the stability and enterprise experience of a mature company. At RIS, Canadian talent is able to collaborate, design, build, test and return a full range of custom IT solutions. RIS is leading the charge to make Windsor Canada's tech hub. Apply today to join a team that offers career growth, amazing benefits and the chance to work with leading industry professionals.
This job description is an outline of the primary responsibilities of this position and may be modified at the discretion of the company at any time.  Decisions related to employment are not based on race, color, religion, national origin, sex, physical or mental disability, sexual orientation, gender identity or expression, age, military or veteran status or any other characteristic protected by state or federal law.  The company provides reasonable accommodations to qualified individuals with disabilities in accordance with applicable state and federal laws.  Applicants requiring reasonable accommodations in completing the application and/or participating in the application process should contact a member of the Human Resources team, at Careers@Rocket.com.
This posting is for an existing vacancy for a Data Analyst Intern at Rocket Innovation Studio.  The compensation for this position is $24.50-$37.00. The position may also be eligible for an annual bonus, incentives, and other employment-related benefits including, but not limited to, medical, dental, and vision benefits, retirement plan, and paid time off.  More information regarding these benefits and others can be found here.  The information regarding compensation and other benefits included in this paragraph is only an estimate and is subject to revision from time to time as the Company, in its sole and exclusive discretion, deems appropriate. The Company may determine during its review of the proposed compensation and benefits provided for this position, that the compensation and benefits for such position should be reduced. In no event will the Company reduce the compensation for the position to a level below the applicable jurisdictional minimum wage rate for the position.
Our Talent Acquisition team uses artificial intelligence to assist in screening, assessing, or selecting applicants. Our hiring process is never completely automated and uses AI in conjunction with our recruiting and talent acquisition professionals. '''

prompt = generate_jd_parsing_prompt(jd)
signals = get_signals(prompt)
selected_projects = rank_projects_for_jd(load_projects(), signals)
print(selected_projects)
renderLatex(selected_projects=selected_projects)
generatePdffromLatex()