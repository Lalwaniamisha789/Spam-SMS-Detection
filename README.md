# Spam SMS Detection

A simple web app built with Flask that classifies SMS messages as **Spam** or **Ham** using a Logistic Regression model. The model uses **NLTK** for preprocessing and **TF-IDF** features via **scikit-learn**.

## Features
- Clean web interface to input SMS text
- Preprocessing: tokenization, stop-word removal, stemming
- TF-IDF-based feature extraction
- Logistic Regression for prediction
- Instant spam/ham classification result

## Run Locally
```bash
git clone https://github.com/your-username/spam-sms-detection.git
cd spam-sms-detection
python3 -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
python app.py
```

## Visit: http://127.0.0.1:5000

This repository is public and open-source — feel free to fork, clone, and contribute!
