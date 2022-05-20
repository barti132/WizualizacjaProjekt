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

billboard_data = []
while today_date.date() > billboard_date.date():
    date = billboard_date.strftime('%Y-%m-%d')
    with urllib.request.urlopen(f'{url}{date}') as resp:
        data = []
        processed_page = BeautifulSoup(resp.read().decode('utf-8'), "html.parser")
        
        "c-tagline  a-font-primary-medium-xs u-font-size-11@mobile-max u-letter-spacing-0106 u-letter-spacing-0089@mobile-max lrv-u-line-height-copy lrv-u-text-transform-uppercase lrv-u-margin-a-00 lrv-u-padding-l-075 lrv-u-padding-l-00@mobile-max"
        billboard_data.append(data)
    billboard_date += relativedelta(months=+3) #change to full year


print(billboard_data[1])

print(len(billboard_data))
print("Ended: " + billboard_date.strftime('%Y-%m-%d'))
