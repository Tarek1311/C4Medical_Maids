import dash_bootstrap_components as dbc
from dash import html, dcc

WHEELCHAIR_IMAGE = (
    "https://1736922617.rsc.cdn77.org/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/"
    "2018/04/AdobeStock_215049877-1.jpeg.webp"
)

Wheelchair_DESCRIPTION = """C4Medical_Maids propose des fauteuils roulants manuels, confortables, légers et facilement 
transportables. Différents accessoires sont disponibles : appuie-tête, gouttière, tablette amovible, 
coussin de positionnement, dossier fixe ou inclinable. La largeur d’assise dépendra de votre morphologie. 
Plusieurs tailles existent en magasin."""

Wheelchair_col = dbc.Col(
    html.Div(
        dbc.Card(
            [
                dbc.CardImg(src=WHEELCHAIR_IMAGE, top=True),
                dbc.CardBody(
                    [
                        html.H4(
                            "Location d'un fauteuil roulant", className="card-title"
                        ),
                        html.P(Wheelchair_DESCRIPTION, className="card-text"),
                        dbc.Button(
                            "En savoir plus",
                            id="open-lit",
                            color="warning",
                            style={"margin": "auto", "width": "100%"},
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader("fauteuil médicalisé"),
                                dbc.ModalBody(
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id="Wheelchair-dropdown",
                                                options=[
                                                    {
                                                        "label": "fauteuil médicalisé standard",
                                                        "value": "FMS",
                                                    },
                                                    {
                                                        "label": "fauteuil médicalisé XXL",
                                                        "value": "FMXXL",
                                                    },
                                                    {
                                                        "label": "fauteuil médicalisé pour les enfants",
                                                        "value": "FMPLE",
                                                    },
                                                ],
                                                value="FMS",
                                                placeholder="",
                                            ),
                                            html.Div(id="output-container"),
                                        ]
                                    )
                                ),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Fermer",
                                        id="close-fauteuil",
                                        className="ml-auto",
                                    )
                                ),
                            ],
                            id="modal-fauteuil",
                        ),
                    ]
                ),
            ],
            style={"width": "18rem"},
        )
    )
)
