# Python Apps

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Run Super-Linter](https://github.com/JakubKorytko/python-apps/actions/workflows/super-linter.yml/badge.svg)](https://github.com/JakubKorytko/python-apps/actions/workflows/super-linter.yml)

## Table of Contents

- [Python Apps](#python-apps)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Menu](#menu)
    - [Categories](#categories)
    - [Programs generated data](#programs-generated-data)
  - [Extending the project](#extending-the-project)
    - [Adding new categories](#adding-new-categories)
    - [Adding new apps](#adding-new-apps)
  - [Building the application](#building-the-application)
  - [Troubleshooting](#troubleshooting)
    - [Missing dependencies](#missing-dependencies)
  - [Contributing](#contributing)
  - [Contact](#contact)
  - [License](#license)

## Introduction

This may feel like just another collection of random Python applications made by a beginner,
but it is not.

It is an extensible yet simple app that allows you to run apps from a menu.
The apps are divided into categories and can be nested.
The app is designed to be easily extensible,
so you can add your own apps and categories because the app will look for them
in the [pyap_apps](./pyap_apps/) directory so no real programming knowledge is required.

Thanks to this project, you can easily create your own collection of applications and share it with others.
For more information, see [extending the project](#extending-the-project).

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- [Python 3.11.4 or later](https://www.python.org/downloads/)
- [Poetry 1.7.1 or later](https://python-poetry.org/docs/#installation)

## Installation

1. Clone this repository to your local machine using Git,
or download the ZIP file and extract it to a directory of your choice:

    ```bash
    git clone https://github.com/JakubKorytko/python-apps.git
    ```

1. Change to the project directory:

    ```bash
    cd python-apps
    ```

1. Run the following command to install the required dependencies:

    ```bash
    poetry install
    ```

You can now run the project by executing the following command:

```bash
poetry run python-apps
```

## Usage

The application has an intuitive menu that allows you to navigate through the applications and categories,
that are displayed when you run the application.

### Menu

The menu displays categories and apps according to the
[pyap_apps](./pyap_apps/) directory structure.

The options are numbered and you can select them by typing the corresponding number.

Applications can be identified by the `[P]` (or `[p]`) at the end of their name,
and categories by the `[C]` (or `[c]`) at the end of their name.
Applications will also have a yellow font color, and categories will have a blue font color.

You can get the description (if `desc.txt` exists,
see [extending the project](#extending-the-project)) of the selected application or category
by typing its number followed by `?`.

### Categories

The application has a built-in categories (with applications) which are located in the [pyap_apps](./pyap_apps/) directory:

- [console_apps[C]](./pyap_apps/console_apps[C]/)
- [matura_tasks[C]](./pyap_apps/matura_tasks[C]/)
- [tkinter_apps[C]](./pyap_apps/tkinter_apps[C]/)

### Programs generated data

When one of the applications generates data, it is stored in the application directory.

For example, if you are running the `pyap_apps/(...)/App[P]/main.py` app,
and the app generates data, it will be stored in the `pyap_apps/(...)/App[P]` directory.
If the applications uses a subdirectory to store the data,
it will be stored in the corresponding subdirectory of the `pyap_apps/(...)/App[P]` directory.

`(...)` represents the category directories as they can be nested.

## Extending the project

App categories and apps are determined by the directories in the [pyap_apps](./pyap_apps/) directory.
A directory can be either a category or an application, but not both.
You can add new categories and apps by creating new directories in the [pyap_apps](./pyap_apps/) directory.

The application will look for `pyap_apps` in the following locations:

1. First, in the parent directory of the [\_\_main\_\_.py](./python_apps/__main__.py) file
2. If not found, in the [\_\_main\_\_.py](./python_apps/__main__.py) file directory

You can rename or move the [pyap_apps](./pyap_apps/) directory to another location,
but you must specify the new location in the [\_\_main\_\_.py](./python_apps/__main__.py) file.
If you intend to build the application, you will need to update the [pyproject.toml](./pyproject.toml) file.

### Adding new categories

Category directories must have a `[C]` (or `[c]`) at the end of their name.
For example, `pyap_apps/Category[C]` is a valid category directory,
but `pyap_apps/Category` is not and will be ignored by the application.

Categories can contain other categories and applications.

You can add a `desc.txt` file to the category directory
to provide a description of the category.

### Adding new apps

Application directories must contain a `[P]` (or `[p]`) at the end of their name.
For example, `pyap_apps/App[P]` is a valid application directory,
but `pyap_apps/App` is not and will be ignored by the application.

You can put a `desc.txt` file in the app directory
to provide a description of the application.

The application will look for a `main.py` file in the app directory
and execute it if found.

Each app is executed in a separate subprocess and so it must be a standalone program.
This makes the app more secure, and less likely to crash the main app or other apps.

If your application requires additional dependencies,
you can add them to the [pyproject.toml](./pyproject.toml) file manually,
or by running the following command:

```bash
poetry add <dependency>
```

## Building the application

To build the application, run the following command:

```bash
poetry build
```

The built application will be located in the `dist` directory.
It should contain `.whl` and `.tar.gz` files. You can install the application by running the following command:

```bash
pip install <path-to-whl-or-tar.gz-file>
```

## Troubleshooting

### Missing dependencies

Running the `poetry install` command should be sufficient in most cases,
but some dependencies may need to be installed manually.
If any of the applications fail to run due to missing dependencies,
make sure that:

- They are listed in the [pyproject.toml](./pyproject.toml) file
- You have run the `poetry install` command
- If the above steps did not help, try installing the dependencies manually
with a [pip](https://pip.pypa.io/en/stable/) command:

    ```bash
    pip install <dependency>
    ```

- If the problem persists, search the web to see if there are any additional steps required
to install the dependency or if it is compatible with your system.
Some dependencies may require you to install additional system packages.
`Tkinter` is one such example on the Linux operating system.

- If you are unable to find a solution, feel free to open an issue.

## Contributing

If you find issues or have suggestions for improvements,
feel free to open an issue or submit a pull request.
Contributions are welcome!

## Contact

If you have any questions, feel free to contact me at <jakub@korytko.me>.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.
