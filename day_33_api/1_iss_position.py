import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.json())

iss_position = response.json()['iss_position']
iss_lat = iss_position['latitude']
iss_lon = iss_position['longitude']
print(f'Latitude: {iss_lat} Longitude: {iss_lon}')
