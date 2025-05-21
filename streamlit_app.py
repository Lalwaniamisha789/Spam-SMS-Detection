import streamlit as st
import pickle
import numpy as np

# Load the trained model and vectorizer
with open('logistic_regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Streamlit app
st.title("Spam SMS Detection")
st.write("Enter an SMS message to check if it's spam or not.")

# Input text
user_input = st.text_area("SMS Message", "")

if st.button("Predict"):
    if user_input:
        # Transform the input using the loaded vectorizer
        transformed_input = vectorizer.transform([user_input])
        # Predict using the loaded model
        prediction = model.predict(transformed_input)
        # Display the result
        result = "Spam" if prediction[0] == 1 else "Not Spam"
        st.success(f"The message is: {result}")
    else:
        st.warning("Please enter a message to classify.")
