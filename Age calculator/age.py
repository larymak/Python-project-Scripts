from datetime import datetime

name = input("What is your name: ")

Birth_Year = int(input("Enter your birth year: "))

Current_time = datetime.now().year

def age_caluu():
    Age_calculated = (Current_time - Birth_Year)
    print ('Hey {} your age is {}'.format(name, Age_calculated))
age_caluu()
