from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import sys
import multiprocessing

def findImageCenter(name, region = None, gray = True, con = .9):
	try:
		file = name + '.png'
		if region != None: 
			return pyautogui.locateCenterOnScreen(file, region = region, confidence = con, grayscale = gray)
		else:
			return pyautogui.locateCenterOnScreen(file, confidence = con, grayscale = gray)
	except pyautogui.ImageNotFoundException:
		return None

def findImageCords(name, region = None, gray = None, con = .9):
	try:
		file = name + '.png'
		if region != None: 
			return pyautogui.locateOnScreen(file, region = region, confidence = con, grayscale = gray)
		else:
			return pyautogui.locateOnScreen(file, confidence = con, grayscale = gray)
	except pyautogui.ImageNotFoundException:
		return None


def clickOnImage(name, region = None, gray = None, con = .9):
	while (center := findImageCenter(name, region, gray = gray, con = con)) == None:
		time.sleep(1)
	pyautogui.moveTo(center[0], center[1])
	pyautogui.click(button='left')