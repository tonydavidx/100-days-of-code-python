import requests
import os
import config
from twilio.rest import Client

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

config = {
    'lat': 13.117363,
    'lon': 80.101572,
    'appid': config.api,
    'exclude': 'current,minutely,daily,alerts'
}

url = 'https://api.openweathermap.org/data/2.5/onecall'

response = requests.get(url, params=config)
response.raise_for_status()
data = response.json()['hourly']

hourly_list = data[0:12]

weather_ids = [x['weather'][0]['id'] for x in hourly_list]

will_rain = False

for i in weather_ids:
    if i < 700:
        will_rain = True

if will_rain:
    message = client.messages \
                    .create(
                        body="you will need an umbrella 🌂",
                        from_='+18043737869',
                        to='+919600134756'
                    )

print(message.status)
