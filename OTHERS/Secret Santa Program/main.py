import os
import numpy as np

command = input("Input command (A Name, Remove, Exit): ")
groupList = []


def printList(list):
  for name in list:
    print(name[0])


def printTrueList(list):
  print("\nDEBUGGING ONLY:\n")
  for name in list:
    print(name)


def randomise(groupList):
  lengthList = list(range(1, len(groupList) + 1))
  groupNumberList = []
  nameList = []
  trueList = []
  Toggle = True

  for i in groupList:
    groupNumberList.append(i[1])
    nameList.append(i[0])

  while Toggle:
    np.random.shuffle(lengthList)
    for i in range(len(groupNumberList)):
      if groupNumberList[i] == lengthList[i]:
        Toggle = True
        break
      else:
        Toggle = False

  for i in range(len(groupList)):
    trueList.append((lengthList[i], groupNumberList[i]))

  for i in trueList:
    print(i[0], "-->", nameList[i[1] - 1])


def groupMaker(command):
  while True:
    if command.upper() == "EXIT":
      os.system('clear')
      print("All names:\n")
      printList(groupList)

      print("\n How the Assignment Works:")
      print(
        "The person holding the number is assigned \nthe person to the right of the arrow \n"
      )
      randomise(groupList)
      break

    elif command.upper() == "REMOVE":
      print("")
      for i, c in enumerate(groupList):
        print(f'{i+1} {c[0]}')
      choice = input("\nWho do you want to remove? (Insert Index Number): ")
      groupList.pop(int(choice) - 1)
      os.system('clear')

    else:
      number = input("\nWhat is your number?: ")
      while True:
        choice = input("Is your number correct? (Yes, No): ")
        if choice.upper() == "YES":
          break
        elif choice.upper() == "NO":
          number = input("\nWhat is your number?: ")
        else:
          pass
      groupList.append((command.lower().capitalize(), int(number)))
      os.system('clear')

    print("Current people in the group")
    printList(groupList)
    command = input("Input command (a name, REMOVE, EXIT): ")


groupMaker(command)
