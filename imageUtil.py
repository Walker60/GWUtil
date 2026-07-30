import time

import pyautogui


def findImageCenter(name, region=None, gray=True, con=.9):
    try:
        file = name + '.png'
        if region is not None:
            return pyautogui.locateCenterOnScreen(file, region=region, confidence=con, grayscale=gray)
        else:
            return pyautogui.locateCenterOnScreen(file, confidence=con, grayscale=gray)
    except pyautogui.ImageNotFoundException:
        return None


def findImageCords(name, region=None, gray=None, con=.9):
    try:
        file = name + '.png'
        if region is not None:
            return pyautogui.locateOnScreen(file, region=region, confidence=con, grayscale=gray)
        else:
            return pyautogui.locateOnScreen(file, confidence=con, grayscale=gray)
    except pyautogui.ImageNotFoundException:
        return None


def waitForImageCenter(name, region=None, gray=True, con=.9, poll=1, timeout=None):
    start = time.time()
    while (result := findImageCenter(name, region, gray, con)) is None:
        if timeout is not None and time.time() - start >= timeout:
            raise TimeoutError(f"Timed out waiting for image '{name}'")
        if poll:
            time.sleep(poll)
    return result


def waitForImageCords(name, region=None, gray=None, con=.9, poll=1, timeout=None):
    start = time.time()
    while (result := findImageCords(name, region, gray, con)) is None:
        if timeout is not None and time.time() - start >= timeout:
            raise TimeoutError(f"Timed out waiting for image '{name}'")
        if poll:
            time.sleep(poll)
    return result


def clickOnImage(name, region=None, gray=None, con=.9):
    center = waitForImageCenter(name, region, gray, con)
    pyautogui.moveTo(center[0], center[1])
    pyautogui.click(button='left')
