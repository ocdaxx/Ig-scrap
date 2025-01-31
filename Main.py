import requests

API_URL = "https://instagram-scraper-stable.p.rapidapi.com"  # Заменим на конкретный эндпоинт позже
API_KEY = "import requests

API_URL = "https://instagram-scraper-stable.p.rapidapi.com"  # Заменим на конкретный эндпоинт позже
API_KEY = "9b15ec699cmsh935c97a62055bb9p19fb96jsn31d011a36e75"  # Вставь ключ API сюда

def test_api():
    # Заменим этот вызов реальным эндпоинтом позже
    url = f"{API_URL}/test-endpoint"
    
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "instagram-scraper-stable.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Успешное подключение к API")
    else:
        print("Ошибка подключения:", response.status_code, response.text)

if __name__ == "__main__":
    test_api()"  # Вставь ключ API сюда

def test_api():
    # Заменим этот вызов реальным эндпоинтом позже
    url = f"{API_URL}/test-endpoint"
    
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "instagram-scraper-stable.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Успешное подключение к API")
    else:
        print("Ошибка подключения:", response.status_code, response.text)

if __name__ == "__main__":
    test_api()
