# import datetime as dt
#
#
# date = input(f"Which Your you want to travel to? Type the date in format YYYY-MM-DD:")
# year, month, day = map(int, date.split("-"))
# DATE = dt.date(year=year, month=month, day=day)
#
# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.getText().strip("\n\t") for song in song_names_spans]

Client_ID = "5ae8c9c78e9745de8413db9788b75717"
Client_Secret = "a39bff9426a14a78a2ac8a31b50423a3"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")




