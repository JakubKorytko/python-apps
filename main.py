from menu import Menu
from explorer.handler import Explorer
import os

def main():
    working_dir = os.getcwd()
    apps_folder = "apps"

    path = os.path.join(working_dir, apps_folder)

    folders = Explorer.getData(path)

    Menu.loop(folders)

if __name__ == "__main__":
    main()