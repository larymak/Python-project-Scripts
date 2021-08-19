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

    def is_legal_state(self, new_move: Move) -> bool:

        # Make the movement, take copies of the grid and remove the movement

        self.put_number(new_move)

        row_to_check = self.grid[new_move.row, :].copy()
        column_to_check = self.grid[:, new_move.column].copy()
        region_to_check = self.get_region_from_move(new_move).copy()

        reset_move = Move(0, new_move.row, new_move.column)
        self.put_number(reset_move)

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
