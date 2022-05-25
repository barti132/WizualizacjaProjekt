import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# cid & secret here
cid = 'b656729f01d7445fa9c83a55273c5c64'
secret = '1b5f5cd62c794904806001e79f68977f'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

json = sp.search(q='Jethro Tull', type='artist')
print(json['artists']['items'][0]['genres'])
