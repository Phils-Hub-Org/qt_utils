from PySide6.QtWidgets import QAbstractScrollArea

def scroll_to_bottom(widget: QAbstractScrollArea, extra_scroll: int = 0) -> None:
    widget.verticalScrollBar().setValue(widget.verticalScrollBar().maximum() + extra_scroll)