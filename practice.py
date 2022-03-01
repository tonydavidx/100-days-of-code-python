import requests

data = requests.get(
    'https://api.themoviedb.org/3/search/movie', params={'api_key': 'b08c06fa9d7e2da44fd003fc721dfcf5', 'query': 'batman'})
print(data)
