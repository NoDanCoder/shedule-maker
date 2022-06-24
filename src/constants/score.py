from enum import IntEnum


class Score(IntEnum):
    BAD = 0
    REGULAR = 1
    GOOD = 2
    EXCELLENT = 3

    UNKNOWN = -1