import requests
from datetime import datetime
import time
import smtplib
import json
import config

email = config.email
password = config.password

MY_LAT = 13.117363
MY_LON = 80.101572

response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.json())

iss_position = response.json()['iss_position']
iss_lat = float(iss_position['latitude'])
iss_lon = float(iss_position['longitude'])
# print(f'Latitude: {iss_lat} Longitude: {iss_lon}')

my_loc = {'lat': 13.117363, 'long': 80.101572, 'formatted': 0}

response = requests.get('https://api.sunrise-sunset.org/json', params=my_loc)
response.raise_for_status()
# print(response.json())

sunrise_hour = int(response.json()['results']['sunrise'].split('T')[
    1].split(':')[0])

sunset_hour = int(response.json()['results']
                  ['sunset'].split('T')[1].split(':')[0])

# print(f"Sunrise: {sunrise_hour}, Sunset: {sunset_hour}")

now = datetime.now()
hour_now = now.hour
# print(f"Current time: {hour_now}")

lat_diff = iss_lat - MY_LAT
lon_diff = iss_lon - MY_LON


def is_iss_close():
    if MY_LAT+5 < iss_lat and MY_LON+5 < iss_lon:
        return True


while True:
    if hour_now > sunset_hour or hour_now < sunrise_hour:
        if is_iss_close():
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(user=email, password=password)
                smtp.sendmail(from_addr=email, to_addrs=email,
                              msg=f"Subject: 🛰️ Look Up\n\nISS is Close by you")
                print("Email sent")

    time.sleep(60)
