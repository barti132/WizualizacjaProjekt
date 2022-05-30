"""
Skrypt ściąga dane z billboard.com i zapisuje je do billboard-data.csv
"""
import datetime
import csv
import billboard
from dateutil.relativedelta import relativedelta

today_date = datetime.datetime(2022, 5, 20)  # date.today()
billboard_date = datetime.datetime(1982, 5, 1)

print("Today is: " + today_date.strftime('%Y-%m-%d'))
print("Start from: " + billboard_date.strftime('%Y-%m-%d'))

url = "https://www.billboard.com/charts/hot-100/"

with open('billboard-data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["week timestamp", "track name", "arist name", "peak position", "last position", "weeks on charts", "rank"])

billboard_data = []
while today_date.date() > billboard_date.date():
    date = billboard_date.strftime('%Y-%m-%d')
    chart = billboard.ChartData('hot-100', date=billboard_date.date())
    with open('billboard-data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for entry in chart.entries:
            writer.writerow([date, entry.title, entry.artist, entry.peakPos, entry.lastPos, entry.weeks, entry.rank])

    billboard_date += relativedelta(weeks=+1)
