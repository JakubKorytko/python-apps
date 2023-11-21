""" Menu for selecting city to display air quality data for. """

from tkinter import Canvas, IntVar, Radiobutton, Tk
from typing import List


class Menu:
    """A class for the menu."""

    is_open = False
    station_buttons: List[Radiobutton] = []

    def __init__(self, stations):
        """Initializes the menu."""

        self.root = None
        self.canvas = None
        self.x_pos = None
        self.y_pos = None
        self.radio_var = None

        self.stations = stations

    def root_init(self):
        """Initializes the menu window."""

        self.root = Tk()
        self.root.title("Select city")

        self.radio_var = IntVar()

        self.canvas = Canvas(self.root)
        self.canvas.pack()

        menu_width = 375
        menu_height = 200

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.x_pos = (screen_width / 2) - (menu_width / 2)
        self.y_pos = (screen_height / 2) - (menu_height / 2)

        self.root.geometry(
            f"{menu_width}x{menu_height}+{int(self.x_pos)}+{int(self.y_pos)}"
        )
        self.root.configure(background="white")

        self.root.protocol("WM_DELETE_WINDOW", self.quit)

    def quit(self):
        """Quits the menu."""

        self.is_open = False
        self.root.destroy()
