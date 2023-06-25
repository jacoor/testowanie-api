import pytest
from imgw_api.sample_data.fake_data import weather_data, jelenia_weather


@pytest.fixture
def fake_weather():

    return weather_data


@pytest.fixture
def fake_jelenia_weather():

    return jelenia_weather