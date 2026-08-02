import streamlit as st


def load_css():

    with open("css/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

load_css()


with st.sidebar:

    st.title("📄 Resume Analyzer")

    st.markdown("---")

    st.write("🏠 Home")

    st.write("📤 Upload Resume")

    st.write("📊 Dashboard")

    st.write("📈 Reports")

    st.write("⚙ Settings")

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)