""" Entry point for the program. """

from os import path as os_path

from python_apps.explorer.handler import Explorer
from python_apps.menu import Menu


def main():
    """Reads the apps folder and runs the menu."""

    working_dir = os_path.dirname(os_path.realpath(__file__))

    apps_folder = "pyap_apps"
    parent_folder = os_path.join(working_dir, "..")

    path = os_path.join(working_dir, apps_folder)
    parent_path = os_path.join(parent_folder, apps_folder)

    if os_path.isdir(parent_path):
        path = parent_path

    folders = Explorer.get_data(path)

    Menu.loop(folders)


if __name__ == "__main__":
    main()
