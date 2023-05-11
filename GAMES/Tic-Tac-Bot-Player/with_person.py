from packages import config
from packages import common_module


def script_with_person():
    """Main block of code which runs when bot-mode gameplay is selected"""

    # Default matrix
    config.the_matrix = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    # Default empty_cells
    config.empty_cells = 9

    # Printing the game box
    common_module.printer(config.the_matrix)

    # Setting the players for the game to proceed by taking turns
    player_1 = 'X'
    player_2 = 'O'
    current_player = player_1
    possibilities = ['X', 'O']
    while config.empty_cells:
        print("Player 1's turn: ") if current_player == 'X' else print("Player 2's turn: ")

        # Making sure player enters correct co-ordinates
        is_success = common_module.board_modifier(config.the_matrix, current_player)
        while is_success == -1:
            print("Try another co-ordinates: ")
            is_success = common_module.board_modifier(config.the_matrix, current_player)

        # Switching the player turn
        current_player = player_1 if current_player == player_2 else player_2

        # Checking if there is any win condition for the current board state after the player's move
        judgement = common_module.the_judge()

        if judgement in possibilities:
            break
        elif config.empty_cells == 0:
            break

    if judgement is None:
        print(f'The game is a draw!')
    else:
        print('Player 1 wins!\n') if judgement == 'X' else print('Player 2 wins!\n')
