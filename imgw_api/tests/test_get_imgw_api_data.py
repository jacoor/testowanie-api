import requests
import requests_mock
from pytest import mark

import pandas as pd

from imgw_api.get_imgw_data import WeatherImgw


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


@mark.imgw
@mark.requestsmock
def test_get_all_current_data_df_mock(fake_weather):
    with requests_mock.Mocker() as mocker:
        mocker.get(WeatherImgw.URL, json=fake_weather)

        result = WeatherImgw.get_all_current_data()
        assert isinstance(result, pd.DataFrame)


@mark.imgw
@mark.requestsmock
def test_get_all_current_data_no_data_mock():
    with requests_mock.Mocker() as mocker:
        mocker.get(WeatherImgw.URL, json=[])

        result = WeatherImgw.get_all_current_data()
        assert isinstance(result, str)
        assert result == "The newest data didn't come yet. " \
                         "Wait 5 min and try again"


@mark.imgw
@mark.requestsmock
def test_get_all_current_data_len_mock(fake_weather):
    with requests_mock.Mocker() as mocker:
        mocker.get(WeatherImgw.URL, json=fake_weather)

        result = WeatherImgw.get_all_current_data()
        assert len(result) == len(fake_weather)


@mark.imgw
@mark.requestsmock
def test_get_all_current_data_values_mock(fake_weather):
    with requests_mock.Mocker() as mocker:
        mocker.get(WeatherImgw.URL, json=fake_weather)

        result = WeatherImgw.get_all_current_data()
        for i, row in result.iterrows():
            assert row["id_stacji"] == fake_weather[i]["id_stacji"]
            assert row["temperatura"] == fake_weather[i]["temperatura"]


@mark.imgw
@mark.requestsmock
def test_get_get_current_weather_data_series_by_station_id(
        requests_mock,
        fake_jelenia_weather
):
    station_id = 12501
    requests_mock.get(
        f"{WeatherImgw.URL}/id/{station_id}",
        json=fake_jelenia_weather
    )

    result = WeatherImgw.get_current_weather_data_by_station_id(station_id)
    assert isinstance(result, pd.Series)


@mark.imgw
@mark.requestsmock
def test_get_get_current_weather_data_len_by_station_id(
        requests_mock,
        fake_jelenia_weather
):
    station_id = 12501
    requests_mock.get(
        f"{WeatherImgw.URL}/id/{station_id}",
        json=fake_jelenia_weather
    )

    result = WeatherImgw.get_current_weather_data_by_station_id(station_id)

    assert len(result) == len(fake_jelenia_weather)


@mark.imgw
@mark.requestsmock
def test_get_get_current_weather_data_values_by_station_id(
        requests_mock,
        fake_jelenia_weather
):
    station_id = 12501
    requests_mock.get(
        f"{WeatherImgw.URL}/id/{station_id}",
        json=fake_jelenia_weather
    )

    result = WeatherImgw.get_current_weather_data_by_station_id(station_id)

    assert result["id_stacji"] == fake_jelenia_weather["id_stacji"]
    assert result["temperatura"] == fake_jelenia_weather["temperatura"]


@mark.imgw
@mark.requestsmock_tdd
def test_get_all_current_data_html(requests_mock, fake_weather):
    requests_mock.get(
        f"{WeatherImgw.URL}/format/html",
        json=fake_weather
    )

    result = WeatherImgw.get_all_current_data_html()

    assert isinstance(result, str)
