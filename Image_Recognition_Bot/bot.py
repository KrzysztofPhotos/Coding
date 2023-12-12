from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
# Tile 1 (x,y): (900, 500)
# Tile 2 (x,y): (779, 500)
# Tile 3 (x,y): (669, 500)
# Tile 4 (x,y): (531, 500)

print('Bot is working')
    
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(900,500)[0] == 0:
        click(900,500)
        print('4 Tile clicked')
    if pyautogui.pixel(779, 500)[0] == 0:
        click(779, 500)
        print('3 Tile clicked')
    if pyautogui.pixel(669, 500)[0] == 0:
        click(669, 500)
        print('2 Tile clicked')
    if pyautogui.pixel(531, 500)[0] == 0:
        click(531, 500)
        print('1 Tile clicked')
    
print('Bot has been stopped')
 