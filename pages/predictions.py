from joblib import load
model = load('assets/pipeline.joblib')
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
        dcc.Markdown('## Predict Whether the customer is churn or not?'),
        dcc.Markdown('#### AGE'),
        dcc.Input(
            id="Customer_Age", type="number", placeholder="input with range",
            min=10, max=100,
        ),
        dcc.Markdown('#### Total Number of products with customer'),
        dcc.Input(
            id="Total_Relationship_Count", type="number", placeholder="input with range",
            min=1,
        ),
        dcc.Markdown('#### Months Inactive For 12 Months'),
        dcc.Slider(
            id='Months_Inactive_12_mon', 
            min=1, 
            max=12, 
            step=1, 
            value=15, 
            marks={n: str(n) for n in range(1, 13, 1)}
            ),
        dcc.Markdown('#### Number of bank interactions per year'),
        dcc.Input(
            id="Contacts_Count_12_mon", type="number",placeholder="input with range",
            min=0,
                    ),
        
    ],
    md=4,
)

column2 = dbc.Col(
    [
        
        
        dcc.Markdown('#### Revolving Balance on the credit card'),
        dcc.Input(
            id="Total_Revolving_Bal", type="number",placeholder="input with range",
            min=0,
        ),
        dcc.Markdown('#### Change in transaction Amout(Q4 over Q1)'),
        dcc.Input(
            id="Total_Amt_Chng_Q4_Q1", type="number",placeholder="input with range",
            min=0,
        ),
        dcc.Markdown('#### Total transaction amount(Last 12 Months)'),
        dcc.Input(
            id="Total_Trans_Amt", type="number",placeholder="input with range",
            min=0,
        ),
        dcc.Markdown('#### Total number of transactions(Last 12 Months)'),
        dcc.Input(
            id="Total_Trans_Ct", type="number",placeholder="input with range",
        ),
        dcc.Markdown('#### Change in transaction count(Q4 over Q1)'),
        dcc.Input(
            id="Total_Ct_Chng_Q4_Q1", type="number",placeholder="input with range",
        ),
        html.H2('Customer Churn Risk'),
        html.Div(id='prediction-content',className='lead')
    ]
)
import pandas as pd

@app.callback(
    Output('prediction-content', 'children'), 
    [Input('Customer_Age', 'value'),Input('Total_Relationship_Count', 'value'), Input('Months_Inactive_12_mon', 'value'), 
    Input('Contacts_Count_12_mon', 'value'), Input('Total_Revolving_Bal', 'value'),Input('Total_Amt_Chng_Q4_Q1', 'value'),
    Input('Total_Trans_Amt', 'value'),
    Input('Total_Trans_Ct', 'value'),Input('Total_Ct_Chng_Q4_Q1', 'value')]
)
def predict(Customer_Age,Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon, Total_Revolving_Bal,
    Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,Total_Trans_Ct,Total_Ct_Chng_Q4_Q1):
    # print(island, bill_length, bill_depth, flipper_length, mass, sex)
    
    df = pd.DataFrame(columns=['Customer_Age','Total_Relationship_Count','Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Total_Revolving_Bal','Total_Amt_Chng_Q4_Q1','Total_Trans_Amt','Total_Trans_Ct','Total_Ct_Chng_Q4_Q1'],
       data=[[Customer_Age ,Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon, Total_Revolving_Bal,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,Total_Trans_Ct,Total_Ct_Chng_Q4_Q1]])

    y_pred = model.predict(df)
    score = model.predict_proba(df)


    if y_pred == 0:
        return f"Low"
    else:
        return f"High"
layout = dbc.Row([column1, column2])