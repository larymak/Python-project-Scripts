import numpy as np


grid = np.full((3,3), '-')
cells = {'0': (0,0), '1': (0,1), '2': (0,2),
         '3': (1,0), '4': (1,1), '5': (1,2),
         '6': (2,0), '7': (2,1), '8': (2,2)}

diagonal_1 = [0,1,2], [0,1,2]  # main diagonal
diagonal_2 = [0,1,2], [2,1,0]  # reverse diagonal
ver_hor_lines = {'v1': grid[:,0], 'v2': grid[:,1], 'v3': grid[:,2],  # verticals
                 'h1': grid[0,:], 'h2': grid[1,:], 'h3': grid[2,:]}  # horizontals

player = ''
turn = 1
free_spots = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
spot = ''

while True:
    # printing the grid
    for el in grid:
        print('  '.join(el.astype(str)))

    # check if player won
    if np.all(grid[diagonal_1] == player) or np.all(grid[diagonal_2] == player):
        print(f"player {player.upper()}, you won !")
        quit()
    for line in ver_hor_lines:
        if np.all(ver_hor_lines[line] == player):
            print(f"player {player.upper()}, you won !")
            quit()
    print('available positions: {}'.format(' '.join(free_spots)))

    # check if game ended as a tie
    if not free_spots:
        print('END GAME: TIE')
        break

    # update the player
    if turn % 2 == 0:
        player = 'o'
    else:
        player = 'x'

    # ask the input
    spot = input('player {}, enter a position: '.format(player.upper()))
    # entering 'out' will end the game at anytime
    if spot == 'out':
        quit()
    # check if input is valid
    if spot in free_spots:
        # update the grid
        position = cells[spot]
        grid[position] = player
        free_spots.remove(spot)
        turn += 1
    else:
        print('not valid. Enter again.')

    print()