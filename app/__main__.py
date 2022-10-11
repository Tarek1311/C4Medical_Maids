import dash_bootstrap_components as dbc
from dash import Dash

from app.callback.callback import register_callbacks
from app.layout.layout import layout

# Instanciate dash object
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create server object for heroku procfile
server = app.server

# inject layout and register callbacks
app.layout = layout
register_callbacks(app)


def run():
    app.run_server(debug=True, port=8888)
