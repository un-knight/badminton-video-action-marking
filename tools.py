"""
author: Junxian Ye
time:
link:
"""
from PyQt5.QtGui import *
import cv2


def numpy_to_pixmap(img, width, height):
    """
    convert and resize numpy array(OpenCV format) image to pixmap(Qt format)
    :param img:
    :param width:
    :param height:
    :return:
    """
    img_resized = cv2.resize(img, (width, height), cv2.INTER_AREA)
    img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
    qt_img = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0], QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(qt_img)
    return pixmap


class VideoProperty():
    def __init__(self):
        self.fps = 0
        self.frame_width = 0
        self.frame_height = 0
        self.frame_count = 0
        self.current_frame = 0

    def initialize(self):
        self.fps = 0
        self.frame_width = 0
        self.frame_height = 0
        self.frame_count = 0
        self.current_frame = 0