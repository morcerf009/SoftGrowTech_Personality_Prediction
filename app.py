import streamlit as st
import nltk
from PyPDF2 import PdfReader
from docx import Document
import io

# Basic page setup
st.set_page_config(page_title="Personality Prediction Through CV Analysis")

nltk.download('punkt', quiet=True)

def extract_text_from_pdf(file_bytes):
    pdf = PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file_bytes):
    doc = Document(io.BytesIO(file_bytes))
    return "\n".join([para.text for para in doc.paragraphs])

# Title and description
st.title("Personality Prediction Through CV Analysis")
st.write("This project uses keyword analysis to look at a resume or CV and predict personality traits. It looks at word choice and experiences to map them to traits like openness, conscientiousness, extraversion, agreeableness, and emotional stability.")
st.write("This helps in making decisions during the hiring process by seeing how well a candidate might fit a role.")

st.markdown("---")

# File upload and text input
col1, col2 = st.columns(2)

with col1:
    st.subheader("Upload CV")
    uploaded_file = st.file_uploader("Upload your resume (PDF, DOCX, or TXT)", type=["txt", "pdf", "docx"])

with col2:
    st.subheader("Paste Text")
    text_input = st.text_area("Or copy and paste resume content here", height=150)

cv_text = ""
if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()
    file_bytes = uploaded_file.read()
    if file_type == 'txt':
        cv_text = file_bytes.decode("utf-8")
    elif file_type == 'pdf':
        cv_text = extract_text_from_pdf(file_bytes)
    elif file_type == 'docx':
        cv_text = extract_text_from_docx(file_bytes)
elif text_input:
    cv_text = text_input

if st.button("Analyze Personality Traits", use_container_width=True):
    if not cv_text.strip():
        st.error("Please provide some text to analyze.")
    else:
        # Dictionary of traits and associated keywords
        traits = {
            "Openness": ["creative", "innovation", "curious", "imagination", "learning", "adaptive", "explore", "open", "new ideas"],
            "Conscientiousness": ["organized", "responsible", "hardworking", "punctual", "detail", "structured", "diligent", "reliable", "efficient"],
            "Extraversion": ["leadership", "communication", "teamwork", "social", "outgoing", "speaker", "collaborative", "network", "public speaking"],
            "Agreeableness": ["helpful", "kind", "cooperative", "supportive", "empathy", "patience", "mentoring", "team-player", "compassionate"],
            "Emotional Stability": ["calm", "stress management", "pressure", "resilient", "balanced", "stable", "emotionally", "composure"]
        }

        results = {}
        for trait, keywords in traits.items():
            score = 0
            for word in keywords:
                if word.lower() in cv_text.lower():
                    score += 1
            results[trait] = score

        st.markdown("---")
        st.subheader("Predicted Personality Profile")
        
        # Display results
        for trait, score in results.items():
            if score >= 3:
                level = "High"
            elif score >= 1:
                level = "Medium"
            else:
                level = "Low"
            st.write(f"**{trait}**: {level} (Score: {score})")

st.markdown("---")
st.caption("Developed for SoftGrowTech AI Internship.")