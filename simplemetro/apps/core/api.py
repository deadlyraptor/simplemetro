import os
from typing import Dict

import requests


class Line:
    def __init__(
        self,
        line: str,
        display_name: str,
        start_station: str,
        end_station: str,
        internal_destination_one: str = '',
        internal_destination_two: str = '',
    ):
        self.line = line
        self.display_name = display_name
        self.start_station = start_station
        self.end_station = end_station
        self.internal_destination_one = internal_destination_one
        self.internal_destination_two = internal_destination_two


class Result:
    def __init__(
        self, status_code: int, message: str = '', data: dict[str, list] = None
    ):
        """Result returned from low-level RestAdapter

        :param status_code: standard HTTP status code
        :param message: Human readable result
        :param data: Python List of Dictionaries
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []


class Metrorail:
    endpoints = {'lines': '/jLines', 'stations': '/jStations'}

    def __init__(
        self,
        base_url: str = 'api.wmata.com',
        base_path: str = 'Rail.svc',
        api_key: str = os.environ['WMATA_KEY'],
        response_format: str = 'json',
    ):
        self.url = f'https://{base_url}/{base_path}/{response_format}/'
        self._api_key = api_key

    def get(self, endpoint: str, params: Dict = None) -> Result:
        full_url = self.url + endpoint
        headers = {'api_key': self._api_key}
        response = requests.get(url=full_url, headers=headers, params=params)
        data_out = response.json()
        return Result(response.status_code, message=response.reason, data=data_out)

    def get_lines(self):
        """Returns information about all rail lines"""
        return self.get(self.endpoints['lines'])

    def get_stations(self, params):
        """Returns a list of station informatiion"""
        return self.get(self.endpoints['stations'], params=params)
