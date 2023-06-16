import pandas as pd
import requests
from pytest import mark


@mark.imgw
def test_get_all_current_data(fake_weather):
    fake_keys = pd.DataFrame(fake_weather).keys()

    response = requests.get("https://danepubliczne.imgw.pl/api/data/synop")
    weather_data = response.json()
    response_keys = pd.DataFrame(weather_data).keys()

    assert list(response_keys) == list(fake_keys)


@mark.imgw
def test_get_all_current_data_by_number():
    response = requests.get("https://danepubliczne.imgw.pl/api/data/synop")
    weather_data = response.json()

    number_of_stations = len(weather_data)
    assert number_of_stations == 62
