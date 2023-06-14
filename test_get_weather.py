from get_weather import get_weather

# sample_data = {'coord': {'lon': 21.0118, 'lat': 52.2298}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'base': 'stations', 'main': {'temp': 291.05, 'feels_like': 290.7, 'temp_min': 289.62, 'temp_max': 291.92, 'pressure': 1014, 'humidity': 69}, 'visibility': 10000, 'wind': {'speed': 3.6, 'deg': 80}, 'clouds': {'all': 20}, 'dt': 1686764812, 'sys': {'type': 2, 'id': 2032856, 'country': 'PL', 'sunrise': 1686708862, 'sunset': 1686769081}, 'timezone': 7200, 'id': 756135, 'name': 'Warsaw', 'cod': 200}
# TDD
def test_get_weather():
    temperature, humidity, pressure, description = get_weather("testkey", "testcity")
    assert temperature == "289.53 K"
    assert humidity == "81 %"
