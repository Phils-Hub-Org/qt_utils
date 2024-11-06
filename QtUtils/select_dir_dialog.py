from typing import Optional
from PySide6.QtWidgets import QFileDialog, QWidget

def selectDirDialog(parent: QWidget = None, window_title: str = 'Select a directory') -> Optional[str]:
    directory_dialog = QFileDialog(parent)
    directory_dialog.setFileMode(QFileDialog.Directory)
    directory_dialog.setOption(QFileDialog.ShowDirsOnly, True)  # Only show directories
    directory_dialog.setWindowTitle(window_title)
    
    if directory_dialog.exec() == QFileDialog.Accepted:
        return directory_dialog.selectedFiles()[0]
    return None

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    selected_directory = selectDirDialog()
    if selected_directory:
        print(f"Selected directory: {selected_directory}")
    else:
        print("No directory selected.")

    sys.exit(0)
