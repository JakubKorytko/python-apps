""" A module for generating the menu and the main window. """

from tkinter import *
from utilities.draw import Draw

class Generating:

    def assign(self, app=None, dropdown=None, menu=None):
        """ Assigns the app, dropdown and menu objects. """

        self.app = app
        self.dropdown = dropdown
        self.menu = menu

    def selectCity(self, selected):
        """ Generates the menu for selecting a city. """

        if (self.menu == None or self.menu.isOpen): return False

        self.menu.isOpen = True
        self.menu.rootInit()

        for index, station in enumerate(self.menu.stations):

            Draw.city(self.menu.canvas, station, {"row": index, "columnspan": 1})
            
            button = Draw.stationButton(self.menu.canvas, index, self.menu.radioVar, lambda arg=index: self.generate(arg))
            self.menu.stationButtons.append(button)

            if (index == selected): button.select()

        menuWidth = 430
        menuHeight = 40*len(self.menu.stations)
        
        self.menu.root.geometry(f'{menuWidth}x{menuHeight}+{int(self.menu.x)}+{int(self.menu.y)}')
        
        return "OK"

    def generate(self, stationID=0):
        """ Generates the main window. """

        if (self.app == None): return False

        if (self.dropdown != None): self.dropdown.clicked.set(self.app.options[stationID])
    
        if (self.app.firstGenerate == False): self.app.canvas.destroy()
            
        self.app.firstGenerate = False

        self.app.canvas = Canvas(self.app.root)
        self.app.canvas.pack()

        station = self.app.stations[stationID]

        for x, sensor in enumerate(station['sensors']): Draw.sensor(self.app.canvas, sensor, {"x": x+2, "y": 0})

        Draw.city(self.app.canvas, station['stationName'], {"row": 0, "columnspan": 2})

        if (self.menu): Draw.selectStation(self.app.canvas, lambda: self.selectCity(stationID))
