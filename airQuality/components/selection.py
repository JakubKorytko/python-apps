from tkinter import *

class Menu:

    isOpen = False
    stationButtons = []

    def __init__(self, stations):
        self.stations = stations

    def rootInit(self):
        self.root = Tk()
        self.root.title("Select city")
        
        self.radioVar = IntVar()

        self.canvas = Canvas(self.root)
        self.canvas.pack()

        menuWidth = 375
        menuHeight = 200

        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        self.x = (screenWidth / 2) - (menuWidth / 2)
        self.y = (screenHeight / 2) - (menuHeight / 2)
        
        self.root.geometry(f'{menuWidth}x{menuHeight}+{int(self.x)}+{int(self.y)}')
        self.root.configure(background='white')
        
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

    def quit(self):
        self.isOpen = False
        self.root.destroy()