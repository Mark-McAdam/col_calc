from joblib import load
pipeline = load('assets/pipeline.joblib')
print('!!! Pipeline Loaded !!!')

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from app import app


column1 = dbc.Col(
    [
        dcc.Markdown('### Predicted Cost of Living', className='mb-4'), 
        dcc.Markdown('##### Based on 566 Cities', className='mb-3'), 
        dcc.Markdown('##### Across 166 Countries', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),



        
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('#### Rent Index'), 
        dcc.Slider(
            id='rent_index', 
            min=5, 
            max=165, 
            step=6, 
            value=27, 
            marks={n: str(n) for n in range(5,165,31)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Restaurant Price Index'), 
        dcc.Slider(
            id='restaurant_price_index', 
            min=10, 
            max=145, 
            step=5, 
            value=58, 
            marks={n: str(n) for n in range(5,160,31)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Groceries Index'), 
        dcc.Slider(
            id='groceries_index', 
            min=20, 
            max=135, 
            step=5, 
            value=56, 
            marks={n: str(n) for n in range(5,160,31)}, 
            className='mb-5', 
        ), 


         
    ],
    md=4,
)

column3 = dbc.Col(
    [
        dcc.Markdown('#### Apartment City Center 1 Bed'), 
        dcc.Slider(
            id='apartment_city_center_1bed', 
            min=85, 
            max=3350, 
            step=5, 
            value=750, 
            marks={n: str(n) for n in range(85,3350,500)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Apartment Utilities'), 
        dcc.Slider(
            id='apartment_utilities', 
            min=15, 
            max=350, 
            step=5, 
            value=135, 
            marks={n: str(n) for n in range(5,350,60)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Internet Monthly'), 
        dcc.Slider(
            id='internet_monthly', 
            min=5, 
            max=235, 
            step=5, 
            value=40, 
            marks={n: str(n) for n in range(5,235,45)}, 
            className='mb-5', 
        ), 


         
    ],
    md=4,
)

layout = dbc.Row([column1, column2, column3])

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input(component_id='rent_index', component_property='value'), 
    Input(component_id='restaurant_price_index', component_property='value'),
    Input(component_id='groceries_index', component_property='value'),
    Input(component_id='apartment_city_center_1bed', component_property='value'),
    Input(component_id='apartment_utilities', component_property='value'),
    Input(component_id='internet_monthly', component_property='value')
    ],
)
def predict (rent_index, restaurant_price_index, groceries_index, apartment_city_center_1bed, apartment_utilities, internet_monthly):
  df = pd.DataFrame(
      columns = ['rent_index', 'restaurant_price_index', 'groceries_index', 'apartment_city_center_1bed', 'apartment_utilities', 'internet_monthly'],
      data = [[rent_index, restaurant_price_index, groceries_index, apartment_city_center_1bed, apartment_utilities, internet_monthly]]
  )
  y_pred = pipeline.predict(df)[0]
  return f'Cost of Living {y_pred:.2f}'
