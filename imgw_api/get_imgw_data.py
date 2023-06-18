import requests
import pandas as pd
from unidecode import unidecode


class WeatherImgw:
    URL = "https://danepubliczne.imgw.pl/api/data/synop"

    @classmethod
    def get_all_current_data(cls):
        """
        Get current data of all stations
        :return:
        DataFrame
        """
        response = requests.get(cls.URL).json()

        if response:
            df_data = pd.DataFrame(response)
            return df_data

        return "The newest data didn't come jet. Wait 5 min and try again"

    @classmethod
    def get_current_weather_data_by_station_id(cls, station_id):
        """
        Get weather data by index
        :return:
        DataFrame
        """
        response = requests.get(
            f"{cls.URL}/id/{station_id}"
        ).json()

        if not response.get("status"):
            return response.get("message")
        print(response.get("status"))
        city_df = pd.DataFrame(response, index=[response.get("id_stacji")])
        return city_df

    @classmethod
    def get_current_weather_data_by_name(cls, station_name):
        """
        Get weather data by station name
        :return:
        DataFrame
        """
        response = requests.get(f"{cls.URL}/station/{station_name}").json()

        if not response.get("status"):
            return response.get("message")

        city_df = pd.DataFrame(response, index=[response.get("id_stacji")])
        return city_df


class WeatherManager(WeatherImgw):
    def __init__(self, name, your_choice=None, action=True):
        self.name = name
        self.choice = your_choice
        self.action = action

    def manage_your_choice(self):
        """
        The Manager helps us to shuffle our weather methods - it depends on
        what the user chooses
        :return:
        Print of right result as Data Frame
        """
        if self.choice == "1":
            print(self.get_all_current_data())
            self.choice = input("Co teraz wybierasz?\n")

        elif self.choice == "2":
            station_id = input("Podaj numer stacji: ")
            print(self.get_current_weather_data_by_station_id(station_id))
            self.choice = input("\nCo teraz wybierasz?\n")
        elif self.choice == "3":
            station_name = input("Podaj numer nazwę stacji: ")
            station_name = station_name.lower().replace(" ", "")
            print(
                self.get_current_weather_data_by_name(unidecode(station_name))
            )
            self.choice = input("\nCo teraz wybierasz?\n")
        elif self.choice == "0":
            self.action = False
            return self.action
        else:
            print("\nWprowadź poprawną wartość z listy")
            self.choice = input("\nCo wybierasz?\n")


if __name__ == "__main__":
    guy = input("Jak masz na imię: ")
    weather_guy = WeatherManager(guy)

    print(
        f"Witaj {weather_guy.name}, w aplikacji dostarczającej aktualnych "
        f"danych pogodowych."
    )
    print(
        "Poniżej masz kilka opcji do wyboru\n"
        "1 - pobierz aktualną pogodę dla całej Polski\n"
        "2 - pobierz aktualną pogodę dla miasta w Polsce podając jego id\n"
        "3 - pobierz aktualną pogodę dla miasta w Polsce podając jego nazwę\n"
        "0 - zakończ działanie programu\n"
    )

    choice = input("Co wybierasz?\n")
    weather_guy.choice = choice

    while weather_guy.action:
        weather_guy.manage_your_choice()




