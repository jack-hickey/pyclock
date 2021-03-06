import sys
from ZoneInfo import ZoneInfo
from ZoneWidget import ZoneWidget
from PySide2 import QtWidgets, QtGui, QtCore
import Constants
import os
import Config


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

        width = 0
        height = 0

        for zone in Config.TOP_ROW_LOCATIONS:
            new_widget = ZoneWidget(ZoneInfo(zone))
            new_size = new_widget.get_size()

            if new_size.width() > width:
                width = new_size.width()

            if new_size.height() > height:
                height = new_size.height()

            top_set.addWidget(new_widget)

        for zone in Config.CENTRE_ROW_LOCATIONS:
            new_widget = ZoneWidget(ZoneInfo(zone))
            new_size = new_widget.get_size()

            if new_size.width() > width:
                width = new_size.width()

            if new_size.height() > height:
                height = new_size.height()

            centre_set.addWidget(new_widget)

        for zone in Config.BOTTOM_ROW_LOCATIONS:
            new_widget = ZoneWidget(ZoneInfo(zone))
            new_size = new_widget.get_size()

            if new_size.width() > width:
                width = new_size.width()

            if new_size.height() > height:
                height = new_size.height()

            bottom_set.addWidget(new_widget)

        top_widget = QtWidgets.QWidget()
        top_widget.setLayout(top_set)

        centre_widget = QtWidgets.QWidget()
        centre_widget.setLayout(centre_set)

        bottom_widget = QtWidgets.QWidget()
        bottom_widget.setLayout(bottom_set)

        if not Config.TOP_ROW_LOCATIONS:
            top_widget.hide()

        if not Config.CENTRE_ROW_LOCATIONS:
            centre_widget.hide()

        if not Config.BOTTOM_ROW_LOCATIONS:
            bottom_widget.hide()

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
            item.update_size(width, height)

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
                    background-color: % s;
                    color: % s;
                }

                .ZoneWidget
                {
                    background-color: % s;
                    padding-top: 15px;
                    border-radius: 10px;
                }
            ''' % (Config.BACKGROUND_COLOR, Config.FOREGROUND_COLOR, Config.CARD_COLOR)
        )
