import algorithms.file_parser
import tkinter

from user_interface.algorithm_buttons import create_algorithm_buttons


def start_user_interface():
    try:
        mainWindow = tkinter.Tk()
        mainWindow.title("ict-app")
        mainWindow.geometry("800x600")
        mainWindow.resizable(width=True, height=True)

        nullImage = tkinter.PhotoImage()
        panel = tkinter.Label(mainWindow, image=nullImage, compound=tkinter.CENTER, width=256, height=256)

        selectImageButton = tkinter.Button(master=mainWindow,
                                           text="Select Image",
                                           width=15,
                                           command=lambda: algorithms.file_parser.open_image(panel))
        panel.pack(pady=24)
        panel.pack_propagate(False)
        selectImageButton.pack(pady=24)

        create_algorithm_buttons(mainWindow)

        mainWindow.mainloop()
    except KeyboardInterrupt:
        print("Program stopped by keyboard")
