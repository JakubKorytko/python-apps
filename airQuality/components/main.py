from tkinter import *

class Main():

    firstGenerate = True

    def __init__(self, options, stations):
        self.options = options
        self.stations = stations

    def rootInit(self):
        self.root = Tk()
        self.root.title("Air quality in Cracow")

        appWidth = 350
        appHeight = 400

        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        x = (screenWidth / 2) - (appWidth / 2)
        y = (screenHeight / 2) - (appHeight / 2)

        self.root.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        self.root.protocol("WM_DELETE_WINDOW", self.destroy)
        self.root.configure(background='white')

    def destroy(self):
        self.root.destroy()