import dash_bootstrap_components as dbc
from dash import html, dcc

from app.layout.bed_layout import bed_col

DESCRIPTION = """Vous propose son matériel performant et de qualité, ses conseils pour l'adaptation et la mise en 
place, avec un service de maintenance permanent. Confort assuré pour les bénéficiaires, tranquillité des familles et 
optimisation de travail des équipes soignantes."""

home_content = html.Div(
    [
        dbc.Row(
            html.Img(
                src="https://porterchester.edu/sites/default/files/styles/blogfeature_large/public/field/image"
                "/MedicalAssistantEmpathy.jpg?itok=YjvZDOrb",
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
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader("C4Medical Maids"),
                                dbc.CardBody(
                                    [
                                        html.H5(
                                            "Enseigne nationale de vente et location de matériel médical ",
                                            className="card-title",
                                        ),
                                        html.P(
                                            DESCRIPTION,
                                            className="card-text",
                                        ),
                                    ]
                                ),
                            ],
                            color="dark",
                            inverse=True,
                        )
                    ),
                )
            )
        ),
        dbc.Row(html.P("")),
        dbc.Row(
            [
                bed_col,
                dbc.Col(
                    html.Div(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src="https://1736922617.rsc.cdn77.org/wp-content/webp-express/webp-images/"
                                    "doc-root/wp-content/uploads/2018/04/AdobeStock_215049877-1.jpeg.webp",
                                    top=True,
                                ),
                                dbc.CardBody(
                                    [
                                        html.H4(
                                            "Location d'un fauteuil roulant",
                                            className="card-title",
                                        ),
                                        html.P(
                                            "C4Medical_Maids propose des fauteuils roulants manuels,confortables,"
                                            " légers et facilement transportables.Différents accessoires sont"
                                            " disponibles : appuie-tête, gouttière, tablette amovible, "
                                            "coussin de positionnement, dossier fixe ou inclinable."
                                            "La largeur d’assise dépendra de votre morphologie. "
                                            "Plusieurs tailles existent en magasin.",
                                            className="card-text",
                                        ),
                                        dbc.Button(
                                            "En savoir plus",
                                            id="opentwo",
                                            color="primary",
                                            style={
                                                "margin": "auto",
                                                "width": "100%",
                                            },
                                        ),
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader("modal-lit"),
                                                dbc.ModalBody(
                                                    html.Div(
                                                        [
                                                            html.H1(
                                                                "Square Root Slider Graph"
                                                            ),
                                                            dcc.Graph(
                                                                id="slider-graph",
                                                                animate=True,
                                                                style={
                                                                    "backgroundColor": "#1a2d46",
                                                                    "color": "#ffffff",
                                                                },
                                                            ),
                                                            dcc.Slider(
                                                                id="slider-updatemode",
                                                                marks={
                                                                    i: "{}".format(i)
                                                                    for i in range(20)
                                                                },
                                                                max=20,
                                                                value=2,
                                                                step=1,
                                                                updatemode="drag",
                                                            ),
                                                            html.Div(
                                                                id="updatemode-output-container",
                                                                style={
                                                                    "margin-top": 20
                                                                },
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                dbc.ModalFooter(
                                                    dbc.Button(
                                                        "close-lit",
                                                        id="closetwo",
                                                        className="ml-auto",
                                                    )
                                                ),
                                            ],
                                            id="modaltwo",
                                        ),
                                    ]
                                ),
                            ],
                            style={"width": "18rem"},
                        )
                    )
                ),
                dbc.Col(
                    html.Div(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src="https://www.pharmacie-leroy.fr/wp-content/uploads/sites/5955/2018/06/"
                                    "location_souleve_malade.jpeg",
                                    top=True,
                                ),
                                dbc.CardBody(
                                    [
                                        html.H4(
                                            "Location d'un lève-malades",
                                            className="card-title",
                                        ),
                                        html.P(
                                            """ Le lève-malades, appelé aussi lève-personnes,permet aux personnes
                                             à mobilité réduite d’être transférées d’un endroit à un autre,tels que 
                                             le lit, le fauteuil roulant ou encore les toilettes ou la salle de bains."
                                             Le lève-personnes offre également la possibilité de passer d’une position 
                                             assise à une position allongée.Il s’agit d’une réelle aide technique 
                                             pour les aidants qui peuvent ainsi réaliser les transferts en toute 
                                             sécurité, sans effort physique.""",
                                            className="card-text",
                                        ),
                                        dbc.Button(
                                            "En savoir plus",
                                            id="openthree",
                                            color="success",
                                            style={
                                                "margin": "auto",
                                                "width": "100%",
                                            },
                                        ),
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader("modal-lit"),
                                                dbc.ModalBody(
                                                    html.Div(
                                                        [
                                                            html.H1(
                                                                "Common Words Graph"
                                                            ),
                                                            dcc.Graph(
                                                                id="txt-graph",
                                                                animate=True,
                                                                style={
                                                                    "backgroundColor": "#1a2d46",
                                                                    "color": "#ffffff",
                                                                },
                                                            ),
                                                            dcc.Textarea(
                                                                id="txt",
                                                                placeholder="Common "
                                                                "Words...",
                                                                value="",
                                                                style={"width": "100%"},
                                                            ),
                                                            html.Div(
                                                                id="text-output-container",
                                                                style={
                                                                    "margin-top": 20
                                                                },
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                dbc.ModalFooter(
                                                    dbc.Button(
                                                        "close-lit",
                                                        id="closethree",
                                                        className="ml-auto",
                                                    )
                                                ),
                                            ],
                                            id="modalthree",
                                        ),
                                    ]
                                ),
                            ],
                            style={"width": "18rem"},
                        )
                    )
                ),
            ],
            style={"margin": "auto", "width": "80vw"},
        ),
    ]
)
