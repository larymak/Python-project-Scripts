# Configuration for the app size and title
from typing import Dict, Tuple, List

WIDTH: int = 600
HEIGHT: int = 700
ICON_PATH: str = 'media/image/empty.ico'
TITLE_APP: str = ''
THEME: str = 'darkly'

# Configuration for the top level
LIST_DAY: tuple[str:] = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',)
TOP_LEVEL: dict[str, int] = dict(WIDTH = 300, HEIGHT = 300)

# Configuration for the backend of alarm
TIME_RELAPSE = 60
TIME_SPEED = 1
