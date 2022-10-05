from random import randint, choice
import os
import re


class MineField:
    def __init__(self, size, n_bombs):
        self.size = size
        self.digged = 0
        self.n_bombs = n_bombs
        self.grid = [[0 for j in range(size)] for i in range(size)]
        self.grid_mask = [['·' for j in range(size)] for i in range(size)]
        self.plant_bombs()
        # self.assign_numbers()
        self.first_dig()
        
    def __str__(self):
            
        _str = '    ';
        
        for i in range(1, self.size+1):
            _str += str(i) + ' '
            if i < 10:
                _str += ' '
        _str += '\n'
        
        _str += ' ' + '―' * (self.size * 3 + 3) + '\n'
        
        for i, row in enumerate(self.grid_mask, 1):
            if i < 10:
                _str += ' '
            _str += str(i) + '| '
            for char in row:
                _str += str(char) + '  '
            _str += '\n'
        return _str
        
    def plant_bombs(self):
        bombs_planted = 0
        while bombs_planted < self.n_bombs:
            row = randint(0, self.size - 1)
            column = randint(0, self.size - 1)
            
            if self.grid[row][column] == '*':
                continue
            
            self.grid[row][column] = '*'
            
            self.fill_neighbors(row, column)
                        
            bombs_planted += 1
            
    def fill_neighbors(self, row, column):
            if row != 0:
                if column != 0:
                    if self.grid[row-1][column-1] != '*':
                        self.grid[row-1][column-1] += 1
                        
                if self.grid[row-1][column] != '*':
                    self.grid[row-1][column] += 1
                    
                if column != self.size-1:
                    if self.grid[row-1][column+1] != '*':
                        self.grid[row-1][column+1] += 1
                        
            if column != 0:
                if self.grid[row][column-1] != '*':
                    self.grid[row][column-1] += 1
                    
            if column != self.size-1:
                if self.grid[row][column+1] != '*':
                    self.grid[row][column+1] += 1
                    
            if row != self.size-1:
                if column != 0:
                    if self.grid[row+1][column-1] != '*':
                        self.grid[row+1][column-1] += 1
                        
                if self.grid[row+1][column] != '*':
                    self.grid[row+1][column] += 1
                    
                if column != self.size-1:
                    if self.grid[row+1][column+1] != '*':
                        self.grid[row+1][column+1] += 1
                
    def first_dig(self):
        zeros = []
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == 0:
                    zeros.append((row, column))
                    
        spot_to_dig = choice(zeros)
        self.dig(spot_to_dig[0], spot_to_dig[1])
        
    def dig(self, row, col):
        spot = self.grid[row][col]
        if spot == '*':
            return False
        elif spot != self.grid_mask[row][col]:
            self.grid_mask[row][col] = spot
            self.digged += 1
            if (spot == 0):
                self.clear_zeros(row, col)
            return True
            
    def clear_zeros(self, row, col):
        if row != 0:
            if col != 0:
                self.dig(row-1, col-1)
                    
            self.dig(row-1, col)
                
            if col != self.size-1:
                self.dig(row-1, col+1)
                    
        if col != 0:
            self.dig(row, col-1)
            
        if col != self.size-1:
            self.dig(row, col+1)
                
        if row != self.size-1:
            if col != 0:
                self.dig(row+1, col-1)
                    
            self.dig(row+1, col)
                
            if col != self.size-1:
                self.dig(row+1, col+1)
                    
    def mark_spot(self, row, col):
        spot_mask = self.grid_mask[row][col]
        if spot_mask == 'X':
            self.grid_mask[row][col] = '·'
        elif spot_mask == '·':
            self.grid_mask[row][col] = 'X'
            
    def show_bombs(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == '*':
                    self.grid_mask[row][column] = '*'
            

def print_help():
    print('――――― Console Minesweeper ―――――')
    print('To dig in a spot, input the row\nand the column you want to dig in.')
    print('For example, if I wanted to dig\nin the row 2, column 4, I would\ntype: 2,4')
    print('―――――――――――――――――――――――――――――――――')
    print('If you just want to mark a spot\nwhere you know is a bomb, type the\ncoordinates followed with an "m".\nExample: 1,4m')
    print('\n')
    

def play(field):        
    pattern = re.compile(r"^[0-9]+,[0-9]+m?$")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(field)
    move = 'h'
    alive = True
    while alive:
        
        move = input("Your move ('h' for help, 'q' to quit): ")
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if move == 'h':
            print_help()
        elif move == 'q':
            print('Bye!\n')
            alive = 'bye'
            break
        elif re.fullmatch(pattern, move):
                row, column= [int(i)-1 for i in move.strip('m').split(',')]
                if (row > field.size) |( column > field.size):
                    print('Invalid coordinates\n')
                elif move[-1] == 'm':
                    field.mark_spot(row, column)
                else:
                    alive = field.dig(row, column)
                    if field.digged == (field.size**2 - field.n_bombs):
                        break
        else:
            print('Invalid input\n')
        
        print(field)
        
    if alive:
        if alive == True:
            print(field)
            print("You won, congratulations!!!")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        field.show_bombs()
        print(field)
        print("You lost :(")
        

field = MineField(10, 10)
play(field)
