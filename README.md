# ai-resume-screener
# 🧠 AI Resume Screener

A smart Flask-based web app that compares a candidate's resume with a job description and evaluates how well it matches, based on required skills.

> 🔍 Built using Python, Flask, Scikit-learn, PyPDF2, and TailwindCSS

---

## 🚀 Features

- 📄 Upload your resume (PDF format)
- 🧾 Paste a job description
- 📊 Get a match score (in %)
- ✅ See matched skills
- ❌ See missing skills
- 📈 Progress chart (doughnut graph)
- 🎨 Clean, modern TailwindCSS UI with animations


## 🛠️ Tech Stack

- Python
- Flask
- scikit-learn
- PyPDF2
- HTML/CSS + Tailwind CSS
- Chart.js

---

## 📂 Project Structure


---

AI-Resume-Screener/
├── app.py # Flask application
├── train_model.py # Train TF-IDF + ML model
├── model.pkl # Trained logistic regression model
├── vectorizer.pkl # Trained TF-IDF vectorizer
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Main UI template

## 🧪 How to Run

### 1. Clone this repository:
```bash
git clone https://github.com/your-username/ai-resume-screener.git
cd ai-resume-screener

python -m venv .venv
.venv/Scripts/activate  # For Windows
source .venv/bin/activate  # For Mac/Linux

pip install -r requirements.txt

Train the Model
python train_model.py

Run the app
python app.py

Then go to:https://127.0.0.1:5000/


---

### 📌 How to Add `README.md` to GitHub

1. Save this as a file named `README.md` inside your project folder.
2. Then run these Git commands:

```bash
git add README.md
git commit -m "Added README file"
git push
