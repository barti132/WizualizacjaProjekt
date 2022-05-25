import csv
import json
import time

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

api_url = "https://lp3.polskieradio.pl/List/GetListResults?listId="

cid = '4bbda1ee53fd4cff9210c87f3d5fc151'
secret = '0057fa7877034586a306f1c0ccb16815'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#with open('lp3-data.csv', 'w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(["week timestamp", "track name", "arist name", "last position", "weeks on list", "rank", "genres"])

#full - 1-5
with open('lp3-data14.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    for i in range(2400, 2710):#2710
        if i % 30 == 0:
            print("sleeping... i = ", i)
            time.sleep(5)

        print(f'{api_url}{i}')
        with requests.get(f'{api_url}{i}') as resp:
            if resp.status_code == 204:
                continue
            processed_page = BeautifulSoup(resp.text, "html.parser")
            site_json = json.loads(processed_page.text)
            for result in site_json['results'][:30]:
                spot = sp.search(q=result.get('artists')[0]['name'], type='artist')
                if len(spot['artists']['items']) == 0:
                    genres = ["Other"]
                else:
                    genres = spot['artists']['items'][0]['genres']

                if result.get('lastPosition') is None:
                    lastPosition = "N"
                else:
                    lastPosition = result.get('lastPosition')

                if result.get('weeksOnList') == "":
                    weeksOnList = "0"
                else:
                    weeksOnList = result.get('weeksOnList')
                writer.writerow([site_json['dateFrom'].split()[0], result.get('name'), result.get('artists')[0]['name'], lastPosition, weeksOnList, result.get('position'), genres])
