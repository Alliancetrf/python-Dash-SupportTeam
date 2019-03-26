import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Support Team Manager:'),

    html.Div(children='''
        Here is an overview of your team's performance.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['James', 'Thomas', 'Willy','Aron','Wilfred','Adam'], 'y': [4, 1, 2,3, 4, 5, 7], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Support Team Members Calls Taken YTD'
            }
        }
    ),
    dcc.Graph(
        id='example-graph2',
        figure={
            'data': [
                {'x': ['Production System','Training System'],'y': [10,40],'type':'bar','name':'WA'},
            ],
            'layout': {
                'title':'Overview of Production vs Training System reported issues'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
 
