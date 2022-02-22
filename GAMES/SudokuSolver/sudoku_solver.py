import numpy as np
from move import Move
from sudoku import Sudoku

LEGIT_DIGITS = list(range(1, 10))
SUDOKU_DIMENSION = 9


def find_naked_cell(sudoku: Sudoku) -> tuple:

    '''
        Finds the first 0 labeled cell in the sudoku
    '''

    naked_cells_indexes = np.where(sudoku.grid == 0)
    if naked_cells_indexes[0].size > 0:
        if naked_cells_indexes[0][0].size > 0 and naked_cells_indexes[1][0].size > 0:
            return (naked_cells_indexes[0][0], naked_cells_indexes[1][0])

    return naked_cells_indexes

def solve_sudoku(sudoku: Sudoku,) -> bool:
    '''
        Solve a given legal sudoku by appliying a
        backtracking strategy.
    '''
    naked_cell = find_naked_cell(sudoku)

    if(not naked_cell[0].size > 0):
        print("The solution to the proposed Sudoku is: \n", sudoku.grid)
        return True

    move = Move(0, naked_cell[0], naked_cell[1])

    for digit in LEGIT_DIGITS:
        move.number = digit
        if sudoku.is_legal_state(move):
            sudoku.put_number(move)
            print(sudoku.grid)
            if(solve_sudoku(sudoku)):
                return True

        move.number = 0
        sudoku.put_number(move)
        
    return False
