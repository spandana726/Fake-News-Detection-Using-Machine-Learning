import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
_stop = set(stopwords.words('english'))

def clean_text(text):
    t = re.sub(r"http\S+|www\S+", " ", str(text).lower())
    t = re.sub(r"[^a-z\s]", " ", t)
    return " ".join(w for w in t.split() if w not in _stop)

def get_vectorizer():
    return TfidfVectorizer(ngram_range=(1,3), max_df=0.75, min_df=5)
