import algorithms.image_operations
from user_interface.popups import warning_no_image_selected

import main
import tkinter

lossyAlgorithmButtons = []
losslessAlgorithmButtons = []
resizeImageButtons = []


def is_image_selected():
    if not hasattr(main, "currentImage"):
        warning_no_image_selected()
        return False
    else:
        return True


def forget_lossy_buttons():
    for button in lossyAlgorithmButtons:
        button.pack_forget()


def forget_lossless_buttons():
    for button in losslessAlgorithmButtons:
        button.pack_forget()


def forget_resize_buttons():
    for button in resizeImageButtons:
        button.pack_forget()


def create_algorithm_buttons(mainWindow: tkinter.Frame):
    currentSelectedAlgorithmsCategory = tkinter.StringVar(mainWindow)
    create_algorithm_category_radio_buttons_for_selection(mainWindow, currentSelectedAlgorithmsCategory)

    algorithmsLabelFrame = tkinter.LabelFrame(mainWindow, labelanchor=tkinter.NW, text="Algorithms")
    current_selected_compression_category = tkinter.StringVar(mainWindow)
    create_subcategory_for_selected_algorithm(algorithmsLabelFrame, current_selected_compression_category)
    algorithmsLabelFrame.pack(side=tkinter.BOTTOM, pady=32)


def hide_lossy_show_lossless(radioValue):
    if is_image_selected():
        forget_lossy_buttons()
        forget_resize_buttons()

        for button in losslessAlgorithmButtons:
            button.pack(side=tkinter.LEFT, padx=12, pady=8)
    else:
        radioValue.set(0)


def hide_lossless_show_lossy(radioValue):
    if is_image_selected():
        forget_lossless_buttons()
        forget_resize_buttons()

        for button in lossyAlgorithmButtons:
            button.pack(side=tkinter.LEFT, padx=12, pady=8)
    else:
        radioValue.set(0)


def hide_compressions_show_resizes(radioValue):
    if is_image_selected():
        forget_lossless_buttons()
        forget_lossy_buttons()

        for button in resizeImageButtons:
            button.pack(side=tkinter.LEFT, padx=12, pady=8)
    else:
        radioValue.set(0)


def create_algorithm_category_radio_buttons_for_selection(mainWindow: tkinter.Frame,
                                                          current_selected_algorithms_category: tkinter.StringVar):
    mainCategoriesFrame = tkinter.LabelFrame(mainWindow, labelanchor=tkinter.NW, text="Categories")
    losslessAlgorithmsRadioButton = tkinter.Radiobutton(mainCategoriesFrame,
                                                        text="Lossless Algorithms",
                                                        width=16,
                                                        variable=current_selected_algorithms_category,
                                                        value=1,
                                                        indicatoron=False,
                                                        command=lambda: hide_lossy_show_lossless(
                                                            current_selected_algorithms_category
                                                        ))
    losslessAlgorithmsRadioButton.pack(side=tkinter.LEFT, padx=32, pady=12)

    resizeImageButton = tkinter.Radiobutton(mainCategoriesFrame,
                                            text="Resize Image",
                                            width=16,
                                            variable=current_selected_algorithms_category,
                                            value=3,
                                            indicatoron=False,
                                            command=lambda: hide_compressions_show_resizes(
                                                current_selected_algorithms_category
                                            ))
    resizeImageButton.pack(side=tkinter.LEFT, padx=32, pady=12)

    lossyAlgorithmsRadioButton = tkinter.Radiobutton(mainCategoriesFrame,
                                                     text="Lossy Algorithms",
                                                     width=16,
                                                     variable=current_selected_algorithms_category,
                                                     value=2,
                                                     indicatoron=False,
                                                     command=lambda: hide_lossless_show_lossy(
                                                         current_selected_algorithms_category
                                                     ))
    lossyAlgorithmsRadioButton.pack(side=tkinter.LEFT, padx=32, pady=12)
    mainCategoriesFrame.pack(expand=1)


def create_subcategory_for_selected_algorithm(mainWindow: tkinter.Label or tkinter.LabelFrame,
                                              currentSelectedAlgorithm: tkinter.StringVar):
    jpegButton = tkinter.Radiobutton(mainWindow,
                                     text="JPEG",
                                     width=12,
                                     variable=currentSelectedAlgorithm,
                                     value=1,
                                     indicatoron=False,
                                     command=algorithms.image_operations.JPEG_compression)
    lossyAlgorithmButtons.append(jpegButton)
    webpButton = tkinter.Radiobutton(mainWindow,
                                     text="WEBP",
                                     width=12,
                                     variable=currentSelectedAlgorithm,
                                     value=2,
                                     indicatoron=False,
                                     command=algorithms.image_operations.WebP_compression)
    lossyAlgorithmButtons.append(webpButton)

    pngButton = tkinter.Radiobutton(mainWindow,
                                    text="PNG",
                                    width=12,
                                    variable=currentSelectedAlgorithm,
                                    value=3,
                                    indicatoron=False,
                                    command=algorithms.image_operations.PNG_compression)
    losslessAlgorithmButtons.append(pngButton)
    gifButton = tkinter.Radiobutton(mainWindow,
                                    text="GIF",
                                    width=12,
                                    variable=currentSelectedAlgorithm,
                                    value=4,
                                    indicatoron=False,
                                    command=algorithms.image_operations.GIF_compression)
    losslessAlgorithmButtons.append(gifButton)
    tiffButton = tkinter.Radiobutton(mainWindow,
                                     text="TIFF",
                                     width=12,
                                     variable=currentSelectedAlgorithm,
                                     indicatoron=False,
                                     value=5,
                                     command=algorithms.image_operations.TIFF_compression)
    losslessAlgorithmButtons.append(tiffButton)

    resize75 = tkinter.Radiobutton(mainWindow,
                                   text="75%",
                                   width=12,
                                   variable=currentSelectedAlgorithm,
                                   value=6,
                                   indicatoron=False,
                                   command=lambda: algorithms.image_operations.resize_by_75(main.currentImage.size))
    resizeImageButtons.append(resize75)
    resize50 = tkinter.Radiobutton(mainWindow,
                                   text="50%",
                                   width=12,
                                   variable=currentSelectedAlgorithm,
                                   value=7,
                                   indicatoron=False,
                                   command=lambda: algorithms.image_operations.resize_by_50(main.currentImage.size))
    resizeImageButtons.append(resize50)
    resize25 = tkinter.Radiobutton(mainWindow,
                                   text="25%",
                                   width=12,
                                   variable=currentSelectedAlgorithm,
                                   value=8,
                                   indicatoron=False,
                                   command=lambda: algorithms.image_operations.resize_by_25(main.currentImage.size))
    resizeImageButtons.append(resize25)
