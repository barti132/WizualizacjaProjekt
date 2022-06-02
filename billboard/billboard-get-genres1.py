import csv
import datetime

import billboard
import spotipy
from dateutil.relativedelta import relativedelta
from spotipy.oauth2 import SpotifyClientCredentials

cid = '4bbda1ee53fd4cff9210c87f3d5fc151'
secret = '0057fa7877034586a306f1c0ccb16815'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

today_date = datetime.datetime(2022, 5, 20)  # date.today()
billboard_date = datetime.datetime(2014, 7, 27)
authors = {}

print("Today is: " + today_date.strftime('%Y-%m-%d'))
print("Start from: " + billboard_date.strftime('%Y-%m-%d'))

with open('billboard-data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        ["week timestamp", "track name", "arist name", "peak position", "last position", "weeks on charts", "rank",
         "genres"])

billboard_data = []
while today_date.date() > billboard_date.date():
    date = billboard_date.strftime('%Y-%m-%d')
    print(date)
    chart = billboard.ChartData('hot-100', date=billboard_date.date())
    with open('billboard-data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for i in range(50):
            genres = []
            entry = chart[i]

            if entry.artist in authors:
                genres = authors.get(entry.artist)
            else:
                spot = sp.search(q=entry.artist, type='artist')
                if len(spot['artists']['items']) == 0:
                    authors[entry.artist] = ['Other']
                else:
                    authors[entry.artist] = spot['artists']['items'][0]['genres']
                genres = authors.get(entry.artist)

            writer.writerow(
                [date, entry.title, entry.artist, entry.peakPos, entry.lastPos, entry.weeks, entry.rank, genres])

    billboard_date += relativedelta(weeks=+1)
