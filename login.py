# -*- coding: utf-8 -*-
import dash
from dash import dcc, html, Input, Output, callback, State
import dash_core_components as dcc
from flask_login import login_user, LoginManager, UserMixin, logout_user, current_user
from app import User

dash.register_page(__name__, path="/login")

layout = html.Div([
        html.H1('Login page'),
        dbc.Label("Username"),
        dbc.Input(id = "input_username"),
        dbc.Label("Password"),
        dbc.Input(id = "input_password"),
        dbc.Button("Login in", id = "button_login"),
        dbc.Label("Please login", id = "label_feedback"),
        dcc.Location(id="redirect"),
])

@callback(
    Output('redirect', 'pathname'),
    Output('label_feedback', 'children'),
    Input('button_login', 'n_clicks'),
    State('input_username', 'value'),
    State('input_password', 'value')
    )
def login_button_click(n_clicks, username, password):
    if n_clicks != 0:
        if username == 'test2' and password == 'test':
            user = User(username)
            login_user(user)
            return (("/"),'Succesfully logged in!')
        else:
            return (None, 'Incorrect username or password')
