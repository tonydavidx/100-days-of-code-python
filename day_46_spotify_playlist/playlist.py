import requests
import config
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

scope = 'playlist-modify-private'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope=scope, client_id=config.client_id, client_secret=config.client_secret, redirect_uri='https://example.com'))

year = input('what year you would top 100 songs for(YYYY-MM-DD): ')

# year = '2019-01-01'
url = 'https://www.billboard.com/charts/hot-100/'

response = requests.get(url+year+'/')

content = response.text

soup = BeautifulSoup(content, 'html.parser')
songs = []

song_class = 'c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only'

s = 'c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet'

first_song = soup.find('h3', class_=s)
first_song = first_song.text.replace('\n', '')
songs.append(first_song)

musics = soup.find_all('h3', class_=song_class)
for music in musics:
    music = music.text
    music = music.replace('\n', '')
    songs.append(music)

song_uri = []

for song in songs:
    result = sp.search(q=f'track:{song}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uri.append(uri)
    except IndexError:
        print(f'{song} not found')

playList = sp.user_playlist_create(user=config.user_id,
                                   name=f"{year} Billboard Hot 100", public=False)

sp.playlist_add_items(playlist_id=playList['id'], items=song_uri)
