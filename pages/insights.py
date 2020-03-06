# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            ### Baseline Accuracy 
            If you predicted the mean for every city, the conclusion would be every city has a cost of living index of 61.68

            ### Mean Absolute Error
            If you predicted the mean for every city, the conclusion would have a mean absolute error of 18.40

            ### Manipulation
            Smaller dataset meant I could distort my numbers for validation and test accuracy by setting a different random state for the split. This is what I felt like I earned instead of what I wanted to show off. 


            """
        ),

    ],
    md=4,

)

column2 = dbc.Col(
    [
        html.Img(src='assets/svr_val.png', className='img-fluid'),
        html.Img(src='assets/sgd_val.png', className='img-fluid'),
        html.Img(src='assets/bay_val.png', className='img-fluid'),
        html.Img(src='assets/lasso_val.png', className='img-fluid'),
        html.Img(src='assets/ard_val.png', className='img-fluid'),
        html.Img(src='assets/par_val.png', className='img-fluid'),
        html.Img(src='assets/theil_val.png', className='img-fluid'),
        html.Img(src='assets/linear_val.png', className='img-fluid'),
    
    ],
    md=4,
)

column3 = dbc.Col(
    [
        html.Img(src='assets/svr_test.png', className='img-fluid'),
        html.Img(src='assets/sgd_test.png', className='img-fluid'),
        html.Img(src='assets/bay_test.png', className='img-fluid'),
        html.Img(src='assets/lasso_test.png', className='img-fluid'),
        html.Img(src='assets/ard_test.png', className='img-fluid'),
        html.Img(src='assets/par_test.png', className='img-fluid'),
        html.Img(src='assets/theil_test.png', className='img-fluid'),
        html.Img(src='assets/linear_test.png', className='img-fluid'),
    ],
    md=4,
)




layout = dbc.Row([column1, column2, column3])


