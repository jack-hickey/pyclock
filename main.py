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

win = Window()
win.start()
