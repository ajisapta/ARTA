# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scane_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_scene_2(object):
    def setupUi(self, scene_2):
        scene_2.setObjectName("scene_2")
        scene_2.resize(1338, 768)
        scene_2.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        scene_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        scene_2.setWindowTitle("MainWindow")
        scene_2.setAutoFillBackground(False)
        scene_2.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(scene_2)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setEnabled(True)
        self.BG.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap("D:/IBE/ARTA/scene_2/BG.png"))
        self.BG.setScaledContents(True)
        self.BG.setOpenExternalLinks(False)
        self.BG.setObjectName("BG")
        self.timer = QtWidgets.QLabel(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(1170, 620, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.timer.setFont(font)
        self.timer.setObjectName("timer")
        scene_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(scene_2)
        QtCore.QMetaObject.connectSlotsByName(scene_2)

    def retranslateUi(self, scene_2):
        _translate = QtCore.QCoreApplication.translate
        self.timer.setText(_translate("scene_2", "20"))



# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# scene_2 = QtWidgets.QMainWindow()
# ui = Ui_scene_2()
# ui.setupUi(scene_2)
#
#
#
#
#
# def main_2():
#     scene_2.show()
#     from threading import Timer
#     import time
#
#     return_val = None
#
#     def timeout():
#
#         global return_val
#         return_val = True
#         return
#
#     a = False
#     t = Timer(5, timeout)
#     t.start()
#     count = 0
#     while not a:
#         time.sleep(1)
#         if return_val:
#             break
#         ui.timer.setText(str(count))
#         count += 1
#     # sys.exit(app.exec_())
# def close_2():
#     scene_2.close()
#     scene_2.destroy()
import sys
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    gui = Ui_scene_2()
    gui.setupUi(form)
    form.show()
    app.exec_()