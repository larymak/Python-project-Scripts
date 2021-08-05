import numpy as np

class Sudoku:

    def __init__(self) -> None:

        self.grid = np.zeros((9,9))

    def put_number(self, number, row, column) -> None:

        self.grid[row, column] = number
