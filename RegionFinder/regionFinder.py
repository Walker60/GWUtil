import pyautogui
import time

time.sleep(1)
screen_size = pyautogui.size()
screen_center = (screen_size[0]/2, screen_size[1]/2)
region = (int(screen_center[0] - 167), int(screen_center[1] - 100), 300, 500)
print(screen_size)
im1 = pyautogui.screenshot(region=(1394,1301,280,50))
im1.save("savedimage.png")
