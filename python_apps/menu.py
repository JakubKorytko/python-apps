""" This module defines a class called 'Menu'
that offers a text-based menu for interacting with a selection of Python applications.
Users can choose categories and programs to run,
get descriptions, and navigate through the menu. """

from os import path as os_path
from random import randint
from re import search as re_search
from re import sub as re_sub
from sys import exit as sys_exit

from python_apps.explorer import Explorer, Text

colorsRange = [120, 229]  # excluded dark colors


class Menu:
    """Menu class for interacting with a selection of Python applications."""

    @staticmethod
    def welcome():
        """Returns a rainbow-colored welcome message."""

        welcome = "\nWelcome to the python-apps menu! Here you can select what app you want to run!"
        start = randint(colorsRange[0], colorsRange[1] - len(welcome))
        colors = colorsRange[1] - start
        return Text.rainbow(welcome, colors, start)

    @staticmethod
    def print_menu(options):
        """Prints the menu."""

        Text.display(
            "[C] means an option is a category, if you select a category, "
            + "it will list the programs inside of it to select",
            "green",
        )
        Text.display(
            "[P] means an option is a program, "
            + "if you select a program, it will run it",
            "green",
        )
        Text.display(
            "[?] Enter a number followed by a ? to get description "
            + "of the category/program (e.g. 1?)\n",
            "green",
        )

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
    def find_by_name(options, name):
        """Returns an option with the given name."""

        for option in options:
            if option["name"] == name:
                return option

        return None

    @staticmethod
    def handle_choice(choice, selected):
        """Handles the user's choice."""

        match (choice):
            case {"type": "exit"}:
                sys_exit()
            case {"type": "back"}:
                selected.pop()
            case {"type": "category"}:
                selected.append(choice["name"])
            case {"type": "program"}:
                Explorer.run(os_path.join(choice["path"], choice["exec"]))

        return selected

    @staticmethod
    def generate_options(options, selected):
        """Generates the menu options."""

        option = options

        for select in selected:
            option = Menu.find_by_name(option["subcategories"], select)

        menu_options = [*option["subcategories"], *option["apps"]]

        if selected == []:
            menu_options.append(
                {"name": "exit", "type": "exit", "desc": "Exit the app"}
            )
        else:
            menu_options.append(
                {
                    "name": "back",
                    "type": "back",
                    "desc": "Go back to the previous directory",
                }
            )

        return menu_options

    @staticmethod
    def limits(min_val, val, max_val):
        """Checks if a value is between two other values."""

        return int(min_val) <= int(val) <= int(max_val)

    @staticmethod
    def error_boundary(choice, opt):
        """Checks if the user's choice is valid."""

        res = {"skip": False, "show_menu": True}

        if choice.strip() == "":
            return [*{"skip": True, "show_menu": False}.values()]

        question_mark = re_search(r"^\d+\?$", choice.strip())
        non_digit = re_search(r"\D", choice)
        out_of_range = not Menu.limits(1, choice, len(opt)) if not non_digit else False

        res["skip"] = bool(question_mark or non_digit or out_of_range)

        if question_mark:
            ind = re_sub(r"\?", "", choice.strip())

            if Menu.limits(1, ind, len(opt)):
                Text.display(opt[int(ind) - 1]["desc"] + "\n", "yellow")
                input("Press enter to continue...")
                print("")
            else:
                res = {"skip": True, "show_menu": False}
                Text.display("Error: Invalid choice.\n", "red")

        elif non_digit or out_of_range:
            Text.display("Error: Invalid choice.\n", "red")
            res = {"skip": True, "show_menu": False}

        return [*res.values()]

    @staticmethod
    def loop(options):
        """Loops the menu."""

        Text.display(Menu.welcome() + "\n")

        selected = []
        choice = "-1"
        show_menu = True

        while True:
            if show_menu:
                opt = Menu.generate_options(options, selected)
                Menu.print_menu(opt)

            choice = input(f"Enter your choice (1-{len(opt)}): ")
            [skip, show_menu] = Menu.error_boundary(choice, opt)

            if skip:
                continue

            selected = Menu.handle_choice(opt[int(choice) - 1], selected)
            print()
