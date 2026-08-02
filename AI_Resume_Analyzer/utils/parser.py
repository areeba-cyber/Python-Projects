import fitz
from docx import Document

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