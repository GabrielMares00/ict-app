from PIL import Image, ImageTk
from tkinter import filedialog, Label, Tk

import main


def open_filename():
    maybeFilename = filedialog.askopenfilename(title='Select an image',
                                               filetypes=[('Image File', '.jpg')])
    return maybeFilename


def open_image(panel: Label):
    filename = open_filename()
    image = Image.open(filename)
    image = image.resize((image.width // 3, image.height // 3), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    main.currentImage = image

    panel.configure(image=main.currentImage)
