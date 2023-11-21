"""
    Here are the settings for the app and the layout.
    You can change the settings below, I used a dictionary format.
"""
# Size and layout app

APP_SIZE: tuple[int, int] = (600, 800)
MAIN_ROW: int = 7
MAIN_COLUMN: int = 4

FONT: str = 'Helvetica'
OUTPUT_FONT_SIZE: int = 70
NORMAL_FONT_SIZE: int = 32
BUTTON_FONT_SIZE: int = 0

NUMBER_POSITIONS: dict[str, str] = {
        
        '0': {'row': 6, 'column': 0, 'span': 2},
        '.': {'row': 6, 'column': 2, 'span': 1},
        '1': {'row': 5, 'column': 0, 'span': 1},
        '2': {'row': 5, 'column': 1, 'span': 1},
        '3': {'row': 5, 'column': 2, 'span': 1},
        '4': {'row': 4, 'column': 0, 'span': 1},
        '5': {'row': 4, 'column': 1, 'span': 1},
        '6': {'row': 4, 'column': 2, 'span': 1},
        '7': {'row': 3, 'column': 0, 'span': 1},
        '8': {'row': 3, 'column': 1, 'span': 1},
        '9': {'row': 3, 'column': 2, 'span': 1},
        }
MATH_POSITIONS: dict[str] = {
        '=': {'row': 6, 'column': 3, 'text': '=', 'symbol': '=', 'span': 1},
        '+': {'row': 5, 'column': 3, 'text': '+', 'symbol': '+', 'span': 1},
        '—': {'row': 4, 'column': 3, 'text': '-', 'symbol': '—', 'span': 1},
        'X': {'row': 3, 'column': 3, 'text': '*', 'symbol': 'X', 'span': 1},
        '/': {'row': 2, 'column': 3, 'text': '/', 'symbol': '÷', 'span': 1},
        }
MATH_OPERATORS: dict[str] = {
        'clear': {'row': 2, 'column': 0, 'span': 1, 'text': 'AC', },
        'invert': {'row': 2, 'column': 1, 'span': 1, 'text': '+/-'},
        'percent': {'row': 2, 'column': 2, 'span': 1, 'text': '%', }
        }

GAP_SIZE: int = 1
TITLE_BAR_COLOR: dict[str, int] = {
        'dark': 0x00000000,
        'light': 0xFFEEEE
        }
BLACK: str = '#000000'
WHITE: str = '#EEEEEE'
