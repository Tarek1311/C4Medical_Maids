# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
import dl as dl
from dash.dependencies import Input, Output, State


import flask
import os
from flask_login import login_user, LoginManager, UserMixin, logout_user, current_user


# Exposing the Flask Server to enable configuring it for logging in
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,
                title='Example Dash login',
                update_title='Loading...',
                suppress_callback_exceptions=True, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.BOOTSTRAP])


# Updating the Flask Server configuration with Secret Key to encrypt the user session cookie
server.config.update(SECRET_KEY=os.getenv('SECRET_KEY'))

# Login manager object will be used to login / logout users
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'

# User data model. It has to have at least self.id as a minimum

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@ login_manager.user_loader
def load_user(username):
    ''' This function loads the user by user id. Typically this looks up the user from a user database.
        We won't be registering or looking up users in this example, since we'll just login using LDAP server.
        So we'll simply return a User object with the passed in username.
    '''
    return User(username)

navbar = dbc.NavbarSimple([
        dbc.NavItem(dbc.NavLink(page['name'], href=page['path']))
        for page in dash.page_registry.values()
        if page["module"] != "pages.not_found_404"
], brand='Dash App')

app.layout = dbc.Container(
    [navbar, dl.plugins.page_container, html.Div(id="logincheck_div"), html.Div(id="output_div")],
)

@app.callback(
    Output("output_div","children"),
    Input("logincheck_div","children"),
)
def check_logged_in(div):
    if current_user.is_authenticated:
        print("User is logged in")
    else:
        print("User is not logged in, you are being redirected.")
        return(dcc.Location(id="redirect",pathname="/login"))

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        # html.H1(children="Welcome to the dash Polling app!"),
        dcc.Location(id="url", refresh=False),
        # dcc.Link('Home',href="/"),
        # html.Br(),
        # dcc.Link('Polls',href="/polls"),
        # html.Br(),
        # dcc.Link('Poll Results',href="/poll-results"),
        html.Div(id="output-div"),
    ]
)

home_layout = html.Div(
    children=[
        html.H1(children="Welcome to the C4MEdical_Maids Application!"),
        dcc.Link("Home", href="/"),
        html.Br(),
        dcc.Link("Page 1", href="/Page 1"),
        html.Br(),
        dcc.Link("Page 2", href="/Page 2"),
    ]
)

polls_layout = html.Div(
    children=[html.H1(children="This is page 1"), dcc.Link("Home", href="/")]
)

polls_results_layout = html.Div(
    children=[html.H1(children="This is Page 2"), dcc.Link("Home", href="/")]
)


@app.callback(
    Output(component_id="output-div", component_property="children"),
    Input(component_id="url", component_property="pathname"),
)
def update_output_div(pathname):
    if pathname == "/page 1":
        return polls_layout
    elif pathname == "/Page 1":
        return polls_results_layout
    else:
        return home_layout
    # output_val = "Output: {}".format(pathname)
    # return output_val


if __name__ == "__main__":
    app.run_server(debug=True)
