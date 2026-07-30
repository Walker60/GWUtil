from pyautogui import *
import pyautogui
import time
import random
import sys
sys.path.insert(1, 'C:/Users/12069/Dropbox/Scripts/Bots/Util')
sys.path.insert(2, 'C:/Users/Chris Walker/Dropbox/Scripts/Bots/Util')
import imageUtil

imagePath = 'Images/'

while (karma := imageUtil.findImageCenter(imagePath + "Karma", region = None, gray = None, con = .9)) != None:
	pyautogui.moveTo(karma[0], karma[1])
	pyautogui.click(button='right')
	imageUtil.clickOnImage(imagePath + "ConsumeAll")
	time.sleep(.25)
