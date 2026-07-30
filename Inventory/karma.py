import os
import sys
import time

import pyautogui

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import imageUtil

imagePath = 'Images/'

while (karma := imageUtil.findImageCenter(imagePath + "Karma", region=None, gray=None, con=.9)) is not None:
    pyautogui.moveTo(karma[0], karma[1])
    pyautogui.click(button='right')
    imageUtil.clickOnImage(imagePath + "ConsumeAll")
    time.sleep(.25)
