from datetime import date
from dateutil.relativedelta import relativedelta
n = input("Enter your name buddy ")
birth_str = input('Enter the date you were born, in format YYYY-MM-DD: ')
try:
    birth = date.fromisoformat(birth_str)
except ValueError:
    print("Don't you know your birthday?")
    exit()

age = relativedelta(date.today(), birth)
print(f'Wohoo {n} is {age.years} years, {age.months} months and {age.days} days old.')