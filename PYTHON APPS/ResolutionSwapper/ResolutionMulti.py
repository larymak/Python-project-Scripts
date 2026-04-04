import pywintypes
import win32con
import win32api
import time


devmode = pywintypes.DEVMODEType()
valid = 0
while valid == 0:
    heightinp = input('Set resolution: -- ')
    if heightinp in ['720','1080','1440']:
        valid += 1
    else:
        print('Invalid resolution. Please try again')
        time.sleep(2)


if heightinp == '720':
    devmode.PelsWidth = 1280
    devmode.PelsHeight =720
if heightinp == '1080':
    devmode.PelsWidth = 1920
    devmode.PelsHeight =1080
if heightinp == '1440':
    devmode.PelsWidth = 2560
    devmode.PelsHeight = 1440

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)
