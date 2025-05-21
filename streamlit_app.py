import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Load model and vectorizer
model = joblib.load('logistic_regression_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    ps = PorterStemmer()
    words = [ps.stem(word) for word in words]
    return ' '.join(words)

# Streamlit app
st.title("📱 Spam SMS Detection")
text_input = st.text_area("Enter an SMS message:")

if st.button("Predict"):
    if text_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        processed = preprocess_text(text_input)
        vectorized = tfidf_vectorizer.transform([processed])
        prediction = model.predict(vectorized)
        label = "Spam" if prediction[0] == 1 else "Not Spam"
        st.success(f"Prediction: {label}")
