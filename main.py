import user_interface.startup as UI


def start_program():
    global currentImage
    global shownImage

    UI.start_user_interface()


if __name__ == "__main__":
    currentImage = None
    shownImage = None

    start_program()
