import datetime
import urllib
from urllib.request import Request
from dateutil.relativedelta import relativedelta

from bs4 import BeautifulSoup

today_date = datetime.datetime(1981, 1, 1)  # date.today()
print("Today is: " + today_date.strftime('%Y-%m-%d'))
billboard_date = datetime.datetime(1980, 1, 5)
print("Start from: " + billboard_date.strftime('%Y-%m-%d'))

url = "https://www.billboard.com/charts/hot-100/"

billboard_pages = []
while today_date.date() > billboard_date.date():
    date = billboard_date.strftime('%Y-%m-%d')
    with urllib.request.urlopen(f'{url}{date}') as resp:
        processed_page = BeautifulSoup(resp.read().decode('utf-8'), "html.parser")
        billboard_pages.append(processed_page)
    billboard_date += relativedelta(months=+1)

print(len(billboard_pages))
print("Ended: " + billboard_date.strftime('%Y-%m-%d'))
