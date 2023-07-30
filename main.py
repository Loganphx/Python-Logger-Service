# This is a sample Python script.
import traceback
from uuid import uuid1

from AnimalModel import AnimalModel
from DiscordWebHookSink import DiscordWebHookSink
from LoggerSink import *
from FileSink import FileSink
from Logger import Logger
from PlayerModel import PlayerModel
from TranscationModel import WETHModel
from WebHookSink import WebHookSink


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def test_exception( vx, y, z):
    try:
        raise Exception("API Timed out")
    except Exception as err:
        traceback.print_exc()
        Logger.handle_exception(err, traceback.format_exc(),  [{"name": "Service Runner Id", "value": "1"}, {"name": "Transaction Id", "value": "420"}, {"name": "API URL", "value": "www.testapi.com/do/something"}])

if __name__ == '__main__':
    print_hi('PyCharm')

    models = [PlayerModel(1, "loganphx"), AnimalModel(2,"panda"), WETHModel(1, str(uuid1()), str(uuid1()), str(uuid1()), str(uuid1()))]

    for model in models:
        print(model.serialize_to_json())

    logger = Logger("TestLogger")
    logger.subscribe_sink(FileSink(LogLevels.WARNING, "log.csv"))
    logger.subscribe_sink(FileSink(LogLevels.LOG, "log.txt"))
    logger.subscribe_sink(DiscordWebHookSink(LogLevels.ERROR, "https://ptb.discord.com/api/webhooks/1135035253162000464/rG4ljlZZYwiGGS6Anf8y98UxnuJ5CdKqgtN2OpV8XxRWbDIF_den_D4EGToYPTeyPCWl", "Python Logger Service", False))

    Logger.handle_log("Logger Test")
    Logger.handle_warning("Test Warning")
    Logger.handle_error("Test Error")
    test_exception(10,20,30)



