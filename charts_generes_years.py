"""
Analiza gatunków muzycznych w odstępach czasowych na podstawie listy radia nr 3
"""

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
"""
lp3 = pd.read_csv('lp3-full.csv')
lp3['week timestamp'] = pd.to_datetime(lp3['week timestamp'])
lp3['genres'] = lp3['genres'].apply(eval)

genres = ["rap", "pop", "rock", "soul", "folk", "jazz", "blues", "metal", "punk", "polish"]

data = []

#można sprobować zapisać do csv, żeby było szybciej
for y in range(1982, 2020):
    print(y)
    genres_popularity = {"rap": 0, "pop": 0, "rock": 0, "soul": 0, "folk": 0, "jazz": 0, "blues": 0, "metal": 0,
                         "punk": 0, "polish": 0}
    for index, row in lp3.iterrows():
        if row['week timestamp'].year == y:
            for genre in genres:
                if any(genre in s for s in row['genres']):
                    genres_popularity[genre] += 1

    for genre in genres_popularity:
        data.append({"Year": y, "Name": genre, "Pop": genres_popularity[genre]})
"""
df = pd.read_csv('genres-popularity.csv')  # raz policzone, można wykorzystać

fig = px.line(df, x='Year', y='Pop', color='Name', title="Popularność gatunków muzycznych na przestrzeni lat w Polsce")
fig.update_layout(xaxis_title='Rok', yaxis_title='Popularność (ilość wystąpień na liście)')

app.layout = html.Div(children=[
    html.H1("Wykresy dla Polski na podstawie danych z listy przebojów Programu 3"),
    html.Div([
        dcc.Graph(id="graph", figure=fig)
    ]),
    html.Div([
        dcc.Graph(id="top-genres"),
        dcc.Dropdown(options=[{'label': x, 'value': x} for x in range(1982, 2020)], value=1982, id="year-picker"),
    ])
])


@app.callback(Output('top-genres', 'figure'), Input('year-picker', 'value'))
def top_artist_by_year(selected_year):
    result = df.loc[df['Year'] == selected_year]
    result = result.sort_values(by='Pop', ascending=False)
    fig1 = px.bar(result, x='Name', y='Pop', title="Popularność gatunków w wybranym roku")
    fig1.update_layout(xaxis_title='Gatunek', yaxis_title='Popularność')
    return fig1


if __name__ == '__main__':
    app.run_server(debug=True)
