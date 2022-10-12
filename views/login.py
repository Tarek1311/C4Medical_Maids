import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash


layout = dbc.Container(
    [
        html.Br(),
        dbc.Container(
            [
                dcc.Location(id="urlLogin", refresh=True),
                html.Div(
                    [
                        dbc.Container(
                            html.Img(
                                src="/assets/dash-logo-stripe.svg", className="center"
                            ),
                        ),
                        dbc.Container(
                            id="loginType",
                            children=[
                                dcc.Input(
                                    placeholder="Enter your username",
                                    type="text",
                                    id="usernameBox",
                                    className="form-control",
                                    n_submit=0,
                                ),
                                html.Br(),
                                dcc.Input(
                                    placeholder="Enter your password",
                                    type="password",
                                    id="passwordBox",
                                    className="form-control",
                                    n_submit=0,
                                ),
                                html.Br(),
                                html.Button(
                                    children="Login",
                                    n_clicks=0,
                                    type="submit",
                                    id="loginButton",
                                    className="btn btn-primary btn-lg",
                                ),
                                html.Br(),
                            ],
                            className="form-group",
                        ),
                    ]
                ),
            ],
            className="jumbotron",
        ),
    ]
)


@app.callback(
    Output("urlLogin", "pathname"),
    [
        Input("loginButton", "n_clicks"),
        Input("usernameBox", "n_submit"),
        Input("passwordBox", "n_submit"),
    ],
    [State("usernameBox", "value"), State("passwordBox", "value")],
)
def sucess(n_clicks, usernameSubmit, passwordSubmit, username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user)
            return "/page1"
        else:
            pass
    else:
        pass


@app.callback(
    Output("usernameBox", "className"),
    [
        Input("loginButton", "n_clicks"),
        Input("usernameBox", "n_submit"),
        Input("passwordBox", "n_submit"),
    ],
    [State("usernameBox", "value"), State("passwordBox", "value")],
)
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return "form-control"
            else:
                return "form-control is-invalid"
        else:
            return "form-control is-invalid"
    else:
        return "form-control"


@app.callback(
    Output("passwordBox", "className"),
    [
        Input("loginButton", "n_clicks"),
        Input("usernameBox", "n_submit"),
        Input("passwordBox", "n_submit"),
    ],
    [State("usernameBox", "value"), State("passwordBox", "value")],
)
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return "form-control"
            else:
                return "form-control is-invalid"
        else:
            return "form-control is-invalid"
    else:
        return "form-control"
