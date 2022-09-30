import base64
from io import BytesIO
import dash_auth
import dash_bootstrap_components as dbc
import requests
from dash import html, dcc, Dash, Output, Input, State

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {"1": "2"}

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

app.layout = html.Div(
    [
        html.H1("Welcome to the app"),
        html.H3("You are successfully authorized"),
        dcc.Dropdown(options=["A", "B"], value="A", id="dropdown"),
        dcc.Graph(id="graph"),
    ],
    className="container",
)


@app.callback(Output("graph", "figure"), [Input("dropdown", "value")])
def update_graph(dropdown_value):
    return {
        "layout": {
            "title": "Graph of {}".format(dropdown_value),
            "margin": {"l": 20, "b": 20, "r": 10, "t": 60},
        },
        "data": [{"x": [1, 2, 3], "y": [4, 1, 2]}],
    }


PLOTLY_LOGO = (
    "https://st2.depositphotos.com/4362315/7819/v/950/"
    "depositphotos_78194060-stock-illustration-"
    "medical-logo-health-care-center.jpg"
)

nav_item = dbc.NavItem(
    dbc.NavLink(
        "ACCUEIL",
        href="/",
    )
)

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(
            "Qui sommes-nous ?",
            href="https://www.myrectoverso.com/static/upload/25-392-7.jpg",
        ),
        dbc.DropdownMenuItem("Youtube Channel", href="https://cryptopotluck.com/"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem(
            "Projet Github",
            href="https://github.com/Tarek1311/C4Medical_Maids",
        ),
        dbc.DropdownMenuItem(
            "services pour les EHPAD",
            href="https://lemagcertification.afnor.org/wp-content/uploads/2018/01/GettyImages-587940524.jpg",
        ),
        dbc.DropdownMenuItem(
            "Maintenance et SAV",
            href="https://ems-concept.com/ems/wp-content/uploads/2011/07/EMS-Concept-Services-770x412.jpg",
        ),
    ],
    nav=True,
    in_navbar=True,
    label="PLUS",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("C4Medical Maids", className="ml-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plot.ly",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        nav_item,
                        dropdown,
                    ],
                    className="ml-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-5",
)

"""App Components"""


def enconde_image(image_url):
    buffered = BytesIO(requests.get(image_url).content)
    image_base64 = base64.b64encode(buffered.getvalue())
    return b"data:image/png;base64," + image_base64


DropdownApp = html.Div(
    [
        dcc.Dropdown(
            id="my-dropdown",
            options=[
                {"label": "Lit médicalisé standard", "value": "NYC"},
                {"label": "Lit médicalisé XXL", "value": "TX"},
                {"label": "Lit médicalisé pour les enfants", "value": "SF"},
            ],
            value="NYC",
            placeholder="Select a city",
        ),
        html.Div(id="output-container"),
    ]
)


def transform_value(value):
    return 10**value


TextApp = html.Div(
    [
        html.H1("Common Words Graph"),
        dcc.Graph(
            id="txt-graph",
            animate=True,
            style={"backgroundColor": "#1a2d46", "color": "#ffffff"},
        ),
        dcc.Textarea(
            id="txt", placeholder="Common Words...", value="", style={"width": "100%"}
        ),
        html.Div(id="text-output-container", style={"margin-top": 20}),
    ]
)

SliderApp = html.Div(
    [
        html.H1("Square Root Slider Graph"),
        dcc.Graph(
            id="slider-graph",
            animate=True,
            style={"backgroundColor": "#1a2d46", "color": "#ffffff"},
        ),
        dcc.Slider(
            id="slider-updatemode",
            marks={i: "{}".format(i) for i in range(20)},
            max=20,
            value=2,
            step=1,
            updatemode="drag",
        ),
        html.Div(id="updatemode-output-container", style={"margin-top": 20}),
    ]
)

