from fastapi import FastAPI
from pydantic import BaseModel
import requests

# Инициализация приложения
app = FastAPI()

API_URL = "https://instagram-scraper-stable.p.rapidapi.com"  # Скоро настроим запросы
API_KEY = "9b15ec699cmsh935c97a62055bb9p19fb96jsn31d011a36e75"  # Вставьте сюда ключ API

# Модель данных для запроса пользователя
class InstagramRequest(BaseModel):
    username: str

# Маршрут проверки подписки
@app.post("/check_subscription")
def check_subscription(request: InstagramRequest):
    url = f"{API_URL}/followers"  # Заменим позже на реальный эндпоинт

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "instagram-scraper-stable.p.rapidapi.com"
    }
    
    params = {"username": request.username}

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return {"success": True, "data": response.json()}
    else:
        return {"success": False, "error": response.text}
