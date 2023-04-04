from utilities.generation import Generating
from utilities.api import API
from config import config
from tkinter import *
from components import *

dropdown, menu = None, None

useDropdown = config["dropdown?"]

uiGen = Generating()

data = API.fetch()

app = Main(data["options"], data["stations"])
app.rootInit()

if not useDropdown: menu = Menu(data["options"])

if (useDropdown):
    dropdown = Dropdown(data["options"], uiGen.generate, app.root)
    dropdown.rootInit()

use = {
    'app': app,
    'dropdown': dropdown if useDropdown else None,
    'menu': menu if not useDropdown else None
}

uiGen.assign(**use)

uiGen.generate()

app.root.mainloop()
