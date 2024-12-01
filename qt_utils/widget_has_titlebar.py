from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget

def widgetHasTitlebar(widget):
    # Get the current window flags
    flags = widget.windowFlags()
    
    # Check for the frameless window hint
    return not (flags & Qt.FramelessWindowHint)

if __name__ == '__main__':
    import sys
    app = QApplication([])

    # Example QWidget with default title bar
    widget_with_titlebar = QWidget()
    widget_with_titlebar.setWindowTitle("With Title Bar")
    widget_with_titlebar.resize(300, 200)

    # Example QWidget without title bar
    widget_without_titlebar = QWidget()
    widget_without_titlebar.setWindowFlags(Qt.FramelessWindowHint)
    widget_without_titlebar.setWindowTitle("Without Title Bar")
    widget_without_titlebar.resize(300, 200)

    print("Widget with title bar:", widgetHasTitlebar(widget_with_titlebar))  # Should print True
    print("Widget without title bar:", widgetHasTitlebar(widget_without_titlebar))  # Should print False

    sys.exit(app.exec())