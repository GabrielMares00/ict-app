import tkinter

lossyAlgorithmButtons = []
losslessAlgorithmButtons = []


def create_algorithm_buttons(main_window: tkinter.Tk):
    currentSelectedAlgorithmsCategory = tkinter.StringVar(main_window, "1")
    create_algorithm_category_radio_buttons_for_selection(main_window, currentSelectedAlgorithmsCategory)

    lossyButtonTest = tkinter.Button(main_window, text="Lossy", width=12)
    lossyAlgorithmButtons.append(lossyButtonTest)

    losslessButtonTest = tkinter.Button(main_window, text="Lossless", width=12)
    losslessAlgorithmButtons.append(losslessButtonTest)


def hide_lossy_show_lossless():
    for button in lossyAlgorithmButtons:
        button.pack_forget()
    for button in losslessAlgorithmButtons:
        button.pack(side=tkinter.BOTTOM, pady=16)


def hide_lossless_show_lossy():
    for button in losslessAlgorithmButtons:
        button.pack_forget()
    for button in lossyAlgorithmButtons:
        button.pack(side=tkinter.BOTTOM, pady=16)


def create_algorithm_category_radio_buttons_for_selection(main_window: tkinter.Tk,
                                                          current_selected_algorithms_category: tkinter.StringVar):
    losslessAlgorithmsRadioButton = tkinter.Radiobutton(main_window,
                                                        text="Lossless Algorithms",
                                                        width=16,
                                                        variable=current_selected_algorithms_category,
                                                        value=1,
                                                        indicatoron=False,
                                                        command=hide_lossy_show_lossless)
    losslessAlgorithmsRadioButton.pack(side=tkinter.LEFT, padx=32)

    lossyAlgorithmsRadioButton = tkinter.Radiobutton(main_window,
                                                     text="Lossy Algorithms",
                                                     width=16,
                                                     variable=current_selected_algorithms_category,
                                                     value=2,
                                                     indicatoron=False,
                                                     command=hide_lossless_show_lossy)
    lossyAlgorithmsRadioButton.pack(side=tkinter.RIGHT, padx=32)