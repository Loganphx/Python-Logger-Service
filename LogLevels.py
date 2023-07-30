from enum import Enum, IntEnum


class LogLevels(IntEnum):
    NONE = 0,
    EXCEPTION = 1,
    ERROR = 2,
    WARNING = 3,
    DEBUG = 4,
    LOG = 5