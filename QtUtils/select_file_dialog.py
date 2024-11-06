from typing import Optional
from PySide6.QtWidgets import QFileDialog, QWidget

def selectFileDialog(parent: QWidget = None, name_filter: str = 'All Files (*.*)', window_title: str = 'Select a file') -> Optional[str]:
    file_dialog = QFileDialog(parent)
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    file_dialog.setNameFilter(name_filter)
    file_dialog.setWindowTitle(window_title)
    
    if file_dialog.exec() == QFileDialog.Accepted:
        return file_dialog.selectedFiles()[0]
    return None

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    selected_file = selectFileDialog()
    if selected_file:
        print(f"Selected file: {selected_file}")
    else:
        print("No file selected.")

    sys.exit(0)