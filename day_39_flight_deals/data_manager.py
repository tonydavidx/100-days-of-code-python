from pprint import pprint
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.destination_data = {}

    def get_data(self) -> dict:
        self.sheety_endpoint = 'https://api.sheety.co/361da9616c088b6600e69e82becc9e71/flightDeals/prices'
        self.response = requests.get(self.sheety_endpoint)
        self.data = self.response.json()
        self.destination_data = self.data['prices']
        return self.destination_data

    def update_iata(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{self.sheety_endpoint}/{city['id']}", json=new_data
            )
            print(response.text)
