from dash import Dash, html, dcc, Input, Output, html
import plotly.express as px
import pandas as pd
import seaborn as sns
import dash_bootstrap_components as dbc


# Create the Dash app object
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

x = [1,2,3,4,5]
y_sales = [0, 0, 0, 0, 0, 0, 0, 0]
range = ['1/2 - 1/8', '1/9 - 1/15', '1/16 - 1/22', '1/23 - 1/29', '1/30 - 2/5', '2/6 - 2/12', '2/13 - 2/19', '2/20 - 2/26', ]
leads = [0, 0, 0, 0, 0, 0, 0, 600]
x = [1,2,3,4,5]
y = [1,3,4,5,6]



line_01 = px.line( x = range , y = leads, title = 'Qualified Leads in Pipeline', template='simple_white', labels={'x': 'Week', 'y': 'Number of Qualified Lead'} )    
bar_01 = px.bar( x = range , y = y_sales, title = 'Prospects Added', template='simple_white', labels={'x': 'Week', 'y': 'Number of Prospects'})   
bar_02 = px.bar( x = range , y = y_sales, title = 'Number of Scheduled Activities (calls, emails, meetings)', template='simple_white', labels={'x': 'Week', 'y': 'Number of Activities'})  


row_content = [
    dbc.Col( dcc.Graph( id='bar_01', figure=bar_01 )),
    dbc.Col(dcc.Graph( id='bar_02', figure=bar_02 )),
]

tab1_content = dbc.Card(
    dbc.CardBody(
        [ 
            dbc.Row(
            [
                dbc.Col(dbc.Toast( [html.P("0 %", className="mb-0")], header="Conversion rate", style={'margin':'5px',})),
                dbc.Col(dbc.Toast( [html.P("0", className="mb-0")], header="Total current sponsor revenue vs target", style={'margin':'5px',})),
                dbc.Col(dbc.Toast( [html.P("0", className="mb-0")], header="Expected Closed Deals in the next 4 weeks", style={'margin':'5px',})),
            ]
        ),
        dbc.Row(dbc.Col( dcc.Graph( id='line_01', figure=line_01 ))),
           dbc.Row(
            row_content,
            justify="around",
        ),
        ] ), className="mt-3", )

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Events Performance", className="card-text"),
            dbc.Button("To be Updated", color="danger"),
        ]
    ), className="mt-3", )

 
app.layout = html.Div(
    # Add a header to the page  
    children=[html.H1(children='Extreme Hangout', style={'padding':'5px',}),
    
    dbc.Tabs( [
                dbc.Tab(tab1_content , label="Sales Performance", tab_id="tab-1"),
                dbc.Tab(tab2_content, label="Event Performance", tab_id="tab-2"),
                html.Div(id="content")
              ], id="tabs"),

    ], style={'padding':'15px',} 

 )

# @app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
# def switch_tab(at):
#     if at == "tab-1":
#         tab1_content=  html.Div([ 
#                                 dbc.Toast( [html.P("50 %", className="mb-0")], header="Conversion rate", style={'margin':'15px',}),
#                                 dbc.Toast( [html.P("50 %", className="mb-0")], header="Conversion rate", style={'margin':'15px',} )
#                                     ])
#         return tab1_content
#     elif at == "tab-2":
#         return tab2_content
#     return html.P("This shouldn't ever be displayed...")    
     
if __name__ == '__main__': 
    app.run_server()