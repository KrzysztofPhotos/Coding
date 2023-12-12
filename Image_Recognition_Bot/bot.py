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
    
# https://www.gamesgames.com/game/magic-piano-tiles
    
# Tile 1 (x,y): (630, 500)
# Tile 2 (x,y): (481, 500)
# Tile 3 (x,y): (327, 500)
# Tile 4 (x,y): (189, 500)


print('Bot is working')





while keyboard.is_pressed('q') == False:
    
    # Provide coordinates of tiles
    counter = [0, 0, 0, 0]
    while counter is not [1, 1, 1, 1]:
        if keyboard.is_pressed('1') and counter[0] == 0:
            print('First tile has been saved')
            counter[0] = 1
            # add here a sound from AI (tile one was saved)
        if keyboard.is_pressed('2') and counter[1] == 0:
            print('Second tile has been saved')
            counter[1] = 1
            # add here a sound from AI (tile one was saved)
        if keyboard.is_pressed('3') and counter[2] == 0:
            print('Third tile has been saved')
            counter[2] = 1
            # add here a sound from AI (tile one was saved)
        if keyboard.is_pressed('4') and counter[3] == 0:
            print('Fourth tile has been saved')
            counter[3] = 1
            # add here a sound from AI (tile one was saved)
    
    print('ALL KEYS HAVE BEEN SAVED')
        
            
            
    
    if pyautogui.pixel(630,500)[0] == 0:
        click(630,500)
        print('4 Tile clicked')
    if pyautogui.pixel(481, 500)[0] == 0:
        click(481, 500)
        print('3 Tile clicked')
    if pyautogui.pixel(327, 500)[0] == 0:
        click(327, 500)
        print('2 Tile clicked')
    if pyautogui.pixel(189, 500)[0] == 0:
        click(189, 500)
        print('1 Tile clicked')
    
print('Bot has been stopped')
 