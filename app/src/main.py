import fasttext
import config
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

classificator_model_ru = config.classificator_model_ru
model = fasttext.load_model(classificator_model_ru)

app = FastAPI()

TOPICS = {
    "business_ec": "Бизнес и экономика",
    "entertainment": "Культура и развлечения",
    "politics": "Политика",
    "science_tech": "Наука и технологии",
    "social": "Люди и общество",
    "sport": "Спорт",
    "travel": "Путешествия"
}

class News(BaseModel):
    text_news: List[str]

class TagPrediction(BaseModel):
    tags: List[str]

@app.post("/predict", response_model=TagPrediction)
def predict_news(news: News):
    """"""
    preds = model.predict(news.text_news)
    return {"tags": [TOPICS[p[0][9:]] for p in preds[0]]}

