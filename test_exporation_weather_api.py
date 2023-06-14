import requests

endpoint = "https://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid=203cf013d30ea88b5ba564107972880b"

def test_external_api():
    url = endpoint

    response = requests.get(url)

    assert response.status_code == 200, 'Odpowiedź API nie ma statusu kodu 200'

    # if 401: https://openweathermap.org/faq#error401