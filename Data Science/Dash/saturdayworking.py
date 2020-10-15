import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets= external_stylesheets)

app.layout = html.Div([
    html.H6("This is the heading"),
    html.Div(["Input: ", dcc.Input(id="my-input", value = "initial value", type = 'text')]),
    html.Br(),
    html.Div(id="my-outputs"),
])


@app.callback(
    Output(component_id = "my-outputs", component_property= "children"),
    [Input(component_id = 'my-input' , component_property = 'value')],
)
def funct(inputtext):
    return "Output:  {}".format(inputtext)

if __name__ == "__main__":
    app.run_server(debug=True)