from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

from train_model import train
from predict import predict

app = FastAPI(title="Fake News Detection API")

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "✅ Fake News Detection API is running! Use POST /predict"}

class NewsRequest(BaseModel):
    title: str
    body: str

@app.post("/predict")
def classify(news: NewsRequest):
    label = predict(news.title + " " + news.body, news.title)
    return {"label": label}

if __name__ == "__main__":
    if not os.path.exists("models/advanced.pkl"):
        print("🔧 Training model for the first time...")
        train()
        print("✅ Model trained and saved at models/advanced.pkl")
    else:
        print("✅ Pretrained model loaded from models/advanced.pkl")

    print("🚀 Starting API at http://localhost:8000 ...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)