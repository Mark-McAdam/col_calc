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
            ### Feature Engineering
            I had a column that obviously leaked data, it was a combination of the target I was trying to predict, cost of living and rent together. When using this column to train my data I was overfitting the validation test set but very much undercutting the test data. 

            I came across some missing values in the data set. Some countries do not allow alcohol so I had missing values. I created a column that indicated alcohol was not allowed and filled the missing values with the mean. 

            ### Next Time 
            I will try using cross validation instead of doing a train, validation, test split. Depending on the random state I set for the split, I ended up with wildly different values for validation and test. It was possible to make my models appear more effective by declaring a different random state. It was not in the interest of learning more, I believe it was because I had a relatively small data set to begin with. 




            ### My Original Project

            ### First Goals

            I started with a totally different goal in mind. I know a woman who is director of sales for a renal therapy company, she manages 40% of the United States with almost a dozen people working under her. Knowing that many jobs in future are going to automation, she approached me and asked what could be done to get ahead of the impending robot job takeover. We developed a plan to forecast what her sales people would be able to produce, so she could better allocate resources where they would be most affective.

            ### Leakage & Anonymizing 

            A great deal of work went into anonymizing the data so that personal or company information would not be shared. Sales rep names, clinic names, and corporation affiliations all contained high cardinality. Ryan M. suggested a hashing algorithm to anonymize the data, I was learning so much. 

            Once the data was anonymous I worked on feature engineering and data cleaning, I worked with the director to pull other useful data from Salesforce and personal rankings within the company. I learned a new workflow for processing data that was not in a csv file and had to be read in bitwise. 

            The problem with this dataset for a class project was the massive amount of leakage from one column to another. When trying to predict future sales numbers, I only had 2 or 3 columns of data that did not include some form of leakage. Most of the data were integers or floats showing what their trend was, past couple months of performance, or how many patients they had in each area of the market. Everything tied in together to leak everywhere.

            """
        ),

    ],
)

layout = dbc.Row([column1])