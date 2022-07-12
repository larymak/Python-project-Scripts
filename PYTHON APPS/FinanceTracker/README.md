# FinanceApp
![Finance_Tracker](https://user-images.githubusercontent.com/59937191/170799233-576fdaf2-6603-4fd1-8966-4b18cb556368.png)


## Installations
````
pip install PyQt5
pip install matplotlib 
pip install db-sqlite3
```` 

## Imports for main.py
````
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import financeDataBase
````

## Imports for financeDataBase.py
````
import sqlite3
from matplotlib import pyplot as plt
````

### Note
financeDataBase is the other python file containing all necessary methods to perform SQL actions 

##  What is this? 
This is a simple finance tracker that allows users to track and mange their expenses on various categories. This app allows users to monitor their finances, add expenses, delete expenses, view their total expesnes, view various graphs on how their money is being spent and more! Some intersting features that were recently added are, users can change the background of their app based on their liking, or they can chose from 3 default gradients. 

![main](https://user-images.githubusercontent.com/59937191/170799097-222e8b83-f73c-4e41-b2bd-a520af125cb4.png)
![main2](https://user-images.githubusercontent.com/59937191/170799105-27d18519-69a4-4abb-ac4c-18d4446b27ce.png)
![settings](https://user-images.githubusercontent.com/59937191/170799166-4a884a29-2587-4d24-a704-1e04c4f9cbb9.png)
![other](https://user-images.githubusercontent.com/59937191/170799111-04ff05df-2af9-4df1-aec7-67b675b66bbe.png)
![piechart](https://user-images.githubusercontent.com/59937191/170799112-7f760048-b9a3-417e-8268-8b46f3cd6f91.png)

## Inspiration 
After taking part in my first hackathon when I was 15, and creatign a pet expense tracker, I decided to take my SQL knowedge and GUI capabilities to the next level. I wanted to create an app that would help my family and other peopel monitor their finances. This is app focuses on the simplicity on just keeping track of how you spend your money. 

## What I learned 
- Pyqt5
- Matplotlib 
- More from SQL
This project allowed me to become more confident in my Object Oriented programming skills, and allowed me to work with new technologies I have previous not worked with before such as a powerful GUI builder "Pyqt5". I was able to learn how to efficiently use Matplot lib to implement graphs and a pie chart. Lastly, I became more familar with SQL commands in python and using better practices to retrieve data. 


## Latest Updates:
### July 9th 2022
- Added some doccumention for code to make it easier to read
- Added ability to tell users when they hit goal or over budget once expense entered

