from colored import fg, attr

class Text:
    @staticmethod
    def rainbow(text, colors, start):
        coloredText = ""

        for i in range(len(text)):
            color = start + i % colors
            coloredText += fg(color) + text[i]

        return coloredText + attr('reset')

    @staticmethod
    def display(text, color="white"):
        print(fg(color) + text + attr('reset'))