# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            The original dataset had 18 features, all continuous variables, regression was chosen to predict the cost of living index, after noticing many of the features had a linear relationship with the target. I tried eight different linear models, and also gradient boosting. 

            -   SVR

            -   SGD Regressor

            -   Bayesian Ridge

            -   LassoLars

            -   ARD Regression

            -   Passive Aggressive Regressor

            -   Theil Sen Regressor

            -   Linear Regression
        
            -   XGBoost


            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/col_rrg.png', className='img-fluid'),
        html.Img(src='assets/col_aai.png', className='img-fluid'),
                dcc.Markdown(
            """
  
            This could have been a classification problem if I rephrased the goal. Instead of predicting a cost of living index number, I could have predicted if a city had “high” or “low” cost of living, and set a threshold to differentiate. 

            """
        ),
    ],
    md=8,

)

layout = dbc.Row([column1, column2])