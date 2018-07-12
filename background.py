#!/usr/bin/python3
import os
import datetime

time = int(str(datetime.datetime.now().time()).split(":")[0])

if time < 12:
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/woolf/Pictures/AbeKislevitz_BambooForest_CD27.jpg")
elif time > 12 and time < 20:
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/woolf/Pictures/Tidal-Wave-Wallpapers-Gallery-71-Plus-PIC-WPT302629.jpg")
else:
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/woolf/Pictures/paint-stains-surface.jpg")
