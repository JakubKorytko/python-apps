""" Module for dropdown component. """

from tkinter import OptionMenu, StringVar

class Dropdown:
    """ A class for the dropdown component. """

    def __init__(self, options, callbackfunc, root):
        """ Constructor. """

        self.root = root
        self.options = options
        self.generate = callbackfunc
        self.clicked = StringVar()

    def callback(self, *_):
        """ Callback function. """

        val = self.clicked.get()
        index = self.options.index(val)
        self.generate(index)

    def root_init(self):
        """ Initializes the dropdown. """

        self.clicked.trace("w", self.callback)
        drop = OptionMenu( self.root , self.clicked , *self.options )
        drop.pack()
