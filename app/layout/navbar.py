import dash_bootstrap_components as dbc
from dash import html

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("C4Medical Maids", className="ml-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                "ACCUEIL",
                                href="/",
                            )
                        ),
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem(
                                    "Qui sommes-nous ?",
                                    href="https://www.myrectoverso.com/static/upload/25-392-7.jpg",
                                ),
                                dbc.DropdownMenuItem(
                                    "Youtube Channel",
                                    href="https://cryptopotluck.com/",
                                ),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem(
                                    "Projet Github",
                                    href="https://github.com/Tarek1311/C4Medical_Maids",
                                ),
                                dbc.DropdownMenuItem(
                                    "services pour les EHPAD",
                                    href="https://lemagcertification.afnor.org/wp-content/uploads/2018/01"
                                    "/GettyImages-587940524.jpg",
                                ),
                                dbc.DropdownMenuItem(
                                    "Maintenance et SAV",
                                    href="https://ems-concept.com/ems/wp-content/uploads/2011/07/EMS-Concept-Services"
                                    "-770x412.jpg",
                                ),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="PLUS",
                        ),
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
