# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_mainWin(object):
    def setupUi(self, mainWin):
        if not mainWin.objectName():
            mainWin.setObjectName(u"mainWin")
        mainWin.setEnabled(True)
        mainWin.resize(1300, 820)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWin.sizePolicy().hasHeightForWidth())
        mainWin.setSizePolicy(sizePolicy)
        mainWin.setMinimumSize(QSize(100, 100))
        mainWin.setBaseSize(QSize(100, 100))
        mainWin.setFocusPolicy(Qt.NoFocus)
        mainWin.setStyleSheet(u"background-image: url(back.png);")
        self.centralwidget = QWidget(mainWin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 800))
        self.oriImage = QLabel(self.centralwidget)
        self.oriImage.setObjectName(u"oriImage")
        self.oriImage.setGeometry(QRect(90, 50, 400, 400))
        self.oriImage.setMouseTracking(True)
        self.oriImage.setStyleSheet(u"background : grey\n"
"")
        self.workedImage = QLabel(self.centralwidget)
        self.workedImage.setObjectName(u"workedImage")
        self.workedImage.setGeometry(QRect(570, 50, 400, 400))
        self.workedImage.setStyleSheet(u"background : grey\n"
"")
        self.camOn = QPushButton(self.centralwidget)
        self.camOn.setObjectName(u"camOn")
        self.camOn.setEnabled(True)
        self.camOn.setGeometry(QRect(200, 520, 201, 31))
        self.camOn.setFocusPolicy(Qt.StrongFocus)
        self.camOn.setStyleSheet(u"border-image:url(camOn.png); \n"
"background:none;\n"
"")
        self.camOn.setCheckable(False)
        self.sendGcode = QPushButton(self.centralwidget)
        self.sendGcode.setObjectName(u"sendGcode")
        self.sendGcode.setEnabled(True)
        self.sendGcode.setGeometry(QRect(660, 520, 201, 31))
        self.sendGcode.setFocusPolicy(Qt.StrongFocus)
        self.sendGcode.setStyleSheet(u"border-image:url(sendeGcode.png); \n"
"background:none;\n"
"")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(1080, 440, 111, 22))
        self.takePhoto = QPushButton(self.centralwidget)
        self.takePhoto.setObjectName(u"takePhoto")
        self.takePhoto.setGeometry(QRect(480, 500, 100, 100))
        sizePolicy.setHeightForWidth(self.takePhoto.sizePolicy().hasHeightForWidth())
        self.takePhoto.setSizePolicy(sizePolicy)
        self.takePhoto.setMinimumSize(QSize(100, 100))
        self.takePhoto.setStyleSheet(u"")
        self.infoScreen = QLabel(self.centralwidget)
        self.infoScreen.setObjectName(u"infoScreen")
        self.infoScreen.setGeometry(QRect(1060, 52, 181, 311))
        self.infoScreen.setStyleSheet(u"background-color: rgb(242, 241, 241);\n"
"background : rgb(242, 241, 241)")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1070, 410, 171, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background: transparent")
        self.refreshPorts = QPushButton(self.centralwidget)
        self.refreshPorts.setObjectName(u"refreshPorts")
        self.refreshPorts.setGeometry(QRect(1200, 440, 22, 22))
        self.refreshPorts.setStyleSheet(u"background : none")
        self.bar1 = QSlider(self.centralwidget)
        self.bar1.setObjectName(u"bar1")
        self.bar1.setGeometry(QRect(690, 510, 221, 20))
        self.bar1.setOrientation(Qt.Horizontal)
        self.bar2 = QSlider(self.centralwidget)
        self.bar2.setObjectName(u"bar2")
        self.bar2.setGeometry(QRect(690, 570, 221, 20))
        self.bar2.setOrientation(Qt.Horizontal)
        self.t1 = QLabel(self.centralwidget)
        self.t1.setObjectName(u"t1")
        self.t1.setGeometry(QRect(610, 510, 71, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.t1.setFont(font1)
        self.t2 = QLabel(self.centralwidget)
        self.t2.setObjectName(u"t2")
        self.t2.setGeometry(QRect(610, 570, 71, 16))
        self.t2.setFont(font1)
        mainWin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1300, 20))
        mainWin.setMenuBar(self.menubar)

        self.retranslateUi(mainWin)

        QMetaObject.connectSlotsByName(mainWin)
    # setupUi

    def retranslateUi(self, mainWin):
        mainWin.setWindowTitle(QCoreApplication.translate("mainWin", u"main", None))
        self.oriImage.setText("")
        self.workedImage.setText("")
        self.camOn.setText("")
        self.sendGcode.setText("")
        self.takePhoto.setText("")
        self.infoScreen.setText(QCoreApplication.translate("mainWin", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("mainWin", u"Serial Port : ", None))
        self.refreshPorts.setText("")
        self.t1.setText(QCoreApplication.translate("mainWin", u"Threshold1 : ", None))
        self.t2.setText(QCoreApplication.translate("mainWin", u"Threshold2 : ", None))
    # retranslateUi

