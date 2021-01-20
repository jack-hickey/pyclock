import sys
from ZoneInfo import ZoneInfo
from ZoneWidget import ZoneWidget
from PySide2 import QtWidgets, QtGui
import Constants


app = QtWidgets.QApplication(sys.argv)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        timezones = [
            ZoneInfo("Europe/London", "Calne, GB", 1, 1),
            ZoneInfo("US/Pacific", "Los Angeles, US", 0, 0),
            ZoneInfo("US/Eastern", "Philadelphia, US", 0, 2),
            ZoneInfo("Europe/Paris", "Paris, FR", 2, 0),
            ZoneInfo("Asia/Calcutta", "Pune, IN", 2, 2)
        ]

        QtGui.QFontDatabase.addApplicationFont(Constants.FONT_LOCATION)
        app.setFont(QtGui.QFont(Constants.FONT_NAME))

        grid = QtWidgets.QGridLayout()

        self.win = QtWidgets.QWidget()
        self.win.setWindowTitle("PyClock")
        self.win.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.win.keyPressEvent = self.keyPressEvent
        self.win.setStyleSheet('background-color: #121212; color: white')

        for zone in timezones:
            grid.addWidget(ZoneWidget(zone), zone.row, zone.col)

        self.win.setLayout(grid)

    def keyPressEvent(self, event):
        if event.key() == Constants.ESCAPE_KEY:
            self.win.close()

    def start(self):
        self.win.showFullScreen()

        app.exec_()
