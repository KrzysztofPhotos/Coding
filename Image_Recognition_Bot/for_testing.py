
import pyautogui
import time
for i in range(6):
    x1, y1 = pyautogui.position()

    print(str(x1) + " " + str(y1))
    time.sleep(1)

