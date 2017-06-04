"""
author: Junxian Ye
time:
link:
"""
from PyQt5.QtCore import *
import time


class VideoThread(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super(VideoThread, self).__init__()
        self.stoped = False
        self.mutex = QMutex()
        self.sleep_time = 0.03

    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False
        while(True):
            if self.stoped:
                return
            self.trigger.emit()
            time.sleep(self.sleep_time)

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped

    def set_sleep_time(self, sleep_time):
        self.sleep_time = sleep_time


class CoverThread(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super(CoverThread, self).__init__()
        self.mutex = QMutex()
        self.stoped = False

    def run(self):
        with QMutexLocker(self.mutex):
            self.mutex = False
        self.trigger.emit()

    def stop(self):
        with QMutexLocker(self.mutex):
            self.mutex = True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped


class FileSaver(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super(FileSaver, self).__init__()
        self.mutex = QMutex()
        self.stoped = False

    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False
        self.trigger.emit()

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped