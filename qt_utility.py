from PySide6.QtWidgets import QMessageBox

def displayMessageBox(message: str) -> None:
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle("Information")
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()

def displayYesNoMessageBox(message: str) -> bool:
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setWindowTitle("Confirmation")
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg_box.setDefaultButton(QMessageBox.No)
    result = msg_box.exec()
    return result == QMessageBox.Yes