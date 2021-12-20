import requests
from bs4 import BeautifulSoup

response = requests.get(
    'https://www.imdb.com/list/ls055592025/')
content = response.text

soup = BeautifulSoup(content, 'html.parser')


movie_name = soup.find_all('h3', class_='lister-item-header')

with open('./movies_list.txt', 'w') as m:
    for movie in movie_name:
        m.write(movie.text)

# print(movie_name)
