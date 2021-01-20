import Constants
from PySide2 import QtCore, QtWidgets, QtGui


class DataDisplay(QtWidgets.QLabel):
    def __init__(self, size: int, text=Constants.DEFAULT_DATA_VALUE):
        super().__init__()

        self.setText(text)
        self.setFont(QtGui.QFont("Roboto", size))
        self.setAlignment(QtCore.Qt.AlignCenter)
