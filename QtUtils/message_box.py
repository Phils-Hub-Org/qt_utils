from PySide6.QtWidgets import QMessageBox

def displayMessageBox(message: str, x: int = None, y: int = None) -> None:
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle("Information")
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    
    if x is None or y is None:
        screenWidth, screenHeight = getScreenDimms()

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
    msgBox.setWindowTitle("Confirmation")
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.No)
    result = msgBox.exec()
    return result == QMessageBox.Yes