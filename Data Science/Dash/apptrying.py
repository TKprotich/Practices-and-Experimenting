import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = [""]
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)


app.layout = html.Div([html.H1("My Title"),
                  html.Div(["Input : ", dcc.Input(id = 'myinput', value = "initial value")]),
                  html.Br(),
                  html.Div(id = "myoutput"),])
@app.callback(Output(component_id = 'myoutput', component_property = 'children'),
               [Input(component_id = 'myinput', component_property = 'value')]
               )
def funct(inputv):
    return 'Output: {}'.format(inputv)

if __name__ =="__main__":
    app.run_server(debug=True)

