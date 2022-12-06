import numpy as np
import pandas as pd
from sudoku import Sudoku

MINIMUM_NUMBERS_FOR_UNIQUE_SOLUTION = 17
NUMBER_REGIONS = 9

def import_sudoku() -> Sudoku:

    filename = input('Enter the filename\'s path of the sudoku to be solved: ') + '.csv'

    read_sudoku = pd.read_csv(filename).to_numpy()

    sudoku = Sudoku(read_sudoku)

    if is_solvable(sudoku):
        return sudoku

def is_solvable(sudoku: Sudoku) -> bool:

    # Check there are at least 17 non 0 numbers for unique solution

    if sudoku.grid[sudoku.grid != 0].size < MINIMUM_NUMBERS_FOR_UNIQUE_SOLUTION:
        return False

    # Check rows' legality
    for row in sudoku.grid:
        row = row[row != 0]
        if np.unique(row).size != row.size:
            return False

    # Check columns' legality
    for column in np.nditer(sudoku.grid, flags = ['external_loop'], order='C'):
        column = column[column != 0]
        if np.unique(column).size != column.size:
            return False

    # Check regions' legality
    for region_number in range(NUMBER_REGIONS):
        region = getattr(sudoku, "{}{}".format('region',region_number+1))
        region = region[region != 0]
        if np.unique(region).size != region.size:
            return False

    return True
