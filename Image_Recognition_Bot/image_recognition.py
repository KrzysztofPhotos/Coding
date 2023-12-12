from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen() != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I'm unable to see it")
        time.sleep(0.5)
        
        
