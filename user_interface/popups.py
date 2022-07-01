import tkinter.messagebox as MessageBox
from tkinter.simpledialog import askstring


def warning_no_image_selected():
    MessageBox.showwarning(title="Image Error", message="Select an Image First")


def image_done(executionTime):
    MessageBox.showinfo(title="Image Compressed",
                        message="Your image has been compressed successfully\nExecution time: "
                                + str(round(executionTime, 2)) + " seconds")


def internal_error_conversion_lost_in_program():
    MessageBox.showerror(title="Internal Error",
                         message="You shouldn't see this normally...\nBut conversion or resize was lost somehow")


def input_new_filename():
    newFilename = askstring("New filename", "Please introduce the compressed/resized image's new name")
    return newFilename
