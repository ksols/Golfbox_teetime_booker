import json

import requests
import time

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'tf=0; tv=5; i00=0000646cc6b9decf0000; l=nb; _sp_ses.786e=*; _sp_id.786e=285e4bff-08ba-4984-8a10-8bce30688ff5.1678122568.59.1718820198.1718811663.da6efff8-e68d-4b3b-a689-d87068931d1b.88f3617c-2cf2-4e2a-8b4d-f41362a7c3c8.87782125-0f21-4fed-a366-8ea857830123.1718820198064.1',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.yr.no/nb/v%C3%A6rvarsel/timetabell/1-2283138/Norge/Vestfold/Sandefjord/Marum?i=0',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.yr.no/api/v0/locations/1-2283138/forecast/currenthour', headers=headers)

print(response.json())
