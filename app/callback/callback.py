from dash import html, Output, Input, State

from app.utils import IMG_BED_DICT, IMG_WHEELCHAIR_DICT, IMG_LIFTER_DICT


def register_callbacks(app):
    @app.callback(
        Output("modal-bed", "is_open"),
        [Input("open-bed", "n_clicks"), Input("close-bed", "n_clicks")],
        [State("modal-bed", "is_open")],
    )
    def toggle_bed_modal(click_bed, click_close_bed, is_bed_open):
        if click_bed or click_close_bed:
            return not is_bed_open
        return is_bed_open

    @app.callback(
        Output("output-container", "children"), [Input("bed-dropdown", "value")]
    )
    def update_bed_modal(value):
        if value in IMG_BED_DICT.keys():
            return html.Div(
                html.Img(
                    src=IMG_BED_DICT[value], style={"width": "100%", "height": "400px"}
                )
            )

    @app.callback(
        Output("modal-wheelchair", "is_open"),
        [Input("open-wheelchair", "n_clicks"), Input("close-wheelchair", "n_clicks")],
        [State("modal-wheelchair", "is_open")],
    )
    def toggle_wheelchair_modal(
        click_wheelchair, click_close_wheelchair, is_wheelchair_open
    ):
        if click_wheelchair or click_close_wheelchair:
            return not is_wheelchair_open
        return is_wheelchair_open

    @app.callback(
        Output("output-wheelchairContainer", "children"),
        [Input("wheelchair-dropdown", "value")],
    )
    def update_wheelchair_modal(value):
        if value in IMG_WHEELCHAIR_DICT.keys():
            return html.Div(
                html.Img(
                    src=IMG_WHEELCHAIR_DICT[value],
                    style={"width": "100%", "height": "400px"},
                )
            )

    @app.callback(
        Output("modal-lifter", "is_open"),
        [Input("open-lifter", "n_clicks"), Input("close-lifter", "n_clicks")],
        [State("modal-lifter", "is_open")],
    )
    def toggle_lifter_modal(click_lifter, click_close_lifter, is_lifter_open):
        if click_lifter or click_close_lifter:
            return not is_lifter_open
        return is_lifter_open

    @app.callback(
        Output("output-containerLifter", "children"),
        [Input("lifter-dropdown", "value")],
    )
    def update_lifter_modal(value):
        if value in IMG_LIFTER_DICT.keys():
            return html.Div(
                html.Img(
                    src=IMG_LIFTER_DICT[value],
                    style={"width": "100%", "height": "400px"},
                )
            )
