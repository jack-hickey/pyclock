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

        self.layout = QtWidgets.QGridLayout()
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        # Weather Icon
        self.weather_icon_widget = QtWidgets.QLabel()
        self.weather_icon_widget.setAlignment(QtCore.Qt.AlignCenter)

        self.update_times()
        self.update_weather()

        self.layout.addWidget(self.zone_text, 0, 1)
        self.layout.addWidget(self.time_text, 1, 1)
        self.layout.addWidget(self.long_date, 2, 1)
        self.layout.addWidget(self.short_date, 3, 1)
        self.layout.addWidget(self.celsius_text, 4, 1)
        self.layout.addWidget(self.fahrenheit_text, 4, 2)
        self.layout.addWidget(self.weather_icon_widget, 4, 0)

        self.setLayout(self.layout)

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
        data = requests.get('http://openweathermap.org/img/wn/%s@2x.png' % self.data.icon_id).content

        pixmap.loadFromData(data)

        self.weather_icon_widget.setPixmap(pixmap)
