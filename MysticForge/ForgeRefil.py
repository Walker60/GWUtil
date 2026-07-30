from pyautogui import *
import pyautogui
import time
import keyboard
import sys
sys.path.insert(1, 'C:/Users/12069/Dropbox/Scripts/Bots/Util')
sys.path.insert(1, 'C:/Users/Chris Walker/Dropbox/Scripts/Bots/Util')
import imageUtil

imagePath = "Images/"

while(not keyboard.is_pressed('1')):
	imageUtil.clickOnImage(imagePath + "Forge", gray = False)
	imageUtil.clickOnImage(imagePath + "Refill", gray = False)