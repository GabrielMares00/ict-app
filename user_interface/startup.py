import tkinter

from user_interface.algorithm_buttons import create_algorithm_buttons
from user_interface.image_selector import create_image_selector_frame


def start_user_interface():
    try:
        mainWindow = tkinter.Tk()
        mainWindow.title("ict-app")
        mainWindow.geometry("800x800")
        mainWindow.resizable(width=False, height=False)

        imageSelectionFrame = tkinter.LabelFrame(mainWindow, height=400, labelanchor=tkinter.NW, text="Image")
        create_image_selector_frame(imageSelectionFrame)
        imageSelectionFrame.pack(side=tkinter.TOP, pady=32)

        selectionFrame = tkinter.Frame(mainWindow, height=400)
        create_algorithm_buttons(selectionFrame)
        selectionFrame.pack(side=tkinter.TOP, pady=32)

        performButton = tkinter.Button(mainWindow, width=18, text="Perform Compression")
        performButton.pack(side=tkinter.BOTTOM, pady=32)

        mainWindow.mainloop()

    except KeyboardInterrupt:
        print("Program stopped by keyboard")
