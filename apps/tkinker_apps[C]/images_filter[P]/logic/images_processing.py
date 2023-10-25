""" This module contains functions for processing images. """

from json import load as json_load
from sys import exit as sys_exit
from tkinter import Tk
from PIL import ImageTk, Image, ImageFilter
import requests

def get_available_filters():
    """ Returns a dictionary of available filters. """

    filters = {
        "BLUR": ImageFilter.BoxBlur(10),
        "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE_MORE,
        "EMBOSS": ImageFilter.EMBOSS
    }

    return filters

def load_images_from_json():
    """ Loads images from a images.json file. """

    try:
        with open("images.json", "r", encoding="utf-8") as file:
            images = json_load(file)
    except FileNotFoundError:
        images = []

    if len(images) == 0:
        print("You need to add at least one image to the images list in the images.json file.")
        print("Exiting...")
        sys_exit()

    return images

def get_image(url, filters, image_filter = "none"):
    """ Returns an image from the given url. """

    image = Image.open(requests.get(url, stream=True, timeout=10).raw)
    image = image.resize((512, 512))
    if image_filter != "none":
        image = image.filter(filters[image_filter])
    return ImageTk.PhotoImage(image)

def generate_list(filters, image_filter="none"):
    """ Returns a list of images. """

    images = load_images_from_json()

    converted = []
    for image in images:

        image_index = str(images.index(image) + 1)
        images_length = str(len(images))

        try:
            item = get_image(image, filters, image_filter)
            converted.append(item)

            print(f"Image {image_index} of {images_length} generated.")

        except requests.exceptions.ConnectionError:
            print(f"Error generating image {image_index} of {images_length}.")
    return converted

def generate_images():
    """ Returns a dictionary of filtered and unfiltered images. """

    filters = get_available_filters()

    image_lists = {}
    image_lists["NOFILTER"] = generate_list(filters)

    print("\nGenerating blured images...")
    image_lists["BLUR"] = generate_list(filters, "BLUR")

    print("\nGenerating edge enhanced images...")
    image_lists["EDGE_ENHANCE"] = generate_list(filters, "EDGE_ENHANCE")

    print("\nGenerating embossed images...")
    image_lists["EMBOSS"] = generate_list(filters, "EMBOSS")

    return image_lists

def generate_app_data():
    """ Returns a dictionary of app data. """

    root = Tk()
    root.title("Image Filter App")

    print("Generating normal images...")

    filtered_images = generate_images()
    number_of_images = len(filtered_images["NOFILTER"])

    app_data = {
        "root": root,
        "number_of_images": number_of_images,
        "filtered_images": filtered_images,
    }

    return app_data
