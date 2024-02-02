from color import Color


class Theme:
    def __init__(
        self, light_bg, dark_bg, light_trace, dark_trace, light_moves, dark_moves
    ):
        self.bg = Color(light_bg, dark_bg)
        self.trace = Color(light_trace, dark_trace)
        self.moves = Color(light_moves, dark_moves)
