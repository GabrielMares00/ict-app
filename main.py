import user_interface.startup as UI

currentImage = None
shownImage = None
imageResultExt = None


def start_program():
    global imageResultExt
    global currentImage
    global shownImage

    UI.start_user_interface()


if __name__ == "__main__":
    start_program()
