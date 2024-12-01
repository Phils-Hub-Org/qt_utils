from PySide6.QtWidgets import QGraphicsDropShadowEffect, QWidget
from PySide6.QtGui import QColor

def setShadow(widget: QWidget, color: tuple, offset_x: int, offset_y: int, blur_radius: int=0) -> None:
    effect = QGraphicsDropShadowEffect(widget)
    effect.setColor(QColor(*color))
    effect.setOffset(offset_x, offset_y)
    effect.setBlurRadius(blur_radius)
    widget.setGraphicsEffect(effect)