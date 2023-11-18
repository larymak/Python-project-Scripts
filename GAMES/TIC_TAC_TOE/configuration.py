# size of the app

MAIN_SIZE: tuple[int, int] = (800, 900)

# Music
MUSIC_PATH: str = 'media/tictacktoe_sound.mp3'

# Layout BoardScore and BoardGame.
BOARD_SIZE: tuple[int, int] = (3, 3)
BOARD_ROW: list[int] = list(range(BOARD_SIZE[0]))
BOARD_COL: list[int] = list(range(BOARD_SIZE[1]))

BOARD_SCORE_SIZE: tuple[int, int] = (9, 2)

# Style and attributes for widgets.

FRAME_STYLE_SCORE: str = 'BoardScore.TFrame'
FRAME_STYLE_GAME: str = 'BoardGame.TFrame'
BUTTON_BOARD_STYLE: str = 'BoardGame.TButton'
BUTTON_RESET_STYLE: str = 'ResetButton.TButton'
LABEL_SCORE_STYLE: str = 'BoardScore.TLabel'

BOARD_GAME = {
        'BACKGROUND': '#1F1F1F',
        'BACKGROUND_FRAME': '#375a7f',
        'BORDER_COLOR': '#375a7f',
        'BORDER_THICKNESS': 0,
        'BORDER_WIDTH': 0,
        'FONT': 'Arial',
        'FONT_SIZE': 110,
        'HOVER_COLOR_ACTIVE': '#222222',
        'HOVER_COLOR_DISABLED': '#222222',
        'JUSTIFY': 'center',
        'RELIEF': 'raised',
        'TEXT_COLOR_ACTIVE': '#E1D9D1',
        'TEXT_COLOR_DISABLED': '#E1D9D1',
        'PADX': 3,
        'PADY': 3
        }
BOARD_SCORE = {
        # the layout of the board
        'COLUMNS': list(range(10)),
        'ROWS': list(range(2)),
        
        # the style and config
        'BACKGROUND': '#121212',
        'BACKGROUND_LABEL': '#303030',
        'FONT': 'Helvetica',
        'FONT_SIZE': 34,
        'TEXT_COLOR': '#E1D9D1',
        'PLAYER_1': {
                'text': 'Player X',
                'row': 0,
                'col': 0,
                'columnspan': 3,
                },
        'PLAYER_2': {
                'text': 'Player O',
                'row': 0,
                'col': 6,
                'columnspan': 3,
                },
        'TIE': {
                'text': 'TIE ',
                'row': 0,
                'col': 4,
                'columnspan': 2,
                },
        'RESET_BUTTON': {
                'row': 0,
                'col': 9,
                'columnspan': 3,
                'rowspan': 2,
                },
        'PLAYER_1_SCORE': {
                'row': 1,
                'column': 0,
                'columnspan': 3,
                },
        'PLAYER_2_SCORE': {
                'row': 1,
                'column': 6,
                'columnspan': 3,
                },
        }
RESET_BUTTON = {
        'BACKGROUND': '#E74C3C',
        'BORDER_COLOR': '#222222',
        'BORDER_THICKNESS': 10,
        'BORDER_WIDTH': 2,
        'FONT': 'Helvetica',
        'HOVER_COLOR_ACTIVE': '#E74C3C',
        'HOVER_COLOR_DISABLED': '#E74C3C',
        'JUSTIFY': 'center',
        'RELIEF': 'solid',
        'SIZE': 34,
        'TEXT_COLOR_ACTIVE': '#E1D9D1',
        'TEXT_COLOR_DISABLED': '#E1D9D1',
        }
