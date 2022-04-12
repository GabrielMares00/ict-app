import algorithms.file_parser
import tkinter

from user_interface.algorithm_buttons import create_algorithm_buttons


def start_user_interface():
    try:
        mainWindow = tkinter.Tk()
        mainWindow.title("ict-app")
        mainWindow.geometry("800x600")
        mainWindow.resizable(width=True, height=True)

        panel = tkinter.Label(mainWindow)

        selectImageButton = tkinter.Button(master=mainWindow,
                                           text="Select Image",
                                           width=15,
                                           command=lambda: algorithms.file_parser.open_image(panel))
        selectImageButton.pack(pady=24)
        panel.pack()

        create_algorithm_buttons(mainWindow)

        mainWindow.mainloop()
    except KeyboardInterrupt:
        print("Program stopped by keyboard")
