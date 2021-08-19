from move import Move
from sudoku import Sudoku

LEGIT_DIGITS = list(range(1, 10))
SUDOKU_DIMENSION = 9

def solve_sudoku(sudoku: Sudoku, row: int, column: int) -> bool:
    '''
        Solve a given legal sudoku by appliying a
        backtracking strategy.
    '''

    # Return True when the last cell is achieved to avoid further backtracking
    
    if (row == SUDOKU_DIMENSION - 1 and column == SUDOKU_DIMENSION - 1):
        print("The solution to the Sudoku proposed is: \n", sudoku.grid)
        return True

    # If we're in the last column, move to the next row

    if column == SUDOKU_DIMENSION:
        row += 1
        column = 0

    if sudoku.grid[row, column] > 0:
        return solve_sudoku(sudoku, row, column + 1)

    move = Move(0, row, column)

    for digit in LEGIT_DIGITS:
        move.number = digit

        if sudoku.is_legal_state(move):
            sudoku.put_number(move)

            if solve_sudoku(sudoku, row, column + 1):
                return True

        sudoku.grid[row, column] = 0

    return False
