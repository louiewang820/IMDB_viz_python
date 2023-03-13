from dash import Dash, html, dcc, Input, Output, dash_table
import altair as alt
from vega_datasets import data
import dash_bootstrap_components as dbc
import pandas as pd 
import numpy as np 



# Read in global data
movies = pd.read_csv("data/imdb_top_1000.csv", dtype={'Runtime': str})
movies['Runtime'] = movies['Runtime'].str.extract('(\d+)').astype(int)
movies = movies.loc[:,['Genre','Series_Title','Released_Year','Runtime','IMDB_Rating','Meta_score','No_of_Votes', 'Gross']]
movies['Released_Year'] =movies['Released_Year'].str.extract('(\d+)')
movies = movies.dropna()
movies['Released_Year'] = movies['Released_Year'].astype(int)
movies['Gross_Revenue_in_USD'] = pd.to_numeric(movies['Gross'].str.replace(',', ''))
movies.drop('Gross', axis=1, inplace=True)
# Setup app and layout/frontend
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    html.H1('IMDB Statistics Visualization'),
     dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='table',
                columns=[{"name": col, "id": col, 'selectable': True if col != 'Name' else False, 'type': 'numeric' 
                          if col != 'Series_Title' else 'text'} for col in movies.columns[1:8]],  
                data=movies.to_dict('records'),
                sort_action="native",
                column_selectable="single",
                page_size=10,
                filter_action='native',
                style_cell={'padding': '5px'},
                style_data_conditional=[{
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'}],
                 style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'}
            ),
        ])
    ]),
    dbc.Row([
        dbc.Col([ html.Label('Select Horizontal Column:'),
            dcc.Dropdown(
                id='xcol-widget',
                value='Released_Year',  # REQUIRED to show the plot on the first page load
                options=[{'label': col, 'value': col} for col in movies.columns[2:8]]),
            html.Label('Select Vertical Column:'),
            dcc.Dropdown(
                id='ycol-widget',
                value='Gross_Revenue_in_USD',  # REQUIRED to show the plot on the first page load
                options=[{'label': col, 'value': col} for col in movies.columns[2:8]])],
            md=4),
        dbc.Col([
            dbc.Row([
                dbc.Col()]),
            html.Iframe(
                id='scatter',
                style={'border-width': '0', 'width': '100%', 'height': '400px'})])])])
# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'),
    Input('ycol-widget', 'value'))
def plot_altair(xcol, ycol):
    corl = movies[[xcol,ycol]].corr().iloc[0,1]
    x_min = movies[xcol].min()
    x_max = movies[xcol].max() + (movies[xcol].max() - x_min)/10
    y_min = movies[ycol].min()
    y_max = movies[ycol].max() + (movies[ycol].max() - y_min)/10
    text = alt.Chart({'values':[{}]}).mark_text(
        align="left", baseline="top"
    ).encode(
        x=alt.value(5),  # pixels from left
        y=alt.value(5),  # pixels from top
        text=alt.value(f"r: {corl:.3f}"),
    )    


    scatter = alt.Chart(movies).mark_point().encode(
        x=alt.X(xcol, scale=alt.Scale(domain=[x_min, x_max])),
        y=alt.Y(ycol, scale=alt.Scale(domain=[y_min, y_max])),
        tooltip=['Series_Title','Genre','Released_Year', 'Runtime','IMDB_Rating'])
    scatter = scatter.properties(title = 'Scatter Plot of ' + xcol + ' and ' + ycol)
    output = scatter + text + scatter.transform_regression(xcol,ycol).mark_line(color = 'red')
    return output.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
