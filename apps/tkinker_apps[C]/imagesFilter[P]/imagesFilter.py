images = [
    "https://picsum.photos/id/1/512",
    "https://picsum.photos/id/2/512",
    "https://picsum.photos/id/3/512",
    "https://picsum.photos/id/4/512",
    "https://picsum.photos/id/5/512"
]
# You can change the images list above to use your own images.

from tkinter import *
from PIL import ImageTk, Image, ImageFilter
import requests

root = Tk()
root.title("Image Filter App")

print("\nWelcome to my image filter app!")
print("In order to use this app, you need to have an internet connection.")
print("If you want to use your own images, you can change the images list in the code at the top of the file.\n")

if (len(images)==0):
    print("You need to add at least one image to the images list in the code.")
    print("Exiting...")
    exit()

print("Generating normal images...")

filters = {
    "BLUR": ImageFilter.BoxBlur(10),
    "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE_MORE,
    "EMBOSS": ImageFilter.EMBOSS
}

def getImage(url, filter="none"):
    im = Image.open(requests.get(url, stream=True).raw)
    im = im.resize((512, 512))
    if (filter != "none"):
        im = im.filter(filters[filter])
    return ImageTk.PhotoImage(im)

def generateList(filter="none"):
    converted = []
    for image in images:
        try:
            item = getImage(image, filter)
            converted.append(item)
            print("Image " + str(images.index(image) + 1) + " of " + str(len(images)) + " generated.")
        except:
            print("Error generating image " + str(images.index(image) + 1) + " of " + str(len(images)) + ".")
    return converted

def generateImages():
    imagesLists = {}
    imagesLists["NOFILTER"] = generateList()
    print("\nGenerating blured images...")
    imagesLists["BLUR"] = generateList("BLUR")
    print("\nGenerating edge enhanced images...")
    imagesLists["EDGE_ENHANCE"] = generateList("EDGE_ENHANCE")
    print("\nGenerating embossed images...")
    imagesLists["EMBOSS"] = generateList("EMBOSS")
    return imagesLists

def endApp():
    print("Exiting...")
    root.destroy()

imagesFiltered = generateImages()
length = len(imagesFiltered["NOFILTER"])

def generateUI(imgNumber=0, useFilter="NOFILTER"):

    UI = {
        "Filters": {
            "Buttons": {
                "Blur": Button(root, text="Blur", command=lambda: generateUI(imgNumber, "BLUR")),
                "Edge Enhance": Button(root, text="Edge Enhance", command=lambda: generateUI(imgNumber, "EDGE_ENHANCE")),
                "Emboss": Button(root, text="Emboss", command=lambda: generateUI(imgNumber, "EMBOSS")),
            },
            "Row": 0,
        },
        "Navigation": {
            "Buttons": {
                "Back": Button(root, text="<-", command=lambda: generateUI(imgNumber - 1)),
                "Exit": Button(root, text='Exit', command=lambda: endApp()),
                "Next": Button(root, text="->", command=lambda: generateUI(imgNumber + 1))
            },
            "Row": 2,
        }
    }

    if imgNumber == length-1:
        UI["Navigation"]["Buttons"]["Next"] = Button(root, text="->", state=DISABLED)
    if imgNumber == 0:
        UI["Navigation"]["Buttons"]["Back"] = Button(root, text="<-", state=DISABLED)

    for item in UI:
        i=0
        for button in UI[item]["Buttons"]:
            UI[item]["Buttons"][button].grid(row=UI[item]["Row"], column=i)
            i+=1

    mainLabel = Label(image=imagesFiltered[useFilter][imgNumber])
    mainLabel.grid(row=1, column=0, columnspan=3)
    status = Label(root, text="Image " + str(imgNumber+1) + " of " + str(length), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)

generateUI()

print("\nDone! App will start now.")

root.mainloop()