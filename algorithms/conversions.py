import PIL.Image
import os

import main

from tkinter import filedialog
from user_interface import popups


def check_and_perform_compression():
    match main.imageResultExt:
        case ".png":
            PNG_perform()
        case ".gif":
            GIF_perform()
        case _:
            popups.internal_error_conversion_lost_in_program()


def save_image():
    dir_name = filedialog.askdirectory()
    os.chdir(dir_name)

    check_and_perform_compression()

    main.currentImage.save("result" + main.imageResultExt, optimize=True)
    popups.image_done()


def PNG_perform():
    main.currentImage = main.currentImage.convert("P", palette=PIL.Image.ADAPTIVE, colors=256)


def PNG_compression():
    main.imageResultExt = ".png"


def GIF_perform():
    main.currentImage = main.currentImage.convert("P", palette=PIL.Image.ADAPTIVE)


def GIF_compression():
    main.imageResultExt = ".gif"
