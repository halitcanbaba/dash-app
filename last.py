import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input, Output
from datetime import date

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "position": "",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H4("Login:", className="mb-0 ml-0"), width=4
                    ),
                dbc.Col(
                    dbc.Input(type="search", placeholder="Search here"), width=8
                    ),
            ]
        ),        
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("Name:", className="text-black-50 font-weight-lighter"), width=4
                    ),
                dbc.Col(
                     html.Div("Ad,Soyad", className="text-left Bold text"), width=8
                    ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("Group:", className="text-black-50 font-weight-lighter"), width=4
                    ),
                dbc.Col(
                     html.Div("Group", className="text-left Bold text"), width=8
                    ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("Leverage:", className="text-black-50 font-weight-lighter"), width=4
                    ),
                dbc.Col(
                     html.Div("1:100", className="text-left Bold text"), width=8
                    ),
                dbc.Col(
                    html.Div("Zip:", className="text-black-50 font-weight-lighter"), width=4
                    ),
                dbc.Col(
                     html.Div("500", className="text-left Bold text"), width=8
                    ),
            ]
        ),
        html.Hr(),        

        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

distance = [
    dbc.DropdownMenuItem("Today"),
    dbc.DropdownMenuItem("Last Week"),
    dbc.DropdownMenuItem("Last Month"),
    dbc.DropdownMenuItem("Last Year"),
]

df = pd.DataFrame(
    {
        "Item": ["Arthur", "Ford", "Zaphod", "Trillian"],
        "Total Lot": ["Dent", "Prefect", "Beeblebrox", "Astra"],
        "Total Profit": ["Dssent", "Prefect", "Beeblebrox", "Astra"],
        "Total Time": ["Dssent", "Prefect", "Beeblebrox", "Astra"],
    }
)


rr_row0 = html.Tr([html.Th("RR Ratio"), html.Th("%RR%")])
rr_row1 = html.Tr([html.Td("LOSS_LOT"), html.Td("Dent")])
rr_row2 = html.Tr([html.Td("LOSS"), html.Td("Prefect")])
rr_row3 = html.Tr([html.Td("WIN_LOT"), html.Td("Beeblebrox")])
rr_row4 = html.Tr([html.Td("WIN"), html.Td("Astra")])
rr_table_body = [html.Tbody([rr_row0, rr_row1, rr_row2, rr_row3, rr_row4])]

indicative_row0 = html.Tr([html.Td("MARKET PL INDICATIVE"), html.Td("%RR%")])
indicative_row1 = html.Tr([html.Td("SPREAD COST INDICATIVE"), html.Td("Dent")])
indicative_row2 = html.Tr([html.Td("COMMISSION"), html.Td("Prefect")])
indicative_row3 = html.Tr([html.Td("SWAP"), html.Td("Beeblebrox")])
indicative_row4 = html.Tr([html.Td("GROSS PL"), html.Td("Astra")])
indicative_table_body = [html.Tbody([indicative_row0, indicative_row1, indicative_row2, indicative_row3, indicative_row4])]

page = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.DatePickerSingle(
                    id='my-date-picker-single-start',
                    min_date_allowed=date(1995, 8, 5),
                    max_date_allowed=date(2017, 9, 19),
                    initial_visible_month=date(2017, 8, 5),
                    date=date(2017, 8, 25),
                    className='mr-3'
                ),
                dcc.DatePickerSingle(
                    id='my-date-picker-single-endd',
                    min_date_allowed=date(1995, 8, 5),
                    max_date_allowed=date(2017, 9, 19),
                    initial_visible_month=date(2017, 8, 5),
                    date=date(2017, 8, 25),
                    className='mr-3',
                    style={"width": "1rem"}
                ),
                html.Div(id='output-container-date-picker-single-endd')
            ])
        ],width=3),
        dbc.Col([
            dbc.DropdownMenu(
                distance, label="All History", color="secondary", className="mb-6 ml-5", bs_size="sm"
            ),
        ], width=2),

    ],className='mb-2 mt-2'),
    dbc.Row([

        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("Account: %Acc%", className="card-title"),
                        dbc.Table(rr_table_body, bordered=False)]
                ),
                style={"width": "18rem"},
            )            
        ], width=4),

        dbc.Col([
            html.Div([dbc.Alert("Winner Symbols", color="success", style={"text-align": "center"})]),
            dbc.Table.from_dataframe(df, striped=False, bordered=False, hover=True, dark=True, responsive=True)
        ], width=8),



    ],className='mb-2'),


    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Table(indicative_table_body, bordered=False)]
                ),
                style={"width": "18rem"},
            )            
        ], width=4),

        dbc.Col([
            html.Div([dbc.Alert("Loser Symbols", color="danger", style={"text-align": "center"})]),
            dbc.Table.from_dataframe(df, striped=False, bordered=False, hover=True, dark=True, responsive=True)
            ], width=8),

    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='line-chart', figure={}),
                ])
            ]),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='bar-chart', figure={}),
                ])
            ]),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='pie-chart', figure={}),
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
], style= CONTENT_STYLE, fluid=False
)




content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content, page])


# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname == "/":
#         return html.P("This is the content of the home page!")
#     elif pathname == "/page-1":
#         return html.P("This is the content of page 1. Yay!")
#     elif pathname == "/page-2":
#         return html.P("Oh cool, this is page 2!")
#     # If the user tries to reach a different page, return a 404 message
#     return dbc.Jumbotron(
#         [
#             html.H1("404: Not found", className="text-danger"),
#             html.Hr(),
#             html.P(f"The pathname {pathname} was not recognised..."),
#         ]
#     )


if __name__ == "__main__":
    app.run_server(port=4242, debug=True)