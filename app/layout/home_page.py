import dash_bootstrap_components as dbc
from dash import html

from app.layout.bed_layout import bed_col
from app.layout.lifter_layout import patient_lifter_col
from app.layout.wheelchair_layout import wheelchair_col

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
                    "margin-left": "auto",
                    "margin-right": "auto",
                    "width": "auto",
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
                wheelchair_col,
                patient_lifter_col,
            ],
            style={"margin": "auto", "width": "80vw"},
        ),
    ]
)
