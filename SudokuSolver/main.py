from read_sudoku import import_sudoku
from sudoku_solver import solve_sudoku

def main() -> None:

    sudoku_to_be_solved = import_sudoku()
    sudoku_solved = solve_sudoku(sudoku_to_be_solved)
    print("The solution to the sudoku proposed is:\n", sudoku_solved.grid)

if __name__ == '__main__':
    main()