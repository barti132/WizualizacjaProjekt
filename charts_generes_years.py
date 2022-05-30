"""
Analiza gatunków muzycznych w odstępach czasowych na podstawie listy radia nr 3
"""

import pandas as pd
import plotly.express as px


lp3 = pd.read_csv('lp3-full.csv')
lp3['week timestamp'] = pd.to_datetime(lp3['week timestamp'])
lp3['genres'] = lp3['genres'].apply(eval)

genres = ["rap", "pop", "rock", "soul", "folk", "jazz", "blues", "metal", "punk", "polish"]

data = []

for y in range(1982, 2020):
    print(y)
    genres_popularity = {"rap": 0, "pop": 0, "rock": 0, "soul": 0, "folk": 0, "jazz": 0, "blues": 0, "metal": 0, "punk": 0, "polish": 0}
    for index, row in lp3.iterrows():
        if row['week timestamp'].year == y:
            for genre in genres:
                if any(genre in s for s in row['genres']):
                    genres_popularity[genre] += 1

    for genre in genres_popularity:
        data.append({"Year": y, "Name": genre, "Pop": genres_popularity[genre]})

df = pd.DataFrame(data)

fig = px.line(df, x='Year', y='Pop', color='Name', title="Popularność gatunków muzycznych na przestrzeni lat w Polsce")
fig.update_layout(xaxis_title='Rok', yaxis_title='Popularność (ilość wystąpień na liście radia nr 3 w danym roku)')
fig.show()
