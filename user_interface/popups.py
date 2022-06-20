import tkinter.messagebox as MessageBox


def warning_no_image_selected():
    MessageBox.showwarning(title="Image Error", message="Select an Image First")


def image_done():
    MessageBox.showinfo(title="Image Compressed", message="Your image has been compressed successfully")


def internal_error_conversion_lost_in_program():
    MessageBox.showerror(title="Internal Error",
                         message="You shouldn't see this normally...\nBut conversion was lost somehow")
