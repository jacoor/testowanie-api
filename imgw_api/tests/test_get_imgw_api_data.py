import pandas as pd
import requests
from pytest import mark


@mark.imgw
@mark.exploration_tests
def test_get_all_current_data(fake_weather):
    fake_keys = pd.DataFrame(fake_weather).keys()

    response = requests.get(
        "https://danepubliczne.imgw.pl/api/data/synop"
    ).json()
    response_keys = pd.DataFrame(response).keys()

    assert list(response_keys) == list(fake_keys)
    assert len(response) == len(fake_weather)


@mark.imgw
@mark.exploration_tests
def test_get_current_weather_data_by_station_id(fake_jelenia_weather):
    response = requests.get(
        "https://danepubliczne.imgw.pl/api/data/synop/id/12500"
    ).json()

    assert response.get("stacja") == fake_jelenia_weather.get("stacja")


@mark.imgw
@mark.exploration_tests
def test_get_current_weather__data_by_bad_station_id():
    response = requests.get(
        "https://danepubliczne.imgw.pl/api/data/synop/id/125e00"
    ).json()

    assert response.get("status") is False


@mark.imgw
@mark.exploration_tests
def test_get_current_weather_data_by_name(fake_jelenia_weather):
    response = requests.get(
        f"https://danepubliczne.imgw.pl/api/data/synop/station/jeleniagora"
    ).json()

    assert response.get("stacja") == fake_jelenia_weather.get("stacja")
