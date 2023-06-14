import requests
import json

endpoint = "https://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid=203cf013d30ea88b5ba564107972880b"

def test_external_api():
    url = endpoint

    response = requests.get(url)

    assert response.status_code == 200, 'Odpowiedź API nie ma statusu kodu 200'

def test_external_response_keys():
    url = endpoint
    sample_data = {'coord': {'lon': 21.0118, 'lat': 52.2298}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 289.58, 'feels_like': 289.37, 'temp_min': 286.7, 'temp_max': 291.43, 'pressure': 1016, 'humidity': 80}, 'visibility': 10000, 'wind': {'speed': 2.06, 'deg': 80}, 'clouds': {'all': 0}, 'dt': 1686730043, 'sys': {'type': 2, 'id': 2032856, 'country': 'PL', 'sunrise': 1686708862, 'sunset': 1686769081}, 'timezone': 7200, 'id': 756135, 'name': 'Warsaw', 'cod': 200}
    sample_keys = sample_data.keys()
    response = requests.get(url)
    data = json.loads(response.text)

    assert sample_keys == data.keys(), 'Odpowiedź API ma inne klucze niż przykładowe dane'