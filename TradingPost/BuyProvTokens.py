from pyautogui import *
import pyautogui
import time
import keyboard
import sys
sys.path.insert(1, 'C:/Users/12069/Dropbox/Scripts/Bots/Util')
sys.path.insert(1, 'C:/Users/Chris Walker/Dropbox/Scripts/Bots/Util')
import imageUtil
import pyperclip

imagePath = "Images/"
excluded = ("Shard of Glory", "Glob of Ectoplasm")
rowOffset = 44
rowRegion = (380, 50)
row = 0


def openTp():
	keyboard.send('o')
	imageUtil.clickOnImage(imagePath + "TpSymbol", con = .8)

def openBuy():
	imageUtil.clickOnImage(imagePath + "BuySymbol", con = .99)

def buy(center, name):
	while imageUtil.findImageCenter(imagePath + "Gear") == None:
		time.sleep(1)
	pyautogui.moveTo(center)
	pyautogui.click()
	pyautogui.click()
	pyautogui.click()
	time.sleep(.25)
	pyautogui.write(name)
	time.sleep(.25)
	imageUtil.clickOnImage(imagePath + "BuyFirstRow")
	imageUtil.clickOnImage(imagePath + "BuyInstant")
	imageUtil.clickOnImage(imagePath + "Close")


time.sleep(1)
openTp()
openBuy()
while (center := imageUtil.findImageCenter(imagePath + "Search")) == None:
	time.sleep(1)

buy(center, "carrion krait battleaxe")
buy(center, "Rampager's Krait Battleaxe")
buy(center, "Carrion Krait Slayer")
buy(center, "Cleric's Krait Warhammer")
buy(center, "Knight's Krait Warhammer")
buy(center, "Valkyrie Krait Morning Star")
buy(center, "Berserker's Krait Shell")
buy(center, "Valkyrie Krait Shell")
buy(center, "Assassin's Krait Machete")

keyboard.send('ENTER')
pyautogui.write("/s" )
keyboard.send('SPACE')
pyautogui.write("[&BAwEAAA=] [&BKgDAAA=] [&BN4HAAA=] [&BNYHAAA=] [&BMwHAAA=]")
keyboard.send('ENTER')