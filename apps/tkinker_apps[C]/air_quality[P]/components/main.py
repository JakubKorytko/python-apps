""" Main component for the air_quality app. """

from tkinter import Tk

class Main():
    """ A class for the main module. """

    first_generate = True

    def __init__(self, options, stations):
        """ Initializes the app. """

        self.root = None

        self.options = options
        self.stations = stations

    def root_init(self):
        """ Initializes the root window. """

        self.root = Tk()
        self.root.title("Air quality in Cracow")

        app_width = 350
        app_height = 400

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_pos = (screen_width / 2) - (app_width / 2)
        y_pos = (screen_height / 2) - (app_height / 2)

        self.root.geometry(f'{app_width}x{app_height}+{int(x_pos)}+{int(y_pos)}')
        self.root.protocol("WM_DELETE_WINDOW", self.destroy)
        self.root.configure(background='white')

    def destroy(self):
        """ Destroys the root window. """

        self.root.destroy()
