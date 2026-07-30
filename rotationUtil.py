import math
import time

import keyboard
import pyautogui


def cast(name, region, hotkey, path='', forceCast=False, confidence=0.9):
    while True:
        try:
            file = path + name + '.png'
            cords = pyautogui.locateOnScreen(file, region=region, confidence=confidence, grayscale=True)
            x = cords[0] + (cords[2] / 2) - 2
            y = cords[1] + 2
            while pyautogui.pixel(int(x), int(y)) != (0, 0, 0):
                keyboard.send(hotkey)
                time.sleep(.1)
            return True
        except pyautogui.ImageNotFoundException:
            if not forceCast:
                return False


def autoAttack(finishChain=False):
    if finishChain:
        for i in range(0, 2):
            keyboard.send('1')
            time.sleep(.55)


def rgb_distance(rgb1, rgb2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)))


def is_closer(rgb1, rgb2, rgb3):
    distance_rgb1_rgb2 = rgb_distance(rgb1, rgb2)
    distance_rgb1_rgb3 = rgb_distance(rgb1, rgb3)

    return distance_rgb1_rgb2 < distance_rgb1_rgb3


def in_location(name, region):
    try:
        file = name + '.png'
        pyautogui.locateCenterOnScreen(file, region=region, confidence=0.9, grayscale=True)
        return True
    except pyautogui.ImageNotFoundException:
        return False
