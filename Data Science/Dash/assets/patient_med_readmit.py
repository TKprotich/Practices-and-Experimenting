import dash
import dash_html_components as html
import dash_core_components as dcc
from assets import patient_demographics, patient_med_readmit, alldata
from dash.dependencies import Input, Output


fh = alldata.opdfh

tab_2_layout = html.Div([
            html.Div([
                html.Div([
                    html.H6('Department'),
                    dcc.Graph(
                        id='med-graph-1',
                        figure={
                            'data': [

                            ],
                            'layout': {
                                'title': 'Graph-1'
                            }
                        }
                    )
                ], className="six columns"),

                html.Div([
                    html.H6('Readmission'),
                    dcc.Graph(
                        id='med-graph-2',
                        figure={
                            'data': [

                            ],
                            'layout': {
                                'title': 'Graph-2'
                            }
                        }
                    )
                ], className="six columns"),

            ], className="row", style={"margin": "1% 3%"})
    ])