"""Body Components"""
cardOne = dbc.Card(
    [
        dbc.CardImg(
            src="https://www.stiegelmeyer.com/"
            "fileadmin/_processed_/3/5/"
            "csm_10-21090_Puro_Pflegeszene_Patient"
            "_verstellt_RL_2017_09_59e8c475b3.jpg",
            top=True,
        ),
        dbc.CardBody(
            [
                html.H4("Location d'un lit médicalisé", className="card-title"),
                html.P(
                    "C4Medical_Maids met à la disposition"
                    " des particuliers le matériel médical "
                    "et les services associés nécessaires"
                    " à la mise en place d’une hospitalisation "
                    "ou de soins à domicile."
                    "Se soigner chez soi et profiter de ses proches,"
                    " c’est possible avec l’Hospitalisation A Domicile (HAD) "
                    "ou le Maintien A Domicile (MAD).",
                    className="card-text",
                ),
                dbc.Button(
                    "En savoir plus",
                    id="open",
                    color="warning",
                    style={"margin": "auto", "width": "100%"},
                ),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Modal"),
                        dbc.ModalBody(DropdownApp),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close", className="ml-auto")
                        ),
                    ],
                    id="modal",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

cardTwo = dbc.Card(
    [
        dbc.CardImg(
            src="https://1736922617.rsc.cdn77.org/"
            "wp-content/webp-express/webp-images/"
            "doc-root/wp-content/uploads/"
            "2018/04/AdobeStock_215049877-1.jpeg.webp",
            top=True,
        ),
        dbc.CardBody(
            [
                html.H4("Location d'un fauteuil roulant", className="card-title"),
                html.P(
                    "C4Medical_Maids propose des fauteuils roulants manuels,"
                    " confortables, légers et facilement transportables. "
                    "Différents accessoires sont disponibles : "
                    "appuie-tête, gouttière, tablette amovible, "
                    "coussin de positionnement, dossier fixe ou inclinable."
                    "La largeur d’assise dépendra de votre morphologie. "
                    "Plusieurs tailles existent en magasin.",
                    className="card-text",
                ),
                dbc.Button(
                    "En savoir plus",
                    id="opentwo",
                    color="primary",
                    style={"margin": "auto", "width": "100%"},
                ),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Modal"),
                        dbc.ModalBody(SliderApp),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="closetwo", className="ml-auto")
                        ),
                    ],
                    id="modaltwo",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

cardThree = dbc.Card(
    [
        dbc.CardImg(
            src="https://www.pharmacie-leroy.fr/"
            "wp-content/uploads/"
            "sites/5955/2018/06/"
            "location_souleve_malade.jpeg",
            top=True,
        ),
        dbc.CardBody(
            [
                html.H4("Location d'un lève-malades", className="card-title"),
                html.P(
                    "Le lève-malades, "
                    "appelé aussi lève-personnes,"
                    " permet aux personnes"
                    " à mobilité réduite d’être transférées "
                    "d’un endroit à un autre,"
                    " tels que le lit,"
                    " le fauteuil roulant "
                    "ou encore les toilettes "
                    "ou la salle de bains."
                    " Le lève-personnes offre également "
                    "la possibilité de passer d’une position assise"
                    " à une position allongée."
                    "Il s’agit d’une réelle aide technique "
                    "pour les aidants qui peuvent "
                    "ainsi réaliser les transferts en toute sécurité, "
                    "sans effort physique.",
                    className="card-text",
                ),
                dbc.Button(
                    "En savoir plus",
                    id="openthree",
                    color="success",
                    style={"margin": "auto", "width": "100%"},
                ),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Modal"),
                        dbc.ModalBody(TextApp),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="closethree", className="ml-auto")
                        ),
                    ],
                    id="modalthree",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

card_content = [
    dbc.CardHeader("C4Medical Maids"),
    dbc.CardBody(
        [
            html.H5(
                "Enseigne nationale de vente et location de matériel médical ",
                className="card-title",
            ),
            html.P(
                "Vous propose son matériel performant et de qualité,"
                " ses conseils pour l'adaptation et la mise en place,"
                " avec un service de maintenance permanent."
                "Confort assuré pour les bénéficiaires,"
                "tranquillité des familles "
                "et optimisation de travail des équipes soignantes.",
                className="card-text",
            ),
        ]
    ),
]

"""Body"""
row = html.Div(
    [
        dbc.Row(
            html.Img(
                src="https://porterchester.edu/"
                "sites/default/files/"
                "styles/blogfeature_large/"
                "public/field/image"
                "/MedicalAssistantEmpathy"
                ".jpg?itok=YjvZDOrb",
                style={
                    "float": "right",
                    "clear": "right",
                    "margin-left": "10%",
                    "width": "80vw",
                    "height": "30vh",
                },
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    dbc.Col(dbc.Card(card_content, color="dark", inverse=True)),
                )
            )
        ),
        dbc.Row(html.P("")),
        dbc.Row(
            [
                dbc.Col(html.Div(cardOne)),
                dbc.Col(html.Div(cardTwo)),
                dbc.Col(html.Div(cardThree)),
            ],
            style={"margin": "auto", "width": "80vw"},
        ),
    ]
)
##

"""Layout"""

app.layout = html.Div([navbar, row])

"""Apps Functions"""


@app.callback(Output("output-container", "children"), [Input("my-dropdown", "value")])
def update_output(value):
    NYC_img = enconde_image("https://www.altivie.fr/api/media/w_433/CvvaQZ_8Y.jpg")
    TX_img = enconde_image("https://www.altivie.fr/api/media//MwqGVQ4hK.jpg")
    SF_img = enconde_image(
        "https://i.pinimg.com/originals/66/6a/a8/666aa81ff3a685bb4f8ee1decab26989.jpg"
    )
    if value == "NYC":
        return html.Div(
            html.Img(src=NYC_img.decode(), style={"width": "100%", "height": "400px"})
        )
    elif value == "TX":
        return html.Div(
            html.Img(src=TX_img.decode(), style={"width": "100%", "height": "400px"})
        )
    elif value == "SF":
        return html.Div(
            html.Img(src=SF_img.decode(), style={"width": "100%", "height": "400px"})
        )


@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modaltwo", "is_open"),
    [Input("opentwo", "n_clicks"), Input("closetwo", "n_clicks")],
    [State("modaltwo", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modalthree", "is_open"),
    [Input("openthree", "n_clicks"), Input("closethree", "n_clicks")],
    [State("modalthree", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)


def run():
    app.run_server(debug=True, port=8888)


if __name__ == "__main__":
    run()
