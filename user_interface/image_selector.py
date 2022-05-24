import algorithms.file_parser
import tkinter


def create_image_selector_frame(mainWindow: tkinter.Frame or tkinter.LabelFrame):
    nullImage = tkinter.PhotoImage()
    panel = tkinter.Label(mainWindow, image=nullImage, compound=tkinter.CENTER, width=640, height=192)

    selectImageButton = tkinter.Button(master=mainWindow,
                                       text="Select Image",
                                       width=18,
                                       command=lambda: algorithms.file_parser.open_image(panel))
    panel.pack(pady=24)
    panel.pack_propagate(False)
    selectImageButton.pack(pady=12)
