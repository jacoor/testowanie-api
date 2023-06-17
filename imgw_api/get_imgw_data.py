import requests
import pandas as pd


def get_all_current_data():
    """
    Get current data of all stations
    :return:
    DataFrame
    """
    response = requests.get(
        "https://danepubliczne.imgw.pl/api/data/synop"
    ).json()

    if response:
        df_data = pd.DataFrame(response)
        return df_data

    return "The newest data didn't come jet. Wait 5 min and try again"


def get_station_current_weather_data(station_id):
    """
    Get weather data by index
    :return:
    DataFrame
    """
    response = requests.get(
        f"https://danepubliczne.imgw.pl/api/data/synop/id/{station_id}"
    ).json()

    if response.get("status"):
        return response.get("message")

    city_df = pd.DataFrame(response, index=[response.get("id_stacji")])
    return city_df


if __name__ == "__main__":
    print(get_all_current_data())
    city = get_station_current_weather_data(12500)
    print(city)