import PIL.Image
import os
import time

import main

from tkinter import filedialog
from user_interface import popups

imageResultExt = ""
qualityFactor = 0

newSize = 0, 0


def check_and_perform_conversion():
    global imageResultExt

    match imageResultExt:
        case ".png" | ".gif" | ".tiff":
            perform_convert()
        case ".jpeg" | ".webp":
            perform_convert_rgb()
        case _:
            popups.internal_error_conversion_lost_in_program()


def save_image():
    dir_name = filedialog.askdirectory()
    os.chdir(dir_name)

    startTime = time.time()

    if imageResultExt == "" and main.currentImage is not None:
        currentFormat = main.currentImage.format
        main.currentImage = main.currentImage.resize(newSize, PIL.Image.ANTIALIAS)
        main.currentImage.save("result" + "." + currentFormat.lower(), optimize=True)
    elif main.currentImage is not None:
        check_and_perform_conversion()
        if imageResultExt == ".jpeg":
            main.currentImage.save("result" + imageResultExt, quality=qualityFactor, optimize=True)
        elif imageResultExt == ".tiff":
            main.currentImage.save("result" + imageResultExt, compression="tiff_lzw", optimize=True)
        else:
            main.currentImage.save("result" + imageResultExt, optimize=True)
    else:
        popups.internal_error_conversion_lost_in_program()

    popups.image_done(time.time() - startTime)


def perform_convert():
    main.currentImage = main.currentImage.convert("RGBA", palette=PIL.Image.ADAPTIVE)


def perform_convert_rgb():
    main.currentImage = main.currentImage.convert("RGB", palette=PIL.Image.ADAPTIVE)


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
    qualityFactor = 75


def WebP_compression():
    global imageResultExt
    imageResultExt = ".webp"


def resize_by_75(size):
    newWidth = size[0] // 4 * 3
    newHeight = size[1] // 4 * 3

    global newSize
    newSize = newWidth, newHeight


def resize_by_50(size):
    newWidth = size[0] // 2
    newHeight = size[1] // 2

    global newSize
    newSize = newWidth, newHeight


def resize_by_25(size):
    newWidth = size[0] // 4
    newHeight = size[1] // 4

    global newSize
    newSize = newWidth, newHeight
