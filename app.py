from flask import Flask, request, render_template
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('logistic_regression_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Preprocessing function
def preprocess_text(text):
    # Convert to lower case
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    # Apply stemming
    ps = PorterStemmer()
    words = [ps.stem(word) for word in words]
    # Join words back to a single string
    return ' '.join(words)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        processed_text = preprocess_text(text)
        vectorized_text = tfidf_vectorizer.transform([processed_text])
        prediction = model.predict(vectorized_text)
        if (prediction == 1): 
            prediction = "Spam"
        else : 
            prediction = "Ham"
        return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
