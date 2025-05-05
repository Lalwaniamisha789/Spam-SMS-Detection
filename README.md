
# Spam SMS Detection

## 📝 Project Overview
This is a simple web application built with Flask that classifies user-entered text messages into **Spam** or **Ham** (not spam) using a Logistic Regression model. It employs NLTK for text preprocessing (tokenization, stop-word removal, stemming) and scikit-learn's TF-IDF vectorizer for feature extraction.

---

## 🎯 Objectives
1. Provide a user-friendly web interface for entering SMS text.  
2. Preprocess raw text (lowercasing, punctuation removal, stop-word filtering, stemming).  
3. Transform text into TF-IDF features.  
4. Predict Spam vs. Ham using a pretrained Logistic Regression model.  
5. Display the classification result on the same page.

---

## 📁 Repository Structure
```
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── logistic_regression_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
```

- **app.py**: Main Flask application script.  
- **templates/index.html**: Jinja2 template for the UI.  
- **static/styles.css**: Styling for the web interface.  
- **logistic_regression_model.pkl**: Serialized Logistic Regression model.  
- **tfidf_vectorizer.pkl**: Serialized TF-IDF vectorizer.  
- **requirements.txt**: Python dependencies.  
- **README.md**: Project documentation.

---

## 🚀 Getting Started
Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/your-username/spam-sms-detection.git
cd spam-sms-detection
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download NLTK data
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### 5. Run the Flask app
```bash
python app.py
```

### 6. Access the app
Open your browser and navigate to: `http://127.0.0.1:5000`

---

## ⚙️ Usage
1. Enter any SMS text message in the input box.  
2. Click **Predict**.  
3. View the result (Spam or Ham) displayed below the form.

---

## 🛠️ Customization & Deployment
- **Model Updates**: Retrain your model and vectorizer, then replace the `.pkl` files in the project root.  
- **UI Tweaks**: Modify `templates/index.html` and `static/styles.css` for a different look.  
- **Production Server**: Use **gunicorn** or **uwsgi** behind Nginx for deployment.  
- **Docker**: Add a `Dockerfile` and `docker-compose.yml` to containerize the app.

---

## 📜 License
This project is released under the [MIT License](LICENSE).

---

## 👤 Author
**Jaideep Jaiswal**  
B.Tech  
Contact: jaideepj2004@gmail.com  

> 🚀 This repository is public and open-source — feel free to fork, clone, and contribute!
```

