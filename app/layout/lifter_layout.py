import dash_bootstrap_components as dbc
from dash import html, dcc

PATIENT_LIFTER_IMAGE = (
    "https://www.pharmacie-leroy.fr/wp-content/uploads/sites/5955/2018/06/"
    "location_souleve_malade.jpeg"
)

PATIENT_LIFTER_DESCRIPTION = """Le lève-malades, appelé aussi lève-personnes,permet aux personnesà mobilité réduite 
d’être transférées d’un endroit à un autre, tels que le lit, le fauteuil roulant ou encore les toilettes ou la salle 
de bains. Le lève-personnes offre également la possibilité de passer d’une position assise à une position allongée. 
Il s’agit d’une réelle aide technique pour les aidants qui peuvent ainsi réaliser les transferts en toute sécurité,
sans effort physique."""

patient_lifter_col = dbc.Col(
    html.Div(
        dbc.Card(
            [
                dbc.CardImg(src=PATIENT_LIFTER_IMAGE, top=True),
                dbc.CardBody(
                    [
                        html.H4("Location d'un lève-malades", className="card-title"),
                        html.P(PATIENT_LIFTER_DESCRIPTION, className="card-text"),
                        dbc.Button(
                            "En savoir plus",
                            id="open-lifter",
                            color="warning",
                            style={"margin": "auto", "width": "100%"},
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader("Lève-malades médicalisé"),
                                dbc.ModalBody(
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id="lifter-dropdown",
                                                options=[
                                                    {
                                                        "label": "lève-malades médicalisé standard",
                                                        "value": "LMS",
                                                    },
                                                    {
                                                        "label": "lève-malades médicalisé XXL",
                                                        "value": "LMXXL",
                                                    },
                                                    {
                                                        "label": "lève-malades médicalisé pour les enfants",
                                                        "value": "LMPLE",
                                                    },
                                                ],
                                                value="LMMS",
                                                placeholder="",
                                            ),
                                            html.Div(id="output-containerLifter"),
                                        ]
                                    )
                                ),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Fermer",
                                        id="close-lifter",
                                        className="ml-auto",
                                    )
                                ),
                            ],
                            id="modal-lifter",
                        ),
                    ]
                ),
            ],
            style={"width": "18rem"},
        )
    )
)
