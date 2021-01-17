import Constants
from PySide2 import QtCore, QtWidgets


class DataDisplay(QtWidgets.QLabel):
    def __init__(self, size: int, text=Constants.DEFAULT_DATA_VALUE):
        super().__init__()

        self.setText(text)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("font-size: %spt;" % size)
