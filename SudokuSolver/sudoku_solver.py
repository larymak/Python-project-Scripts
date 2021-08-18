import numpy as np
import random
from move import Move
from sudoku import Sudoku

LEGIT_DIGITS = list(range(1,10))

def solve_sudoku(sudoku: Sudoku) -> Sudoku:

    '''
        Solve a given legal sudoku by appliying a
        backtracking strategy.
    '''

    if np.count_nonzero(sudoku.grid) == 0:
        return sudoku
        
    # Test a move for the first nakedcell encountered
    naked_cells_indexes = np.where(sudoku.grid == 0)
    first_naked_cell = (naked_cells_indexes[0][0], naked_cells_indexes[1][0])
    #digits_in_row = sudoku.grid[first_naked_cell[0], :]
    #digits_in_column = sudoku.grid[:, first_naked_cell[1]]
    #digits_in_region = sudoku.get_region_from_move(Move(0, first_naked_cell[0], first_naked_cell[1]))

    move = Move(0, first_naked_cell[0], first_naked_cell[1])

    for digit in LEGIT_DIGITS:
        move.number = digit
        sudoku.put_number(move)
        if sudoku.check_legal_state(move):
            print("Legal move")
            print(sudoku.grid)
            solve_sudoku(sudoku)
            move.number = 0
            sudoku.put_number(move)