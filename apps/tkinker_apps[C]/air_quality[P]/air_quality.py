""" Entry point for air_quality app """

from app_data import generate_ui, get_app_data, set_drawing_methods

APP_DATA = get_app_data()

set_drawing_methods(APP_DATA)

generate_ui(APP_DATA)

APP = APP_DATA["app"]

APP.root.mainloop()
