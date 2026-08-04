import pandas as pd


SPECIAL_SKILLS = { 
    "Aws": "AWS", 
    "Vs Code": "VS Code", 
    "Github": "GitHub", 
    "Gitlab": "GitLab", 
    "Node.Js": "Node.js", 
    "Express.Js": "Express.js", 
    "Next.Js": "Next.js", 
    "Vue.Js": "Vue.js", 
    "Nuxt.Js": "Nuxt.js", 
    "C++": "C++", 
    "C#": "C#", 
    "Sql": "SQL", 
    "Rest Api": "REST API", 
    "Scikit-Learn": "Scikit-learn", 
    "Pytorch": "PyTorch", 
    "Spacy": "spaCy" 
    }

def load_skills():
    df = pd.read_csv("data/skills.csv")

    skills = df["Skill"].tolist()
    skills = [
        skill
        for skill in skills
        if isinstance(skill, str)
        ]
    skills = [skill.strip() for skill in skills]
    skills = [ 
        SPECIAL_SKILLS.get(skill.title(), skill.title()) 
        for skill in skills 
        ]
    # A set automatically removes duplicates
    skills = list(set(skills))
    skills = sorted(skills)
    return skills

# EXTRACT SKILLS
def extract_skills(resume_text):
    """ Extract technical skills from resume text. """
    if not resume_text: 
        return []
    skills_database = load_skills()
    clean_resume = resume_text.strip()
    clean_resume = clean_resume.lower()
    clean_resume = " ".join(clean_resume.split())
    matched_skills = []
    for skill in skills_database:
      clean_skill = skill.strip()
      clean_skill_lower = clean_skill.lower()
      if clean_skill_lower in clean_resume:
          matched_skills.append(skill)
    matched_skills = list(set(matched_skills))
    matched_skills = sorted(matched_skills)
    return matched_skills