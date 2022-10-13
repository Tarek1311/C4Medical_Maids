import dash_bootstrap_components as dbc
from dash import html, dcc

BED_IMAGE = (
    "https://www.stiegelmeyer.com/fileadmin/_processed_/3/5/csm_10"
    "-21090_Puro_Pflegeszene_Patient_verstellt_RL_2017_09_59e8c475b3.jpg"
)

BED_DESCRIPTION = """C4Medical_Maids met à la disposition des particuliers le matériel médical et les services 
associés nécessaires à la mise en place d’une hospitalisation ou de soins à domicile. Se soigner chez soi et profiter 
de ses proches, c’est possible avec l’Hospitalisation A Domicile (HAD) ou le Maintien A Domicile (MAD)."""

bed_col = dbc.Col(
    html.Div(
        dbc.Card(
            [
                dbc.CardImg(src=BED_IMAGE, top=True),
                dbc.CardBody(
                    [
                        html.H4("Location d'un lit médicalisé", className="card-title"),
                        html.P(BED_DESCRIPTION, className="card-text"),
                        dbc.Button(
                            "En savoir plus",
                            id="open-bed",
                            color="warning",
                            style={"margin": "auto", "width": "100%"},
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader("Lit médicalisé"),
                                dbc.ModalBody(
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id="bed-dropdown",
                                                options=[
                                                    {
                                                        "label": "Lit médicalisé standard",
                                                        "value": "LMS",
                                                    },
                                                    {
                                                        "label": "Lit médicalisé XXL",
                                                        "value": "LMXXL",
                                                    },
                                                    {
                                                        "label": "Lit médicalisé pour les enfants",
                                                        "value": "LMPLE",
                                                    },
                                                ],
                                                value="LMS",
                                                placeholder="",
                                            ),
                                            html.Div(id="output-container"),
                                        ]
                                    )
                                ),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Fermer",
                                        id="close-bed",
                                        className="ml-auto",
                                    )
                                ),
                            ],
                            id="modal-bed",
                        ),
                    ]
                ),
            ],
            style={"width": "18rem"},
        )
    )
)
