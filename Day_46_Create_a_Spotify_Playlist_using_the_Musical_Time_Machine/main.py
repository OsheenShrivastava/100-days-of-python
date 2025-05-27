
# TODO-3 - Import BeautifulSoup from bs4 module and requests module

import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# TODO-1 - Create an input() prompt that asks the user what year they would like to travel to in YYY-MM-DD format

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
print(date)

# TODO-2 - Include a header when making your request to billboard.com.

header = {
    "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/136.0.0.0 Safari/537.36"
}

# TODO-4 - Requests data from URL,raise exceptions and Scrape the top 100 song titles on any date of your choice into
#  a Python List.

URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=URL, headers=header)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

# Method 1 (My method)
songs = soup.find_all(class_="o-chart-results-list-row-container")

songs_list = []
for song in songs:
    songs_list.append(song.find(name="h3", id="title-of-a-story").text.strip())
print(songs_list)

# Method 2 (Tutor's Method)
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)

# TODO-5 - In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have
#  an account, you can sign up for a free one here: http://spotify.com/signup/ . Once you've signed up/ signed in, go
#  to the developer dashboard and create a new Spotify App using the link: https://developer.spotify.com/dashboard/

# TODO-6 - Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project [.ENV FILE].

# TODO-7 - Import os and dotenv at the top and export all the credentials from .env to main.py file

#  Load the .env file
load_dotenv()

# Access the environment variables
Redirect_URL = os.environ["REDIRECT_URL"]
Client_ID = os.environ["CLIENT_ID"]
Client_Secret = os.environ["CLIENT_SECRET"]

Scope = "playlist-modify-private"

# TODO-8 - Import spotipy and SpotifyOAuth at the top and pass Client_ID,Client_Secret,Redirect_URL and scope for
#  user authentication

spotify_endpoint = "https://accounts.spotify.com/authorize/"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=Client_ID,
    client_secret=Client_Secret,
    redirect_uri=Redirect_URL,
    scope=Scope,
)
)

# TODO-9 - Use https://example.com as your Redirect URI. You're looking to get the currentuser id
#  (your Spotify username). As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as
#  well.

current_user = sp.current_user()
User_ID = current_user['id']
print(User_ID)

# TODO-10 - If successful, you should see the page below show up automatically (be sure to click Agree): [I have
#  attached a snap of it]

# TODO-11 - Then it will take you to the page below, example.com and you need to copy the entire URL in the address bar:
#  [I have attached a snap of it]

# TODO-12 - Finally, you need to paste the URL into the prompt in PyCharm: [I have attached a snap of it]

# TODO-13 - Now if you right-click in the project tree and select Reload from Disk, you should see a new file in this
#  project called .cache.

# TODO-14 - The output of the above method is a dictionary, look for the value of the "id" key. You may receive it in
#  your RUN window.

# TODO-15 - Separate year from date entered
year = date.split("-")[0]
print(year)

# TODO-16 - Import pprint.
from pprint import pprint

song_uris = []

# TODO-17 - Create a list of Spotify song URIs for the list of song names found above in songs_list
#  (scraping billboard 100) using FOR Loop.
for song in songs_list:

    # TODO-18 - Use the query format "track: {name} year: {YYYY}" to narrow down on a track name from a particular year.

    # TODO-19 - Sometimes a song is not available in Spotify, so we will use exception handling to skip over those
    #  songs.
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)

# TODO-20 - Create a new private playlist with the name "YYYY-MM-DD Billboard 100", where the date is the date we
#  inputted above.
playlist = sp.user_playlist_create(user=User_ID, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)