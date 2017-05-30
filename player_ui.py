# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.play_window = QtWidgets.QLabel(self.centralwidget)
        self.play_window.setGeometry(QtCore.QRect(50, 100, 400, 300))
        self.play_window.setText("")
        self.play_window.setObjectName("play_window")
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(550, 130, 111, 51))
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setGeometry(QtCore.QRect(550, 230, 111, 51))
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_pause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pause.setGeometry(QtCore.QRect(550, 330, 111, 51))
        self.pushButton_pause.setObjectName("pushButton_pause")

        self.pushButton_play.setEnabled(False)
        self.pushButton_pause.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.window_width, self.window_height = self.play_window.width(), self.play_window.height()

        # Load image/frame and convert it into QPixmap
        # image = load_image(window_width, window_height)
        # qimg = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
        # pixmap = QtGui.QPixmap.fromImage(qimg)
        # qt_img = QtGui.QImage()
        # qt_img.load(r'D:\mark_video_action\cover.jpg')
        # pixmap = QtGui.QPixmap.fromImage(qt_img)

        # pixmap = QtGui.QPixmap(r'D:\mark_video_action\cover.jpg')
        # resize image to fit play_window
        # pixmap = pixmap.scaled(window_width, window_height, QtCore.Qt.KeepAspectRatio)
        # self.play_window.setPixmap(pixmap)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_load.setText(_translate("MainWindow", "加载文件"))
        self.pushButton_play.setText(_translate("MainWindow", "播放"))
        self.pushButton_pause.setText(_translate("MainWindow", "暂停"))


class CustomDialog(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('New Dialog')
        # Add button
        button = QtWidgets.QDIalogButtonBox.Ok
        button_box = QtWidgets.QDialogButtonBox(button)
        button_box.accepted.connect(self.accept)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(button_box)
        self.setLayout(layout)


