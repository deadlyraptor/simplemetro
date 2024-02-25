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
        self,
        status_code: int,
        message: str = '',
        data: dict[str, list] = None,
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
    urls = {
        'Lines': 'https://api.wmata.com/Rail.svc/json/jLines',
        'Stations': 'https://api.wmata.com/Rail.svc/json/jStations',
    }

    def __init__(self, api_key: str = os.environ['WMATA_KEY']):
        self._api_key = api_key

    def get(self, url: str, params: Dict = None) -> Result:
        headers = {'api_key': self._api_key}
        response = requests.get(url=url, headers=headers, params=params)
        data = response.json()
        return Result(response.status_code, message=response.reason, data=data)

    def get_lines(self):
        """Returns information about all rail lines"""
        return self.get(self.urls['Lines'])

    def get_stations(self, params):
        """Returns a list of station information"""
        return self.get(self.urls['Stations'], params=params)
