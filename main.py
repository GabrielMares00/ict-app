import user_interface.startup as UI

currentImage = None
shownImage = None


def start_program():
    global currentImage
    global shownImage

    UI.start_user_interface()


if __name__ == "__main__":
    start_program()
