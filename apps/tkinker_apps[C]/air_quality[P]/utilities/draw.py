""" A module for drawing elements on the canvas. """

from tkinter import EW, NS, Label, Button, Radiobutton


class Draw:
    """A class for drawing elements on the canvas."""

    @staticmethod
    def set_font(config):
        """Sets the font."""
        Draw.font = (config["font"]["name"], config["font"]["size"])

    @staticmethod
    def city(canvas, text, grid):
        """Draws a city label."""

        city_label = Label(canvas, text=text, background="white", font=Draw.font)
        city_label.grid(
            column=0, row=grid["row"], columnspan=grid["columnspan"], sticky=EW
        )

    @staticmethod
    def select_station(canvas, callback):
        """Draws a button for selecting a station."""

        button = Button(canvas, text="Change station", command=callback)
        button.grid(column=0, row=1, columnspan=2, sticky=EW)

    @staticmethod
    def station_button(canvas, value, variable, callback):
        """Draws a radio button for selecting a station."""

        button = Radiobutton(canvas, variable=variable, value=value, command=callback)
        button.grid(column=1, row=value, columnspan=1, sticky=EW)
        return button

    @staticmethod
    def sensor(canvas, sensor, coords):
        """Draws a sensor."""

        k_name = Label(canvas, text=sensor["name"], font=Draw.font)

        k_val = Label(
            canvas,
            text=Draw.translate(sensor["value"]),
            fg=Draw.color(sensor["value"]),
            font=Draw.font,
        )

        k_name.grid(column=coords["y"], row=coords["x"], sticky=NS)
        k_val.grid(column=coords["y"] + 1, row=coords["x"], sticky=NS)

    @staticmethod
    def color(desc):
        """Returns a color for a given description."""

        if desc == "Bardzo dobry":
            return "#00FF00"

        if desc == "Dobry":
            return "#FFA500"

        if desc == "Umiarkowany":
            return "#000000"

        return "#FF0000"

    @staticmethod
    def translate(text):
        """Translates a description to English."""

        if text == "Bardzo dobry":
            return "Very good"

        if text == "Dobry":
            return "Good"

        if text == "Umiarkowany":
            return "Moderate"

        return "Bad"
