from Window import Window
import os
import yaml
import Config
import Constants


if not os.path.exists("settings.yaml"):
    yaml.dump(Constants.DEFAULT_SETTINGS, open("settings.yaml", "w"))

with open("settings.yaml") as data:
    document = yaml.full_load(data)[0]

    Config.TOP_ROW_LOCATIONS = document.get("top_row")
    Config.CENTRE_ROW_LOCATIONS = document.get("centre_row")
    Config.BOTTOM_ROW_LOCATIONS = document.get("bottom_row")

    Config.BACKGROUND_COLOR = document.get("background_colour")
    Config.CARD_COLOR = document.get("card_colour")
    Config.FOREGROUND_COLOR = document.get("foreground_colour")

win = Window()
win.start()
