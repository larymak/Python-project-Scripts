import pyautogui
import time

text = open('text', 'r')
time.sleep(5)

for word in text:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(5)