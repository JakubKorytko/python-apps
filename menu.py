from explorer.submodules.text import Text
from explorer.handler import Explorer
from random import randint
import re
import os

colorsRange = [120,229] # excluded dark colors

class Menu:
    @staticmethod
    def welcome():
        welcome = "\nWelcome to the python-apps menu! Here you can select what app you want to run!"
        start = randint(colorsRange[0], colorsRange[1]-len(welcome))
        colors = colorsRange[1]-start
        return Text.rainbow(welcome, colors, start)

    @staticmethod
    def print_menu(options):
        Text.display("[C] means an option is a category, if you select a category, it will list the programs inside of it to select", "green")
        Text.display("[P] means an option is a program, if you select a program, it will run it", "green")
        Text.display("[?] Enter a number followed by a ? to get description of the category/program (e.g. 1?)\n", "green")

        for index, item in enumerate(options):
            name = item["name"]
            if item["type"] == "exit":
                color = "red"
            elif item["type"] == "back":
                color = "magenta"
            elif item["type"] == "category":
                color = "blue"
            elif item["type"] == "program":
                color = "yellow"
            Text.display(f"{index+1}. {name}", color)
            # print(f"{fg('green')}{key}. {value}{attr('reset')}")
        print()

    @staticmethod
    def findByName(options, name):
        for option in options:
            if option["name"] == name:
                return option

    @staticmethod
    def handle_choice(choice, selected):

        match(choice):
            case {"type": "exit"}:
                exit()
            case {"type": "back"}:
                selected.pop()
            case {"type": "category"}:
                selected.append(choice["name"])
            case {"type": "program"}:
                Explorer.run(os.path.join(choice["path"],choice["exec"]))
            
        return selected
    
    @staticmethod
    def generateOptions(options, selected):
        option = options

        for s in selected:
            option = Menu.findByName(option["subcategories"], s)

        menuOptions = [*option["subcategories"], *option["apps"]]

        if (selected == []):
            menuOptions.append({"name": "exit", "type": "exit", "desc": "Exit the app"})
        else:
            menuOptions.append({"name": "back", "type": "back", "desc": "Go back to the previous directory"})

        return menuOptions
    
    @staticmethod
    def limits(min, val, max):
        return int(min) <= int(val) <= int(max)

    @staticmethod
    def errorBoundary(choice, opt):
        res = {"skip": False, "showMenu": True}

        if (choice.strip() == ""): return [*{"skip": True, "showMenu": False}.values()]

        QuestionMark = re.search("^\d+\?$", choice.strip())
        NonDigit = re.search("\D", choice)
        OutOfRange = not Menu.limits(1, choice, len(opt)) if not NonDigit else False

        res["skip"] = True if (QuestionMark or NonDigit or OutOfRange) else False

        if QuestionMark:
            ind = re.sub("\?", "", choice.strip())

            if (Menu.limits(1, ind, len(opt))):
                Text.display(opt[int(ind)-1]["desc"]+"\n", "yellow")
                input("Press enter to continue...")
                print("")
            else: 
                res = {"skip": True, "showMenu": False}
                Text.display("Error: Invalid choice.\n", "red")
            
        elif NonDigit or OutOfRange:
            Text.display("Error: Invalid choice.\n", "red")
            res = {"skip": True, "showMenu": False}

        return [*res.values()]

    @staticmethod
    def loop(options):

        Text.display(Menu.welcome()+"\n")

        selected = []
        choice = "-1"
        showMenu = True
        
        while True:
            if (showMenu): 
                opt = Menu.generateOptions(options, selected)
                Menu.print_menu(opt)
            
            choice = input(f"Enter your choice (1-{len(opt)}): ")
            [skip, showMenu] = Menu.errorBoundary(choice, opt)

            if skip: continue
            
            selected = Menu.handle_choice(opt[int(choice)-1], selected)
            print()