import ttkbootstrap as ttk
from tkinter import IntVar
from pygame import mixer
from configuration import MUSIC_PATH, BOARD_SIZE, BOARD_GAME, BOARD_SCORE, BOARD_ROW, BOARD_COL


def play_sound():
    mixer.music.play(loops = 0)


class BoardGame(ttk.Frame):
    
    def __init__(
            self, parent, player_1, player_2,
            style_cells, style_frame, tie,
            ):
        super().__init__(master = parent, style = style_frame)
        # set mixer and the music file
        
        mixer.init()
        mixer.music.load(MUSIC_PATH)
        
        # set score
        self.o_score = 0
        self.t_score = 0
        self.x_score = 0
        
        # set player
        self.player_1 = player_1
        self.player_2 = player_2
        self.tie_score = tie
        
        # set board, player list and the player symbol
        self.board_position = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                ]
        self.players_list = ['X', 'O']
        self.player = self.players_list[0]
        
        # layout
        self.columnconfigure(BOARD_COL, weight = 1, uniform = 'a')
        self.rowconfigure(BOARD_ROW, weight = 1, uniform = 'a')
        self.pack(expand = True, fill = 'both', side = 'top')
        
        #  add the buttons/cells
        for rows in range(BOARD_SIZE[0]):
            for cols in range(BOARD_SIZE[1]):
                self.board_position[rows][cols] = Button(
                        parent = self,
                        column = cols,
                        columnspan = 1,
                        command = lambda row = rows, column = cols: self.player_move(row = row, column = column),
                        row = rows,
                        rowspan = 1,
                        style_button = style_cells,
                        text = '',
                        )
    
    def player_move(self, row: int, column: int) -> None:
        """
        It updates the board when the player click the cells and is the hole logic for the board

        """
        play_sound()
        if self.board_position[row][column]['text'] == "" and self.check_win() is False:
            self.round(row = row, column = column)
        else:
            if self.empty_space() or self.check_win():
                self.clean_board()
    
    def round(self, row: int, column: int) -> None:
        """
         It check the round if it is X or O round and
        check the round if is done and update the score
        
        """
        
        # The first move is always for the X player
        
        if self.player == self.players_list[0]:
            self.round_x(row = row, column = column)
        else:
            self.round_o(row = row, column = column)
    
    def round_x(self, row: int, column: int) -> None:
        """
        Update the board and the score for the X  player
        
        """
        self.board_position[row][column]['text'] = self.player
        
        if self.check_win() is False:
            self.player = self.players_list[1]
        
        elif self.check_win() is True:
            
            self.player_1.set(self.player_1.get() + 1)
        
        elif self.check_win() == "Tie":
            
            self.tie_score.set(self.tie_score.get() + 1)
    
    def round_o(self, row: int, column: int) -> None:
        """
        
        Update the board and the score for the O  player

        """
        self.board_position[row][column]['text'] = self.player
        
        if self.check_win() is False:
            self.player = self.players_list[0]
        
        elif self.check_win() is True:
            self.player_2.set(self.player_2.get() + 1)
        
        elif self.check_win() == "Tie":
            self.tie_score.set(self.tie_score.get() + 1)
    
    def check_win(self):
        # Check for winning conditions
        if self.row_check() or self.column_check():
            return True
        
        elif self.check_first_diagonal() or self.check_second_diagonal():
            return True
        
        elif self.empty_space():
            return 'Tie'
        else:
            return False
    
    def column_check(self):
        
        for column in range(BOARD_SIZE[1]):
            if self.board_position[0][column]['text'] == self.board_position[1][column]['text'] == \
                    self.board_position[2][column]['text'] != "":
                
                return True
    
    def row_check(self):
        
        for row in range(BOARD_SIZE[0]):
            if self.board_position[row][0]['text'] == self.board_position[row][1]['text'] == \
                    self.board_position[row][2]['text'] != "":
                
                return True
    
    def check_first_diagonal(self) -> bool:
        """
        Check the first diagonal of the board, from left to right

        """
        if self.board_position[0][0]['text'] == self.board_position[1][1]['text'] == \
                self.board_position[2][2]['text'] != "":
            
            return True
    
    def check_second_diagonal(self) -> bool:
        """
        Check the first diagonal of the board, from right to left

        """
        
        if self.board_position[0][2]['text'] == self.board_position[1][1]['text'] == \
                self.board_position[2][0]['text'] != "":
            
            return True
    
    def empty_space(self) -> bool:
        """
        Check the empty space of the board, and return True if is there are no space

        """
        spaces: int = 9
        for row in range(BOARD_SIZE[0]):
            for column in range(BOARD_SIZE[1]):
                
                if self.board_position[row][column]['text'] != '':
                    spaces -= 1
        
        return True if spaces == 0 else False
    
    def clean_board(self) -> None:
        # Clear the button texts and backgrounds
        
        for row in range(BOARD_SIZE[0]):
            for column in range(BOARD_SIZE[1]):
                
                self.board_position[row][column]['text'] = ''


