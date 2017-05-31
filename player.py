"""
author: Junxian Ye
time:
link:
"""
from player_ui import Ui_MainWindow
from threads import VideoThread
from tools import VideoProperty, numpy_to_pixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2


STATUS = {
    'open_app': 0,
    'load_video': 1,
    'play_video': 2,
    'pause_video': 3,
}

_translate = QCoreApplication.translate

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.status = STATUS['open_app']

        self.cap = cv2.VideoCapture()
        self.video_property = VideoProperty()
        self.video_thread = VideoThread()

        # setup single slot
        self.video_thread.trigger.connect(self._play_video)
        self.pushButton_load.clicked.connect(self._load_file)
        self.pushButton_play.clicked.connect(self._play_or_pause_video)


    def _load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video", QDir.currentPath(),
                                                   "MP4视频(*.mp4);;图像(*.jpg)")
        self.file_name = file_name
        if file_name:
            # load video
            if self.cap.isOpened():
                self.video_thread.stop()
                self.pushButton_play.setText(_translate("MainWindow", "播放"))
                self.cap.release()
            self.cap.open(file_name)

            # get video properties
            self.video_property.initialize()
            self.video_property.fps = self.cap.get(cv2.CAP_PROP_FPS)
            self.video_property.frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
            self.video_property.frame_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.video_property.frame_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

            sleep_time = round(1.0 / self.video_property.fps, 3)
            self.video_thread.set_sleep_time(sleep_time)

            self.status = STATUS['load_video']

            # using 1st frame as the video cover
            self._play_video()
            self.status = STATUS['pause_video']

            self.pushButton_play.setEnabled(True)

    def _save_file(self):
        pass

    def _play_or_pause_video(self):
        if self.status == STATUS['pause_video']:
            self.video_thread.start()
            self.pushButton_play.setText(_translate("MainWindow", "暂停"))
            self.status = STATUS['play_video']
        elif self.status == STATUS['play_video']:
            self.video_thread.stop()
            self.pushButton_play.setText(_translate("MainWindow", "播放"))
            self.status = STATUS['pause_video']

    def _play_video(self):
        flag, frame = self.cap.read()
        if flag:
            self.video_property.current_frame += 1
            pixmap_frame = numpy_to_pixmap(frame, self.play_window.width(), self.play_window.height())
            self.play_window.setPixmap(pixmap_frame)
            print("frame: {}".format(self.video_property.current_frame))
        else:
            # @BUG: Need to be processed
            print("No frame")
            self.cap.release()