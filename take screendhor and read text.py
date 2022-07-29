#take screendhor 
import time
from cgi import test
import pyautogui


time.sleep(10)


myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\Tejas\Desktop\file name.png')


