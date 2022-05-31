from user_interface.warning_popups import warning_no_image_selected

import main
import tkinter

lossyAlgorithmButtons = []
losslessAlgorithmButtons = []
resizeImageButtons = []


def create_algorithm_buttons(mainWindow: tkinter.Frame):
    currentSelectedAlgorithmsCategory = tkinter.StringVar(mainWindow, "1")
    create_algorithm_category_radio_buttons_for_selection(mainWindow, currentSelectedAlgorithmsCategory)

    algorithmsLabelFrame = tkinter.LabelFrame(mainWindow, labelanchor=tkinter.NW, text="Algorithms")
    create_subcategory_for_selected_algorithm(algorithmsLabelFrame)
    algorithmsLabelFrame.pack(side=tkinter.BOTTOM, pady=32)


def hide_lossy_show_lossless():
    if not hasattr(main, "currentImage"):
        warning_no_image_selected()
    else:
        for button in lossyAlgorithmButtons:
            button.pack_forget()
        for button in resizeImageButtons:
            button.pack_forget()
        for button in losslessAlgorithmButtons:
            button.pack(side=tkinter.LEFT, padx=12, pady=8)


def hide_lossless_show_lossy():
    if not hasattr(main, "currentImage"):
        warning_no_image_selected()
    else:
        for button in losslessAlgorithmButtons:
            button.pack_forget()
        for button in resizeImageButtons:
            button.pack_forget()
        for button in lossyAlgorithmButtons:
            button.pack(side=tkinter.LEFT, padx=12, pady=8)


def hide_compressions_show_resizes():
    if not hasattr(main, "currentImage"):
        warning_no_image_selected()
    else:
        for button in losslessAlgorithmButtons:
            button.pack_forget()
        for button in lossyAlgorithmButtons:
            button.pack_forget()
        for button in resizeImageButtons:
            button.pack(side=tkinter.LEFT, padx=12, pady=8)


def create_algorithm_category_radio_buttons_for_selection(mainWindow: tkinter.Frame,
                                                          current_selected_algorithms_category: tkinter.StringVar):
    mainCategoriesFrame = tkinter.LabelFrame(mainWindow, labelanchor=tkinter.NW, text="Categories")
    losslessAlgorithmsRadioButton = tkinter.Radiobutton(mainCategoriesFrame,
                                                        text="Lossless Algorithms",
                                                        width=16,
                                                        variable=current_selected_algorithms_category,
                                                        value=1,
                                                        indicatoron=False,
                                                        command=hide_lossy_show_lossless)
    losslessAlgorithmsRadioButton.pack(side=tkinter.LEFT, padx=32, pady=12)

    resizeImageButton = tkinter.Radiobutton(mainCategoriesFrame,
                                            text="Resize Image",
                                            width=16,
                                            variable=current_selected_algorithms_category,
                                            value=3,
                                            indicatoron=False,
                                            command=hide_compressions_show_resizes)
    resizeImageButton.pack(side=tkinter.LEFT, padx=32, pady=12)

    lossyAlgorithmsRadioButton = tkinter.Radiobutton(mainCategoriesFrame,
                                                     text="Lossy Algorithms",
                                                     width=16,
                                                     variable=current_selected_algorithms_category,
                                                     value=2,
                                                     indicatoron=False,
                                                     command=hide_lossless_show_lossy)
    lossyAlgorithmsRadioButton.pack(side=tkinter.LEFT, padx=32, pady=12)
    mainCategoriesFrame.pack(expand=1)


def create_subcategory_for_selected_algorithm(mainWindow: tkinter.Label or tkinter.LabelFrame):
    jpegButton = tkinter.Button(mainWindow, text="JPEG", width=12)
    lossyAlgorithmButtons.append(jpegButton)
    bpgButton = tkinter.Button(mainWindow, text="BGP", width=12)
    lossyAlgorithmButtons.append(bpgButton)
    webpButton = tkinter.Button(mainWindow, text="WEBP", width=12)
    lossyAlgorithmButtons.append(webpButton)

    pngButton = tkinter.Button(mainWindow, text="PNG", width=12)
    losslessAlgorithmButtons.append(pngButton)
    gifButton = tkinter.Button(mainWindow, text="GIF", width=12)
    losslessAlgorithmButtons.append(gifButton)
    flifButton = tkinter.Button(mainWindow, text="FLIF", width=12)
    losslessAlgorithmButtons.append(flifButton)

    resize75 = tkinter.Button(mainWindow, text="75%", width=12)
    resizeImageButtons.append(resize75)
    resize50 = tkinter.Button(mainWindow, text="50%", width=12)
    resizeImageButtons.append(resize50)
    resizeCustom = tkinter.Button(mainWindow, text="Custom Size", width=12)
    resizeImageButtons.append(resizeCustom)
