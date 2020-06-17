# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scane_1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import serial
import playsound
days = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]

class Ui_scene_1(object):
    def setupUi(self, scene_1):
        scene_1.setObjectName("scene_1")
        scene_1.resize(1338, 768)
        scene_1.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        scene_1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        scene_1.setWindowTitle("MainWindow")
        scene_1.setAutoFillBackground(False)
        scene_1.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(scene_1)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setEnabled(True)
        self.BG.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap("D:/IBE/ARTA/scene_1/BG_1.png"))
        self.BG.setScaledContents(True)
        self.BG.setOpenExternalLinks(False)
        self.BG.setObjectName("BG")
        self.hari = QtWidgets.QLabel(self.centralwidget)
        self.hari.setGeometry(QtCore.QRect(1050, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hari.setFont(font)
        self.hari.setObjectName("hari")
        self.koma = QtWidgets.QLabel(self.centralwidget)
        self.koma.setGeometry(QtCore.QRect(1110, 20, 25, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.koma.setFont(font)
        self.koma.setObjectName("koma")
        self.tanggal = QtWidgets.QLabel(self.centralwidget)
        self.tanggal.setGeometry(QtCore.QRect(1120, 20, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tanggal.setFont(font)
        self.tanggal.setObjectName("tanggal")
        self.strip = QtWidgets.QLabel(self.centralwidget)
        self.strip.setGeometry(QtCore.QRect(1150, 20, 10, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.strip.setFont(font)
        self.strip.setObjectName("strip")
        self.bulan = QtWidgets.QLabel(self.centralwidget)
        self.bulan.setGeometry(QtCore.QRect(1160, 20, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bulan.setFont(font)
        self.bulan.setObjectName("bulan")
        self.strip_2 = QtWidgets.QLabel(self.centralwidget)
        self.strip_2.setGeometry(QtCore.QRect(1190, 20, 10, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.strip_2.setFont(font)
        self.strip_2.setObjectName("strip_2")
        self.tahun = QtWidgets.QLabel(self.centralwidget)
        self.tahun.setGeometry(QtCore.QRect(1200, 20, 61, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tahun.setFont(font)
        self.tahun.setObjectName("tahun")
        self.strip_3 = QtWidgets.QLabel(self.centralwidget)
        self.strip_3.setEnabled(True)
        self.strip_3.setGeometry(QtCore.QRect(1248, 10, 10, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.strip_3.setFont(font)
        self.strip_3.setObjectName("strip_3")
        self.jam = QtWidgets.QLabel(self.centralwidget)
        self.jam.setGeometry(QtCore.QRect(1260, 20, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.jam.setFont(font)
        self.jam.setObjectName("jam")
        self.titik2 = QtWidgets.QLabel(self.centralwidget)
        self.titik2.setGeometry(QtCore.QRect(1285, 20, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titik2.setFont(font)
        self.titik2.setObjectName("titik2")
        self.menit = QtWidgets.QLabel(self.centralwidget)
        self.menit.setGeometry(QtCore.QRect(1295, 20, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menit.setFont(font)
        self.menit.setObjectName("menit")
        self.tekanan = QtWidgets.QLabel(self.centralwidget)
        self.tekanan.setGeometry(QtCore.QRect(1060, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.tekanan.setFont(font)
        self.tekanan.setObjectName("tekanan")
        self.bar = QtWidgets.QLabel(self.centralwidget)
        self.bar.setGeometry(QtCore.QRect(1140, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.bar.setFont(font)
        self.bar.setObjectName("bar")
        self.derajat = QtWidgets.QLabel(self.centralwidget)
        self.derajat.setGeometry(QtCore.QRect(1220, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.derajat.setFont(font)
        self.derajat.setObjectName("derajat")
        self.o_derajat = QtWidgets.QLabel(self.centralwidget)
        self.o_derajat.setGeometry(QtCore.QRect(1265, 50, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.o_derajat.setFont(font)
        self.o_derajat.setObjectName("o_derajat")
        self.celcius = QtWidgets.QLabel(self.centralwidget)
        self.celcius.setGeometry(QtCore.QRect(1280, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.celcius.setFont(font)
        self.celcius.setObjectName("celcius")
        scene_1.setCentralWidget(self.centralwidget)

        x = datetime.datetime.now()


        def cek(value):
            if value < 10:
                value = "0" + str(value)
            else:
                value = str(value)
            return value

        time = QtCore.QTime.currentTime()
        self.hari.setText(days[x.weekday()])
        self.bulan.setText(cek(x.month))
        self.tahun.setText(cek(x.year))
        self.tanggal.setText(cek(x.day))

        self.jam.setText(cek(time.hour()))
        self.menit.setText(cek(time.minute()))


        self.retranslateUi(scene_1)
        QtCore.QMetaObject.connectSlotsByName(scene_1)
        self.lblHidden = False
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.flashLbl)
        self.timer.start(1000)

    def flashLbl(self):
        if self.lblHidden == False:
            self.titik2.hide()
            self.lblHidden = True
        else:
            self.titik2.show()
            self.lblHidden = False

    def retranslateUi(self, scene_1):
        _translate = QtCore.QCoreApplication.translate
        # self.hari.setText(_translate("scene_1", "Jumat"))
        self.koma.setText(_translate("scene_1", ","))
        # self.tanggal.setText(_translate("scene_1", "17"))
        self.strip.setText(_translate("scene_1", "-"))
        # self.bulan.setText(_translate("scene_1", "12"))
        self.strip_2.setText(_translate("scene_1", "-"))
        # self.tahun.setText(_translate("scene_1", "2020"))
        self.strip_3.setText(_translate("scene_1", "|"))
        # self.jam.setText(_translate("scene_1", "24"))
        self.titik2.setText(_translate("scene_1", ":"))
        # self.menit.setText(_translate("scene_1", "59"))
        self.tekanan.setText(_translate("scene_1", "0.29"))
        self.bar.setText(_translate("scene_1", "bar"))
        self.derajat.setText(_translate("scene_1", "20"))
        self.o_derajat.setText(_translate("scene_1", "o"))
        self.celcius.setText(_translate("scene_1", "C"))
class Sensor(object):
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
    def Read(self):
        print("Ceeek")
        portname = self.port
        baud = self.baudrate
        ard = serial.Serial(portname, baud, timeout=2)  # deklarasi port komunikasi serial
        ard.write(b't')  # kirim perintah ke arduino
        msg = ard.readline()  # baca data serial dari arduino
        # data = msg.split(',')
        # print (len(msg))
        if (len(msg) > 5):  # jika panjang karakter data > 5
            global dis, temp, hum
            strmsg = str(msg)  # ini data dari serial yg sudah string
            data = strmsg.split(',')  # karena formatnya "data1,data2,data3", maka dipisah berdasar tanda koma
            dis = int(data[2].replace("\\r\\n'", ""))  # biar cuma tinggal angkanya
            temp = data[1]  # sudah tinggal angka
            hum = data[0].replace("b'", "")  # biar cuma tinggal angkanya
            print(data)

            if (dis < 150):
                playsound('Rekaman ARTA\Slide 1 - Introduction ARTA.mp3')
                # playsound('Rekaman ARTA\Slide 2 (Sebelum Memulai).mp3')
                ard.close()
                form.destroy()
                import scane_2.main



import sys
import datetime
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    gui = Ui_scene_1()
    gui.setupUi(form)

    form.show()
    sensor = Sensor(port='com10')
    sensor.Read()

    form.update()
    app.exec_()
