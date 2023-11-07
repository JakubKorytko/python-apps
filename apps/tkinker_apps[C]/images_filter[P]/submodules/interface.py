""" This module contains the logic for the UI. """

from tkinter import Label, Button, DISABLED, SUNKEN, E, W, NORMAL


class UIHandler:
    """Handles the UI."""

    @staticmethod
    def print_welcome_message():
        """Prints a welcome message."""

        print("\nWelcome to my image filter app!")
        print("In order to use this app, you need to have an internet connection.")
        print("If you want to use your own images,", end=" ")
        print("you can change the images list in the images.json file.\n")

    @staticmethod
    def terminate_app(app):
        """Ends the app."""

        print("Exiting...")
        app.destroy()

    @staticmethod
    def set_app_data(app_data):
        """Sets the app data."""

        UIHandler.app_data = app_data

    @staticmethod
    def generate_filter_button(text, image_filter="NOFILTER"):
        """Generates the image button."""

        image_button = Button(
            UIHandler.app_data["root"],
            text=text,
            command=lambda: UIHandler.select_image(UIHandler.image_index, image_filter),
        )

        return image_button

    @staticmethod
    def generate_filter_buttons():
        """Generates the filter buttons."""

        filters_buttons = ["Blur", "Edge Enhance", "Emboss"]

        buttons = {}

        for filter_button in filters_buttons:
            buttons[filter_button] = UIHandler.generate_filter_button(
                filter_button, filter_button.upper().replace(" ", "_")
            )

        return buttons

    @staticmethod
    def generate_navigation_buttons():
        """Generates the navigation buttons."""

        buttons = {}
        navigation_state = UIHandler.get_navigation_state()

        buttons["Back"] = Button(
            UIHandler.app_data["root"],
            text="<-",
            command=lambda: UIHandler.select_image(UIHandler.image_index - 1),
            state=navigation_state["Back"],
        )

        buttons["Exit"] = Button(
            UIHandler.app_data["root"],
            text="Exit",
            command=lambda: UIHandler.terminate_app(UIHandler.app_data["root"]),
        )

        buttons["Next"] = Button(
            UIHandler.app_data["root"],
            text="->",
            command=lambda: UIHandler.select_image(UIHandler.image_index + 1),
            state=navigation_state["Next"],
        )

        return buttons

    @staticmethod
    def generate_ui_object():
        """Returns a dictionary of UI components."""

        ui_object = {
            "Filters": {
                "Buttons": UIHandler.generate_filter_buttons(),
                "Row": 0,
            },
            "Navigation": {
                "Buttons": UIHandler.generate_navigation_buttons(),
                "Row": 2,
            },
        }

        UIHandler.ui_object = ui_object

    @staticmethod
    def get_navigation_state():
        """Returns the navigation state."""

        navigation_state = {
            "Back": DISABLED if UIHandler.image_index <= 0 else NORMAL,
            "Next": DISABLED
            if (UIHandler.image_index >= UIHandler.app_data["number_of_images"] - 1)
            else NORMAL,
        }

        return navigation_state

    @staticmethod
    def get_current_image_index_label():
        """Returns the images label."""

        image_index = UIHandler.image_index
        number_of_images = UIHandler.app_data["number_of_images"]

        current_image_index_label = Label(
            UIHandler.app_data["root"],
            text=f"Image {str(image_index+1)} of {str(number_of_images)}",
            bd=1,
            relief=SUNKEN,
            anchor=E,
        )

        return current_image_index_label

    @staticmethod
    def generate_ui():
        """Generates the UI."""

        [image_index, image_filter] = [UIHandler.image_index, UIHandler.image_filter]

        for ui_component in UIHandler.ui_object.values():
            i = 0
            for button in ui_component["Buttons"]:
                ui_component["Buttons"][button].grid(row=ui_component["Row"], column=i)
                i += 1

        main_label = Label(
            image=UIHandler.app_data["filtered_images"][image_filter][image_index]
        )
        main_label.grid(row=1, column=0, columnspan=3)

        image_index_label = UIHandler.get_current_image_index_label()

        image_index_label.grid(row=3, column=0, columnspan=3, sticky=W + E)

    @staticmethod
    def select_image(image_index, image_filter="NOFILTER"):
        """Selects an image."""

        UIHandler.image_index = image_index
        UIHandler.image_filter = image_filter

        UIHandler.generate_ui_object()
        UIHandler.generate_ui()

    @staticmethod
    def start_app(generate_app_data_func):
        """Runs the app."""

        UIHandler.print_welcome_message()

        print("Loading the app data...\n")

        app_data = generate_app_data_func()

        UIHandler.set_app_data(app_data)

        print("\nDone! App will start now.")

        UIHandler.select_image(0)

        UIHandler.app_data["root"].mainloop()
