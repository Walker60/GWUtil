import os
import sys
import time

import keyboard
import pyautogui

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import imageUtil

imagePath = "Images/"
excluded = ("Shard of Glory", "Glob of Ectoplasm", "Memories of Battle", "Tiny Fang", "Tiny Scale")
rowOffset = 44
rowRegion = (380, 50)
y = 0
tpRegion = (0, 0, 0, 0)

WAIT_TIMEOUT = 15
MAX_ROW_SKIPS = 20
MAX_CONSECUTIVE_FAILURES = 3


class TooManySkipsError(RuntimeError):
    pass


def log(message):
    print(f"[TpSellAll] {message}")


def openTp():
    global tpRegion
    log("Opening trading post...")
    keyboard.send('o')
    center = imageUtil.waitForImageCenter(imagePath + "TpSymbol", con=.6, poll=.1, timeout=WAIT_TIMEOUT)
    pyautogui.moveTo(center[0], center[1])
    pyautogui.click(button='left')
    tpRegion = [int(center[0]), int(center[1] - 166), 1000, 716]
    log("Trading post opened.")


def openSell():
    log("Switching to Sell tab...")
    imageUtil.clickOnImage(imagePath + "SellSymbol", con=.99)
    log("Sell tab open.")


def rowIsExcluded(x, y):
    region = (x - rowRegion[0], y - rowRegion[1], rowRegion[0], rowRegion[1] * 2)
    return any(imageUtil.findImageCenter(imagePath + img, region, con=.9) for img in excluded)


def skipExcludedRows(x, y):
    skips = 0
    while rowIsExcluded(x, y):
        if skips >= MAX_ROW_SKIPS:
            raise TooManySkipsError(f"Skipped {skips} consecutive excluded/unsellable rows without finding a sellable item")
        y = y + rowOffset
        skips += 1
    if skips:
        log(f"Skipped {skips} excluded/unsellable row(s).")
    return y


def sellUndercut():
    global y
    global tpRegion
    noBuy = None

    log("Looking for next item row...")
    center = imageUtil.waitForImageCenter(imagePath + "FirstRow", region=tpRegion, timeout=WAIT_TIMEOUT)
    x = center[0]
    if y == 0:
        y = center[1]

    y = skipExcludedRows(x, y)

    pyautogui.moveTo(x, y)
    pyautogui.click(button='left')
    pyautogui.moveTo(10, 10)
    log(f"Selected item row (y={int(y)}).")

    start = time.time()
    while (region := imageUtil.findImageCords(imagePath + "SellCheckBox", region=tpRegion)) is None:
        if time.time() - start >= WAIT_TIMEOUT:
            raise TimeoutError("Timed out waiting for SellCheckBox")
        time.sleep(1)
        if (noBuy := imageUtil.findImageCenter(imagePath + "NoBuy", region=tpRegion)) is not None:
            break

    if noBuy is None:
        imageUtil.clickOnImage(imagePath + "CheckBox", region)
        log("Matched current lowest sell listing.")
    else:
        log("No active buy orders for this item - listing without a price match.")

    region = imageUtil.waitForImageCords(imagePath + "Copper", region=tpRegion, gray=True, timeout=WAIT_TIMEOUT)

    imageUtil.clickOnImage(imagePath + "DownArrow", region, False)
    time.sleep(.25)
    log("Undercut price by 1 copper.")
    if imageUtil.findImageCenter(imagePath + "MinPriceWarning", region=tpRegion, con=.9) is None:
        if imageUtil.findImageCenter(imagePath + "SellingMax", region=tpRegion, con=.9) is None:
            log("Setting quantity to max.")
            sellCenter = imageUtil.waitForImageCenter(imagePath + "SellNumBar", region=tpRegion, con=.9, timeout=WAIT_TIMEOUT)
            pyautogui.moveTo(sellCenter)
            pyautogui.drag(500, 0, 1, button='left')

        if (listCords := imageUtil.findImageCenter(imagePath + "ListItem", region=tpRegion)) is None:
            log("No pending listing - selling instantly.")
            imageUtil.clickOnImage(imagePath + "SellInstant", region=tpRegion)
        else:
            if pyautogui.pixelMatchesColor(int(listCords[0] + 50), int(listCords[1]), (101, 98, 90), tolerance=10):
                log("Listing button disabled - cancelling and skipping this row.")
                imageUtil.clickOnImage(imagePath + "Cancel", region=tpRegion)
                y = y + (rowOffset)
                return
            log("Confirming listing at undercut price.")
            imageUtil.clickOnImage(imagePath + "ListItem", region=tpRegion)

        pyautogui.moveTo(10, 10)
        imageUtil.waitForImageCenter(imagePath + "Cancel", region=tpRegion, poll=.1, timeout=WAIT_TIMEOUT)
        time.sleep(.25)
        oakyCenter = imageUtil.findImageCenter(imagePath + "Okay", region=tpRegion, con=.95) is not None
        while oakyCenter:
            log("Confirming low-price warning popup...")
            imageUtil.clickOnImage(imagePath + "Okay")
            region = imageUtil.waitForImageCords(imagePath + "Copper", region=tpRegion, gray=True, timeout=WAIT_TIMEOUT)
            if imageUtil.findImageCenter(imagePath + "ListItem", region=tpRegion, con=.8) is None:
                imageUtil.clickOnImage(imagePath + "SellInstant", region=tpRegion)
            else:
                imageUtil.clickOnImage(imagePath + "ListItem", region=tpRegion)
            pyautogui.moveTo(10, 10)
            imageUtil.waitForImageCenter(imagePath + "Cancel", region=tpRegion, poll=.1, timeout=WAIT_TIMEOUT)
            oakyCenter = imageUtil.findImageCenter(imagePath + "Okay", region=tpRegion, con=.95)
        imageUtil.clickOnImage(imagePath + "Close", region=tpRegion)
        log("Item processed, sell panel closed.")
    else:
        log("Price floor reached - cancelling and skipping this row.")
        imageUtil.clickOnImage(imagePath + "Cancel", region=tpRegion)
        y = y + (rowOffset)


time.sleep(1)
openTp()
openSell()

log("Starting sell-all loop. Press '=' to stop.")
failures = 0
while not keyboard.is_pressed('=') and failures < MAX_CONSECUTIVE_FAILURES:
    try:
        sellUndercut()
        failures = 0
    except (TimeoutError, TooManySkipsError) as e:
        log(f"sellUndercut failed, recovering: {e}")
        pyautogui.press('escape')
        time.sleep(.5)
        failures += 1
    pyautogui.moveTo(100, 100)

if failures >= MAX_CONSECUTIVE_FAILURES:
    log(f"Stopping: {MAX_CONSECUTIVE_FAILURES} consecutive failures.")
else:
    log("Stopped by user ('=' pressed).")
