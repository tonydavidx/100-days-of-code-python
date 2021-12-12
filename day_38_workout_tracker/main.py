import requests
import config
from datetime import datetime

GENDER = 'male'
WEIGHT = 60
HEIGHT = 180
AGE = 28

endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_input = input('What activity did you do today? ')

headers = {
    'x-app-id': config.app_id,
    'x-app-key': config.app_key,
}

parameters = {
    'query': exercise_input,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE,
}

response = requests.post(endpoint, json=parameters, headers=headers)

result = response.json()

print(result)

today_date = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')

sheet_endpoint = 'https://api.sheety.co/361da9616c088b6600e69e82becc9e71/myWorkouts/workouts'

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    sheet_reponse = requests.post(
        sheet_endpoint, json=sheet_inputs, auth=(config.username, config.password,))
    print(sheet_reponse.text)
