from PySide6.QtWidgets import QMessageBox

def displayMessageBox(message: str) -> None:
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle('Information')
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def displayMessageBox2(screenWidth: int, screenHeight: int, message: str, x: int = None, y: int = None) -> None:
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle('Information')
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    
    if x is None or y is None:
        if x is None:
            # Get screen geometry and center horizontally
            msgBox_width = msgBox.sizeHint().width()
            x = (screenWidth - msgBox_width) // 2

        if y is None:
            # Get screen geometry and center vertically
            msgBox_height = msgBox.sizeHint().height()
            y = (screenHeight - msgBox_height) // 2  # Vertically center
    
    msgBox.move(x, y)  # Set position
    msgBox.exec()

def displayYesNoMessageBox(message: str) -> bool:
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setWindowTitle('Confirmation')
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.No)
    result = msgBox.exec()
    return result == QMessageBox.Yes

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    displayMessageBox('Hello, World!')
    # displayMessageBox2(1920, 1080, 'Hello, World!')
    # displayYesNoMessageBox('Are you sure?')

    sys.exit(app.exec())