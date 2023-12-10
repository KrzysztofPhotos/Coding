import pyautogui
import time

def rysuj_kwadrat():
    # Poczekaj 5 sekund, abyś miał czas otworzyć Paint
    time.sleep(5)

    # Pobierz rozmiar ekranu
    width, height = pyautogui.size()

    # Przesuń myszkę do lewego górnego rogu
    pyautogui.moveTo(0, 0, duration=0.5)

    # Kliknij lewy przycisk myszy
    pyautogui.mouseDown()

    # Rysuj kwadrat
    pyautogui.moveTo(500, 500, duration=0.5)
    pyautogui.dragRel(200, 0, duration=0.2)
    pyautogui.dragRel(0, 200, duration=0.2)
    pyautogui.dragRel(-200, 0, duration=0.2)
    pyautogui.dragRel(0, -200, duration=0.2)

    # Puść lewy przycisk myszy
    pyautogui.mouseUp()

    print("Kwadrat narysowany!")

# Wywołaj funkcję rysującą kwadrat
rysuj_kwadrat()
