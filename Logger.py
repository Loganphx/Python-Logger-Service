import traceback

from LoggerSink import LoggerSink


class Logger:
    sinks: list()
    name: str

    def __init__(self, name: str):
        Logger.instance = self
        self.name = name
        self.sinks = list()

    def subscribe_sink(self, sink: LoggerSink):
        print(f"Subscribing Sink: {str(sink)}")
        self.sinks.append(sink)
        return self

    @staticmethod
    def handle_log(message: str):
        for sink in Logger.instance.sinks:
            sink.handle_log(message)

    @staticmethod
    def handle_warning(message: str):
        for sink in Logger.instance.sinks:
            sink.handle_warning(message)

    @staticmethod
    def handle_error(message: str):
        for sink in Logger.instance.sinks:
            sink.handle_error(message)

    @staticmethod
    def handle_exception(exception: Exception, trace: traceback, fields: [] = None):
        for sink in Logger.instance.sinks:
            sink.handle_exception(exception, trace, fields)
