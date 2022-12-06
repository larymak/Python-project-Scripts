# coding=utf-8
import random
# random module is a built-in module to generate pseudo-random variables

def display_gameplay():
    """
    Displays the gameplay
    : return: None
    """
    print('\nWelcome to Number Guessing Game!')
    print('In this game you\'ve just 7 trials to guess a number between the range of 1-10')
    print('Note: enter \'exit\' to end game')

def startGame():
    """
    Gets user response to start or end the game
    : return: str
    """
    # call the function to display gameplay
    displayGameplay = display_gameplay()
    # make a list of the possible inputs
    # to start or end the game
    possible_responses = ['Y','YES','N','NO','EXIT']
    # get user's response
    user_response = input('\nStart game? (yes/no): ').strip().upper()
    while user_response not in possible_responses:
        print('\nInvalid Input!')
        user_response = input('\nStart game? (yes/no): ').strip().upper()
    else: return user_response

def game():
    """
    Controls the game
    : return: None
    """
    # call the function to get user's response
    play_game = startGame()
    # assign the number of trials the user has to a variable
    number_of_trials = 7
    # initialise new_game to true
    new_game = True
    while play_game == 'YES' or play_game == 'Y':
        # make a list that contains all the
        # numbers a user can guess
        accepted_number_picks = [str(i) for i in range(1,11)]
        # get user's number
        user_input = input('\nGuess a number between the range of 1-10: ').strip().upper()
        while user_input not in accepted_number_picks and user_input != 'EXIT' :
            print('Invalid Input!')
            user_input = input('\nGuess a valid number between the range of 1-10: ').strip().upper()
        if user_input == 'EXIT':
            print('Bye Player!')
            break
        else:
            # generate a random number in the range 1-10
            # and assign it to a variable
            # check if new_game, if true generate new computer_number else don't
            if new_game:
                computer_number = random.randint(1,10)
                new_game = False
            user_input = int(user_input)
            if user_input < computer_number:
                number_of_trials -= 1
                print(f'Oops, {user_input} is too low')
                if number_of_trials != 0:
                    print(f'You\'ve {number_of_trials} trial(s) left')
                    play_game = input('\nGuess again? (yes/no): ').strip().upper()
                else:
                    print('\nGame over!, you\'ve 0 trial left..try harder next time 😉')
                    break
            elif user_input > computer_number:
                number_of_trials -= 1
                print(f'Oops, {user_input} is too high')
                if number_of_trials != 0:
                    print(f'You\'ve {number_of_trials} trial(s) left')
                    play_game = input('\nGuess again? (yes/no): ').strip().upper()
                else:
                    print('\nGame over!, you\'ve 0 trial left..try harder next time 😉')
                    break
            elif user_input == computer_number:
                number_of_trials -= 1
                print(f'Congratulations!!..you guessed right, after {7 - number_of_trials} trial(s)')
                play_game = input('\nDo you wish to play again? (yes/no): ').strip().upper()
                # if the user wishes to play again, assign
                # the number of trials the user has to a variable
                number_of_trials = 7
                # start a new game
                new_game = True

game()