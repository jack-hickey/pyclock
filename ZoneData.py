from datetime import datetime
from pyowm.commons.exceptions import InvalidSSLCertificateError
from pytz import timezone
from pyowm import OWM
import Constants
from ZoneInfo import ZoneInfo


class ZoneData:
    def __init__(self, zone: ZoneInfo):
        self.zone = zone
        self.weather_mgr = OWM(Constants.WEATHER_API).weather_manager()
        self.datetime_data = None
        self.zone_code = ""
        self.icon_id = ""
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
            self.icon_id = weather.weather_icon_name
        except InvalidSSLCertificateError:
            pass
