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
           ### A manager at the bank is disturbed with more and more customers leaving their credit card services. 
           They would really appreciate it if one could predict for them who is going to get churned, 
           so they could proactively go to the customer to provide them with better services and turn customers' decisions in the opposite direction.

            ## Is the Customer Churned?

            """
        ),
        dcc.Link(dbc.Button('Try it out!', color='primary'), href='/predictions'),
        dcc.Markdown(
            """

            ### For more details...

            """
        ),
        dcc.Link(dbc.Button('Check insights', color='primary'), href='/insights'),
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)
df = pd.read_csv('https://raw.githubusercontent.com/Annapurnaj91/Creditcardcustomers/main/BankChurners.csv')
fig = px.scatter(df, x="Customer_Age", y="Total_Trans_Amt", color="Attrition_Flag",
           hover_name="Attrition_Flag", size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])