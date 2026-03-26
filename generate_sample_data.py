
import random
import pandas as pd
from datetime import datetime, timedelta

# --- The data we'll randomly combine to make realistic job listings ---

companies = [
    "Siemens", "BMW", "Bosch", "SAP", "Allianz", "MAN", "Adidas", "KPMG",
    "Deloitte", "McKinsey", "Accenture", "Capgemini", "T-Systems", "Infosys",
    "msg systems", "Fujitsu", "Datev", "Nürnberger Versicherung", "1&1", "Zalando"
]

cities = [
    "München", "München", "München",   # more common because more jobs there
    "Berlin", "Berlin",
    "Nürnberg", "Nürnberg",
    "Hamburg", "Frankfurt", "Stuttgart",
    "Erlangen", "Augsburg", "Düsseldorf"
]

role_types = [
    ("Data Analyst", "Data / Analytics"),
    ("Business Intelligence Analyst", "Data / Analytics"),
    ("Data Science", "Data / Analytics"),
    ("IT Consultant", "IT Consulting / Business Analysis"),
    ("Business Analyst", "IT Consulting / Business Analysis"),
    ("Process Consultant", "IT Consulting / Business Analysis"),
    ("Software Developer", "Software Development"),
    ("Python Developer", "Software Development"),
    ("Backend Developer", "Software Development"),
    ("Full Stack Developer", "Software Development"),
]

skills_pool = {
    "Data / Analytics":               ["Python", "Power BI", "SQL", "Excel", "Tableau", "R", "pandas"],
    "IT Consulting / Business Analysis": ["Excel", "PowerPoint", "SQL", "SAP", "Power BI", "Visio", "JIRA"],
    "Software Development":           ["Python", "JavaScript", "Git", "SQL", "Docker", "Java", "REST APIs"],
}

platforms = ["LinkedIn", "Indeed", "StepStone", "Company Website", "Xing"]
statuses = ["Applied", "Applied", "Applied", "Saved", "Saved", "Rejected", "Interview"]

# Generate 80 rows 
rows = []
today = datetime.today()

for i in range(80):
    role_name, category = random.choice(role_types)
    city = random.choice(cities)
    company = random.choice(companies)
    platform = random.choice(platforms)
    status = random.choice(statuses)

    # Picking 3-5 random skills from the relevant pool
    skill_list = random.sample(skills_pool[category], k=random.randint(3, min(5, len(skills_pool[category]))))

    # Random date posted within the last 60 days
    days_ago = random.randint(1, 60)
    date_posted = (today - timedelta(days=days_ago)).strftime("%Y-%m-%d")

    # Salary range (some missing — realistic!)
    if random.random() > 0.4:
        salary = random.choice([14, 15, 16, 17, 18])
        salary_str = f"{salary} €/hr"
    else:
        salary_str = "Not listed"

    rows.append({
        "Job Title":        f"Werkstudent {role_name} (m/f/d)",
        "Company":          company,
        "City":             city,
        "Category":         category,
        "Skills Required":  ", ".join(skill_list),
        "Salary":           salary_str,
        "Platform":         platform,
        "Date Posted":      date_posted,
        "Status":           status,
        "Notes":            ""
    })

df = pd.DataFrame(rows)
df.to_excel("jobs_raw.xlsx", index=False)
print(" Created jobs_raw.xlsx with", len(df), "job postings.")
print("   Open the file to see the data, then run: python clean_jobs.py")
