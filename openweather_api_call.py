from get_weather import get_weather

def main():
    # Wprowadzenie klucza API OpenWeatherMap
    api_key = '203cf013d30ea88b5ba564107972880b'

    # Wprowadzenie nazwy miasta
    city = 'Warsaw'

    # Pobranie danych pogodowych
    temperature, humidity, pressure, description = get_weather(api_key, city)

    # Wyświetlenie danych pogodowych
    if temperature is not None:
        print('Pogoda w', city + ':')
        print('Temperatura:', temperature, 'K')
        print('Wilgotność:', humidity, '%')
        print('Ciśnienie:', pressure, 'hPa')
        print('Opis:', description)
    else:
        print('Błąd podczas pobierania danych pogodowych.')

if __name__ == '__main__':
    main()
