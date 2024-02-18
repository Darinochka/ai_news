# Сервер для предсказания новостей.
## Как запустить?
```
docker compose up
```

Сервер запустится на порту 4444 по умолчанию. Его можно сменить в docker-compose.yml

## config
В папку app/config необходимо добавить чекпоинт модели:
https://drive.google.com/file/d/1o3-PXy_Av7RI919XaWKRgReC44JvrVlJ/view?usp=drive_link

## Пример использования
```
curl -H "Content-Type: application/json" -X POST -d '{"text_news": ["Вооруженные отряды из проправительственной восточнотиморской милиции  устроили сего","Вооруженные отряды из проправительственной восточнотиморской милиции  устроили сего"]}' http://localhost:4444/predict
```

## Пример результата
{"tags":["__label__entertainment","__label__entertainment"]}
