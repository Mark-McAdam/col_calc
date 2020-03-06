# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Know Before You Go

            """
        ),
        dcc.Markdown(
            """

            Estimate the cost of living, using easy to find, everyday information. 

            C.O.L. Calculator allows you to determine the overall cost of living for a given area. Based on an index of rent, restaurant prices and groceries, living expenses are added in. The output is a number that allows you to compare the Cost of Living across different cities.


            """
        ),
        dcc.Link(dbc.Button('Calc your C.O.L.', color='primary'), href='/calculator')
    ],
    md=4,
)



# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)



column2 = dbc.Col(
    [
        html.Img(src='assets/dist_plot_index.png', className='img-fluid'),

    ]
)

layout = dbc.Row([column1, column2])