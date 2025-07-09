# 📰 Fake News Detection System with ML & NLP 🧠

An advanced Chrome Extension + FastAPI-based tool that detects fake news in real-time using **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques.

> Uses TF-IDF + Ensemble Classifier (LogisticRegression + LinearSVC + RandomForest)  
> 🚀 Accuracy: ~95–96% | ⚙️ Works in browser + backend | 🔍 NLP-powered predictions

---

## 🚀 Features

- **NLP Preprocessing**: stopword removal, cleaning, n-grams
- **TF-IDF Vectorization**: for numerical transformation of text
- **Ensemble ML Model**:
  - Logistic Regression
  - LinearSVC
  - Random Forest (VotingClassifier)
- **Contextual override rules** to improve accuracy
- ✅ Chrome Extension UI with emoji-based results
- 🔐 Secure prediction via local FastAPI backend
- 🧪 Real-world test support (URL + content classification)

---

## 📁 Folder Structure

```
fake_news_detector/
├── models/
│   └── advanced.pkl
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── predict.py
├── main.py
├── popup.html
├── popup.js
├── manifest.json
└── README.md
```

---

## 🧠 Model Overview

| Component        | Description                             |
|------------------|-----------------------------------------|
| Preprocessing    | Clean + tokenize + TF-IDF (1–3 grams)   |
| Feature Selection| Top 10k terms via Chi²                  |
| Classifier       | VotingClassifier (LogReg, SVC, RF)      |
| Context Logic    | Rewrites "legislation"-related cases    |

---

## 🔍 Example 1: Real News
```
Title: Indian state Karnataka proposes jail terms for spreading 'fake news'
Body: Karnataka proposes jail time for misinformation under a new bill...
```

✅ Output:
```
✔️ REAL (Legislation News)
```

---

## 🚨 Example 2: Fake News
```
Title: NASA confirms alien base on Mars
Body: A leaked report claims NASA found structures on Mars resembling alien outposts...
```

❌ Output:
```
❌ FAKE
```

---

## 📸 Demo Screenshot

![demo](https://github.com/user/screenshots/fake-news-extension-demo.png)

---

## ⚙️ How to Run

### 1. Clone and Setup
```bash
git clone https://github.com/<your-username>/fake_news_detector.git
cd fake_news_detector
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Train the Model (Optional)
```bash
python src/train_model.py
```

### 4. Run the API Server
```bash
python main.py
```

### 5. Load the Chrome Extension
- Go to `chrome://extensions/`
- Enable **Developer mode**
- Click **Load Unpacked** → select project folder
- Click the extension icon to test

---

## 🧪 Test Dataset Sources

| Dataset             | Description                       |
|---------------------|-----------------------------------|
| Kaggle Fake News    | Real vs Fake headlines + bodies   |
| Custom Examples     | From Reuters, WPost, Snopes, etc. |

---

## 🌐 API Structure

| Route     | Method | Description                       |
|-----------|--------|-----------------------------------|
| `/`       | GET    | Welcome route                     |
| `/predict`| POST   | Returns real/fake label           |

> Example request:
```json
POST /predict
{
  "title": "Fake claim about USAID paying celebrities",
  "body": "Russia-linked fake news claims..."
}
```

---

## 🛠 Future Enhancements

- Upgrade to DistilBERT model
- Highlight suspicious words/phrases
- Auto-categorize as satire / deepfake / disinfo
- Save results in history

---

## 🙌 Credits

- FastAPI  
- Scikit-learn  
- NLTK  
- TF-IDF  
- Reuters & WPost data for examples  

---

## 👩‍💻 Author

**Spandana Gunaganti**  
Built with ❤️ to improve media literacy