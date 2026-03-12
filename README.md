# Personality Prediction Through CV Analysis

This project is a personality prediction system built during my AI internship at SoftGrowTech. It analyzes resumes and CVs to predict traits like openness, conscientiousness, extraversion, agreeableness, and emotional stability.

## How it works
The system uses keywords found in the CV text to identify different traits. It looks at word choices, professional experiences, and accomplishments to determine the personality profile of a candidate.

## Features
- Supports PDF, DOCX, and TXT files.
- Can analyze pasted text directly.
- Provides a personality profile based on keyword frequency.
- Built with a clean Streamlit interface.

## Libraries used
- Streamlit
- PyPDF2
- python-docx
- NLTK

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

Developed as part of the SoftGrowTech AI Internship task.