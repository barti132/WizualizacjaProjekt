import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# cid & secret here


client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

json = sp.search(q='Jethro Tull', type='artist')
print(json['artists']['items'][0]['genres'])