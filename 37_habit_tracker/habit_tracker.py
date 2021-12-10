import requests
from datetime import date, datetime
import random

endpoint = 'https://pixe.la/v1/users'
TOKEN = 'dshlidfs54kjxgz56'
USERNAME = 'tony19'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
graph_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'
graph_params = {
    'id': 'reading',
    'name': 'Reading',
    'unit': 'pages',
    'type': 'int',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': TOKEN,
}


def create_graph():
    response = requests.post(
        url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)


today = datetime(2020, 12, 20)
date_str = today.strftime('%Y%m%d')
print(date_str)


def post_pixel():
    post_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/reading'
    post_params = {
        'date': date_str,
        'quantity': str(random.randint(1, 100))
    }

    response = requests.post(
        url=post_endpoint, json=post_params, headers=headers)

    print(response.text)


def update_pixel():
    update_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/reading/20201210'
    update_params = {
        'quantity': '100'
    }
    response = requests.delete(
        url=update_endpoint,  headers=headers)

    print(response.text)


for m in range(4, 12):
    datei = datetime(2020, m, 1)
    for i in range(1, 30):
        datei = datetime(2021, m, i)
        date_str = datei.strftime('%Y%m%d')
        post_pixel()

# post_pixel()
# update_pixel()
