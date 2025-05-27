# 🤖 Reverse Job AI – Smart Resume Analyzer

A Streamlit web app that uses Google's Gemini AI to analyze resumes and suggest relevant job roles and required skills. Upload your resume and discover job roles that suit your profile!

## 🚀 Features

- 🔍 Upload your PDF resume and get real-time AI analysis  
- 🧠 Powered by Google's Generative AI (Gemini)  
- 📝 Get suggested job roles and identify skill gaps  
- ⚡ Fast, intuitive, and user-friendly interface  
- ☁️ Deployed live via Streamlit Cloud  

## 📸 Live Demo

Try it here:  
👉 [https://hackathon-project-zrrgjnqfe9fjgxplafn84r.streamlit.app/](https://hackathon-project-zrrgjnqfe9fjgxplafn84r.streamlit.app/)

## 🛠️ Installation

Clone the repo and set up your environment:

```bash
git clone https://github.com/Pedri-8/Hackathon-Project.git
cd Hackathon-Project/Streamlit
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Unix/macOS

pip install -r requirements.txt
````

## 🔐 Configuration

Create a `.streamlit/secrets.toml` file with your Gemini API key:

```toml
GEMINI_API_KEY = "your_google_generative_ai_api_key"
```

⚠️ **Important:** Do **not** push your `secrets.toml` to GitHub. It should be listed in `.gitignore`.

## 🏃 Run the App Locally

```bash
streamlit run app.py
```

## 📁 Project Structure

```
Hackathon-Project/
└── Streamlit/
    ├── app.py
    ├── requirements.txt
    ├── .gitignore
    └── .streamlit/
        └── secrets.toml
```

## 🧠 Built With

* [Streamlit](https://streamlit.io/)
* [Google Generative AI (Gemini)](https://ai.google.dev/)
* [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) – for PDF parsing

## 👤 Author

Made with ❤️ by [Pedri-8](https://github.com/Pedri-8)

---

Feel free to fork the repo or contribute!

```

---

Let me know if you want to add badges (build status, license, etc.), contribution guidelines, or a feature roadmap!
```
