# 📰 Fake News Detection System with ML & NLP 

An advanced Chrome Extension + FastAPI-based tool that detects fake news in real-time using **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques.

> Uses TF-IDF + Ensemble Classifier (LogisticRegression + LinearSVC + RandomForest)  
> Accuracy: ~95–96% | ⚙️ Works in browser + backend |  NLP-powered predictions

---

## Features

- **NLP Preprocessing**: stopword removal, cleaning, n-grams
- **TF-IDF Vectorization**: for numerical transformation of text
- **Ensemble ML Model**:
  - Logistic Regression
  - LinearSVC
  - Random Forest (VotingClassifier)
- **Contextual override rules** to improve accuracy
- Chrome Extension UI with emoji-based results
- Secure prediction via local FastAPI backend
- Real-world test support (URL + content classification)

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

## Model Overview

| Component        | Description                             |
|------------------|-----------------------------------------|
| Preprocessing    | Clean + tokenize + TF-IDF (1–3 grams)   |
| Feature Selection| Top 10k terms via Chi²                  |
| Classifier       | VotingClassifier (LogReg, SVC, RF)      |
| Context Logic    | Rewrites "legislation"-related cases    |

---

## Example 1: Real News
```
Title: Tata Motors to invest up to $4 billion over 5 years for EVs, new cars
Body: In June 2025, Tata Motors outlined a bold plan: ₹32,000 crore (~$4 billion) over five years toward electric vehicle R&D and production, marking a push toward sustainable transport innovation.....
Source: Reuters 
```

✅ Output:
```
✔️ REAL (Legislation News)
```

---

## 🚨 Example 2: Fake News
```
Title: Operation Sindoor military attack claims
Body: During May 2025 tensions, videos of airstrikes, drone strikes, and explosions (including video game footage) were shared as real events in “Operation Sindoor.” PIB and NDTV quickly labelled them false.....
Source: NDTV/PIB
```

❌ Output:
```
❌ FAKE
```

---

## 📸 Demo Screenshots
![Screenshot 2025-07-09 005058](https://github.com/user-attachments/assets/00abf6e4-cb5d-4a22-abea-bdb6daadc848)
![Screenshot 2025-07-09 004949](https://github.com/user-attachments/assets/bb1171df-6569-48a3-aaf9-4d171fb16dcf)
![Screenshot 2025-07-09 004828](https://github.com/user-attachments/assets/1a9ac454-5286-427e-a371-336525615f47)

---

## How to Run

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

## Test Dataset Sources

| Dataset             | Description                       |
|---------------------|-----------------------------------|
| Kaggle Fake News    | Real vs Fake headlines + bodies   |
| Custom Examples     | From Reuters, WPost, Snopes, etc. |

---

## API Structure

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

## Future Enhancements

- Upgrade to DistilBERT model
- Highlight suspicious words/phrases
- Auto-categorize as satire / deepfake / disinfo
- Save results in history

---

## Credits

- FastAPI  
- Scikit-learn  
- NLTK  
- TF-IDF  
- Reuters & WPost data for examples  

---

## 👩‍💻 Author
**Spandana Gunaganti**  
