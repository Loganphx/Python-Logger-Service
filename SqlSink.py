import traceback

from LoggerSink import LoggerSink


class SqlSink(LoggerSink):
    sql_connection_string: str

    def __init__(self, sql_connection_string):
        self.sql_connection_string = sql_connection_string

    def handle_log(self, message: str):
        pass

    def handle_warning(self, message: str):
        pass

    def handle_error(self, message: str):
        pass

    def handle_exception(self, exception: Exception, trace: traceback, fields: []):
        pass

    def serialize_to_json(self):
        data = super().serialize_to_json()
        data["sql_connection_string"] = self.sql_connection_string
        return data

    def __str__(self):
        return str(self.serialize_to_json())


