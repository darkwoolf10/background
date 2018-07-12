#!/usr/bin/python3
import os, os.path
import random

DIR = '/home/woolf/Workspace/background/images'

count_wallpaper = (len([name for name in os.listdir(DIR)]))

if os.listdir(DIR):
    random_image = random.randint(1,count_wallpaper)
    print("Change image")
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + DIR + "/" + str(random_image) + ".jpg")
else:
    print("Not found files in " + str(DIR))
