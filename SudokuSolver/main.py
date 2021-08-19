from read_sudoku import import_sudoku
from sudoku_solver import solve_sudoku

def main() -> None:

    sudoku_to_be_solved = import_sudoku()
    solve_sudoku(sudoku_to_be_solved)

if __name__ == '__main__':
    main()