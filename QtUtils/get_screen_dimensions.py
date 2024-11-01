from PySide6.QtWidgets import QApplication

def getScreenDimensions() -> tuple[int, int]:
    # Get the screen geometry
    screen = QApplication.primaryScreen()
    screen_geometry = screen.geometry()

    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()

    return screen_width, screen_height

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    print(getScreenDimensions())  # (1920, 1080)

    sys.exit(app.exec())
    