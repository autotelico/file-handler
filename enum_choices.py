from enum import Enum

class DateOption(Enum):
    """
        Yields date options for day, month, and year
    """
    DAY = 0
    MONTH = 1
    YEAR = 2

class Direction(Enum):
    """
        Enum that selects files from before, after, or between dates.
    """
    BEFORE = 0
    AFTER = 1
    BETWEEN = 2
