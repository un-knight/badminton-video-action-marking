"""
author: Junxian Ye
time:
link:
"""
from PyQt5.QtCore import *
from tools import numpy_to_pixmap
import cv2
import time


class VideoThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, cap, play_window, video_property):
        super(VideoThread, self).__init__()
        self.cap = cap
        self.play_window = play_window
        self.file_name = None
        self.video_property = video_property
        self.play_video_flag = True

    def set_file_name(self, file_name):
        self.file_name = file_name

    def run(self):
        # self.cap.open(self.file_name)
        width, height = self.play_window.width(), self.play_window.height()
        play_rate = round(1.0 / self.video_property.fps, 3)

        while(self.play_video_flag):
            flag, frame = self.cap.read()
            if flag:
                self.video_property.current_frame += 1
                pixmap_frame = numpy_to_pixmap(frame, width, height)
                self.play_window.setPixmap(pixmap_frame)
                time.sleep(play_rate)
            else:
                print("No frame")
                break
        # self.cap.release()
        self.trigger.emit()


class CoverThread(QThread):
    cover_change_signal = pyqtSignal()

    def __init__(self, cap, play_window, video_property):
        super(CoverThread, self).__init__()
        self.cap = cap
        self.play_window = play_window
        self.video_property = video_property
        self.file_name = None

    def set_file_name(self, file_name):
        self.file_name = file_name

    def run(self):
        # open video
        self.cap.open(self.file_name)

        # get video information
        self.video_property.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.video_property.frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.video_property.frame_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.video_property.frame_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.video_property.current_frame = 0

        # get 1st frame as video cover and release video source
        flag, img = self.cap.read()
        self.video_property.current_frame += 1
        # self.cap.release()

        # convert and resize numpy array(OpenCV format) image to pixmap(Qt format)
        width, height = self.play_window.width(), self.play_window.height()
        pixmap_img = numpy_to_pixmap(img, width, height)

        self.play_window.setPixmap(pixmap_img)
        self.cover_change_signal.emit()