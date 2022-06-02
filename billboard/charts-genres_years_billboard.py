"""
Analiza gatunków muzycznych w odstępach czasowych na podstawie listy radia nr 3
"""

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
"""
billboard = pd.read_csv('billboard/billboard-data.csv')
billboard['week timestamp'] = pd.to_datetime(billboard['week timestamp'])
billboard['genres'] = billboard['genres'].apply(eval)

genres = ["rap", "pop", "rock", "soul", "folk", "r&b", "blues", "metal", "punk", "country"]

data = []

#można sprobować zapisać do csv, żeby było szybciej
for y in range(1982, 2020):
    print(y)
    genres_popularity = {"rap": 0, "pop": 0, "rock": 0, "soul": 0, "folk": 0, "r&b": 0, "blues": 0, "metal": 0,
                         "punk": 0, "country": 0}
    for index, row in billboard.iterrows():
        if row['week timestamp'].year == y:
            for genre in genres:
                if any(genre in s for s in row['genres']):
                    genres_popularity[genre] += 1

    for genre in genres_popularity:
        data.append({"Year": y, "Name": genre, "Pop": genres_popularity[genre]})

df = pd.DataFrame(data)
df.to_csv('genres-popularity-billboard.csv')  # raz policzone, można wykorzystać
"""
df = pd.read_csv('genres-popularity-billboard.csv')

fig = px.line(df, x='Year', y='Pop', color='Name', title="Popularność gatunków muzycznych na przestrzeni lat w USA")
fig.update_layout(xaxis_title='Rok', yaxis_title='Popularność (ilość wystąpień na liście)')

app.layout = html.Div(children=[
    html.H1("Wykresy dla USA na podstawie danych z listy Hot 100 billboard"),
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
