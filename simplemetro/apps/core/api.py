import os

import requests


def lines():
    url = 'https://api.wmata.com/Rail.svc/json/jLines'
    headers = {'api_key': os.environ['WMATA_KEY']}

    response = requests.get(url, headers)
    lines = response.json()['Lines']

    return lines

class Line:
    def __init__(self, 
                 line: str,
                 display_name: str,
                 start_station: str,
                 end_station: str,
                 internal_destination_one: str = '',
                 internal_destination_two: str = ''):
        self.line = line
        self.display_name = display_name
        self.start_station = start_station
        self.end_station = end_station
        self.internal_destination_one = internal_destination_one
        self.internal_destination_two = internal_destination_two
        
class Result:
    def __init__(self, status_code: int, message: str = '', data:dict[str, list] = None):
        """Result returned from low-level RestAdapter

        :param status_code: standard HTTP status code
        :param message: Human readable result
        :param data: Python List of Dictionaries
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

class Metro:
    """
    1. Instantiate the Metro class
    2. Call Metro.get_lines()...
    3. ...which returns Metro.get()...
    4. ...which returns the Result object...
    5. ...which contains the API response in the data parameter
    """
    def __init__(self,
                 base_url: str = 'api.wmata.com',
                 api_key: str = os.environ['WMATA_KEY'],
                 api: str = 'Rail.svc',
                 response_format: str = 'json',
                ):
        self.url = 'https://{}/{}/{}/'.format(base_url, api, response_format)
        self._api_key = api_key
        self.api = api

    def get(self, endpoint: str) -> Result:
        full_url = self.url + endpoint
        headers = {'api_key': self._api_key}
        response = requests.get(url=full_url, headers=headers)
        data_out = response.json()
        return Result(response.status_code, message=response.reason, data=data_out)

    def get_lines(self):
        return self.get('jLines')

