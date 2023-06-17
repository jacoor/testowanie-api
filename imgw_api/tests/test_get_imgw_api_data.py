import pandas as pd
import requests
from pytest import mark


@mark.imgw
def test_get_all_current_data(fake_weather):
    fake_keys = pd.DataFrame(fake_weather).keys()

    response = requests.get(
        "https://danepubliczne.imgw.pl/api/data/synop"
    ).json()
    response_keys = pd.DataFrame(response).keys()

    assert list(response_keys) == list(fake_keys)


@mark.imgw
def test_get_all_current_data_by_number(fake_weather):
    response = requests.get(
        "https://danepubliczne.imgw.pl/api/data/synop"
    ).json()

    assert len(response) == len(fake_weather)


@mark.imgw
def test_get_station_current_weather_data(fake_jelenia_weather):
    response = requests.get(
        "https://danepubliczne.imgw.pl/api/data/synop/id/12500"
    ).json()
    df = pd.DataFrame(response, index=[response.get("id_stacji")])
    station = df.at["12500", "stacja"]

    assert station == fake_jelenia_weather.get("stacja")


@mark.imgw
def test_get_station_current_weather_by_bad_number():
    response = requests.get(
        "https://danepubliczne.imgw.pl/api/data/synop/id/125e00"
    ).json()

    assert response.get("status") is False
