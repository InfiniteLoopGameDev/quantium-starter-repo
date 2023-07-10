from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

data_file = pd.read_csv('data/pink_morsel.csv')

fig = px.line(data_file, x='date', y='sales', color='region')

app.layout = html.Div([
    html.H1('Pink Morsel Sales', style={
        'textAlign': 'center',
        'fontFamily': 'sans-serif'
    }),
    dcc.Graph(figure=fig)
])
                      
if __name__ == '__main__':
    app.run(debug=True)