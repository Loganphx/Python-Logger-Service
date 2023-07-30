# This is a sample Python script.
from uuid import uuid1

from AnimalModel import AnimalModel
from LoggerSink import *
from FileSink import FileSink
from Logger import Logger
from PlayerModel import PlayerModel
from TranscationModel import WETHModel


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    p = Logger("TestLogger")
    fileSink = FileSink("log.csv")
    fileSink2 = FileSink("log.txt")
    p.subscribe_sink(fileSink)
    p.subscribe_sink(fileSink2)
    models = [PlayerModel(1, "loganphx"), AnimalModel(2,"panda"), WETHModel(1, str(uuid1()), str(uuid1()), str(uuid1()), str(uuid1()))]

    for model in models:
        print(model.serialize_to_json())

    Logger.handle_log("Logger Test")
    Logger.handle_warning("Test Warning")
    Logger.handle_error("Test Error")
    Logger.handle_exception(Exception("Test Exception"))


