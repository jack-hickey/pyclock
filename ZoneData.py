from datetime import datetime
from pyowm.commons.exceptions import InvalidSSLCertificateError
from pytz import timezone
from pyowm import OWM
import os
import Constants
from ZoneInfo import ZoneInfo


class ZoneData:
    def __init__(self, zone: ZoneInfo):
        self.zone = zone
        self.weather_mgr = OWM(os.environ["WEATHER_API"]).weather_manager()
        self.datetime_data = None
        self.zone_code = ""
        self.condition = "clear_sky"
        self.celsius = ""
        self.fahrenheit = ""

    def update_times(self):
        data = timezone(self.zone.zone)

        self.datetime_data = datetime.now(data)
        self.zone_code = self.datetime_data.strftime(Constants.ZONE_CODE_FORMAT)

    def update_weather(self):
        try:
            weather = self.weather_mgr.weather_at_place(self.zone.weather_name).weather

            self.celsius = str(weather.temperature('celsius')['temp'])
            self.fahrenheit = str(weather.temperature('fahrenheit')['temp'])

            self.condition = weather.status.lower()

            if self.condition == "smoke"\
                    or self.condition == "haze"\
                    or self.condition == "dust"\
                    or self.condition == "fog"\
                    or self.condition == "sand"\
                    or self.condition == "ash"\
                    or self.condition == "squall":
                self.condition = "mist"

            if self.condition != "tornado" and weather.weather_icon_name.endswith("n"):
                self.condition += "_night"
        except InvalidSSLCertificateError:
            if self.condition == "":
                self.condition = "clear"

            if self.celsius == "":
                self.celsius = "?"

            if self.fahrenheit == "":
                self.fahrenheit = "?"
