# Resolution
This is a small application for switching monitor resolution without having to go into your computer settings. Very useful if you have an older system, and are having trouble running newer/more demanding games.

# Prerequisites
pywintypes
win32con
win32api
time
Pyinstaller (optional, but recommended)

# Usage
This app currently features 720p, 1080p and 1440p resolutions. If you wish to add more, add them in the same format as the other resolutions. The number is a string, so you could choose to set the input to letters if that is your preference.

When run, the app will create a popup terminal for you to enter the resolution you want. It will first check if what you input is valid, then set your monitor's resolution based on the preset dimensions.

# Export to exe 
 For ease of use, I'd recommend exporting this to an exe using pyinstaller.
 Instructions for this can be found here -
 ```https://pyinstaller.org/en/stable/usage.html```
From there, create a shortcut to have it on your taskbar. To set the image, you can use any image you choose, but it will need to be in a .ico format. You can find converters to make these from other formats online.
That done, simply click on the icon, then enter your resolution in the terminal popup (only the width). 
