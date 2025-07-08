import joblib
from preprocessing import clean_text

CONTEXT_KW = ['bill', 'law', 'legislation', 'draft', 'proposes', 'government', 'minister', 'act', 'prohibition', 'jail']

def predict(text, title=""):
    obj = joblib.load("models/advanced.pkl")
    vec, sel, model = obj["vec"], obj["sel"], obj["model"]

    cleaned = clean_text(text)
    x = vec.transform([cleaned])
    xs = sel.transform(x)
    pred = model.predict(xs)[0]

    if pred == 'FAKE' and any(w in title.lower() for w in CONTEXT_KW):
        return 'REAL (Legislation news)'
    return pred
