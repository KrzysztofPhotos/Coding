# PIANO TITLES BOT

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
    
# GAME FOR TESTING IN BROWSER
# https://www.gamesgames.com/game/magic-piano-tiles

print('Bot is working')

counter = [0, 0, 0, 0]

while keyboard.is_pressed('q') == False:
    
    # Provide coordinates of tiles
    
    while True:
        if keyboard.is_pressed('1') and counter[0] == 0:
            print('First tile has been saved')
            counter[0] = 1
            
            # Save mouse position
            x1, y1 = pyautogui.position()
            #TODO add here a sound from AI (tile one was saved)
        if keyboard.is_pressed('2') and counter[1] == 0:
            print('Second tile has been saved')
            counter[1] = 1
            
            # Save mouse position
            x2, y2 = pyautogui.position()
            #TODO add here a sound from AI (tile one was saved)
            
        if keyboard.is_pressed('3') and counter[2] == 0:
            print('Third tile has been saved')
            counter[2] = 1
            
            # Save mouse position
            x3, y3 = pyautogui.position()
            #TODO add here a sound from AI (tile one was saved)
            
        if keyboard.is_pressed('4') and counter[3] == 0:
            print('Fourth tile has been saved')
            counter[3] = 1
            
            # Save mouse position
            x4, y4 = pyautogui.position()
            #TODO add here a sound from AI (tile one was saved)
            
        if counter == [1, 1, 1, 1]:
            #print('ALL KEYS HAVE BEEN SAVED')
            break
        
    
    #TODO add AI voice here
        
     
    if pyautogui.pixel(x1, y1)[0] == 0:
        click(x1, y1)
        print('1 Tile clicked')
    if pyautogui.pixel(x2, y1)[0] == 0:
        click(x2, y1)
        print('2 Tile clicked')
    if pyautogui.pixel(x3, y1)[0] == 0:
        click(x3, y1)
        print('3 Tile clicked')
    if pyautogui.pixel(x4, y1)[0] == 0:
        click(x4, y1)
        print('4 Tile clicked')
    
print('Bot has been stopped')

