""" Text module for displaying formatted text in the terminal. """

from colored import fg, attr

class Text:
    @staticmethod
    def rainbow(text, colors, start):
        """ Returns a rainbow-colored text. """

        coloredText = ""

        for i in range(len(text)):
            color = start + i % colors
            coloredText += fg(color) + text[i]

        return coloredText + attr('reset')

    @staticmethod
    def display(text, color="white"):
        """ Displays the given text in the given color. """

        print(fg(color) + text + attr('reset'))
