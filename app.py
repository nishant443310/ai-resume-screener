from flask import Flask, render_template, request
import PyPDF2
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text() or ''
    return text

def extract_skills(text):
    keywords = [
        'python', 'django', 'flask', 'html', 'css', 'javascript', 'js',
        'react', 'reactjs', 'react.js',
        'node', 'nodejs', 'node.js',
        'mysql', 'mongodb', 'firebase',
        'git', 'github', 'api', 'rest api',
        'sql', 'java', 'c++', 'c plus plus',
        'aws', 'docker', 'linux', 'tailwind', 'tailwindcss', 'scss'
    ]
    text = text.lower()
    return [kw for kw in keywords if kw in text]

@app.route('/', methods=['GET', 'POST'])
def index():
    match_score = None
    matched_skills = []
    missing_skills = []

    if request.method == 'POST':
        if 'resume' not in request.files or request.files['resume'].filename == '':
            return render_template('index.html', score="No file selected.")

        resume_file = request.files['resume']
        job_description = request.form['job_description']

        resume_text = extract_text_from_pdf(resume_file)

        combined = [resume_text, job_description]
        vectors = vectorizer.transform(combined)
        similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        match_score = round(similarity * 100, 2)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        matched_skills = list(set(resume_skills) & set(jd_skills))
        missing_skills = list(set(jd_skills) - set(resume_skills))

    return render_template('index.html',
                           score=match_score,
                           matched_skills=matched_skills,
                           missing_skills=missing_skills)

if __name__ == '__main__':
    app.run(debug=True)
