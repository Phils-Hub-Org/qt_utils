from typing import Union

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, QWidget

class UiUtility:
    """Utility class for UI.
    
    label example:
        label = UiUtility.create_label("hello world", "label_1", self)
        size_policy = UiUtility.create_size_policy()  # can use same size policy for other widgets
        UiUtility.set_size_policy(label, size_policy)
    
    reminders:
        layout.addWidget(widget)
        layout.addWidget(widget, 0, Qt.AlignmentFlag.AlignLeft)
    
    alignments:
        Qt.AlignmentFlag.AlignLeft
        Qt.AlignmentFlag.AlignRight
        Qt.AlignmentFlag.AlignHCenter
    """
    @staticmethod
    def create_label(
            parent: QWidget, text: str, object_name: str, font: QFont=None,
            style_sheet: str="QLabel {}", alignment: Qt.AlignmentFlag=Qt.AlignmentFlag.AlignCenter) -> QLabel:
        """Create a label."""
        label = QLabel(text, parent)
        label.setObjectName(object_name)
        if font:
            label.setFont(font)
        label.setStyleSheet(style_sheet)
        label.setAlignment(alignment)
        return label

    @staticmethod
    def create_frame(
            parent: QWidget, object_name: str,
            shape: QFrame.Shape=QFrame.Shape.NoFrame, shadow: QFrame.Shadow=QFrame.Shadow.Plain,
            style_sheet: str="QFrame {}") -> QFrame:
        """Create a frame."""
        frame = QFrame(parent)
        frame.setObjectName(object_name)
        frame.setStyleSheet(style_sheet)
        frame.setFrameShape(shape)
        frame.setFrameShadow(shadow)
        return frame
    
    @staticmethod
    def create_size_policy(
            horizontal: QSizePolicy.Policy=QSizePolicy.Policy.Preferred, vertical: QSizePolicy.Policy=QSizePolicy.Policy.Preferred,
            horizontal_stretch: int = 0, vertical_stretch: int = 0) -> QSizePolicy:
        """Create a size policy."""
        size_policy = QSizePolicy(horizontal, vertical)
        size_policy.setHorizontalStretch(horizontal_stretch)
        size_policy.setVerticalStretch(vertical_stretch)
        return size_policy

    @staticmethod
    def set_size_policy(widget: QWidget, size_policy: QSizePolicy) -> None:
        """Set the size policy of a widget."""
        widget.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(size_policy)
    
    @staticmethod
    def create_font(families: str="Anybody Expanded", size: int=12, bold: bool=False) -> QFont:
        """Create a font."""
        font = QFont()
        font.setFamilies([families])
        font.setPointSize(size)
        font.setBold(bold)
        return font
    
    @staticmethod
    def create_layout(
            parent: QWidget, layout_class: Union[QVBoxLayout, QHBoxLayout], object_name: str,
            contents_margins: tuple=(9,9,9,9), spacing: int=6) -> Union[QVBoxLayout, QHBoxLayout]:
        """Create a layout."""
        layout = layout_class(parent)
        layout.setObjectName(object_name)
        layout.setContentsMargins(*contents_margins)
        layout.setSpacing(spacing)
        return layout