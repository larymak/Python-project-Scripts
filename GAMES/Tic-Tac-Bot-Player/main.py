import with_person
import bot


def choice_checker(choice):
    """This checks if the user has entered a valid choice"""

    global choices
    while choice not in choices:
        print("Enter a valid choice!")
        print("""Choose the mode of game.
        '1' to play with a friend,
        '2' to play with a bot (P.S: You might not win)
        '3' to quit this\n""")
        choice = input()
    return choice


# Giving the user a choice to select the mode of the game they want to play
choices = ['1', '2', '3']
print("""Choose the mode of game.
'1' to play with a friend,
'2' to play with a bot (P.S: You might not win)
'3' to quit this\n""")
choice = input()
choice = choice_checker(choice)

while True:
    if choice == choices[0]:
        with_person.script_with_person()
    elif choice == choices[1]:
        bot.script_with_bot()
    else:
        break

    print("Would you like to try again..?")
    print("""Choose the mode of game.
    '1' to play with a friend,
    '2' to play with a bot (P.S: You might not win)
    '3' to quit this\n""")
    choice = input()
    choice = choice_checker(choice)
