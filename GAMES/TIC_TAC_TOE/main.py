import os
import sys
import ttkbootstrap as ttk

from tkinter import IntVar
from widgets import BoardGame, BoardScore
from configuration import (
    # layout
    MAIN_SIZE, BOARD_GAME, BOARD_SCORE, RESET_BUTTON,
    # style
    FRAME_STYLE_SCORE, FRAME_STYLE_GAME, BUTTON_BOARD_STYLE, BUTTON_RESET_STYLE, LABEL_SCORE_STYLE,
    )

# import the modules for windows (it works  only on windows)

try:
    from ctypes import windll, byref, sizeof, c_int
except Exception:
    pass


def path_resource(relative_path: str) -> str:
    """
    it take the relative path and return the absolute path of the file from your system, is used for making the
    app into a exe file for window

    """
    try:
        base_path: str = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)


class TicTacToe(ttk.Window):
    
    player_1: IntVar
    player_2: IntVar
    tie_score: IntVar
    
    def __init__(self):
        super().__init__()
        
        self.bind('<Alt-s>', lambda event: self.destroy())
        self.title('')
        self.set_emtpy_icon()
        self.set_title_bar_color()
        self.set_window_size(width = MAIN_SIZE[0], height = MAIN_SIZE[1])
        
        # set up the style
        self.Style = ttk.Style(theme = 'darkly')
        
        # style for the score/ board_score
        self.Style.configure(
                
                background = BOARD_SCORE['BACKGROUND'],
                style = FRAME_STYLE_SCORE,
                
                )
        
        self.Style.configure(
                
                background = BOARD_GAME['BACKGROUND_FRAME'],
                style = FRAME_STYLE_GAME,
                
                )
        
        self.Style.configure(
                
                background = BOARD_GAME['BACKGROUND'],
                bordercolor = BOARD_GAME['BORDER_COLOR'],
                borderthickness = BOARD_GAME['BORDER_THICKNESS'],
                borderwidth = BOARD_GAME['BORDER_WIDTH'],
                font = (BOARD_GAME['FONT'], BOARD_GAME['FONT_SIZE']),
                justify = BOARD_GAME['JUSTIFY'],
                relief = BOARD_GAME['RELIEF'],
                style = BUTTON_BOARD_STYLE,
                
                )
        
        self.Style.map(
                
                style = BUTTON_BOARD_STYLE,
                foreground = [
                        ('active', BOARD_GAME['TEXT_COLOR_ACTIVE']),
                        ('disabled', BOARD_GAME['TEXT_COLOR_DISABLED'])
                        ],
                background = [
                        ('active', BOARD_GAME['HOVER_COLOR_ACTIVE']),
                        ('disabled', BOARD_GAME['HOVER_COLOR_DISABLED'])
                        ]
                )
        
        self.Style.configure(
                
                background = RESET_BUTTON['BACKGROUND'],
                bordercolor = RESET_BUTTON['BORDER_COLOR'],
                borderthickness = RESET_BUTTON['BORDER_THICKNESS'],
                borderwidth = RESET_BUTTON['BORDER_WIDTH'],
                font = (RESET_BUTTON['FONT'], RESET_BUTTON['SIZE']),
                justify = RESET_BUTTON['JUSTIFY'],
                relief = RESET_BUTTON['RELIEF'],
                style = BUTTON_RESET_STYLE,
                
                )
        self.Style.map(
                
                style = BUTTON_RESET_STYLE,
                foreground = [
                        ('active', RESET_BUTTON['TEXT_COLOR_ACTIVE']),
                        ('disabled', RESET_BUTTON['TEXT_COLOR_DISABLED'])
                        ],
                background = [
                        ('active', RESET_BUTTON['HOVER_COLOR_ACTIVE']),
                        ('disabled', RESET_BUTTON['HOVER_COLOR_DISABLED'])]
                
                )
        
        self.Style.configure(
                
                background = BOARD_SCORE['BACKGROUND'],
                font = (BOARD_SCORE['FONT'], BOARD_SCORE['FONT_SIZE']),
                foreground = BOARD_SCORE['TEXT_COLOR'],
                style = LABEL_SCORE_STYLE,
                
                )
        
        # 	set player data
        self.player_1 = ttk.IntVar(value = 0)
        self.player_2 = ttk.IntVar(value = 0)
        self.tie_score = ttk.IntVar(value = 0)
        
        # set widgets
        self.board_game = BoardGame(
                
                parent = self,
                style_cells = BUTTON_BOARD_STYLE,
                style_frame = FRAME_STYLE_GAME,
                player_1 = self.player_1,
                tie = self.tie_score,
                player_2 = self.player_2,
                
                )
        
        self.board_score = BoardScore(
                
                parent = self,
                style_labels = LABEL_SCORE_STYLE,
                style_frame = FRAME_STYLE_SCORE,
                style_button = BUTTON_RESET_STYLE,
                player_1 = self.player_1,
                tie = self.tie_score,
                player_2 = self.player_2,
                function = self.clean_board
                
                )
        
        # run
        self.mainloop()
    
    def clean_board(self):
        """
        It clean the board and reset the score
        """
        self.board_game.clean_board()
        self.player_1.set(0)
        self.player_2.set(0)
        self.tie_score.set(0)
    
    def set_emtpy_icon(self) -> None:
        """
        It sets the icon to  one empty from the title bar

        """
        try:
            path_image: str = path_resource('image/empty.ico')
            self.iconbitmap(path_image)
        except Exception:
            pass
    
    def set_window_size(self, width: int, height: int) -> None:
        """
        It adjust the window size to be in the center of the screen
        
        """
        left = int(self.winfo_screenwidth() / 2 - width / 2)
        top = int(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(f'{width}x{height}+{left}+{top}')
    
    def set_title_bar_color(self) -> None:
        """
    It works only on Windows, not on GNU/Linux and macOS.
        """
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE: int = 35  # target the title bar
            color_tile: int = 0x00030303
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(color_tile)), sizeof(c_int))
        except Exception:
            pass


if __name__ == '__main__':
    
    # starts the game
    TicTacToe()
