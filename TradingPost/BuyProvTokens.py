import os
import sys
import time

import keyboard
import pyautogui

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import imageUtil

imagePath = "Images/"
excluded = ("Shard of Glory", "Glob of Ectoplasm")
rowOffset = 44
rowRegion = (380, 50)
row = 0


def openTp():
    keyboard.send('o')
    imageUtil.clickOnImage(imagePath + "TpSymbol", con=.8)


def openBuy():
    imageUtil.clickOnImage(imagePath + "BuySymbol", con=.99)


def buy(center, name):
    imageUtil.waitForImageCenter(imagePath + "Gear")
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
center = imageUtil.waitForImageCenter(imagePath + "Search")

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
pyautogui.write("/s")
keyboard.send('SPACE')
pyautogui.write("[&BAwEAAA=] [&BKgDAAA=] [&BN4HAAA=] [&BNYHAAA=] [&BMwHAAA=]")
keyboard.send('ENTER')
