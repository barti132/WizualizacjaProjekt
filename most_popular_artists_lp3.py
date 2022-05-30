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

# wykresy 1982-1990
res = df.loc[df['year'] < 1990]
res = res.groupby(['artist name'])['artist name'].count().reset_index(name="count")
res = res.sort_values(by='count', ascending=False).head(20)
fig1 = px.bar(res, x='artist name', y='count', title="Najpopularniejsi artyści i zespoły w latach 1982-1990")
fig1.update_layout(xaxis_title='Nazwa artysty', yaxis_title='Ilość wystąpień na liście')
fig2 = px.pie(values=[0.45, 0.2, 0.05, 0.05, 0.25], labels=['Polska', 'USA', 'Norwegia', 'Irlandia', 'UK'], names=['Polska', 'USA', 'Norwegia', 'Irlandia', 'UK'],
              title="Stosunek artystów polskich do zagranicznych", hole=.4)

# wykresy 1990-2000
res = df.loc[df['year'].between(1990, 2000)]
res = res.groupby(['artist name'])['artist name'].count().reset_index(name="count")
res = res.sort_values(by='count', ascending=False).head(20)
fig3 = px.bar(res, x='artist name', y='count', title="Najpopularniejsi artyści i zespoły w latach 1990-2000")
fig3.update_layout(xaxis_title='Nazwa artysty', yaxis_title='Ilość wystąpień na liście')
fig4 = px.pie(values=[0.40, 0.3, 0.05, 0.15, 0.1], labels=['Polska', 'USA', 'Szwedzia', 'Irlandia', 'UK'], names=['Polska', 'USA', 'Szwedzia', 'Irlandia', 'UK'],
              title="Stosunek artystów polskich do zagranicznych", hole=.4)

# wykresy 2000-2010
res = df.loc[df['year'].between(2000, 2010)]
res = res.groupby(['artist name'])['artist name'].count().reset_index(name="count")
res = res.sort_values(by='count', ascending=False).head(20)
fig5 = px.bar(res, x='artist name', y='count', title="Najpopularniejsi artyści i zespoły w latach 2000-2010")
fig5.update_layout(xaxis_title='Nazwa artysty', yaxis_title='Ilość wystąpień na liście')
fig6 = px.pie(values=[0.40, 0.25, 0.25, 0.05, 0.05], labels=['Polska', 'USA', 'UK', 'Irlandia', 'Norwegia'], names=['Polska', 'USA', 'UK', 'Irlandia', 'Norwegia'],
              title="Stosunek artystów polskich do zagranicznych", hole=.4)

# wykresy 2010-2020
res = df.loc[df['year'].between(2010, 2020)]
res = res.groupby(['artist name'])['artist name'].count().reset_index(name="count")
res = res.sort_values(by='count', ascending=False).head(20)
fig7 = px.bar(res, x='artist name', y='count', title="Najpopularniejsi artyści i zespoły w latach 2010-2020")
fig7.update_layout(xaxis_title='Nazwa artysty', yaxis_title='Ilość wystąpień na liście')
fig8 = px.pie(values=[0.6, 0.3, 0.05, 0.05], labels=['Polska', 'UK', 'USA', 'Irlandia'], names=['Polska', 'UK', 'USA', 'Irlandia'],
              title="Stosunek artystów polskich do zagranicznych", hole=.4)

app.layout = html.Div(children=[
    html.Div([
        html.H4("Najpopularniejsi artyści i zespoły w wybranym roku"),
        dcc.Graph(id='top-artists'),
        dcc.Dropdown(options=[{'label': x, 'value': x} for x in range(1982, 2020)], value=1982, id="year-picker"),
    ]),
    html.Div([
        html.Div([
            dcc.Graph(id='top-artists-1982-1990', figure=fig1, style={'display': 'inline-block'}),
            dcc.Graph(id='top-artists-1982-1990-pie', figure=fig2, style={'display': 'inline-block'}),
        ]),
    ]),
    html.Div([
        html.Div([
            dcc.Graph(id='top-artists-1990-2000', figure=fig3, style={'display': 'inline-block'}),
            dcc.Graph(id='top-artists-1990-2000-pie', figure=fig4, style={'display': 'inline-block'}),
        ]),
    ]),
    html.Div([
        html.Div([
            dcc.Graph(id='top-artists-2000-2010', figure=fig5, style={'display': 'inline-block'}),
            dcc.Graph(id='top-artists-2000-2010-pie', figure=fig6, style={'display': 'inline-block'}),
        ]),
    ]),
    html.Div([
        html.Div([
            dcc.Graph(id='top-artists-2010-2020', figure=fig7, style={'display': 'inline-block'}),
            dcc.Graph(id='top-artists-2010-2020-pie', figure=fig8, style={'display': 'inline-block'}),
        ]),
    ])
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
