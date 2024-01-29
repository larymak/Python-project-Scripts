# Configuration for the app size and title
from typing import Dict, Tuple, List

WIDTH: int = 700
HEIGHT: int = 700
ICON_PATH: str = 'media/image/empty.ico'
TITLE_APP: str = ''
THEME: str = 'darkly'

CLOCK = {
        'X': 0,
        'Y': 0,
        'WIDTH': 1,
        'HEIGHT': 0.3,
        }
PANEL = {
        'X': 0,
        'Y': 0.3,
        'WIDTH': 1,
        'HEIGHT': 0.6,
        }
BUTTON = {
        'X': 0.5,
        'Y': 0.95,
        }

TIME = {
        'ROW': 0,
        'COLUMN': 0,
        'SPAN': 2,
        'STICKY': 'ns'
        }
DATE = {
        'ROW': 1,
        'COLUMN': 0,
        'SPAN': 2,
        'STICKY': 'n'
        }
# Configuration for the top level
LIST_DAY: tuple[str:] = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',)
TOP_LEVEL: dict[str, int] = dict(WIDTH = 300, HEIGHT = 200)

# Configuration for the backend of alarm
TIME_RELAPSE = 60
TIME_SPEED = 1

# TODO: I need to make the configuration file and to make a much clean code
