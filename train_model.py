import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, f1_score
from preprocessing import clean_text, get_vectorizer

def train():
    df = pd.read_csv("data/fake_or_real_news.csv")
    df["combined"] = (df["title"].fillna("") + " " + df["text"].fillna("")).apply(clean_text)
    X, y = df["combined"], df["label"]

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    vec = get_vectorizer()
    Xtr_v = vec.fit_transform(Xtr)
    Xte_v = vec.transform(Xte)

    sel = SelectKBest(chi2, k=10000)
    Xtr_s = sel.fit_transform(Xtr_v, ytr)
    Xte_s = sel.transform(Xte_v)

    lr = LogisticRegression(class_weight="balanced", max_iter=1000)
    svc = LinearSVC(class_weight="balanced")
    rf = RandomForestClassifier(n_estimators=200, class_weight="balanced", random_state=42)

    ensemble = VotingClassifier(
        estimators=[("lr", lr), ("svc", svc), ("rf", rf)],
        voting="hard",
        weights=[2, 2, 1]
    )
    ensemble.fit(Xtr_s, ytr)

    ypred = ensemble.predict(Xte_s)

    print("Accuracy:", accuracy_score(yte, ypred))
    print("F1 (FAKE):", f1_score(yte, ypred, pos_label="FAKE"))

    joblib.dump({"vec": vec, "sel": sel, "model": ensemble}, "models/advanced.pkl")
