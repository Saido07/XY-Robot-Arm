# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from PyQt5 import QtGui, QtWidgets, uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import  QWidget, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile
from PyQt5 import QtWidgets, uic
import cv2
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setFixedSize(1000, 600)
        call=uic.loadUi('form.ui',self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = main()
    widget.show()
    sys.exit(app.exec_())
