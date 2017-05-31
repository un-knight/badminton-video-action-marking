"""
author: Junxian Ye
time:
link:
"""
from PyQt5.QtGui import *
import cv2
import os


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


def save_file(result, video_filename):
    # split file path and file name
    path, video_name = os.path.split(video_filename)
    # split file name and file extension
    video_name = os.path.splitext(video_name)[0]
    # create output file name
    output_filename = os.path.join(path, "result.txt")

    with open(output_filename, 'a') as f:
        f.write("{} ".format(video_name))
        frame_windows = list(result.keys())
        frame_windows.sort()

        for frame_window in frame_windows:
            start_frame = int(frame_window[0])
            over_frame = int(frame_window[1])
            category = result.get(frame_window)
            f.write("{start_frame},{over_frame}:{category} ".format(**locals()))
        f.write('\n')


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