import numpy as np
from move import Move

class Sudoku:

    def __init__(self, grid: np.ndarray) -> None:

        self.grid = grid
        self.region1 = self.grid[:3, :3]
        self.region2 = self.grid[:3, 3:6]
        self.region3 = self.grid[:3, 6:9]
        self.region4 = self.grid[3:6, :3]
        self.region5 = self.grid[3:6, 3:6]
        self.region6 = self.grid[3:6, 6:9]
        self.region7 = self.grid[6:9, :3]
        self.region8 = self.grid[6:9, 3:6]
        self.region9 = self.grid[6:9, 6:9]

    def put_number(self, move: Move) -> None:

        self.grid[move.row, move.column] = move.number

    def check_legal_state(self, previous_move: Move) -> bool:

        row_to_check = self.grid[previous_move.row, :].copy()
        column_to_check = self.grid[:, previous_move.column].copy()
        region_to_check = self.get_region_from_move(previous_move)

        # Remove 0's from the areas to be checked

        row_to_check = row_to_check[row_to_check != 0]
        column_to_check = column_to_check[column_to_check != 0]
        region_to_check = region_to_check[region_to_check != 0]

        # Check if there are repeated numbers after the move

        row_check = np.unique(row_to_check).size == row_to_check.size
        column_check = np.unique(column_to_check).size == column_to_check.size
        region_check = np.unique(region_to_check).size == region_to_check.size

        return row_check and column_check and region_check

    def get_region_from_move(self, move: Move) -> np.ndarray :

        if move.row <= 2 and move.column <= 2:
            return self.region1
        elif move.row <= 2 and move.column <= 5 and move.column > 2:
            return self.region2
        elif move.row <= 2 and move.column <= 9 and move.column > 5:
            return self.region3
        elif move.row <= 5 and move.row > 2 and move.column <= 2:
            return self.region4
        elif move.row <= 5 and move.row > 2 and move.column <= 5 and move.column > 2:
            return self.region5
        elif move.row <= 5 and move.row > 2 and move.column <= 9 and move.column > 5:
            return self.region6
        elif move.row <= 9 and move.row > 5 and move.column <= 2:
            return self.region7
        elif move.row <= 9 and move.row > 5 and move.column <= 5 and move.column > 2:
            return self.region8
        else:
            return self.region9
