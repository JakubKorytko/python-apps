from tkinter import *

class Dropdown:        
    def __init__(self, options, callbackfunc, root):
        self.root = root
        self.options = options
        self.generate = callbackfunc
        self.clicked = StringVar()

    def callback(self, *args):
        val = self.clicked.get()
        index = self.options.index(val)
        self.generate(index)

    def rootInit(self):
        self.clicked.trace("w", self.callback)
        drop = OptionMenu( self.root , self.clicked , *self.options )
        drop.pack()