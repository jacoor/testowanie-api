import pytest
from imgw_api.sample_data.fake_data import weather_data


@pytest.fixture
def fake_weather():

    return weather_data
