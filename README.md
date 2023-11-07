# Python apps

- [Python apps](#python-apps)
  - [Description](#description)
  - [Available programs](#available-programs)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)

## Description

"python-apps" is a console app with a menu from which you can choose many programs coded in Python, including graphical ones. The program scans the "apps" directory (which can be changed in the "main.py" file) and finds programs based on the following rules:

- Folders marked with "[C]" are categories that can contain programs and can be entered in the menu
- Folders marked with "[P]" are programs that can be run from the menu. The program will search for a "main.py" file inside and attempt to run it.
(Note that folders cannot have both markers at the same time.)

"Category" folders can contain other "categories," "programs," and a "desc.txt" file. The "desc.txt" file is read when the user selects the corresponding option in the menu. It can contain a description of the category.

"Program" folders can contain a "desc.txt" file, program files and folders, and a "main.py" file. Without a "main.py" file, the program cannot be run from the console menu. The "desc.txt" file is read when the user selects the corresponding option in the menu. It can contain a description of the program.

## Available programs

The "python-apps" program comes with many apps included:

**airQuality**
This app displays current air quality in Cracow and nearby cities
**imagesFilter**
This app takes array of images as the input and displays them with options to add filters
**anagram**
This program finds anagrams in a list of words.
**line**
The program checks if a point belongs to a straight line
**palindrome**
This program checks if a phrase is a palindrome
**segment**
This is a module with functions for calculating the distance of a point from a segment by the equation of a line
**sortLetters**
This program will sort letters from given word or phase
**triangle**
This program will check if you can create triangle from the given sides
**average**
This program calculates the grade point average based on a "grades.txt" file in the directory or manual input. The "grades.txt" file must contain only numbers from 1 to 6 separated by commas and be in the program directory.

... and many more!

You can add new programs and categories and change existing ones.


## Prerequisites
Before you can run the "python-apps" program, you will need to have the following installed on your system:

- [Python 3](https://www.python.org/downloads/)
- [pip (Python package manager)](https://pip.pypa.io/en/stable/installation/)

To check if you have Python 3 installed, open your terminal and run the following command:

```bash
python3 --version
```

To check if you have pip installed, run the following command:

```bash
pip --version
```

## Installation
To install "python-apps", follow these steps:

1. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/JakubKorytko/python-apps.git
```

2. Navigate to the main app directory using the command-line interface.

```bash
cd python-apps
```

3. Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

This command will install all the required packages that are listed in the "requirements.txt" file.

Once you have installed the required packages, you can run the program by navigating to the main app directory and running the following command:

```bash
python main.py
```

## Usage

To use the "python-apps" program, run the following command:

```bash
python main.py
```

This will start the program and display the main menu. From there, you can navigate the menu and run the programs.

## License

This project uses the following license: [MIT](https://choosealicense.com/licenses/mit/)