import requests
from datetime import datetime

my_loc = {'lat': 13.117363, 'long': 80.101572, 'formatted': 0}

response = requests.get('https://api.sunrise-sunset.org/json', params=my_loc)
response.raise_for_status()
print(response.json())

sunrise_hour = response.json()['results']['sunrise'].split('T')[
    1].split(':')[0]

sunset_hour = response.json()['results']['sunset'].split('T')[1].split(':')[0]

print(f"Sunrise: {sunrise_hour}, Sunset: {sunset_hour}")

now = datetime.now()
hour_now = now.hour
print(f"Current time: {hour_now}")
