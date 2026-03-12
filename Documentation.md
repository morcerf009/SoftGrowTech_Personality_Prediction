# Project Documentation: Personality Prediction Through CV Analysis

## 1. Introduction
This project is an automated personality prediction system designed to analyze resumes and CVs. By using keyword matching and linguistic analysis, the system predicts a candidate's placement within the "Big Five" personality traits: Openness, Conscientiousness, Extraversion, Agreeableness, and Emotional Stability.

## 2. Objective
The primary goal is to provide recruiters with a data-driven tool to assist in the hiring process. The system helps identify candidates whose professional experiences and communication styles align with specific company cultures or role requirements.

## 3. Key Features
- **Multi-Format Parsing:** Support for PDF, DOCX, and TXT files using specialized libraries (PyPDF2, python-docx).
- **Linguistic Keyword Mapping India:** A dictionary-based approach mapping professional terminology to psychological traits.
- **Interactive Dashboard:** A clean, user-friendly interface built with Streamlit for real-time analysis.
- **Instant Profiling:** High-speed processing of text data to provide immediate personality snapshots.

## 4. Methodology
The system follows a three-step process:
1. **Data Extraction:** Content is parsed from the uploaded document or text input.
2. **Trait Scoring:** The software searches for predefined keywords associated with each of the Big Five traits within the extracted text.
3. **Weighting and Classification:** Scores are calculated based on keyword frequency, determining if a candidate ranks High, Medium, or Low for each trait.

## 5. Technology Stack
- **Programming Language:** Python
- **UI Framework:** Streamlit
- **Document Processing:** PyPDF2 (PDF), python-docx (DOCX)
- **Natural Language Toolkit:** NLTK (Text normalization)

## 6. Setup and Installation
1. Clone the repository.
2. Install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python -m streamlit run app.py
   ```

## 7. Conclusion
This tool demonstrates the application of linguistic analysis in HR technology, offering a scalable solution for early-stage candidate screening.

---
**Developed by:** [Your Name]  
**Internship:** SoftGrowTech AI Internship Task
