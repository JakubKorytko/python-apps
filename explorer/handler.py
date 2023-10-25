""" This module defines a class called 'Explorer'
that provides methods for exploring a directory structure containing programs and categories.
It can categorize programs and categories, retrieve program descriptions,
run programs, and provide information about them. """

from sys import exit as sys_exit
from os import path as os_path, listdir as os_listdir
from re import search as re_search
from subprocess import call as subprocess_call
from explorer import Text

class Explorer:
    """ Explorer class for exploring a directory structure containing programs and categories. """

    @staticmethod
    def get_data(path):
        """ Returns a list of categories in the given path. """

        categories = Explorer.categories(path)
        if not categories:
            Text.display("Programs folder is empty", "red")
            sys_exit()
        return categories

    @staticmethod
    def isdir(path):
        """ Returns True if the given path is a directory, False otherwise. """

        exists = os_path.exists(path)
        if not exists:
            return False
        isdir = os_path.isdir(path)
        if not isdir:
            return False
        return True

    @staticmethod
    def list_dir(path):
        """ Returns a list of files in the given directory. """

        if not Explorer.isdir(path):
            return False
        dirs = os_listdir(path)
        files = [os_path.join(path, file) for file in dirs]
        return files

    @staticmethod
    def regexp(data, option):
        """ Returns True if the given option is in the given data, False otherwise. """

        upper = option.upper()
        lower = option.lower()
        reg_match = re_search(rf"\w+\[({lower}|{upper})\]", data)
        return reg_match is not None

    @staticmethod
    def sort_files(files):
        """ Returns a dictionary containing a list of categories and a list of programs. """

        data = {"subcategories": [], "apps": []}
        for file in files:
            base = os_path.basename(file)

            regexp_c = Explorer.regexp(base, "c")
            regexp_p = Explorer.regexp(base, "p")
            c_and_p = re_search(r"(\[(c|C)\]\[P|p\])|(\[(p|P)\]\[C|c\])", base)

            if c_and_p:
                Text.display(
                    "\nError: file can't be both a category and a program", "red")
                Text.display(
                    "Please rename the file to remove the [C] or [P] tag", "red")
                Text.display("File: "+file, "red")
                Text.display("File will be ignored", "red")
                continue
            if regexp_c and Explorer.isdir(file):
                data["subcategories"].append(Explorer.categories(file))
            elif regexp_p and Explorer.isdir(file):
                data["apps"].append(Explorer.program(file))

        return data

    @staticmethod
    def categories(folder):
        """ Returns a dictionary containing the name, path,
        description, and contents of the given folder. """

        contents = Explorer.list_dir(folder)
        if not contents:
            return False
        data = {
            "name": os_path.basename(folder),
            "path": folder,
            "type": "category",
            "desc": Explorer.desc_file(folder),
            **Explorer.sort_files(contents)
        }
        return data

    @staticmethod
    def desc_file(folder):
        """ Returns the contents of the desc.txt file in the given folder. """

        contents = Explorer.list_dir(folder)
        if not contents:
            return False
        for file in contents:
            base = os_path.basename(file)
            if base == "desc.txt":
                return open(file, "r", encoding="utf-8").read()
        return "No description file provided (desc.txt)"

    @staticmethod
    def run(path):
        """ Runs the program at the given path. """

        if os_path.basename(path) == "notfound":
            Text.display("\nCould not find main.py file in the program folder", "red")
            return False

        Text.display("\nStarting app...\n", "blue")
        subprocess_call(["python", path])

        return True

    @staticmethod
    def program(folder):
        """ Returns a dictionary containing the name, path,
        description, and entry point of the given folder. """

        contents = Explorer.list_dir(folder)
        if not contents:
            return False

        data = {
            "name": os_path.basename(folder),
            "path": folder,
            "desc": Explorer.desc_file(folder),
            "exec": Explorer.exec_file(folder),
            "type": "program",
        }

        return data

    @staticmethod
    def exec_file(folder):
        """ Returns the entry point of the app in the given folder. """

        contents = Explorer.list_dir(folder)
        if not contents:
            return False
        for file in contents:
            base = os_path.basename(file)
            if base == "main.py":
                return "main.py"
        return "notfound"
