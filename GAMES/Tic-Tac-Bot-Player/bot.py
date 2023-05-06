from packages import module_for_bot
from packages import common_module
from packages import config


def script_with_bot():
    """Main block of code which runs when bot-mode gameplay is selected"""

    # Default matrix
    config.the_matrix = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    # Default empty_cells
    config.empty_cells = 9

    # Printing the game box
    common_module.printer(config.the_matrix)

    while config.empty_cells:

        # To check if the user has entered valid co-ordinates of matrix
        is_success = common_module.board_modifier(config.the_matrix)
        while is_success == -1:
            print("Try another co-ordinates: ")
            is_success = common_module.board_modifier(config.the_matrix)

        common_module.printer(config.the_matrix)

        # 'state' will be 'None' if the game is not finished yet
        state = module_for_bot.bot_turn(config.the_matrix)

        # Exiting the 'while' loop if a valid end-game state has been achieved
        if state is not None:
            break

    if state == 1:
        print('The bot has won the game...\n')
    elif state == -1:
        print('The player has won the game!\n')
    else:
        print('The game is a draw!\n')