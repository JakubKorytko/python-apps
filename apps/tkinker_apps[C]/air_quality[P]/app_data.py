""" Functions for preparing data for the app. """

from config import get_config
from utilities import UIHandler, Draw, API
from components import Dropdown, Menu, Main


def get_dropdown_bool():
    """Returns whether to use dropdown or not."""

    config = get_config()
    use_dropdown = config["dropdown?"]
    return use_dropdown


def set_font_from_config_file():
    """Sets the font from config file."""

    config = get_config()
    Draw.set_font(config)


def set_handler(use_dropdown, app_data):
    """Sets the dropdown based on config."""

    handler = None

    if not use_dropdown:
        handler = Menu(app_data["data"]["options"])

    if use_dropdown:
        handler = Dropdown(
            app_data["data"]["options"],
            app_data["ui_gen"].generate,
            app_data["app"].root,
        )

        handler.root_init()

    return handler


def get_app_data():
    """Prepares data for the app."""

    data = API.fetch()
    ui_gen = UIHandler()
    app = Main(data["options"], data["stations"])
    app.root_init()

    return {"data": data, "ui_gen": ui_gen, "app": app}


def set_drawing_methods(app_data):
    """Sets the drawing methods."""

    draw_methods = {
        "city": Draw.city,
        "station_button": Draw.station_button,
        "select_station": Draw.select_station,
        "sensor": Draw.sensor,
    }

    app_data["ui_gen"].set_drawing_methods(draw_methods)


def get_ui_gen_data(app_data, use_dropdown, handler):
    """Returns ui_gen data."""

    ui_gen_data = {
        "app": app_data["app"],
        "dropdown": handler if use_dropdown else None,
        "menu": handler if not use_dropdown else None,
    }

    return ui_gen_data


def generate_ui(app_data):
    """Assigns ui_gen data."""

    use_dropdown = get_dropdown_bool()

    handler = set_handler(use_dropdown, app_data)

    ui_gen_data = get_ui_gen_data(app_data, use_dropdown, handler)

    app_data["ui_gen"].assign(**ui_gen_data)

    set_font_from_config_file()

    app_data["ui_gen"].generate()
