from enum import Enum

class DateOption(Enum):
    DAY = 0
    MONTH = 1
    YEAR = 2

class Direction(Enum):
    BEFORE = 0
    AFTER = 1
    BETWEEN = 2