class BoardScore(ttk.Frame):
    
    def __init__(
            self, parent, style_labels, style_frame, player_1,
            tie, player_2, function, style_button,
            ):
        super().__init__(master = parent, style = style_frame)
        # data score
        self.player_1_score: IntVar = player_1
        self.player_2_score: IntVar = player_2
        self.tie_score: IntVar = tie
        
        self.columnconfigure(BOARD_SCORE['COLUMNS'], weight = 1, uniform = 'b')
        self.rowconfigure(BOARD_SCORE['ROWS'], weight = 1, uniform = 'b')
        self.pack(fill = 'both', side = 'bottom')
        
        # show players name
        self.player_1 = Label(
                parent = self,
                text = BOARD_SCORE['PLAYER_1']['text'],
                row = BOARD_SCORE['PLAYER_1']['row'],
                column = BOARD_SCORE['PLAYER_1']['col'],
                columnspan = BOARD_SCORE['PLAYER_1']['columnspan'],
                style = style_labels,
                )
        self.tie = Label(
                
                parent = self,
                text = BOARD_SCORE['TIE']['text'],
                row = BOARD_SCORE['TIE']['row'],
                column = BOARD_SCORE['TIE']['col'],
                columnspan = BOARD_SCORE['TIE']['columnspan'],
                style = style_labels,
                
                )
        
        self.player_2 = Label(
                
                parent = self,
                text = BOARD_SCORE['PLAYER_2']['text'],
                row = BOARD_SCORE['PLAYER_2']['row'],
                column = BOARD_SCORE['PLAYER_2']['col'],
                columnspan = BOARD_SCORE['PLAYER_2']['columnspan'],
                style = style_labels,
                
                )
        self.reset_button = Button(
                
                parent = self,
                text = 'Reset\nGame',
                command = function,
                row = 0,
                column = 9,
                columnspan = 3,
                rowspan = 2,
                style_button = style_button,
                
                )
        # show score
        self.label_player_1_score = LabelScore(
                
                parent = self,
                textvariable = self.player_1_score,
                row = 1,
                column = 0,
                columnspan = 3,
                style = style_labels,
                
                )
        
        self.label_tie_score = LabelScore(
                
                parent = self,
                textvariable = self.tie_score,
                row = 1,
                column = 4,
                columnspan = 2,
                style = style_labels,
                
                )
        self.label_player_2_score = LabelScore(
                
                parent = self,
                textvariable = self.player_2_score,
                row = 1,
                column = 6,
                columnspan = 3,
                style = style_labels,
                
                )


class Button(ttk.Button):
    
    def __init__(
            self, parent, text, command, row,
            column, columnspan, rowspan, style_button,
            ):
        # set data
        super().__init__(
                
                master = parent,
                text = text,
                command = command,
                style = style_button,
                
                )
        
        # set layout
        self.grid(
                
                row = row,
                column = column,
                sticky = 'news',
                columnspan = columnspan,
                rowspan = rowspan,
                padx = BOARD_GAME['PADX'],
                pady = BOARD_GAME['PADY'],
                )


class Label(ttk.Label):
    def __init__(self, parent, text, row, column, columnspan, style, ):
        super().__init__(
                
                master = parent,
                text = text,
                style = style,
                anchor = 'center',
                
                )
        
        self.grid(
                
                row = row,
                column = column,
                sticky = 'news',
                columnspan = columnspan,
                padx = 10,
                pady = 10,
                
                )


class LabelScore(ttk.Label):
    def __init__(self, parent, textvariable, row, column, columnspan, style):
        super().__init__(
                
                master = parent,
                textvariable = textvariable,
                style = style,
                anchor = 'center',
                
                )
        self.grid(
                
                row = row,
                column = column,
                sticky = 'news',
                columnspan = columnspan,
                padx = 10,
                pady = 10
                
                )
