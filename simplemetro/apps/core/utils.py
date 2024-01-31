import os

import requests


def lines():
    url = 'https://api.wmata.com/Rail.svc/json/jLines'
    headers = {'api_key': os.environ['WMATA_KEY']}

    response = requests.get(url, headers)
    lines = response.json()['Lines']

    return lines


