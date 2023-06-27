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
        DataFrame if exist
        """
        response = requests.get(cls.URL).json()

        if response:
            df_data = pd.DataFrame(response)
            return df_data

        return "The newest data didn't come yet. Wait 5 min and try again"

    @classmethod
    def get_current_weather_data_by_station_id(cls, station_id):
        """
        Get weather data by index
        :return:
        Series if exist
        """
        response = requests.get(
            f"{cls.URL}/id/{station_id}"
        ).json()
        print(response)
        if response.get("status") is False:
            return response.get("message")

        city_df = pd.Series(response)
        return city_df

    @classmethod
    def get_current_weather_data_by_name(cls, station_name):
        """
        Get weather data by station name
        :return:
        Series if exist
        """
        response = requests.get(f"{cls.URL}/station/{station_name}").json()

        if response.get("status") is False:
            return response.get("message")

        city_df = pd.Series(response)

        return city_df

    @classmethod
    def get_all_current_data_html(cls):
        response = requests.get(f"{cls.URL}/format/html").text
        return response


class WeatherManager(WeatherImgw):
    def __init__(self, name, choice_number=None, action=True):
        self.name = name
        self.choice_number = choice_number
        self.action = action

    def manage_your_choice(self):
        """
        The Manager helps us to shuffle our weather methods - it depends on
        what the user chooses
        :return:
        Print of right result as Data Frame or DataSeries
        """
        if self.choice_number == "1":
            print(self.get_all_current_data())
            self.choice_number = input("Co teraz wybierasz?\n")

        elif self.choice_number == "2":
            station_id = input("Podaj numer stacji: ")
            print(self.get_current_weather_data_by_station_id(station_id))
            self.choice_number = input("\nCo teraz wybierasz?\n")

        elif self.choice_number == "3":
            station_name = input("Podaj numer nazwę stacji: ")
            station_name = station_name.lower().replace(" ", "")
            print(self.get_current_weather_data_by_name(
                unidecode(
                    station_name
                )
            ))
            self.choice_number = input("\nCo teraz wybierasz?\n")

        elif self.choice_number == "4":
            print(self.get_all_current_data_list())
            self.choice_number = input("Co teraz wybierasz?\n")

        elif self.choice_number == "0":
            self.action = False
            return self.action

        else:
            print("\nWprowadź poprawną wartość z listy")
            self.choice_number = input("\nCo wybierasz?\n")


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
        "4 - pobierz aktualną pogodę dla całej Polski jako lista lokalizacji\n"
        "0 - zakończ działanie programu\n"
    )

    choice = input("Co wybierasz?\n")
    weather_guy.choice_number = choice

    while weather_guy.action:
        weather_guy.manage_your_choice()




