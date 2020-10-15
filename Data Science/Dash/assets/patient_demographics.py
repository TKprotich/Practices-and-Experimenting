import dash
import dash_html_components as html
import dash_core_components as dcc
from assets import patient_demographics, patient_med_readmit, alldata
from dash.dependencies import Input, Output

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Data
fh = alldata.opdfh

# Gender
genderfh = pd.DataFrame(fh.GENDER.value_counts())
genderfh = genderfh.reset_index()
genderfig = px.bar(genderfh, x="index", y="GENDER", color= 'GENDER', barmode="group")

# Age
agefh = pd.DataFrame(fh.Age)
agerfig = px.histogram(agefh, x="Age",  nbins=30)


# COROLORRY
corfh = pd.DataFrame(fh.COROLORRY.value_counts())
corfh = corfh.reset_index()
corfig = px.bar(corfh, x="index", y="COROLORRY", color= 'COROLORRY', barmode="group")

tab_1_layout = html.Div([
            # html.H3('Patient Demographics'),

                html.Div([
                    html.Div([
                        html.H6('Gender', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-1',
                            figure= genderfig
                        )
                    ], className="four columns"),

                    html.Div([
                        html.H6('COROLORRY', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-2',
                            figure = corfig
                        )
                    ], className="four columns"),

                    html.Div([
                        html.H6('Age', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-3',
                            figure=agerfig
                        )
                    ], className="four columns")

                ], className="row", style={"margin": "1% 3%"}),

                html.Div([
                    html.Div([
                        html.H6('Race - Gender distribution', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-4',
                            figure={
                                'data': [

                                ],
                                'layout': {
                                    'title': 'Graph-4'
                                }
                            }
                        )
                        ], className="six columns"),

                    html.Div([
                        html.H6('Age - Gender Disrtibution', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-5',
                            figure={
                                'data': [

                                ],
                                'layout': {
                                    'title': 'Graph-5'
                                }
                            }
                        )
                    ], className="six columns"),
                ], className="row", style={"margin": "1% 3%"}),

                html.Div([
                    html.Div([
                        html.H6('Race - Age Disrtibution', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-6',
                            figure=agerfig
                        )
                    ])
                ], className="row", style={"margin": "1% 3%"})

            ]
        )