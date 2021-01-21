import Constants
from DataDisplay import DataDisplay
from ZoneData import ZoneData
from PySide2 import QtCore, QtWidgets, QtGui
from ZoneInfo import ZoneInfo
import requests


class ZoneWidget(QtWidgets.QWidget):
    def __init__(self, zone: ZoneInfo):
        super().__init__()

        self.data = ZoneData(zone)

        self.setStyleSheet("background-color:red")

        # Zone Code
        self.zone_text = DataDisplay(Constants.ZONE_FONT_SIZE, self.data.zone_code)

        # Time
        self.time_text = DataDisplay(Constants.TIME_FONT_SIZE)

        # Long Date
        self.long_date = DataDisplay(Constants.LONG_DATE_FONT_SIZE)

        # Short Date
        self.short_date = DataDisplay(Constants.SHORT_DATE_FONT_SIZE)

        # Celsius
        self.celsius_text = DataDisplay(Constants.TEMPERATURE_FONT_SIZE)

        # Fahrenheit
        self.fahrenheit_text = DataDisplay(Constants.TEMPERATURE_FONT_SIZE)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.layout.setSpacing(0)

        # Weather Icon
        self.weather_icon_widget = QtWidgets.QLabel()
        self.weather_icon_widget.setAlignment(QtCore.Qt.AlignCenter)

        self.icon_size = QtGui.QFontMetrics(self.long_date.font()).height() * 2

        self.update_times()
        self.update_weather()

        self.layout.addWidget(self.zone_text)
        self.layout.addWidget(self.time_text)
        self.layout.addWidget(self.long_date)
        self.layout.addWidget(self.short_date)

        self.init_weather_controls()

        self.setLayout(self.layout)

    def init_weather_controls(self):
        weather_grid = QtWidgets.QHBoxLayout()

        margin = int((self.icon_size * 1.5))

        self.celsius_text.setContentsMargins(margin, 0, margin, 0)

        weather_grid.addWidget(self.weather_icon_widget)
        weather_grid.addWidget(self.celsius_text)
        weather_grid.addWidget(self.fahrenheit_text)

        self.weather_icon_widget.setFixedWidth(
            QtGui.QFontMetrics(self.fahrenheit_text.font()).width(self.fahrenheit_text.text()))

        weather_widget = QtWidgets.QWidget()
        weather_widget.setLayout(weather_grid)

        self.layout.addWidget(weather_widget)

    def update_times(self):
        self.data.update_times()

        self.time_text.setText(self.data.datetime_data.strftime(Constants.TIME_FORMAT))
        self.long_date.setText(self.data.datetime_data.strftime(Constants.LONG_DATE_FORMAT))
        self.short_date.setText(self.data.datetime_data.strftime(Constants.SHORT_DATE_FORMAT))

    def update_weather(self):
        self.data.update_weather()

        self.celsius_text.setText("%s °C" % self.data.celsius)
        self.fahrenheit_text.setText("%s °F" % self.data.fahrenheit)

        pixmap = QtGui.QPixmap()
        data = requests.get('https://openweathermap.org/img/wn/%s@2x.png' % self.data.icon_id).content

        pixmap.loadFromData(QtCore.QByteArray(data))
        pixmap = pixmap.scaled(self.icon_size, self.icon_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        self.weather_icon_widget.setPixmap(pixmap)
