"""
author: Junxian Ye
time:
link:
"""
from new_player_ui import Ui_MainWindow
from threads import VideoThread, FileSaver
from tools import VideoProperty, numpy_to_pixmap, save_file
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
        self.mark_start_flag = True
        # save result in a dict
        self.result = {}
        self.tmp = []
        self.action_categories = None

        self.cap = cv2.VideoCapture()
        self.video_property = VideoProperty()
        self.video_thread = VideoThread()
        self.file_saver = FileSaver()

        # setup single slot
        self.video_thread.trigger.connect(self._play_video)
        self.file_saver.trigger.connect(self._save_file)

        self.pushButton_load.clicked.connect(self._load_file)
        self.pushButton_play.clicked.connect(self._play_or_pause_video)
        self.pushButton_save.clicked.connect(self._start_saver)
        self.pushButton_mark.clicked.connect(self._mark_action)

        # self.horizontalSlider.valueChanged[int].connect(self._change_slider)
        self.horizontalSlider.sliderPressed.connect(self._press_slider)
        self.horizontalSlider.sliderReleased.connect(self._release_slider)

        self.radioButton_CQ.toggled.connect(self._action_CQ)
        self.radioButton_GYQ.toggled.connect(self._action_GYQ)
        self.radioButton_Other.toggled.connect(self._action_Other)
        self.radioButton_PC.toggled.connect(self._action_PC)
        self.radioButton_PD.toggled.connect(self._action_PD)
        self.radioButton_SQ.toggled.connect(self._action_SQ)
        self.radioButton_TQ.toggled.connect(self._action_TQ)
        self.radioButton_Hidden.toggled.connect(self._action_None)

        self.actionAbout.triggered.connect(self._help)

    def reset_properties(self):
        self.result = {}
        self.tmp = []


    def _load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video", QDir.currentPath(),
                                                   "MP4视频(*.mp4)")
        self.file_name = file_name
        if file_name:
            # load video
            if self.cap.isOpened():
                self.video_thread.stop()
                self.pushButton_play.setText(_translate("MainWindow", "播放"))
                self.cap.release()
            self.cap.open(file_name)

            # get video properties
            self.video_property.fps = self.cap.get(cv2.CAP_PROP_FPS)
            self.video_property.frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
            self.video_property.frame_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.video_property.frame_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

            # reset some key properties
            self.reset_properties()

            # setup the video play rate
            sleep_time = round(1.0 / self.video_property.fps, 3)
            self.video_thread.set_sleep_time(sleep_time)

            self.status = STATUS['load_video']

            # using 1st frame as the video cover
            self._play_video()
            self.status = STATUS['pause_video']

            self.pushButton_play.setEnabled(True)

    def _start_saver(self):
        self.file_saver.start()
        self.file_saver.stop()

    def _save_file(self):
        save_file(self.result, self.file_name)
        QMessageBox.information(self, "提示", "完成保存", QMessageBox.Yes)

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
            # update image
            pixmap_frame = numpy_to_pixmap(frame, self.play_window.width(), self.play_window.height())
            self.play_window.setPixmap(pixmap_frame)

            # update QSlider
            current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            slider_pos = int(current_frame / self.video_property.frame_count * \
                         self.horizontalSlider.maximum())
            # print(slider_pos)
            self.horizontalSlider.setValue(slider_pos)
            # print("frame: {}".format(self.video_property.current_frame))
        else:
            # print("No frame")
            self.video_thread.stop()
            self.pushButton_play.setText(_translate("MainWindow", "播放"))

    def _change_slider(self, value):
        # print(value)
        pass

    def _release_slider(self):
        slider_pos = self.horizontalSlider.value()
        next_frame = int(slider_pos / self.horizontalSlider.maximum() * \
                         self.video_property.frame_count)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, next_frame)
        self._play_video()

    def _press_slider(self):
        self.video_thread.stop()
        self.status = STATUS['pause_video']
        self.pushButton_play.setText(_translate("MainWindow", "播放"))

    def _mark_action(self):
        if self.mark_start_flag:
            self.pushButton_mark.setText(_translate("MainWindow", "标记结束帧"))
            self.mark_start_flag = False

            # record start frame position
            self.tmp = []
            current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES) - 1
            current_frame = max(current_frame, 0)
            self.tmp.append(current_frame)
            # print('start mark')
        else:
            if self.action_categories is None:
                QMessageBox.information(self, "警告", "请选择一种动作标签", QMessageBox.Yes)
                return
            self.pushButton_mark.setText(_translate("MainWindow", "标记开始帧"))
            self.mark_start_flag = True

            # record end frame position
            if self.horizontalSlider.value() == self.horizontalSlider.maximum():
                current_frame = self.video_property.frame_count - 1
            else:
                current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES) - 1
            current_frame = max(current_frame, 0)
            self.tmp.append(current_frame)
            self.result[tuple(self.tmp)] = self.action_categories
            # self.action_categories = None
            # print('end mark')
            # print(self.result)

            self.reset_radio_button()
        # self.pushButton_mark.disconnect(self._mark_action_start)

    def _action_CQ(self, value):
        if value:
            self.action_categories = "CQ"

    def _action_GYQ(self, value):
        if value:
            self.action_categories = "GYQ"

    def _action_Other(self, value):
        if value:
            self.action_categories = "Other"

    def _action_PC(self, value):
        if value:
            self.action_categories = "PC"

    def _action_PD(self, value):
        if value:
            self.action_categories = "PD"

    def _action_SQ(self, value):
        if value:
            self.action_categories = "SQ"

    def _action_TQ(self, value):
        if value:
            self.action_categories = "TQ"

    def _action_None(self, value):
        if value:
            self.action_categories = None

    def _help(self):
        infor = """
        作者：叶俊贤
        日期：2017.5.31
        邮箱：yjx.underworld@gmail.com
        版本号：0.1.0
        如果在使用过程遇到任何问题，或者想提
        修改建议，欢迎联系:)
        """
        QMessageBox.information(self, "提示", infor, QMessageBox.Yes)

    def reset_radio_button(self):
        self.radioButton_Hidden.setChecked(True)