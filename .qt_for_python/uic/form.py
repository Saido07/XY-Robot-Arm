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
"")
        self.camOn.setCheckable(False)
        self.sendGcode = QPushButton(self.centralwidget)
        self.sendGcode.setObjectName(u"sendGcode")
        self.sendGcode.setEnabled(True)
        self.sendGcode.setGeometry(QRect(660, 520, 201, 31))
        self.sendGcode.setFocusPolicy(Qt.StrongFocus)
        self.sendGcode.setStyleSheet(u"border-image:url(sendeGcode.png); \n"
"")
        self.infoScreen = QListWidget(self.centralwidget)
        self.infoScreen.setObjectName(u"infoScreen")
        self.infoScreen.setGeometry(QRect(1060, 50, 221, 321))
        self.infoScreen.setStyleSheet(u"background: rgb(242, 241, 241);\n"
"")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(1120, 400, 111, 31))
        font = QFont()
        font.setUnderline(True)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(u"border : none;\n"
"outline : none;")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(1120, 490, 111, 22))
        self.takePhoto = QPushButton(self.centralwidget)
        self.takePhoto.setObjectName(u"takePhoto")
        self.takePhoto.setGeometry(QRect(480, 500, 100, 100))
        sizePolicy.setHeightForWidth(self.takePhoto.sizePolicy().hasHeightForWidth())
        self.takePhoto.setSizePolicy(sizePolicy)
        self.takePhoto.setMinimumSize(QSize(100, 100))
        self.takePhoto.setStyleSheet(u"")
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
        self.plainTextEdit.setPlainText(QCoreApplication.translate("mainWin", u"Serial Port", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWin", u"COM 4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWin", u"COM 5", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("mainWin", u"COM 6", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("mainWin", u"com 7", None))

        self.takePhoto.setText("")
    # retranslateUi

