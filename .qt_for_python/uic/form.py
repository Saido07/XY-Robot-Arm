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
        mainWin.resize(1000, 600)
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
        self.oriImage.setGeometry(QRect(60, 140, 261, 211))
        self.oriImage.setMouseTracking(True)
        self.oriImage.setStyleSheet(u"background : grey\n"
"")
        self.workedImage = QLabel(self.centralwidget)
        self.workedImage.setObjectName(u"workedImage")
        self.workedImage.setGeometry(QRect(390, 140, 261, 211))
        self.workedImage.setStyleSheet(u"background : grey\n"
"")
        self.camOn = QPushButton(self.centralwidget)
        self.camOn.setObjectName(u"camOn")
        self.camOn.setEnabled(True)
        self.camOn.setGeometry(QRect(90, 380, 201, 31))
        self.camOn.setStyleSheet(u"border-image:url(camOn.png); \n"
"")
        self.camOn.setCheckable(False)
        self.sendGcode = QPushButton(self.centralwidget)
        self.sendGcode.setObjectName(u"sendGcode")
        self.sendGcode.setEnabled(False)
        self.sendGcode.setGeometry(QRect(410, 380, 201, 31))
        self.sendGcode.setStyleSheet(u"border-image:url(sendeGcode.png); \n"
"")
        self.infoScreen = QListWidget(self.centralwidget)
        self.infoScreen.setObjectName(u"infoScreen")
        self.infoScreen.setGeometry(QRect(760, 20, 221, 321))
        self.infoScreen.setStyleSheet(u"background: rgb(242, 241, 241);\n"
"")
        self.comPortsLst = QListWidget(self.centralwidget)
        self.comPortsLst.setObjectName(u"comPortsLst")
        self.comPortsLst.setGeometry(QRect(770, 360, 171, 151))
        mainWin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 20))
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
    # retranslateUi

