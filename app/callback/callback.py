from dash import html, Output, Input, State

from app.utils import lms_img, lmxxl_img, lmple_img


def register_callbacks(app):
    @app.callback(
        Output("modal-lit", "is_open"),
        [Input("open-lit", "n_clicks"), Input("close-lit", "n_clicks")],
        [State("modal-lit", "is_open")],
    )
    def toggle_lit_modal(click_lit, click_close_lit, is_lit_open):
        if click_lit or click_close_lit:
            return not is_lit_open
        return is_lit_open

    @app.callback(
        Output("output-container", "children"), [Input("bed-dropdown", "value")]
    )
    def update_output(value):

        if value == "LMS":
            return html.Div(
                html.Img(src=lms_img, style={"width": "100%", "height": "400px"})
            )
        elif value == "LMXXL":
            return html.Div(
                html.Img(src=lmxxl_img, style={"width": "100%", "height": "400px"})
            )
        elif value == "LMPLE":
            return html.Div(
                html.Img(src=lmple_img, style={"width": "100%", "height": "400px"})
            )
