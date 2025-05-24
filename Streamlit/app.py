import streamlit as st
import google.generativeai as genai
import fitz  # PyMuPDF

# Streamlit Page Config
st.set_page_config(page_title="Reverse Job Interview AI", page_icon="💼", layout="wide")

# Configure Gemini 2.0 Flash API
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

# PDF Text Extraction
def extract_text_from_pdf(uploaded_pdf):
    text = ""
    with fitz.open(stream=uploaded_pdf.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text.strip()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("💼 Reverse Job Interview AI")
st.write("Empower job seekers with AI-driven insights on employers!")

# PDF Upload
st.subheader("📂 Upload Job Description (PDF)")
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
job_description = ""

if pdf_file:
    try:
        job_description = extract_text_from_pdf(pdf_file)
        st.text_area("📝 Extracted Job Description:", job_description, height=200, disabled=True)
    except Exception as e:
        st.error(f"❌ Error reading PDF: {str(e)}")

# Manual Input
st.subheader("📝 Or Paste Job Description Below")
manual_input = st.text_area("Paste Job Description:", height=200)
if manual_input.strip():
    job_description = manual_input.strip()

# Analyze Button
if st.button("🔍 Analyze Job Description"):
    if job_description:
        with st.spinner("Analyzing..."):
            try:
                prompt = f"""
                Analyze the following job description and provide a text-based summary with insights. 
                Focus on job title, company name, salary transparency, and red flags like unrealistic expectations 
                or toxic culture signs.

                Job Description:
                {job_description}
                """
                response = model.generate_content(prompt)
                ai_analysis = response.text if hasattr(response, "text") else "⚠ No response generated."

                st.subheader("📊 AI Analysis")
                st.write(ai_analysis)
            except Exception as e:
                st.error(f"❌ Error generating AI response: {str(e)}")
    else:
        st.warning("⚠ Please upload or enter a job description first.")

# Chatbot Interaction
st.subheader("🤖 AI Interview Chatbot")
user_input = st.text_input("💬 Ask about salary negotiation, interview tips, or company insights:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    try:
        response = model.generate_content(user_input)
        ai_reply = response.text if hasattr(response, "text") else "⚠ No reply generated."
    except Exception as e:
        ai_reply = f"❌ Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)

# Chat History
st.subheader("📝 Chat History")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])