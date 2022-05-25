import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# cid & secret here
cid = '4bbda1ee53fd4cff9210c87f3d5fc151'
secret = '0057fa7877034586a306f1c0ccb16815'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

json = sp.search(q='Jethro Tull', type='artist')
print(json['artists']['items'][0]['genres'])
