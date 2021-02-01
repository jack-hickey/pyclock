from timezonefinder import TimezoneFinder
import Constants


class ZoneInfo:
    def __init__(self, location: str):
        self.weather_name = location
        location = Constants.GEO_LOCATOR.geocode(self.weather_name)

        self.zone = TimezoneFinder().timezone_at(lng=location.longitude, lat=location.latitude)
