from utils.parser import ( 
    extract_resume_text, 
    extract_name,
    extract_email
    )
import streamlit as st
from utils.parser import extract_resume_text

# LOAD CSS
def load_css():

    with open("css/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

load_css()

# CREATE SIDE BAR
with st.sidebar:

    st.title("📄 Resume Analyzer")

    st.markdown("----")

    st.write("🏠 Home")

    st.write("📤 Upload Resume")

    st.write("📊 Dashboard")

    st.write("📈 Reports")

    st.write("⚙ Settings")

# HERO SECTION (HEADING)
st.markdown(
"""
<div class="hero-title">
AI Resume Analyzer
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="hero-subtitle">
Analyze your resume with AI and improve your chances of getting hired.
</div>
""",
unsafe_allow_html=True
)

# ADD SPACE
st.write("")
st.write("")

# CREATE TWO COLUMNS
left, right = st.columns([2,1])

# LEFT CARD (COLUMN)
with left:
    st.markdown(
"""
<div class="glass-card">

<h2>Upload Your Resume</h2>

<p>Supports PDF and DOCX files.</p>

</div>
""",
unsafe_allow_html=True
)
uploaded_file = st.file_uploader(
    "Choose Resume",
    type=["pdf", "docx"]
)

resume_text = ""

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")
    st.write("### File Details")

    st.write("Filename:", uploaded_file.name)
    st.write("File Type:", uploaded_file.type)
    st.write("File Size:", uploaded_file.size, "bytes")

    # Extract text only after a file is uploaded
    resume_text = extract_resume_text(uploaded_file)
    name = extract_name(resume_text)
    email = extract_email(resume_text)
    if resume_text:
        st.subheader("Candidate Information")
        st.write("👤 Name:", name)
        st.write("📧 Email:", email)
        st.divider()
        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume",
            resume_text,
            height=400
        )
    else:
        st.error("Unable to read this file.")
# RIGHT COLUMN
with right:

    st.markdown(
"""
<div class="glass-card">

<h2>Quick Stats</h2>

<p>ATS Score</p>

<h1>0%</h1>

</div>
""",
unsafe_allow_html=True
)

# STATISTIC ROW
col1,col2,col3,col4 = st.columns(4)
with col1:
    st.metric(
    "Skills",
    "0"
)
with col2:
    st.metric(
    "Experience",
    "0 Years"
)
with col3:
    st.metric(
    "Projects",
    "0"
)
with col4:
    st.metric(
    "ATS",
    "0%"
)

# FEATURES SECTION
st.markdown("## Features")
c1,c2,c3 = st.columns(3)
with c1:
    st.info("🤖 AI Resume Analysis")
with c2:
    st.info("📊 ATS Score")
with c3:
    st.info("🎯 Skill Matching")

# FOOTER
st.markdown("---")

st.caption(
"Built with ❤️ using Python and Streamlit"
)



st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)