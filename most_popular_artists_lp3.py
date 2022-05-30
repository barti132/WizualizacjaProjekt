"""
Najpopularniejsi artysci co roku + 10 lat
"""

from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('lp3-full.csv')
df['week timestamp'] = pd.to_datetime(df['week timestamp'])
df['year'] = pd.DatetimeIndex(df['week timestamp']).year

app.layout = html.Div([
    html.H4("Najpopularniejsi artysci i zespoły w wybranym roku"),
    dcc.Graph(id='top-artists'),
    dcc.Dropdown(options=[{'label': x, 'value': x} for x in range(1982, 2020)], value=1982, id="year-picker")
])


@app.callback(Output('top-artists', 'figure'), Input('year-picker', 'value'))
def top_artist_by_year(selected_year):
    result = df.loc[df['year'] == selected_year]
    result = result.groupby(['artist name'])['artist name'].count().reset_index(name="count")
    result = result.sort_values(by='count', ascending=False).head(20)
    fig = px.bar(result, x='artist name', y='count')
    fig.update_layout(xaxis_title='Nazwa artysty', yaxis_title='Ilość wystąpień na liście')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
