import os

import requests


def lines():
    url = 'https://api.wmata.com/Rail.svc/json/jLines'
    headers = {'api_key': os.environ['WMATA_KEY']}

    response = requests.get(url, headers)
    lines = response.json()['Lines']

    return lines

class Result:
    def __init__(self, status_code: int, message: str = '', data:dict[str, list] = None):
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

class RestAdapter:
    def __init__(self,
                 host: str = 'api.wmata.com',
                 api_key: str = os.environ['WMATA_KEY'],
                 api: str = 'Rail.svc',
                 json: str = 'json',
                ):
        self.url = 'https://{}/{}/{}/'.format(host, api, json)
        self._api_key = api_key
        self.api = api

    def get(self, endpoint: str) -> dict[str, list]:
        full_url = self.url + endpoint
        headers = {'api_key': self._api_key}
        response = requests.get(url=full_url, headers=headers)
        data_out = response.json()
        if response.status_code >= 200 and response.status_code <= 299: # OK
            return data_out
        raise Exception(data_out['message']) # Todo: raise custom exception later

