import time # importing time module
import pyautogui # importing pyautogui

T = int(input("How many seconds do you want to wait before sending each message?\nEnter 0 for the quickest sending!\n")) # Desired Time before sending each messages
Text = input("Type the message you want to send as text BOMBING! :  \n") # Desired Text
Time = int(input("How many times do you want to send the message?\n")) # How many messages the user want to send

# I'll use while loop here

i = 0

while (i <= Time-1 ): # The loop started
    time.sleep(T) # will wait T times before sending each automated message
    pyautogui.typewrite(Text) # will write the text the user want
    pyautogui.press('enter') # will work as the 'Enter' button
    i+=1 # i will increment as 1 each time
