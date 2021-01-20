import sys
from ZoneInfo import ZoneInfo
from ZoneWidget import ZoneWidget
from PySide2 import QtWidgets
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

        grid = QtWidgets.QGridLayout()

        self.win = QtWidgets.QWidget()
        self.win.keyPressEvent = self.keyPressEvent
        self.win.setStyleSheet('background-color: #121212; color: white; font-family: "Verdana"')

        for zone in timezones:
            grid.addWidget(ZoneWidget(zone), zone.row, zone.col)

        self.win.setLayout(grid)

    def keyPressEvent(self, event):
        if event.key() == Constants.ESCAPE_KEY:
            self.win.close()

    def start(self):
        self.win.showFullScreen()

        app.exec_()
