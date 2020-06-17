
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtCore import pyqtSignal, QObject
# import threading
# import time
# from threading import Thread
#
# class Ui_scene_1(object):
#     def setupUi(self, scene_1):
#         scene_1.setObjectName("scene_1")
#         scene_1.resize(1338, 768)
#         scene_1.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
#         scene_1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
#         scene_1.setWindowTitle("MainWindow")
#         scene_1.setAutoFillBackground(False)
#         scene_1.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
#         self.centralwidget = QtWidgets.QWidget(scene_1)
#         self.centralwidget.setEnabled(True)
#         self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
#         self.centralwidget.setObjectName("centralwidget")
#         self.BG = QtWidgets.QLabel(self.centralwidget)
#         self.BG.setEnabled(True)
#         self.BG.setGeometry(QtCore.QRect(0, 0, 1366, 768))
#         self.BG.setText("")
#         self.BG.setPixmap(QtGui.QPixmap("D:/IBE/ARTA/scene_1/BG_1.png"))
#         self.BG.setScaledContents(True)
#         self.BG.setOpenExternalLinks(False)
#         self.BG.setObjectName("BG")
#         self.hari = QtWidgets.QLabel(self.centralwidget)
#         self.hari.setGeometry(QtCore.QRect(1050, 20, 100, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.hari.setFont(font)
#         self.hari.setObjectName("hari")
#         self.koma = QtWidgets.QLabel(self.centralwidget)
#         self.koma.setGeometry(QtCore.QRect(1110, 20, 25, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.koma.setFont(font)
#         self.koma.setObjectName("koma")
#         self.tanggal = QtWidgets.QLabel(self.centralwidget)
#         self.tanggal.setGeometry(QtCore.QRect(1120, 20, 30, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.tanggal.setFont(font)
#         self.tanggal.setObjectName("tanggal")
#         self.strip = QtWidgets.QLabel(self.centralwidget)
#         self.strip.setGeometry(QtCore.QRect(1150, 20, 10, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.strip.setFont(font)
#         self.strip.setObjectName("strip")
#         self.bulan = QtWidgets.QLabel(self.centralwidget)
#         self.bulan.setGeometry(QtCore.QRect(1160, 20, 30, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.bulan.setFont(font)
#         self.bulan.setObjectName("bulan")
#         self.strip_2 = QtWidgets.QLabel(self.centralwidget)
#         self.strip_2.setGeometry(QtCore.QRect(1190, 20, 10, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.strip_2.setFont(font)
#         self.strip_2.setObjectName("strip_2")
#         self.tahun = QtWidgets.QLabel(self.centralwidget)
#         self.tahun.setGeometry(QtCore.QRect(1200, 20, 61, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.tahun.setFont(font)
#         self.tahun.setObjectName("tahun")
#         self.strip_3 = QtWidgets.QLabel(self.centralwidget)
#         self.strip_3.setEnabled(True)
#         self.strip_3.setGeometry(QtCore.QRect(1248, 10, 10, 40))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         self.strip_3.setFont(font)
#         self.strip_3.setObjectName("strip_3")
#         self.jam = QtWidgets.QLabel(self.centralwidget)
#         self.jam.setGeometry(QtCore.QRect(1260, 20, 30, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.jam.setFont(font)
#         self.jam.setObjectName("jam")
#         self.titik2 = QtWidgets.QLabel(self.centralwidget)
#         self.titik2.setGeometry(QtCore.QRect(1285, 20, 20, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.titik2.setFont(font)
#         self.titik2.setObjectName("titik2")
#         self.menit = QtWidgets.QLabel(self.centralwidget)
#         self.menit.setGeometry(QtCore.QRect(1295, 20, 30, 30))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.menit.setFont(font)
#         self.menit.setObjectName("menit")
#         self.tekanan = QtWidgets.QLabel(self.centralwidget)
#         self.tekanan.setGeometry(QtCore.QRect(1060, 60, 91, 41))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(22)
#         font.setBold(True)
#         font.setWeight(75)
#         self.tekanan.setFont(font)
#         self.tekanan.setObjectName("tekanan")
#         self.bar = QtWidgets.QLabel(self.centralwidget)
#         self.bar.setGeometry(QtCore.QRect(1140, 60, 61, 41))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(22)
#         font.setBold(True)
#         font.setWeight(75)
#         self.bar.setFont(font)
#         self.bar.setObjectName("bar")
#         self.derajat = QtWidgets.QLabel(self.centralwidget)
#         self.derajat.setGeometry(QtCore.QRect(1220, 60, 51, 41))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(22)
#         font.setBold(True)
#         font.setWeight(75)
#         self.derajat.setFont(font)
#         self.derajat.setObjectName("derajat")
#         self.o_derajat = QtWidgets.QLabel(self.centralwidget)
#         self.o_derajat.setGeometry(QtCore.QRect(1265, 50, 21, 31))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(10)
#         font.setBold(True)
#         font.setWeight(75)
#         self.o_derajat.setFont(font)
#         self.o_derajat.setObjectName("o_derajat")
#         self.celcius = QtWidgets.QLabel(self.centralwidget)
#         self.celcius.setGeometry(QtCore.QRect(1280, 60, 51, 41))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(22)
#         font.setBold(True)
#         font.setWeight(75)
#         self.celcius.setFont(font)
#         self.celcius.setObjectName("celcius")
#         self.next = QtWidgets.QPushButton(self.centralwidget)
#         self.next.setGeometry(QtCore.QRect(750, 350, 93, 28))
#         self.next.setObjectName("next")
#         # self.next.hide()
#         scene_1.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(scene_1)
#         QtCore.QMetaObject.connectSlotsByName(scene_1)
#
#     def retranslateUi(self, scene_1):
#         _translate = QtCore.QCoreApplication.translate
#         self.hari.setText(_translate("scene_1", "Jumat"))
#         self.koma.setText(_translate("scene_1", ","))
#         self.tanggal.setText(_translate("scene_1", "17"))
#         self.strip.setText(_translate("scene_1", "-"))
#         self.bulan.setText(_translate("scene_1", "12"))
#         self.strip_2.setText(_translate("scene_1", "-"))
#         self.tahun.setText(_translate("scene_1", "2020"))
#         self.strip_3.setText(_translate("scene_1", "|"))
#         self.jam.setText(_translate("scene_1", "24"))
#         self.titik2.setText(_translate("scene_1", ":"))
#         self.menit.setText(_translate("scene_1", "59"))
#         self.tekanan.setText(_translate("scene_1", "0.29"))
#         self.bar.setText(_translate("scene_1", "bar"))
#         self.derajat.setText(_translate("scene_1", "20"))
#         self.o_derajat.setText(_translate("scene_1", "o"))
#         self.celcius.setText(_translate("scene_1", "C"))
#         self.next.setText(_translate("scene_1", "Next"))
# class Ui_scene_2(object):
#     def setupUi(self, scene_2):
#         scene_2.setObjectName("scene_2")
#         scene_2.resize(1338, 768)
#         scene_2.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
#         scene_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
#         scene_2.setWindowTitle("MainWindow")
#         scene_2.setAutoFillBackground(False)
#         scene_2.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
#         self.centralwidget = QtWidgets.QWidget(scene_2)
#         self.centralwidget.setEnabled(True)
#         self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
#         self.centralwidget.setObjectName("centralwidget")
#         self.BG = QtWidgets.QLabel(self.centralwidget)
#         self.BG.setEnabled(True)
#         self.BG.setGeometry(QtCore.QRect(0, 0, 1366, 768))
#         self.BG.setText("")
#         self.BG.setPixmap(QtGui.QPixmap("D:/IBE/ARTA/scene_2/BG.png"))
#         self.BG.setScaledContents(True)
#         self.BG.setOpenExternalLinks(False)
#         self.BG.setObjectName("BG")
#         self.timer = QtWidgets.QLabel(self.centralwidget)
#         self.timer.setGeometry(QtCore.QRect(1170, 620, 51, 61))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(22)
#         font.setBold(True)
#         font.setWeight(75)
#         self.timer.setFont(font)
#         self.timer.setObjectName("timer")
#         scene_2.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(scene_2)
#         QtCore.QMetaObject.connectSlotsByName(scene_2)
#
#     def retranslateUi(self, scene_2):
#         _translate = QtCore.QCoreApplication.translate
#         self.timer.setText(_translate("scene_2", "20"))
# import sys
# import datetime
#
#
# class ThreadingExample(object):
#     """ Threading example class
#     The run() method will be started and it will run in the background
#     until the application exits.
#     """
#
#     def __init__(self, interval=1):
#         """ Constructor
#         :type interval: int
#         :param interval: Check interval, in seconds
#         """
#         self.interval = interval
#
#         thread = threading.Thread(target=self.run, args=())
#         thread.daemon = True                            # Daemonize thread
#         thread.start()                                  # Start the execution
#
#     def run(self):
#         """ Method that runs forever """
#         while True:
#             # Do something
#             print('Doing something imporant in the background')
#
#             time.sleep(self.interval)
# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.ui_scene_1 = Ui_scene_1()
#         self.ui_scene_2 = Ui_scene_2()
#         thread1 = Thread(target = self.startUI_Scene_1())
#
#         thread1.start()
#         time.sleep(6)
#         thread1.join()
#         thread2 = Thread(target=self.startUI_Scene_2())
#         thread2.start()
#         thread2.join()
#
#     def startUI_Scene_1(self):
#         self.ui_scene_1.setupUi(self)
#         x = datetime.datetime.now()
#
#         def cek(value):
#             if value < 10:
#                 value = "0" + str(value)
#             else:
#                 value = str(value)
#             return value
#         self.ui_scene_1.next.clicked.connect(self.startUI_Scene_2)
#         self.ui_scene_1.bulan.setText(cek(x.month))
#         self.ui_scene_1.tahun.setText(cek(x.year))
#         self.ui_scene_1.tanggal.setText(cek(x.day))
#         self.ui_scene_1.jam.setText(cek(x.hour))
#         self.ui_scene_1.menit.setText(cek(x.minute))
#         self.show()
#         # self.startUI_Scene_2()
#
#
#     def closeUI_Scene_1(self):
#         self.ui_scene_1.setupUi(self)
#         self.close()
#         self.startUI_Scene_2()
#
#
#
#
#
#
#     def startUI_Scene_2(self):
#         self.ui_scene_2.setupUi(self)
#         self.show()
#
# if __name__ == '__main__':
#
#     app = QtWidgets.QApplication(sys.argv)
#     w = MainWindow()
#
#     sys.exit(app.exec_())

from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import scane_1
import scane_2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal, QObject
import threading
import time
from threading import Thread


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    gui = scane_1.Ui_scene_1()
    gui.setupUi(form)

    form.show()

    app.exec_()
    time.sleep(4)
    form.update()
    gui = scane_2.Ui_scene_2()
    gui.setupUi(form)
    form.show()