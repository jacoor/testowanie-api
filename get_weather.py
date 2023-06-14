import requests
import json


def get_weather(api_key, city):
    # Tworzenie URL zapytania API dla podanego miasta
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    # https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    # Wykonanie zapytania API
    response = requests.get(url)
    # Sprawdzenie poprawności odpowiedzi
    if response.status_code == 200:
        # Konwersja odpowiedzi na format JSON
        data = json.loads(response.text)
        
        # Pobranie danych pogodowych
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']

        # Zwrócenie danych pogodowych
        return temperature, humidity, pressure, description
    else:
        # Zwrócenie pustych danych w przypadku błędu
        return None, None, None, None