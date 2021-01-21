import sys
from ZoneInfo import ZoneInfo
from ZoneWidget import ZoneWidget
from PySide2 import QtWidgets, QtGui, QtCore
import Constants


app = QtWidgets.QApplication(sys.argv)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.timer_count = 0

        Constants.ICON_SIZE = int(app.primaryScreen().geometry().width() / 20)

        self.timezone_controls = [
            ZoneWidget(ZoneInfo("Europe/London", "Calne, GB", 1, 1)),
            ZoneWidget(ZoneInfo("US/Pacific", "Los Angeles, US", 0, 0)),
            ZoneWidget(ZoneInfo("US/Eastern", "Philadelphia, US", 0, 2)),
            ZoneWidget(ZoneInfo("Europe/Paris", "Paris, FR", 2, 0)),
            ZoneWidget(ZoneInfo("Asia/Calcutta", "Pune, IN", 2, 2))
        ]

        QtGui.QFontDatabase.addApplicationFont(Constants.FONT_LOCATION)

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(0)

        self.win = QtWidgets.QWidget()
        self.win.setWindowTitle("PyClock")
        self.win.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.win.keyPressEvent = self.keyPressEvent
        self.win.setStyleSheet('background-color: #121212; color:white; font-family:Roboto')

        for control in self.timezone_controls:
            grid.addWidget(control, control.data.zone.row, control.data.zone.col)

        self.win.setLayout(grid)

        # Data Timer
        self.timer = QtCore.QTimer()

        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def update_data(self):
        self.timer_count += 1
        reset_timer = False

        for control in self.timezone_controls:
            control.update_times()

            if self.timer_count == Constants.WEATHER_UPDATE_INTERVAL:
                control.update_weather()
                reset_timer = True

        if reset_timer:
            self.timer_count = 0

    def keyPressEvent(self, event):
        if event.key() == Constants.ESCAPE_KEY:
            self.win.close()

    def start(self):
        self.win.showFullScreen()

        app.exec_()
