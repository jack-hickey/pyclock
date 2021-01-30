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

            self.condition = "clear_sky"

            if weather.weather_icon_name.startswith("01"):
                self.condition = "clear_sky"
            elif weather.weather_icon_name.startswith("02"):
                self.condition = "few_clouds"
            elif weather.weather_icon_name.startswith("03"):
                self.condition = "scattered_clouds"
            elif weather.weather_icon_name.startswith("04"):
                self.condition = "broken_clouds"
            elif weather.weather_icon_name.startswith("09"):
                self.condition = "shower_rain"
            elif weather.weather_icon_name.startswith("10"):
                self.condition = "rain"
            elif weather.weather_icon_name.startswith("11"):
                self.condition = "thunderstorm"
            elif weather.weather_icon_name.startswith("13"):
                self.condition = "snow"
            elif weather.weather_icon_name.startswith("50"):
                self.condition = "mist"
        except InvalidSSLCertificateError:
            pass
