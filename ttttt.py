import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication
sp_oauth = SpotifyOAuth(
    client_id='Your_Client_Id',
    client_secret='Your_Client_Secret',
    redirect_uri='http://localhost:8080/callback/',
    scope='user-library-read'  # Adjust scope as needed
)



# pip install apple-music-python

import applemusicpy

secret_key = "your_secret_key"
key_id = "your_key_id"
team_id = "your_team_id"

# Connect to Apple Music API
am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
