import requests
import pandas as pd


def get_all_current_data():
    response = requests.get(
        "https://danepubliczne.imgw.pl/api/data/synop"
    ).json()

    if response:
        df_data = pd.DataFrame(response)
        return df_data

    return "The newest data didn't come jet. Wait 5 min and try again"


if __name__ == "__main__":
    print(get_all_current_data())

