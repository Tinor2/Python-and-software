# constants.py
from enum import Enum

TOTAL_LAYERS = 5
TIME_STEP = 1/60

class Shape(Enum):
    CIRCLE = 1
    RECTANGLE = 2

class Color(Enum):
    def __new__(cls, r, g, b):
            obj = object.__new__(cls)
            obj._value_ = (r, g, b)
            return obj
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)