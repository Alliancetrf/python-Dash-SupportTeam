from dash import Dash, dcc, html  # Updated imports to use the latest Dash module structure

app = Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Support Team Manager:'),

    html.Div(children='''
        Here is an overview of your team's performance.
    '''),

    dcc.Graph(
        id='team-performance-graph',  # Updated to a more descriptive ID
        figure={
            'data': [
                {'x': ['James', 'Thomas', 'Willy', 'Aron', 'Wilfred', 'Adam'], 
                 'y': [4, 1, 2, 3, 4, 5],  # Fixed data mismatch
                 'type': 'bar', 
                 'name': 'SF'},
            ],
            'layout': {
                'title': 'Support Team Members Calls Taken YTD'
            }
        }
    ),
    dcc.Graph(
        id='system-issues-graph',  # Updated to a more descriptive ID
        figure={
            'data': [
                {'x': ['Production System', 'Training System'], 
                 'y': [10, 40], 
                 'type': 'bar', 
                 'name': 'WA'},
            ],
            'layout': {
                'title': 'Overview of Production vs Training System Reported Issues'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)  # Set debug to False for production

