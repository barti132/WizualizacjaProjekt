import pandas as pd
import plotly.express as px

#for subplots
import plotly.graph_objects as go
from plotly.subplots import make_subplots

lp3 = pd.read_csv('lp3-full.csv')
most_popular = lp3.groupby(['artist name'])['artist name'].count().reset_index(name="count")
most_popular = most_popular.sort_values(by='count', ascending=False).head(20)

fig1 = px.bar(most_popular, x='artist name', y='count', title="Najpopularniejsi artysci od 1982")
fig1.show()

fig2 = px.pie(values=[0.4, 0.6], labels=['Polskie', 'Zagraniczne'], title="Stosunek artystów polskich do zagranicznych", hole=.4)
fig2.show()
