# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# custom libraries
import pandas as pd
from sklearn.model_selection import train_test_split

# load model
from joblib import load
model = load('assets/pipeline.joblib')

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Understanding Credit Card Customer Churning Metrics

             I have taken the data set from kaggle, which has 10000 records of the credit card customers. 
             I want to predict whether the customer is an existing customer or if the person has left the bank.
             If the person left the bank I want to check on what basis the customer is leaving the bank, and then I drop some of the columns which cause
             leakage of the data and the data that is unrelated by using permutation importances.


            The target variable of this particular data set is "Attrition Flag", which defines whether the customer is existing or attrited. The target variables
             have imbalanced classes of 83% and 17% respectively.

            So I did two processes, one with the actual target variable and one with balancing my target variable.

             ## With Imbalanced Data:

             The baseline accuracy is 0.83 and hence i can say that it has an imbalance classes
            """
        ),
        html.Img(src='assets/imbalance.png', width=400),
        dcc.Markdown(
            """
            The above graph says that the classes are imbalanced.I split the data into train and validation sets using the 
            train-test-split method from Sklearn.
            Performed Logistic Regression,Random Tree Classifier, Gradient Boosting and Random Search CV for hyperparameter tuning.
            The scores of the models are as follows:

            """
        ),
        html.Img(src='assets/imbalancemetrics.png', width=950),
        dcc.Markdown(
            """
        By seeing the above metrics,we can say that both gradient boosting and Random search CV (Hyperparameter tuning on Random forest classifier)are performing good.
        
        ### Confusion Matrix:
            """
        ),
        html.Img(src='assets/confimbalanc.png', width=400),
        dcc.Markdown(
            """
        The above confusion matrix has more true positives and true negatives comparitively to false positives and false negatives.
        
        ### Classification Report:

            """
        ),

        html.Img(src='assets/reportimbalanc.png', width=950),

        dcc.Markdown(
            """
        ## With Balanced Data:

        I balanced the target variable by oversampling the minority class with the resample method.

        The baseline accuracy is 0.499 after balancing the classes
            """
        ),

        html.Img(src='assets/resampling.png', width=650),
        html.Img(src='assets/balancegraph.png', width=400),
        dcc.Markdown(
            """

        The below are the metrics of the Performed Logistic Regression,Random Tree Classifier, Gradient Boosting and Random Search CV for hyperparameter tuning.
        The scores of the balanced models are as follows:

            """
        ),

        html.Img(src='assets/metricbalanc.png', width=950),

        dcc.Markdown(
            """

        By seeing the above metrics,we can say that both gradient boosting and Random search CV (Hyperparameter tuning on Random forest classifier)are performing good.


        ### Classification Report:


            """
        ),


        html.Img(src='assets/balancedreport.png', width=750),


        dcc.Markdown(

            """


        The above confusion matrix has more true positives and true negatives comparitively to false positives and false negatives.


        ## Conclusion:

        ### As we compare both the balanced and imbalanced class models, we can say that the model performs well after upsampling the target variable. 
        The Precision,Recall and F1 scores are also increasing.

            """
        ),
    ]
)


layout = dbc.Row([column1])