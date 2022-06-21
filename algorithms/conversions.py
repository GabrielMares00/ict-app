import PIL.Image
import os

import main

from tkinter import filedialog
from user_interface import popups

imageResultExt = ""
qualityFactor = 0


def check_and_perform_compression():
    global imageResultExt

    match imageResultExt:
        case ".png" | "gif" | ".tiff":
            perform_convert()
        case ".jpeg" | ".webp":
            perform_convert_rgb()
        case _:
            popups.internal_error_conversion_lost_in_program()


def save_image():
    dir_name = filedialog.askdirectory()
    os.chdir(dir_name)

    check_and_perform_compression()

    if imageResultExt is not ".jpeg":
        main.currentImage.save("result" + imageResultExt, optimize=True)
    else:
        main.currentImage.save("result" + imageResultExt, quality=qualityFactor, optimize=True)
    popups.image_done()


def perform_convert():
    main.currentImage = main.currentImage.convert("P", palette=PIL.Image.ADAPTIVE, colors=256)


def perform_convert_rgb():
    main.currentImage = main.currentImage.convert("RGB", palette=PIL.Image.ADAPTIVE, colors=256)


def PNG_compression():
    global imageResultExt
    imageResultExt = ".png"


def GIF_compression():
    global imageResultExt
    imageResultExt = ".gif"


def TIFF_compression():
    global imageResultExt
    imageResultExt = ".tiff"


def JPEG_compression():
    global imageResultExt, qualityFactor
    imageResultExt = ".jpeg"
    qualityFactor = 95


def WebP_compression():
    global imageResultExt
    imageResultExt = ".webp"
