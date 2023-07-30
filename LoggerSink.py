from abc import *

class LoggerSink(ABC):

    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def serialize_to_json(self):
        return {"name": type(self).__name__}

    @abstractmethod
    def handle_log(self, message: str):
        pass

    @abstractmethod
    def handle_warning(self, message: str):
        pass

    @abstractmethod
    def handle_error(self, message: str):
        pass

    @abstractmethod
    def handle_exception(self, exception: Exception):
        pass

    @abstractmethod
    def __str__(self):
        return str(self.serialize_to_json())
