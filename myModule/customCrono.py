# encoding: utf-8

# library
from datetime import datetime

# export relevant data
__all__ = ['CronoTime']

# class CronoTime
class CronoTime:
    def __init__(self):
        super().__init__()

    def start(self):
        # save time start
        self.timeStart = datetime.now()

    def stop(self):
        # save time finally
        timeFinally = datetime.now()
        # extract time elapsed
        timeElapsed = timeFinally - self.timeStart
        # return timeElapsed
        return timeElapsed
