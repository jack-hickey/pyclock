import sys
from ZoneInfo import ZoneInfo
from ZoneWidget import ZoneWidget
from PySide2 import QtWidgets, QtGui, QtCore
import Constants
import os


app = QtWidgets.QApplication(sys.argv)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.timer_count = 0

        font = ""

        for file in os.listdir(os.getcwd()):
            if file.endswith(".ttf"):
                font = file
                break

        if font != "":
            QtGui.QFontDatabase.addApplicationFont(font)

        grid = QtWidgets.QGridLayout()

        top_set = QtWidgets.QHBoxLayout()
        centre_set = QtWidgets.QHBoxLayout()
        bottom_set = QtWidgets.QHBoxLayout()

        top_set.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        bottom_set.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        top_set.addWidget(ZoneWidget(ZoneInfo("Los Angeles, US")))
        top_set.addWidget(ZoneWidget(ZoneInfo("Philadelphia, US")))

        bottom_set.addWidget(ZoneWidget(ZoneInfo("Paris, FR")))
        bottom_set.addWidget(ZoneWidget(ZoneInfo("Calne, GB")))
        bottom_set.addWidget(ZoneWidget(ZoneInfo("Pune, IN")))

        top_widget = QtWidgets.QWidget()
        top_widget.setLayout(top_set)

        centre_widget = QtWidgets.QWidget()
        centre_widget.setLayout(centre_set)

        centre_widget.hide()

        bottom_widget = QtWidgets.QWidget()
        bottom_widget.setLayout(bottom_set)

        grid.addWidget(top_widget, 0, 0)
        grid.addWidget(centre_widget, 1, 0)
        grid.addWidget(bottom_widget, 2, 0)

        bottom_set.setSpacing(15)
        top_set.setSpacing(15)

        self.win = QtWidgets.QWidget()
        self.win.setWindowTitle("PyClock")
        self.win.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.win.keyPressEvent = self.keyPressEvent

        self.set_css()

        self.win.setLayout(grid)

        # Data Timer
        self.timer = QtCore.QTimer()

        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

        for item in self.win.findChildren(ZoneWidget):
            item.update_size()

    def update_data(self):
        self.timer_count += 1
        reset_timer = False

        for control in self.win.findChildren(ZoneWidget):
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

    def set_css(self):
        self.win.setStyleSheet(
            '''
                QWidget
                {
                    background-color: #212121;
                    color: #DFDFDF;
                }

                .ZoneWidget
                {
                    background-color: %s;
                    padding-top: 15px;
                    border-radius: 10px;
                }
            ''' % Constants.CARD_BACKGROUND
        )
