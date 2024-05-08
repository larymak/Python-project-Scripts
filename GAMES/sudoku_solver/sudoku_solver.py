import tkinter as tk

class SudokuSolverGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.input_sudoku()
        self.create_widgets()

    def input_sudoku(self):
        print("Enter the Sudoku puzzle values row by row:")
        for i in range(9):
            row_input = input().split()
            for j in range(9):
                self.board[i][j] = int(row_input[j])

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=450, height=450, bg="white")
        self.canvas.pack()

        for i in range(10):
            line_width = 2 if i % 3 == 0 else 1
            self.canvas.create_line(50 * i, 0, 50 * i, 450, width=line_width)
            self.canvas.create_line(0, 50 * i, 450, 50 * i, width=line_width)

        for i in range(9):
            for j in range(9):
                value = self.board[i][j]
                if value != 0:
                    x, y = j * 50 + 25, i * 50 + 25
                    self.canvas.create_text(x, y, text=str(value), font=("Arial", 14, "bold"))

        self.solve_button = tk.Button(self.master, text="Solve", command=self.solve_sudoku)
        self.solve_button.pack()

    def solve_sudoku(self):
        self.solve_button.config(state="disabled")
        self.solve()

    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            self.solve_button.config(state="normal")
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(num, row, col):
                self.board[row][col] = num
                self.update_cell(row, col, num)
                if self.solve():
                    return True
                self.board[row][col] = 0
                self.update_cell(row, col, 0)
        return False

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def is_valid_move(self, num, row, col):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def update_cell(self, row, col, num):
        x, y = col * 50 + 25, row * 50 + 25
        self.canvas.delete(f"number_{row}_{col}")
        if num != 0:
            self.canvas.create_text(x, y, text=str(num), font=("Arial", 14, "bold"), tags=f"number_{row}_{col}")

def main():
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
