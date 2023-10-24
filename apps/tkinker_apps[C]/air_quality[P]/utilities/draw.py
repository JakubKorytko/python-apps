""" A module for drawing elements on the canvas. """
from tkinter import *

class Draw:
    """ A class for drawing elements on the canvas. """

    @staticmethod
    def set_font(config):
        """ Sets the font. """    
        Draw.font = (config["font"]["name"], config["font"]["size"])

    @staticmethod
    def city(canvas, text, grid):
        """ Draws a city label. """

        cityLabel = Label(canvas, text=text, background='white', font=Draw.font)
        cityLabel.grid(column=0, row=grid["row"], columnspan=grid["columnspan"], sticky=EW)

    @staticmethod
    def selectStation(canvas, callback):
        """ Draws a button for selecting a station. """

        button = Button(canvas, text='Change station', command=callback)
        button.grid(column=0, row=1, columnspan=2, sticky=EW)
    
    @staticmethod
    def stationButton(canvas, value, variable, callback):
        """ Draws a radio button for selecting a station. """

        button = Radiobutton(canvas, variable=variable, value=value, command=callback)
        button.grid(column=1, row=value, columnspan=1, sticky=EW)
        return button

    @staticmethod
    def sensor(canvas, sensor, coords):
        """ Draws a sensor. """

        kName = Label(canvas, text=sensor["name"], font=Draw.font)
        kVal = Label(canvas, text=Draw.translate(sensor["value"]), fg=Draw.color(sensor["value"]), font=Draw.font)

        kName.grid(column=coords["y"], row=coords["x"], sticky=NS)
        kVal.grid(column=coords["y"]+1,row=coords["x"], sticky=NS)

    @staticmethod
    def color(desc):
        """ Returns a color for a given description. """

        if desc == 'Bardzo dobry':
            return '#00FF00'
        elif desc == 'Dobry':
            return '#FFA500'
        elif desc == 'Umiarkowany':
            return '#000000'
        else:
            return '#FF0000'
    
    @staticmethod
    def translate(text):
        """ Translates a description to English. """

        if text == 'Bardzo dobry':
            return 'Very good'
        elif text == 'Dobry':
            return 'Good'
        elif text == 'Umiarkowany':
            return 'Moderate'
        else:
            return 'Bad'
