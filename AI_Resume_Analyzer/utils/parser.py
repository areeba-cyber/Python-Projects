import re
import fitz
import spacy
from docx import Document

# This loads the English NLP model only once when the application starts.
nlp = spacy.load("en_core_web_sm")

# Create a PDF Extraction Function
def extract_pdf_text(pdf_file):

    text = ""

    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text

# Create a DOCX Extraction Function
def extract_docx_text(docx_file):

    document = Document(docx_file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text

# CREATE ONE COMMON FUNCTION
def extract_resume_text(uploaded_file):

    if uploaded_file.type == "application/pdf":

        return extract_pdf_text(uploaded_file)

    elif uploaded_file.type in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]:

        return extract_docx_text(uploaded_file)

    else:

        return None

# EXTRACT NAME
def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Ignore headings
        if line.upper() in [
            "CONTACT",
            "SKILLS",
            "EDUCATION",
            "EXPERIENCE",
            "PROJECTS",
            "SUMMARY"
        ]:
            continue

        # First valid line is the candidate's name
        return line.title()

    return "Name not found"

# EXTRACT EMAIL
def extract_email(text): 
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}" 
    match = re.search(pattern, text) 
    if match: 
        return match.group() 
    return "Email not found"