"""This python script contains a class to solve a sudoku.
"""

from copy import deepcopy
import pygame as pg

VISITED_COLOR = (50,50,50)
AGENT_COLOR = (255,0,0)
BOARD_COLOR = (0,0,0)
WALL_COLOR = (255,255,255)
SOLUTION_COLOR = (0,255,0)
START_CELL_COLOR = (200,0,200)
END_CELL_COLOR = (0,128,128)

SIZE = (600,600)

class Cell():
    """Cell element of sudoku.
    """
    def __init__(self, name:int|str, domain:list[int]) -> None:
        """Initialise a cell of the sudoku.

        Args:
            name (int): the actual cell position.
            domain (list[int]): list of all the possible values the cell can take.
        """
        self.name = name
        self.value:int|str = None
        self.domain:list[int] = deepcopy(domain)
    
class Grid():
    """The actual sudoku grid.
    """
    def __init__(self, rows:int|None = None, columns:int|None = None) -> None:
        """Initialise the sudoku grid.

        Args:
            rows (int | None, optional): The number of rows in a block eg 3 for a 9x9 sudoku. Defaults to None.
            columns (int | None, optional): The number of columns in a block. Defaults to None.
        """
        self.rows = rows
        self.columns = columns
        if not self.rows or not self.columns:
            return
        self.grid_len = self.rows * self.columns
        self.domain:list[int] = [i for i in range(1, min(10, self.grid_len+1))]
        if self.grid_len >= 10:
            self.domain.extend(chr(ord('A') + i - 10) for i in range(10, self.grid_len+1))
        self.cells:list[Cell] = [Cell(i, self.domain) for i in range(self.grid_len * self.grid_len)]
        self.unsolved_cells:list[int] = [i for i in range(self.grid_len * self.grid_len)]
        self.solved_cells:list[int] = []
        self.initial_solved:list[int] = []
        self.initial_unsolved:list[int] = [i for i in range(self.grid_len * self.grid_len)]
    
    def preassign(self, values:dict[tuple, int]) -> None:
        """Preassigns particular value to the cells already given in the problem.

        Args:
            values (dict[tuple, int]): a dictionary with keys of the (row,column) and value of the actual value of the cell.
        """
        for i, value in values.items():
            number = int(i[0]*self.grid_len + i[1])
            if number in self.initial_solved:
                self.unassign_last(number)
            self.cells[number].value = value
            self.cells[number].domain = []
            self.unsolved_cells.remove(number)
            self.initial_unsolved.remove(number)
            self.initial_solved.append(number)
            self.solved_cells.append(number)
    
    def unassign_last(self, number:int|None = None):
        """Unassigns either the last value assigned to a cell or a particular cell given by number.

        Args:
            number (int | None, optional): The number of the cell in the grid, starting from 0 at the top right and moving left. Defaults to None.
        """
        if not number:
            number = self.solved_cells.pop()
            self.initial_solved.pop()
        else:
            self.solved_cells.remove(number)
            self.initial_solved.remove(number)
        self.unsolved_cells.append(number)
        self.initial_unsolved.append(number)
        self.cells[number].domain = deepcopy(self.domain)
        self.cells[number].value = None
    
    def solve(self) -> None:
        """Tries to solve the sudoku.
        """
        while len(self.unsolved_cells) > 0:
            changed = False
            i = 0
            # first update domains based on known cells
            while i < len(self.solved_cells):
                val = self.cells[self.solved_cells[i]].value
                r,c = int(self.solved_cells[i]/self.grid_len), int(self.solved_cells[i]%self.grid_len)
                # first check cells on the same row
                for j in range(r*self.grid_len, (r+1)*self.grid_len):
                    try:
                        self.cells[j].domain.remove(val)
                        if len(self.cells[j].domain) == 1:
                            self.cells[j].value = self.cells[j].domain[0]
                            self.cells[j].domain = []
                            self.unsolved_cells.remove(j)
                            self.solved_cells.append(j)
                        changed = True
                        i = -1
                    except ValueError:
                        pass
                # next check cells on the same column
                for k in range(self.grid_len):
                    j = k*self.grid_len + c
                    try:
                        self.cells[j].domain.remove(val)
                        if len(self.cells[j].domain) == 1:
                            self.cells[j].value = self.cells[j].domain[0]
                            self.cells[j].domain = []
                            self.unsolved_cells.remove(j)
                            self.solved_cells.append(j)
                        changed = True
                        i = -1
                    except ValueError:
                        pass
                # next check cells on the same block
                br = int(r/self.rows)
                bc = int(c/self.columns)
                for k in range(self.grid_len):
                    cr = br*self.rows + int(k/self.columns)
                    cc = bc*self.columns + int(k%self.columns)
                    j = cr*self.grid_len + cc
                    try:
                        self.cells[j].domain.remove(val)
                        if len(self.cells[j].domain) == 1:
                            self.cells[j].value = self.cells[j].domain[0]
                            self.cells[j].domain = []
                            self.unsolved_cells.remove(j)
                            self.solved_cells.append(j)
                        changed = True
                        i = -1
                    except ValueError:
                        pass
                i += 1
            # next check for unique value in domains of cells in row column or block
            # first check rows
            to_break = False
            for k in range(self.grid_len):
                values:dict[int|str, list[int]] = {val:[] for val in self.domain}
                for m in range(self.grid_len):
                    j = k*self.grid_len + m
                    for v in self.cells[j].domain:
                        values[v].append(j)
                for val,ls in values.items():
                    if len(ls) == 1:
                        self.cells[ls[0]].value = val
                        self.cells[ls[0]].domain = []
                        self.unsolved_cells.remove(ls[0])
                        self.solved_cells.append(ls[0])
                        to_break = True
                        break
                if to_break:
                    break
            if to_break:
                continue
            # first check columns
            to_break = False
            for k in range(self.grid_len):
                values:dict[int|str, list[int]] = {val:[] for val in self.domain}
                for m in range(self.grid_len):
                    j = m*self.grid_len + k
                    for v in self.cells[j].domain:
                        values[v].append(j)
                for val,ls in values.items():
                    if len(ls) == 1:
                        self.cells[ls[0]].value = val
                        self.cells[ls[0]].domain = []
                        self.unsolved_cells.remove(ls[0])
                        self.solved_cells.append(ls[0])
                        to_break = True
                        break
                if to_break:
                    break
            if to_break:
                continue
            if not changed:
                return
    
    def render_cells(self, window:pg.Surface) -> None:
        """Draws the grid and populates it with the value of the cells.

        Args:
            window (pg.Surface): a pygame window to be used to populate the grid and cells.
        """
        size = window.get_size()
        py = int(size[1] / self.grid_len)
        px = int(size[0] / self.grid_len)
        ball = pg.Rect(0, 0, size[0], size[1])
        pg.draw.rect(window, BOARD_COLOR, ball)
        for i in range(self.grid_len+1):
            if i%self.columns:
                pg.draw.line(window, VISITED_COLOR, (i*px, 0), (i*px, size[1]))
            else:
                pg.draw.line(window, WALL_COLOR, (i*px, 0), (i*px, size[1]))
            if i%self.rows:
                pg.draw.line(window, VISITED_COLOR, (0, i*py), (size[0], i*py))
            else:
                pg.draw.line(window, WALL_COLOR, (0, i*py), (size[0], i*py))
        font = pg.font.SysFont(None, min(py, px))
        for i in self.initial_solved:
            text = font.render(str(self.cells[i].value), True, AGENT_COLOR, BOARD_COLOR)
            textRect = text.get_rect()
            y = int(i/self.grid_len)
            x = int(i%self.grid_len)
            textRect.center = (int((x+0.5)*px),int((y+0.5)*py))
            window.blit(text, textRect)
        for i in self.initial_unsolved:
            if val:=self.cells[i].value:
                text = font.render(str(val), True, SOLUTION_COLOR, BOARD_COLOR)
                textRect = text.get_rect()
                y = int(i/self.grid_len)
                x = int(i%self.grid_len)
                textRect.center = (int((x+0.5)*px),int((y+0.5)*py))
                window.blit(text, textRect)
            # else:
            #     for dv in self.cells[i].domain:
            #         text = font.render(str(val), True, SOLUTION_COLOR, BOARD_COLOR)
            #         textRect = text.get_rect()
            #         y = int(i/self.grid_len)
            #         x = int(i%self.grid_len)
            #         textRect.center = (int((x+0.5)*px),int((y+0.5)*py))
            #         window.blit(text, textRect)
    
    def render_grid(self, size:tuple[int, int]=SIZE) -> None:
        """Creates the grid window and renders it.

        Args:
            size (tuple[int, int], optional): The size of the window to be used. Defaults to (600,600).
        """
        pg.init()
        window = pg.display.set_mode(size)
        window.fill(BOARD_COLOR)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.display.quit()
                    return
            self.render_cells(window)
            pg.display.update()
    
    def input_to_grid(self, size:tuple[int, int]=SIZE) -> None:
        """Allows for input of the value of the grid cells by clicking on a cell and typing the value.

        Args:
            size (tuple[int, int], optional): The size of the window to which the grid will be rendered. Defaults to (600,600).
        """
        pg.init()
        window = pg.display.set_mode(size)
        window.fill(BOARD_COLOR)
        size = window.get_size()
        py = int(size[1] / self.grid_len)
        px = int(size[0] / self.grid_len)
        clicked_cell = None
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.display.quit()
                    return
                if event.type == pg.MOUSEBUTTONUP:
                    clicked_cell = event.dict['pos']
                if event.type == pg.KEYDOWN:
                    key = event.dict['unicode']
                    if key >= '0' and key <= '9':
                        if clicked_cell:
                            pos = (int(clicked_cell[1] / py), int(clicked_cell[0] / px))
                            if int(key) <= self.grid_len:
                                self.preassign({pos:int(key)})
                    elif key >= 'A' and key <= 'Z':
                        if clicked_cell:
                            pos = (int(clicked_cell[1] / py), int(clicked_cell[0] / px))
                            if (ord(key) - ord('A') + 10) <= self.grid_len:
                                self.preassign({pos:key})
                    elif key == ' ':
                        self.unassign_last()
            self.render_cells(window)
            pg.display.update()
    
    def save(self, filename:str) -> None:
        """Saves the current state of the grid in a file.\n
        Save format is:\n
        rows,columns\n
        (cell_number,cell_value)|(cell_number,cell_value)|...|(cell_number,cell_value)\n
        (cell_number,cell_value)|(cell_number,cell_value)|...|(cell_number,cell_value)\n
        \n
        where the second line is the initial cell values before trying to solve\n
        \t the third line is the initially unsolved cell values after solving if Grid.solve() has been run\n

        Args:
            filename (str): The path of the file to be saved to.
        """
        s = f"{self.rows},{self.columns}\n"
        s += "|".join(f"({a},{self.cells[a].value})" for a in self.initial_solved)
        s += "\n"
        s += "|".join(f"({a},{self.cells[a].value})" for a in self.initial_unsolved)
        with open(filename, 'w') as f:
            f.write(s)
            f.close()
    
    def load(self, filename:str):
        """Loads the grid from a saved state file created by calling Grid.save(filename)

        Args:
            filename (str): The path to the file containing the grid status to be loaded.
        """
        with open(filename, 'r') as f:
            for i,line in enumerate(f):
                line = line.replace("\n","")
                if i == 0:
                    rows, columns = line.replace("(","").replace(")","").split(",")
                    self.rows = int(rows)
                    self.columns = int(columns)
                elif i == 1:
                    initial_solved_pairs = [tuple(int(i) for i in a.split(",")) for a in line.replace("(","").replace(")","").split("|")]
                elif i == 2:
                    initial_unsolved_pairs = [tuple(eval(i) for i in a.split(",")) for a in line.replace("(","").replace(")","").split("|")]
            f.close()
        self.grid_len = self.rows * self.columns
        self.domain:list[int] = [i for i in range(1, min(10, self.grid_len+1))]
        if self.grid_len >= 10:
            self.domain.extend(chr(ord('A') + i - 10) for i in range(10, self.grid_len+1))
        self.cells:list[Cell] = [Cell(i, self.domain) for i in range(self.grid_len * self.grid_len)]
        self.unsolved_cells:list[int] = [i for i in range(self.grid_len * self.grid_len)]
        self.solved_cells:list[int] = []
        self.initial_solved:list[int] = []
        self.initial_unsolved:list[int] = [i for i in range(self.grid_len * self.grid_len)]
        for (number,value) in initial_solved_pairs:
            self.initial_solved.append(number)
            self.solved_cells.append(number)
            self.cells[number].value = value
            self.cells[number].domain = []
            self.initial_unsolved.remove(number)
            self.unsolved_cells.remove(number)
        for (number,value) in initial_unsolved_pairs:
            if value:
                self.solved_cells.append(number)
                self.cells[number].value = value
                self.cells[number].domain = []
                self.unsolved_cells.remove(number)
    
    def save_grid_image(self, path:str, size:tuple[int, int]=SIZE) -> None:
        pg.init()
        window = pg.display.set_mode(size)
        window.fill(BOARD_COLOR)
        self.render_cells(window)
        pg.image.save(window, path)
        pg.quit()
          
def main():
    r = int(input("Enter number of rows in a block: "))
    c = int(input("Enter number of columns in a block: "))
    grid = Grid(r,c)
    # grid = Grid()
    # grid.load("s2.txt")
    grid.input_to_grid()
    grid.save("s3.txt")
    grid.solve()
    grid.save("s3.txt")
    # grid = Grid()
    # grid.load("s1.txt")
    grid.render_grid()
  
if __name__ == "__main__":
    main()
