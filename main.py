# This is a sample Python script.
from uuid import uuid1

from Sinks.DiscordWebHookSink import DiscordWebHookSink
from Sinks.LoggerSink import *
from Sinks.FileSink import FileSink
from Sinks.Logger import Logger
def test_exception( vx, y, z):
    try:
        raise Exception("API Timed out")
    except Exception as err:
        traceback.print_exc()
        Logger.handle_exception(err, traceback.format_exc(),  [{"name": "Service Runner Id", "value": "1"}, {"name": "Transaction Id", "value": "420"}, {"name": "API URL", "value": "www.testapi.com/do/something"}])

if __name__ == '__main__':

    logger = Logger("TestLogger")
    logger.subscribe_sink(FileSink(LogLevels.WARNING, "log.csv"))
    logger.subscribe_sink(FileSink(LogLevels.LOG, "log.txt"))
    logger.subscribe_sink(DiscordWebHookSink(LogLevels.ERROR, "https://ptb.discord.com/api/webhooks/1135035253162000464/rG4ljlZZYwiGGS6Anf8y98UxnuJ5CdKqgtN2OpV8XxRWbDIF_den_D4EGToYPTeyPCWl", "Python Logger Service", False))

    Logger.handle_log("Logger Test")
    Logger.handle_warning("Test Warning")
    Logger.handle_error("Test Error")
    test_exception(10,20,30)



