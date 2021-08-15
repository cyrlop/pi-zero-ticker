from inky_custom import Inky, Inky_SSD1608_Fast


class InkyPHAT_SSD1608_Custom(Inky):
    """Inky pHAT V2 (250x122 pixel) e-Ink Display Driver."""

    WIDTH = 250
    HEIGHT = 122

    WHITE = 0
    BLACK = 1
    RED = 2
    YELLOW = 2

    def __init__(self, colour, h_flip=False, v_flip=False):
        """Initialise an Inky pHAT Display.
        :param colour: one of red, black or yellow, default: black
        """
        Inky.__init__(
            self,
            resolution=(self.WIDTH, self.HEIGHT),
            colour=colour,
            h_flip=h_flip,
            v_flip=v_flip,
        )

class InkyPHAT_SSD1608_Fast(Inky_SSD1608_Fast):
    """Inky pHAT V2 (250x122 pixel) e-Ink Display Driver."""

    WIDTH = 250
    HEIGHT = 122

    WHITE = 0
    BLACK = 1
    RED = 2
    YELLOW = 2

    def __init__(self, colour, h_flip=False, v_flip=False):
        """Initialise an Inky pHAT Display.
        :param colour: one of red, black or yellow, default: black
        """
        Inky_SSD1608_Fast.__init__(
            self,
            resolution=(self.WIDTH, self.HEIGHT),
            colour=colour,
            h_flip=h_flip,
            v_flip=v_flip,
        )
