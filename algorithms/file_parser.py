import PIL.Image
from PIL import Image, ImageOps, ImageTk
from tkinter import filedialog, Label, Tk

import main
import os


def open_filename():
    maybeFilename = filedialog.askopenfilename(title='Select an image',
                                               filetypes=[('Image File', '.raw .jpg .jpeg .png .webm .gif')])
    return maybeFilename


def open_image(panel: Label):
    filename = open_filename()
    image = Image.open(filename)

    main.currentImage = image

    containedImage = ImageOps.contain(image, (432, 192))
    main.shownImage = ImageTk.PhotoImage(containedImage)

    panel.configure(image=main.shownImage)
