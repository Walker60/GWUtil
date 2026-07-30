import os
import sys

import keyboard

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import imageUtil

imagePath = "Images/"

while not keyboard.is_pressed('1'):
    imageUtil.clickOnImage(imagePath + "Forge", gray=False)
    imageUtil.clickOnImage(imagePath + "Refill", gray=False)
