# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_data()
sheet_data = sheet_data
# print(sheet_data)
flight_search = FlightSearch()

if sheet_data[0]['iataCode'] == "":
    for r in sheet_data:
        r['iataCode'] = flight_search.get_destination_codes(r['city'])
        data_manager.destination_data = sheet_data
        data_manager.update_iata()
