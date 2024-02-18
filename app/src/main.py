import fasttext
import config
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

classificator_model_ru = config.classificator_model_ru
model = fasttext.load_model(classificator_model_ru)

app = FastAPI()


class News(BaseModel):
    text_news: List[str]

class TagPrediction(BaseModel):
    tags: List[str]

@app.post("/predict", response_model=TagPrediction)
def predict_news(news: News):
    """"""
    preds = model.predict(news.text_news)
    return {"tags": [p[0] for p in preds[0]]}

