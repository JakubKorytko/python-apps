""" Text module for displaying formatted text in the terminal. """

from colored import attr, fg


class Text:
    """Text class for displaying formatted text in the terminal."""

    @staticmethod
    def rainbow(text, colors, start):
        """Returns a rainbow-colored text."""

        colored_text = ""

        for i, letter in enumerate(text):
            color = start + i % colors
            colored_text += fg(color) + letter

        return colored_text + attr("reset")

    @staticmethod
    def display(text, color="white"):
        """Displays the given text in the given color."""

        print(fg(color) + text + attr("reset"))
