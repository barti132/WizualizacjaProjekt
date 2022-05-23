import csv
import json
import requests
from bs4 import BeautifulSoup

api_url = "https://lp3.polskieradio.pl/List/GetListResults?listId="

with open('lp3-data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["week timestamp", "track name", "arist name", "last position", "weeks on list", "rank"])

with open('lp3-data.csv', 'a', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    for i in range(1, 2000):
        print(f'{api_url}{i}')
        with requests.get(f'{api_url}{i}') as resp:
            if resp.status_code == 204:
                continue
            processed_page = BeautifulSoup(resp.text, "html.parser")
            site_json = json.loads(processed_page.text)
            for result in site_json['results']:
                writer.writerow([site_json['dateFrom'].split()[0], result.get('name'), result.get('artists')[0]['name'], result.get('lastPosition'), result.get('weeksOnList'), result.get('position')])
