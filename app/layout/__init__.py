from dash import html

from app.layout.navbar import navbar
from app.layout.home_page import home_content

layout = html.Div([navbar, home_content])
