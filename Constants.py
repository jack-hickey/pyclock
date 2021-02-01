import os
from pyowm import OWM
from geopy.geocoders import Nominatim

ZONE_FONT_SIZE = 26
TEMPERATURE_FONT_SIZE = 16
TIME_FONT_SIZE = 58
LONG_DATE_FONT_SIZE = 16
SHORT_DATE_FONT_SIZE = 14
ICON_SIZE = 64
CARD_BACKGROUND = "#272727"
GEO_LOCATOR = Nominatim(user_agent="geoapiExercises")

API_INSTANCE = OWM(os.environ["WEATHER_API"]).weather_manager()

TIME_FORMAT = "%H:%M:%S"
LONG_DATE_FORMAT = "%A %d %B %Y"
SHORT_DATE_FORMAT = "%d/%m/%y"
WEATHER_UPDATE_INTERVAL = 600
DEFAULT_DATA_VALUE = ""
ZONE_CODE_FORMAT = "%Z"
ESCAPE_KEY = 16777216

DEFAULT_SETTINGS = [
        {
            "top_row": [
                "Los Angeles, US",
                "Philadelphia, US"
            ],
            "centre_row":[],
            "bottom_row":[
                "Paris, FR",
                "Calne, GB",
                "Pune, IN"
            ]
        }
    ]
