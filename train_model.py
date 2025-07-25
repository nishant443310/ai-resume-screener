import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample training data
# Replace with real labeled data (text, label)
data = {
    'text': [
        'Looking for a web developer with experience in HTML, CSS, and JavaScript.',
        'Need a backend developer skilled in Python and Django.',
        'ReactJS frontend developer needed with TailwindCSS experience.',
        'Full-stack engineer required: Node.js, React, MongoDB.',
        'We want someone proficient in SQL, API development and Git.',
        'Hiring DevOps with Docker, Linux, and AWS skills.'
    ],
    'label': [0, 1, 0, 1, 0, 1]  # Example binary classification
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1, 2),
    max_df=0.85,
    min_df=2
)

X = vectorizer.fit_transform(df['text'])
y = df['label']

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model and vectorizer saved successfully.")
