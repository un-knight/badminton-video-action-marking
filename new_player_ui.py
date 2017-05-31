# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_palyer_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(50, 470, 91, 41))
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(370, 530, 91, 41))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setGeometry(QtCore.QRect(170, 470, 91, 41))
        self.pushButton_play.setObjectName("pushButton_play")

        # @Junxian Ye
        # op: add feature
        self.pushButton_play.setEnabled(False)

        self.pushButton_mark = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mark.setGeometry(QtCore.QRect(370, 470, 91, 41))
        self.pushButton_mark.setObjectName("pushButton_mark")
        self.radioButton_SQ = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_SQ.setGeometry(QtCore.QRect(510, 520, 89, 16))
        self.radioButton_SQ.setObjectName("radioButton_SQ")
        self.radioButton_GYQ = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_GYQ.setGeometry(QtCore.QRect(510, 480, 89, 16))
        self.radioButton_GYQ.setObjectName("radioButton_GYQ")
        self.radioButton_PC = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_PC.setGeometry(QtCore.QRect(610, 480, 89, 16))
        self.radioButton_PC.setObjectName("radioButton_PC")
        self.radioButton_PD = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_PD.setGeometry(QtCore.QRect(610, 520, 89, 16))
        self.radioButton_PD.setObjectName("radioButton_PD")
        self.radioButton_TQ = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_TQ.setGeometry(QtCore.QRect(700, 480, 89, 16))
        self.radioButton_TQ.setObjectName("radioButton_TQ")
        self.radioButton_CQ = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_CQ.setGeometry(QtCore.QRect(700, 520, 89, 16))
        self.radioButton_CQ.setObjectName("radioButton_CQ")
        self.radioButton_Other = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Other.setGeometry(QtCore.QRect(780, 480, 89, 16))
        self.radioButton_Other.setObjectName("radioButton_Other")

        # @Junxian Ye
        # op: add feautre
        self.radioButton_Hidden = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Hidden.setGeometry(QtCore.QRect(780, 520, 89, 16))
        self.radioButton_Hidden.setObjectName("radioButton_Other")
        self.radioButton_Hidden.hide()

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 430, 900, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        # @Junxian Ye
        # op: add feature
        self.horizontalSlider.setRange(0, 216000)

        self.play_window = QtWidgets.QLabel(self.centralwidget)
        self.play_window.setGeometry(QtCore.QRect(10, 10, 900, 400))
        self.play_window.setText("")
        self.play_window.setObjectName("play_window")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 923, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_load.setText(_translate("MainWindow", "加载视频"))
        self.pushButton_save.setText(_translate("MainWindow", "保存文件"))
        self.pushButton_play.setText(_translate("MainWindow", "播放"))
        self.pushButton_mark.setText(_translate("MainWindow", "标记起始帧"))
        self.radioButton_SQ.setText(_translate("MainWindow", "杀球"))
        self.radioButton_GYQ.setText(_translate("MainWindow", "高远球"))
        self.radioButton_PC.setText(_translate("MainWindow", "平抽"))
        self.radioButton_PD.setText(_translate("MainWindow", "平挡"))
        self.radioButton_TQ.setText(_translate("MainWindow", "挑球"))
        self.radioButton_CQ.setText(_translate("MainWindow", "搓球"))
        self.radioButton_Other.setText(_translate("MainWindow", "其它"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))

