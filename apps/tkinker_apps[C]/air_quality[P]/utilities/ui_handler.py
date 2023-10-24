""" A module for generating the menu and the main window. """

from tkinter import Canvas

class UIHandler():
    """ A class for handling the UI. """

    def __init__(self):
        self.app = None
        self.dropdown = None
        self.menu = None
        self.draw_methods = None

    def set_drawing_methods(self, draw_methods):
        """ Sets the drawing methods. """

        self.draw_methods = draw_methods

    def draw(self, method_name):
        """ Returns the drawing method. """

        return self.draw_methods[method_name]

    def assign(self, app=None, dropdown=None, menu=None):
        """ Assigns the app, dropdown and menu objects. """

        self.app = app
        self.dropdown = dropdown
        self.menu = menu

    def select_city(self, selected):
        """ Generates the menu for selecting a city. """

        if (self.menu is None or self.menu.is_open):
            return False

        self.menu.is_open = True
        self.menu.root_init()

        for index, station in enumerate(self.menu.stations):

            self.draw("city")(self.menu.canvas, station, {"row": index, "columnspan": 1})

            button = self.draw("station_button")(
                self.menu.canvas, index, self.menu.radio_var, lambda arg=index: self.generate(arg)
            )

            self.menu.station_buttons.append(button)

            if index == selected:
                button.select()

        menu_width = 430
        menu_height = 40*len(self.menu.stations)

        self.menu.root.geometry(
        f'{menu_width}x{menu_height}+{int(self.menu.x_pos)}+{int(self.menu.y_pos)}'
        )

        return True

    def generate(self, station_id=0):
        """ Generates the main window. """

        if self.app is None:
            return False

        if self.dropdown is not None:
            self.dropdown.clicked.set(self.app.options[station_id])

        if self.app.first_generate is False:
            self.app.canvas.destroy()

        self.app.first_generate = False

        self.app.canvas = Canvas(self.app.root)
        self.app.canvas.pack()

        station = self.app.stations[station_id]

        for index, sensor in enumerate(station['sensors']):
            self.draw("sensor")(self.app.canvas, sensor, {"x": index+2, "y": 0})

        self.draw("city")(self.app.canvas, station['stationName'], {"row": 0, "columnspan": 2})

        if self.menu:
            self.draw("select_station")(self.app.canvas, lambda: self.select_city(station_id))

        return True
