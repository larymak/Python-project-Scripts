# Sudoku Solver
## Description
A minimalist Python application which solves a given Sudoku problem in a *.csv file* following certain *formatting rules*.

### Formatting rules for .txt Sudokus
- The **first row** of the *.csv file* must be the following: `a,b,c,d,e,f,g,h`.
- The following rows will be the **numbers** of the sudoku given. The number **zero (0)** represents an empty cell or *naked cell*.
- The numbers will be separatted by commas, formatting the **columns**.
- Example of *.csv file* can be found under the folder **examples**.

## Requirements

This projects uses the following external libraries:
- **NumPy**
- **Pandas**

To be able to run this project, execute: `pip install -r requirements.txt`

## Steps To Execution

- Under the folder *SudokuSolver*, run: `python3 main.py`
- The path for a *.csv file* following the above formatting rules will be required. **YOU SHOULDN'T TYPE THE .CSV EXTENSION ALONG THE NAME OF THE FILE**.
- Example of input: **examples/ex2**

## TODOS
- Implement a simple **GUI** by using *tkinter* library.
- In the above mentioned **GUI**, implement an speed regulator to be able to see how the algorithm tests, fails, and backtracks.