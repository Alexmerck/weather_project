import requests


def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "386ffb17bbaf4f5f903132930210412",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False


if __name__ == "__main__":
    weather = weather_by_city("Moscow,Russia")
    img = weather['weatherIconUrl'][0]['value']
    print(weather)
    print(f"Сейчас {weather['temp_C']},ощущается как {weather['FeelsLikeC']}")
    print(img)
