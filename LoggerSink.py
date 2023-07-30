import traceback
from abc import *

from LogLevels import LogLevels


class LoggerSink(ABC):
    required_log_level: LogLevels

    @abstractmethod
    def __init__(self, required_log_level: LogLevels):
        self.required_log_level = required_log_level

    @abstractmethod
    def serialize_to_json(self):
        return {"name": type(self).__name__, "required_log_level" : str(self.required_log_level)}

    @abstractmethod
    def handle_log(self, message: str):
        return int(self.required_log_level) >= int(LogLevels.LOG)

    @abstractmethod
    def handle_warning(self, message: str):
        return int(self.required_log_level) <= int(LogLevels.WARNING)

    @abstractmethod
    def handle_error(self, message: str):
        return int(self.required_log_level) >= int(LogLevels.ERROR)

    @abstractmethod
    def handle_exception(self, exception: Exception, trace: traceback, fields: []):
        return int(self.required_log_level) >= int(LogLevels.EXCEPTION)

    @abstractmethod
    def __str__(self):
        return str(self.serialize_to_json())
