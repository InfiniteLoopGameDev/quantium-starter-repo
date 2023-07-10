from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

data = pd.read_csv('data/pink_morsel.csv')
data = data.sort_values(by="date")

fig = px.line(data, x='date', y='sales', color='region')

graph = dcc.Graph(
    figure=fig,
    style={
        'width' : '80vw',
        'height' : '80vh',
        'display': 'block',
        'margin': 'auto',
    },
    id='graph')

header = html.H1('Pink Morsel Sales', style={
        'textAlign': 'center',
        'fontFamily': 'sans-serif'
})

radio = dcc.RadioItems(
    ["North", "East", "South", "West", "All"],
    "All",
    id="radio",
    inline=True,
    labelStyle={
        'padding': '1em',
    },
    style={
        'textAlign': 'center',
        'fontFamily': 'sans-serif',
        'display': 'block',
    }
)

app.layout = html.Div([
    header,
    graph,
    radio
])

@callback(
    Output('graph', 'figure'),
    Input('radio', 'value'))
def update_graph(selected):
    selected = [selected.lower()]
    if selected == ["all"]:
        selected = ["north", "east", "south", "west"]
    filtered_data = data[data.region.isin(selected)]
    fig = px.line(filtered_data, x='date', y='sales', color='region', labels={
    'date': 'Date',
    'sales': 'Sales ($)',
    'region': 'Region',
})
    fig.update_layout()
    return fig
                      
if __name__ == '__main__':
    app.run_server(debug=True)