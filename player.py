"""
author: Junxian Ye
time:
link:
"""
from player_ui import Ui_MainWindow, CustomDialog
from threads import VideoThread, CoverThread
from tools import VideoProperty
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2

"""
status:
0   open application
1   load video
2   play video
3   pause video
"""

STATUS = {
    'open_app': 0,
    'load_video': 1,
    'play_video': 2,
    'pause_video': 3,
}

_translate = QCoreApplication.translate

class MainWindow(QMainWindow, Ui_MainWindow):

    pause_video_signal = pyqtSignal(str)
    play_video_signal = pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.status = STATUS['open_app']

        self.cap = cv2.VideoCapture()
        self.video_property = VideoProperty()
        self.video_thread = VideoThread(self.cap, self.play_window, self.video_property)
        self.cover_thread = CoverThread(self.cap, self.play_window, self.video_property)

        # setup single slot
        self.pushButton_load.clicked.connect(self._load_file)
        # self.cover_change_signal.connect(self._enable_play_button)
        self.pushButton_play.clicked.connect(self._start_video)
        self.pause_video_signal.connect(self._pause_video)
        self.play_video_signal.connect(self._play_video)


    def _load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video", QDir.currentPath(),
                                                   "MP4视频(*.mp4);;图像(*.jpg)")
        self.file_name = file_name
        if file_name:
            self.cover_thread.set_file_name(file_name)
            self.cover_thread.start()
            self.cover_thread.cover_change_signal.connect(self._enable_play_button)

    def _save_file(self):
        pass

    def _enable_play_button(self):
        self.status = STATUS['load_video']
        self.pushButton_play.setEnabled(True)

    def _start_video(self):
        if self.status == STATUS['pause_video'] or self.status == STATUS['load_video']:
            self.video_thread.start()
            self.status = STATUS['play_video']
            self.pushButton_play.setText(_translate("MainWindow", "暂停"))
            #print(1)
            self.play_video_signal.emit()
            #print(2)
        elif self.status == STATUS['play_video']:
            self.status = STATUS['pause_video']
            self.pushButton_play.setText(_translate("MainWindow", "开始"))
            self.pause_video_signal.emit()
            # pause video
            pass
        # self.video_thread.set_file_name(self.file_name)

    def _pause_video(self):
        #self.video_thread.play_video_flag = False
        print('pause')

    def _play_video(self):
        #self.video_thread.play_video_flag = True
        print('play')
