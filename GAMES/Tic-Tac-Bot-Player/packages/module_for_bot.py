from packages import common_module, config
from time import sleep


def modify_board_bot(letter, position, the_matrix):
    """Simultaneously updates the matrix and checks for a win or draw condition.
    This function is only specific to the bot-mode of the game
    """

    the_matrix[position[0]][position[1]] = letter

    check_for_win = common_module.the_judge()
    if check_for_win == 'X':
        print('The player has won the game!\n')
        return -1
    elif check_for_win == 'O':
        # print('The bot has won the game...\n')
        return 1
    elif common_module.check_for_draw():
        print('The game is a draw!\n')
        return 0
    else:
        return None
    

def the_algorithm(the_matrix, is_bot):
    """This function is the brain of the bot"""

    if common_module.finder('O'):
        return 1
    elif common_module.finder('X'):
        return -1
    elif common_module.check_for_draw():
        return 0

    if is_bot:
        best_score = -1000
        for row in range(3):
            for column in range(3):
                if the_matrix[row][column] == '_':
                    the_matrix[row][column] = 'O'
                    score = the_algorithm(the_matrix, False)
                    the_matrix[row][column] = '_'

                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = 1000
        for row in range(3):
            for column in range(3):
                if the_matrix[row][column] == '_':
                    the_matrix[row][column] = 'X'
                    score = the_algorithm(the_matrix, True)
                    the_matrix[row][column] = '_'
                    if score < best_score:
                        best_score = score
        return best_score


def bot_turn(the_matrix):
    """Decides which move the bot has to do."""

    print('The bot\'s turn: ')
    sleep(0.3)
    print('The bot is thinking..')
    sleep(0.8)
    best_score = -1000
    best_move = [-1, -1]

    for row in range(3):
        for column in range(3):
            if the_matrix[row][column] == '_':
                the_matrix[row][column] = 'O'
                current_score = the_algorithm(the_matrix, False)
                the_matrix[row][column] = '_'
                if current_score > best_score:
                    best_score = current_score
                    best_move = row, column
    config.empty_cells -= 1
    value = modify_board_bot('O', best_move, the_matrix=the_matrix)
    common_module.printer(the_matrix)
    return value
