from os import system
from time import sleep
from packages import config


def printer(the_matrix):
    """Prints the game board"""

    print()
    print('-' * 9)
    for i in range(3):
        print('|', end=' ')
        for j in range(3):
            if the_matrix[i][j] == '_' or the_matrix[i][j] == ' ':
                print("_ ", end='')
            else:
                print(the_matrix[i][j], end=' ')
        print('|')
    print('-' * 9)
    print()


def check_for_draw():
    if config.empty_cells != 0:
        return False
    else:
        return True


def the_judge():
    """This function calls another function and sees if any one player has won"""
    # Checking the game state
    x_found = finder('X')
    o_found = finder('O')

    # If either one of them is found in a row, it wins the game
    if x_found:
        return 'X'
    elif o_found:
        return 'O'
    else:
        return None


def finder(letter):
    """Returns True if the win condition is achieved for a specific letter(player) in the board, else returns False"""

    # Checking by ROWS
    matrix = config.the_matrix
    for i in range(0, 3):
        counter = 0
        for j in range(0, 3):
            if matrix[i][j] == letter:
                counter += 1

        # Checking if the letter is found in a row
        if counter == 3:
            return True

    # Checking by COLUMNS
    for i in range(0, 3):
        counter = 0
        for j in range(0, 3):
            if matrix[j][i] == letter:
                counter += 1

        if counter == 3:
            return True

    # Checking by first diagonal by indices
    counter = 0
    for i in range(0, 3):
        if matrix[i][i] == letter:
            counter += 1

    if counter == 3:
        return True

    # Checking by second diagonal by indices
    counter = 0
    j_index = 2
    for i in range(0, 3):
        if matrix[i][j_index] == letter:
            counter += 1
        j_index -= 1

    if counter == 3:
        return True

    return False
    

def board_modifier(the_matrix, player=None):
    """Modifies the game board as per the player's moves.
    Behaves dynamically to the mode of the game(with person, or with a bot)"""

    sleep(0.5)
    the_coords = input("Player's turn: ").split() if player is None else input().split()
    if len(the_coords) != 2:
        print('Enter two coordinate numbers!')
        return -1
    x, y = the_coords
    try:
        for index in the_coords:
            index = int(index)
    except ValueError:
        print('You should enter numbers!')
        return -1
    else:
        x = int(x)
        y = int(y)
        if x not in range(1, 4) or y not in range(1, 4):
            print('Coordinates should be from 1 to 3!')
            return -1
        else:
            x, y = x-1, y-1
        if the_matrix[x][y] != '_':
            print('This cell is occupied! Choose another one!')
            return -1
        else:
            if player is None:
                from packages import module_for_bot
                module_for_bot.modify_board_bot('X', [x, y], the_matrix=the_matrix)
            else:
                the_matrix[x][y] = player
            # config.turns += 1
            # Clearing the terminal and writing the updated matrix
            system('cls')
            if player is None:
                pass
            else:
                printer(the_matrix)
            config.empty_cells -= 1
            return 2
