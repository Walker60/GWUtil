from pyautogui import *
import pyautogui
import time
import keyboard
import sys
sys.path.insert(1, 'C:/Users/12069/Dropbox/Scripts/Bots/Util')
sys.path.insert(1, 'C:/Users/Chris Walker/Dropbox/Scripts/Bots/Util')
import imageUtil

imagePath = "Images/"
excluded = ("Shard of Glory", "Glob of Ectoplasm", "Memories of Battle", "Tiny Fang", "Tiny Scale")
rowOffset = 44
rowRegion = (380, 50)
cantSell = 0
y = 0
tpRegion = (0,0,0,0)

def openTp():
	global tpRegion
	keyboard.send('o')
	while (center := imageUtil.findImageCenter(imagePath + "TpSymbol", con = .6)) == None:
		pass
	pyautogui.moveTo(center[0], center[1])
	pyautogui.click(button='left')
	tpRegion = [int(center[0]), int(center[1] - 166), 1000, 716]

def openSell():
	imageUtil.clickOnImage(imagePath + "SellSymbol", con = .99)


def sellUndercut():
	global y 
	global tpRegion
	noBuy = None

	while (center := imageUtil.findImageCenter(imagePath + "FirstRow", region = tpRegion)) == None:
		time.sleep(1)
	x = center[0]
	if y == 0:
		y = center[1]

	for img in excluded:
		if (imageUtil.findImageCenter(imagePath + img, (x-rowRegion[0], y-rowRegion[1], rowRegion[0], rowRegion[1]*2), con = .9)):
			y = y + (rowOffset)
	pyautogui.moveTo(x, y)
	pyautogui.click(button='left')
	pyautogui.moveTo(10,10)

	while ((region := imageUtil.findImageCords(imagePath + "SellCheckBox",region = tpRegion)) == None):
		time.sleep(1)
		if (noBuy := imageUtil.findImageCenter(imagePath + "NoBuy", region = tpRegion)) != None:
			break

	if(noBuy == None):
		imageUtil.clickOnImage(imagePath + "CheckBox", region)

	while (region := imageUtil.findImageCords(imagePath + "Copper", region = tpRegion, gray = True)) == None:
		time.sleep(1)

	imageUtil.clickOnImage(imagePath + "DownArrow", region, False)
	time.sleep(.25)
	if (imageUtil.findImageCenter(imagePath + "MinPriceWarning", region = tpRegion, con = .9) == None):
		if (imageUtil.findImageCenter(imagePath + "SellingMax", region = tpRegion, con = .9) == None):
			sellCenter = imageUtil.findImageCenter(imagePath + "SellNumBar", region = tpRegion, con = .9)
			pyautogui.moveTo(sellCenter)
			pyautogui.drag(500, 0, 1, button='left')

		if (imageUtil.findImageCenter(imagePath + "ListItem", region = tpRegion) == None):
			imageUtil.clickOnImage(imagePath + "SellInstant", region = tpRegion)
		else:
			listCords = imageUtil.findImageCenter(imagePath + "ListItem", region = tpRegion)
			if (pyautogui.pixelMatchesColor(int(listCords[0] + 50), int(listCords[1]), (101, 98, 90), tolerance=10)):
				imageUtil.clickOnImage(imagePath + "Cancel", region = tpRegion)
				y = y + (rowOffset)
				return
			imageUtil.clickOnImage(imagePath + "ListItem", region = tpRegion)

		pyautogui.moveTo(10,10)
		while (center := imageUtil.findImageCenter(imagePath + "cancel", region = tpRegion)) == None:
			pass
		time.sleep(.25)
		if (oakyCenter := imageUtil.findImageCenter(imagePath + "Okay", region = tpRegion, con = .95) != None):
			while(oakyCenter):
				imageUtil.clickOnImage(imagePath + "Okay")
				while (region := imageUtil.findImageCords(imagePath + "Copper", region = tpRegion, gray = True)) == None:
					time.sleep(1)
				if (imageUtil.findImageCenter(imagePath + "ListItem", region = tpRegion, con = .8) == None):
					imageUtil.clickOnImage(imagePath + "SellInstant", region = tpRegion)
				else:
					imageUtil.clickOnImage(imagePath + "ListItem", region = tpRegion)
				pyautogui.moveTo(10,10)
				while (imageUtil.findImageCenter(imagePath + "cancel", region = tpRegion)) == None:
					pass
				oakyCenter = imageUtil.findImageCenter(imagePath + "Okay", region = tpRegion, con = .95)
		imageUtil.clickOnImage(imagePath + "Close", region = tpRegion)
	else:
		imageUtil.clickOnImage(imagePath + "Cancel", region = tpRegion)
		y = y + (rowOffset)
time.sleep(1)
openTp()
openSell()
while(not keyboard.is_pressed('=')):
	sellUndercut()
	pyautogui.moveTo(100,100)
