from PIL import Image, ImageOps, ImageTk
from tkinter import filedialog, Label, Tk

import main


def open_filename():
    maybeFilename = filedialog.askopenfilename(title='Select an image',
                                               filetypes=[('Image File', '.raw .jpg .jpeg .png .webm .gif')])
    return maybeFilename


def open_image(panel: Label):
    filename = open_filename()
    image = Image.open(filename)
    image = ImageOps.contain(image, (432, 192))
    image = ImageTk.PhotoImage(image)

    main.currentImage = image

    panel.configure(image=main.currentImage)
