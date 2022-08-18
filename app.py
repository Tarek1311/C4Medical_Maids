import base64
from collections import Counter
from io import BytesIO
import dash
import dash_bootstrap_components as dbc
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import plotly.graph_objs as go
import requests
from dash import dcc
from dash import html
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from celery import Celery

PLOTLY_LOGO = (
    "https://st2.depositphotos.com/4362315/7819/v/950/"
    "depositphotos_78194060-stock-illustration-"
    "medical-logo-health-care-center.jpg"
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)











"""Navbar"""
# dropdown Items

# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(
    dbc.NavLink(
        "ACCUEIL",
        href="/",
    )
)

# make a reuseable dropdown for the different examples
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

# Navbar Layout
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical
                # alignment of logo / brand
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

##############
"""App Components"""


# Dropdown App


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


# Textarea App #


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

# Slider
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
# Cards
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
# rows
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


# dropdown App #


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


# Slider App
@app.callback(
    [
        Output("slider-graph", "figure"),
        Output("updatemode-output-container", "children"),
    ],
    [Input("slider-updatemode", "value")],
)
def display_value(value):
    x = []
    for i in range(value):
        x.append(i)

    y = []
    for i in range(value):
        y.append(i * i)

    graph = go.Scatter(x=x, y=y, name="Manipulate Graph")
    layout = go.Layout(
        paper_bgcolor="#27293d",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[min(y), max(y)]),
        font=dict(color="white"),
    )
    return {
        "data": [graph],
        "layout": layout,
    }, f"Value: {round(value, 1)} Square: {value * value}"


# Text App
@app.callback(Output("txt-graph", "figure"), [Input("txt", "value")])
def display_value(value):
    word_list = value.split()
    word_dic = Counter(word_list)
    x = list(word_dic.keys())
    y = list(word_dic.values())

    graph = go.Bar(
        x=x, y=y, name="Manipulate Graph", type="bar", marker=dict(color="lightgreen")
    )

    layout = go.Layout(
        paper_bgcolor="#27293d",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(type="category"),
        yaxis=dict(range=[-4, 4]),
        font=dict(color="white"),
    )
    return {"data": [graph], "layout": layout}


# module One
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# Module Two
@app.callback(
    Output("modaltwo", "is_open"),
    [Input("opentwo", "n_clicks"), Input("closetwo", "n_clicks")],
    [State("modaltwo", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# Module Three
@app.callback(
    Output("modalthree", "is_open"),
    [Input("openthree", "n_clicks"), Input("closethree", "n_clicks")],
    [State("modalthree", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# we use a callback to toggle the collapse on small screens
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# the same function (toggle_navbar_collapse) is used in all three callbacks
for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)


# for gunicorn to find server to launch
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
