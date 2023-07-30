import traceback
from datetime import datetime

from LogLevels import LogLevels
from LoggerSink import LoggerSink


class FileSink(LoggerSink):
    file_path: str

    file_path: str

    def __init__(self, required_log_level: LogLevels, filePath: str):
        super().__init__(required_log_level)
        self.file_path = filePath
        file = open(self.file_path, "r+")
        lines = file.readlines()
        if len(lines) == 0:
            if filePath.endswith(".csv"):
                file.write("LogType, Message, TimeStamp\n")
        file.close()

    def handle_log(self, message: str):
        file = open(self.file_path, "a")
        file.write(f"Log, {message},  {datetime.now()}\n")
        file.close()
        pass

    def handle_warning(self, message: str):
        file = open(self.file_path, "a")
        file.write(f"Warning, {message}, {datetime.now()}\n")
        file.close()
        pass

    def handle_error(self, message: str):
        file = open(self.file_path, "a")
        file.write(f"Error, {message}, {datetime.now()}\n")
        file.close()
        pass

    def handle_exception(self, exception: Exception, trace: traceback, fields: []):
        file = open(self.file_path, "a")
        file.write(f"Exception, {exception}, {datetime.now()}\n")
        file.close()
        pass

    def serialize_to_json(self):
        data = super().serialize_to_json()
        data["file_path"] = str(self.file_path)
        return data

    def __str__(self):
        return str(self.serialize_to_json())
