import time
import requests
import json
import requests
from datetime import datetime
from datetime import datetime, timezone, timedelta
from selenium_test import Booker
headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'tf=0; tv=5; i00=0000646cc6b9decf0000; l=nb; _sp_ses.786e=*; _sp_id.786e=285e4bff-08ba-4984-8a10-8bce30688ff5.1678122568.58.1718811517.1718808955.88f3617c-2cf2-4e2a-8b4d-f41362a7c3c8.2c88034a-0f37-45a2-a16a-1f3d874af6ed.034a5acf-9f73-4bcc-8975-f48eed5b8a66.1718811514514.2',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.yr.no/nb/v%C3%A6rvarsel/daglig-tabell/1-2283138/Norge/Vestfold/Sandefjord/Marum',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.yr.no/api/v0/locations/1-2283138/forecast', headers=headers)
iterate_me = response.json()["shortIntervals"]


def get_weather_from_time(time):
    # Get the current date and time
    now = datetime.now(timezone.utc)

    # Add two days to the current date and time
    future_date = now + timedelta(days=2)

    future_date = future_date.replace(
        hour=(time - 2), minute=0, second=0, microsecond=0)

    # Define the desired timezone offset (+02:00)
    desired_timezone = timezone(timedelta(hours=2))

    # Convert the future datetime to the desired timezone
    future_date_in_desired_timezone = future_date.astimezone(desired_timezone)

    # Format the datetime as a string
    formatted_datetime = future_date_in_desired_timezone.strftime(
        '%Y-%m-%dT%H:%M:%S%z')

    # Insert a colon in the timezone offset
    formatted_datetime_with_colon = formatted_datetime[:-
                                                       2] + ':' + formatted_datetime[-2:]

    # print("Formatted future date and time:", formatted_datetime_with_colon)
    return formatted_datetime_with_colon


sytten_nullnull_format = get_weather_from_time(17)
atten_nullnull_format = get_weather_from_time(18)
nitten_nullnull_format = get_weather_from_time(19)

for x in iterate_me:
    if x["start"] == atten_nullnull_format and x["wind"]["speed"] < 12 and x["wind"]["gust"] < 15 and x["temperature"]["value"] > 14 and x["precipitation"]["min"] < 0.1:
        # Sjekk om tee time er ledig:
        print("Dato: ", x["start"])
        print("vind hastighet: ", x["wind"]
              ["speed"], " kast: ", x["wind"]["gust"])
        print("temp: ", x["temperature"]["value"],
              " nedbør: ", x["precipitation"]["min"])
        print()
        print("Booker tee time")
        # datetime_str = "2024-06-23T18:00:00+02:00"
        datetime_str = x["start"]
        date_part = datetime_str.split("T")[0]
        date_components = date_part.split("-")
        month_day = "-".join(date_components[1:3])
        month_day = "".join(date_components[1:3])
        # Target dato format: 20240624T000000
        print("Target string: ", "2024" + month_day + "T000000")
        booker = Booker("2024" + month_day + "T000000")
        print("Ran successfully")

    # if x["start"] == sytten_nullnull_format:
    #     print("Klarte sytten også: ", x["start"])
    #     print("vind hastighet: ", x["wind"]
    #           ["speed"], " kast: ", x["wind"]["gust"])
    #     print("temp: ", x["temperature"]["value"],
    #           " nedbør: ", x["precipitation"]["min"])
    #     print()
    # if x["start"] == nitten_nullnull_format:
    #     print("Klarte nitten også: ", x["start"])
    #     print("vind hastighet: ", x["wind"]
    #           ["speed"], " kast: ", x["wind"]["gust"])
    #     print("temp: ", x["temperature"]["value"],
    #           " nedbør: ", x["precipitation"]["min"])
    #     print()
