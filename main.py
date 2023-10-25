""" Entry point for the program. """

from os import path as os_path, getcwd
from menu import Menu
from explorer.handler import Explorer

def main():
    """ Reads the apps folder and runs the menu. """

    working_dir = getcwd()
    apps_folder = "apps"

    path = os_path.join(working_dir, apps_folder)

    folders = Explorer.get_data(path)

    Menu.loop(folders)

if __name__ == "__main__":
    main()
