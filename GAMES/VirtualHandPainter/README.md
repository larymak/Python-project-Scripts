# HandPainter
![Virtual_Hand_Painter](https://user-images.githubusercontent.com/59937191/170613993-6a08904e-e1cc-4032-9f52-6b9b5e4e662f.png)

## Installation
There are a few things to install when using this program!
````bash 
pip install opencv-python
pip install pygame
pip install pyautogui
pip install mediapipe
````

## Imports 
````Python
import cv2 as cv
import mediapipe as mp
import pygame
import math
import pyautogui
import os
````

## What is this?
Use your thumb and index finger to draw onto your computer screen. By bringing your index and thumb finger together, it will allow you to draw onto a whiteboard, displayed on screen. Users can take screen shots of their work by moving their index finger together beside their middle finger tip. Within a certain distance screen shots will be taken aswell as drawing. 


![visual](https://user-images.githubusercontent.com/59937191/170798233-c10752d2-6df0-4349-a9b5-fd96902c3489.png)


## Inspiration
This project was made integrating computer vision and pygame!
I first got this idea, after I worked on a similar project called "Catch me if you can". The goal of catch me if you can was to mov a 2d square around your screen, by controlling it through your hand. This was a very interesting project I developed with my cousin, that eventually lead me to take on this new one. After learning open CV, I decided to create an application, where users could draw onto their computer screen, if they didn't have a mouse. This would finally allow users to have precise drawings all without having to spend money on a stylus or mouse!

## What I learned
Through this project I learned more details about Pygame, and open CV. Aswell as enhancing my experience with Python, I was able to learn how to use generators effectively. This project taught me many applications of mathematical equations learned in school, such as the distance formula. Lastly, I was able to learn how to create screen shots through Python, through the windows machine. This project allowed me to become more comfortable using the "OS" module in Python, as I was able to experiment through grabbing the users directory, and allowing images to be saved on that pathway, if they want to take a screen shot. 
