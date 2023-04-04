from explorer.submodules.text import Text
import os
import re


class Explorer:

    @staticmethod
    def getData(path):
        categories = Explorer.categories(path)
        if (not categories):
            Text.display("Programs folder is empty", "red")
            exit()
        return categories

    @staticmethod
    def isdir(path):
        exists = os.path.exists(path)
        if not exists:
            return False
        isdir = os.path.isdir(path)
        if not isdir:
            return False
        return True

    @staticmethod
    def listDir(path):
        if not Explorer.isdir(path):
            return False
        dirs = os.listdir(path)
        files = [os.path.join(path, file) for file in dirs]
        return files

    @staticmethod
    def regexp(data, option):
        upper = option.upper()
        lower = option.lower()
        regMatch = re.search(f"\w+\[({lower}|{upper})\]", data)
        return regMatch != None

    @staticmethod
    def sortFiles(files):
        data = {"subcategories": [], "apps": []}
        for file in files:
            base = os.path.basename(file)

            c = Explorer.regexp(base, "c")
            p = Explorer.regexp(base, "p")
            c_and_p = re.search("(\[(c|C)\]\[P|p\])|(\[(p|P)\]\[C|c\])", base)

            if c_and_p:
                Text.display(
                    "\nError: file can't be both a category and a program", "red")
                Text.display(
                    "Please rename the file to remove the [C] or [P] tag", "red")
                Text.display("File: "+file, "red")
                Text.display("File will be ignored", "red")
                continue
            elif c:
                if (Explorer.isdir(file)): data["subcategories"].append(Explorer.categories(file))
            elif p:
                if (Explorer.isdir(file)): data["apps"].append(Explorer.program(file))

        return data
    
    @staticmethod
    def categories(folder):
        contents = Explorer.listDir(folder)
        if (not contents):
            return False
        data = {
            "name": os.path.basename(folder),
            "path": folder,
            "type": "category",
            "desc": Explorer.descFile(folder),
            **Explorer.sortFiles(contents)
        }
        return data
    
    @staticmethod
    def descFile(folder):
        contents = Explorer.listDir(folder)
        if (not contents):
            return False
        for file in contents:
            base = os.path.basename(file)
            if base == "desc.txt":
                return open(file, "r").read()
        return "No description file provided (desc.txt)"
    
    @staticmethod
    def run(path):
        if (os.path.basename(path) == "notfound"): 
            Text.display("\nCould not find main.py file in the program folder", "red")
            return False
        Text.display("\nStarting app...\n", "blue")
        os.system(f"python {path}")

    @staticmethod
    def program(folder):
        contents = Explorer.listDir(folder)
        if (not contents):
            return False
        data = {
            "name": os.path.basename(folder),
            "path": folder,
            "desc": Explorer.descFile(folder),
            "exec": Explorer.execFile(folder),
            "type": "program",
        }
        return data

    @staticmethod
    def execFile(folder):
        contents = Explorer.listDir(folder)
        if (not contents):
            return False
        for file in contents:
            base = os.path.basename(file)
            if base == "main.py":
                return "main.py"
        return "notfound"
