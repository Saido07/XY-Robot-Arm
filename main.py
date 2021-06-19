# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from typing import overload

from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import __init__
import gOut
import gRead
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
import numpy as np
import serial
import time
import argparse
import serial.tools.list_ports
import winreg
import utlis
import itertools
from skimage.filters import threshold_local
from imutils.perspective import four_point_transform


class main(QMainWindow):
    Port=" "
    def __init__(self):
        super(main, self).__init__()
        self.setFixedSize(1300, 650)
        call=uic.loadUi('form.ui',self)
        call.camOn.clicked.connect(self.camClicked)
        call.sendGcode.clicked.connect(self.sendGClicked)
        call.takePhoto.clicked.connect(self.takePhotoClicked)
        call.refreshPorts.clicked.connect(self.refreshPortClicked)
        self.infoScreen.setText("--")
        self.infoScreen.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.infoScreen.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.infoScreen.setWordWrap(True)
        self.camOn.setVisible(True)
        self.sendGcode.setVisible(True)
        self.takePhoto.setVisible(False)
        self.bar1.setVisible(False)
        self.bar2.setVisible(False)
        self.t1.setVisible(False)
        self.t2.setVisible(False)
        self.bar1.setStyleSheet("background:transparent")
        self.bar2.setStyleSheet("background:transparent")
        self.t1.setStyleSheet("background:transparent")
        self.t2.setStyleSheet("background:transparent")
        image = QIcon("camera.png")         
        call.takePhoto.setIcon(image)
        size = QSize(100, 100)
        call.takePhoto.setIconSize(size)
        call.takePhoto.setStyleSheet("background:transparent")
        imageRefresh = QIcon("reload.png")         
        call.refreshPorts.setIcon(imageRefresh)
        sizeRefresh = QSize(6,6)
        call.refreshPorts.setIconSize(size)
        call.refreshPorts.setStyleSheet("background:transparent")
        self.serial_ports()
        self.refreshPortClicked()

    def refreshPortClicked(self):
        self.serial_ports()
        self.Port=self.comboBox.currentText()

    def serial_ports(self) -> list:
        self.comboBox.clear()
        path = 'HARDWARE\DEVICEMAP\SERIALCOMM'
        

        ports = []

        for i in itertools.count():
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
                ports.append(winreg.EnumValue(key, i)[1])
                self.comboBox.addItem(winreg.EnumValue(key, i)[1])
            except EnvironmentError:
                break
        # print(ports)
        return ports


    def removeComment(self, string):
        if (string.find(';')==-1):
            return string
        else:
            return string[:string.index(';')]
    
    def camClicked(self):
        print("camClicked")
        self.infoScreen.setText(self.infoScreen.text()+"\n--Die Kamera war eingeschaltet.")  
        self.logic=0
        self.bar1.setMaximum(255)
        self.bar1.setMinimum(0)
        self.bar2.setMaximum(255)
        self.bar2.setMinimum(0)
        self.bar2.setValue(200)
        self.bar1.setValue(200)
        count = 0
        self.oriImage.setVisible(True)
        self.workedImage.setVisible(True)
        self.camOn.setVisible(False)
        self.sendGcode.setVisible(False)
        self.takePhoto.setVisible(True)
        self.bar1.setVisible(True)
        self.bar2.setVisible(True)
        self.t1.setVisible(True)
        self.t2.setVisible(True)
        print("Cam ON")
        widthImg = 400
        heightImg = 400
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cap.set(10, 160)
        
        kernel = np.ones((5,5), np.uint8)

        while True:
            success, img = cap.read()
            img = cv2.resize(img, (widthImg, heightImg))  # RESIZE IMAGE
            imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)  # CREATE A BLANK IMAGE FOR TESTING DEBUGING IF REQUIRED
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # CONVERT IMAGE TO GRAY SCALE
            imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # ADD GAUSSIAN BLUR
            imgThreshold = cv2.Canny(imgBlur, self.bar1.value(), self.bar2.value())  # APPLY CANNY BLUR
            kernel = np.ones((5, 5))
            imgDial = cv2.dilate(imgThreshold, kernel, iterations=2)  # APPLY DILATION
            imgThreshold = cv2.erode(imgDial, kernel, iterations=1)  # APPLY EROSION
            imgWarpColored=None

            ## FIND ALL COUNTOURS
            imgContours = img.copy()  # COPY IMAGE FOR DISPLAY PURPOSES
            imgBigContour = img.copy()  # COPY IMAGE FOR DISPLAY PURPOSES
            contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)  # FIND ALL CONTOURS
            cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)  # DRAW ALL DETECTED CONTOURS

            # FIND THE BIGGEST COUNTOUR
            biggest, maxArea = utlis.biggestContour(contours)  # FIND THE BIGGEST CONTOUR
            if biggest.size != 0:
                biggest = utlis.reorder(biggest)
                cv2.drawContours(imgBigContour, biggest, -1, (0, 255, 0), 20)  # DRAW THE BIGGEST CONTOUR
                imgBigContour = utlis.drawRectangle(imgBigContour, biggest, 2)
                pts1 = np.float32(biggest)  # PREPARE POINTS FOR WARP
                pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])  # PREPARE POINTS FOR WARP
                matrix = cv2.getPerspectiveTransform(pts1, pts2)
                imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

                # REMOVE 20 PIXELS FORM EACH SIDE
                imgWarpColored = imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
                imgWarpColored = cv2.resize(imgWarpColored, (widthImg, heightImg))

                # APPLY ADAPTIVE THRESHOLD
                imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
                imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
                imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
                imgAdaptiveThre = cv2.medianBlur(imgAdaptiveThre, 3)

                # Image Array for Display
                imageArray = ([imgContours])
                imageArray2 = ([imgWarpColored])

            else:
                imageArray = ([imgContours])
                imageArray2= ([imgBlank])

            # LABELS FOR DISPLAY
            lables = [["Original", "Gray", "Threshold", "Contours"],
                    ["Biggest Contour", "Warp Prespective", "Warp Gray", "Adaptive Threshold"]]

            stackedImage = utlis.stackImages(imageArray, 1)
            stackedImage2 = utlis.stackImages(imageArray2, 1)
            #cv2.imshow("Result", stackedImage)
            self.displayImage(self.oriImage,stackedImage[:400],1)
            self.displayImage(self.workedImage,stackedImage2[:400],1)
            #self.displayImage(self.oriImage,ori,1)

            if not success:
                break

        
            if self.logic==2:
                print("Cam OFF")
                self.camOn.setVisible(True)
                self.sendGcode.setVisible(True)
                self.takePhoto.setVisible(False)
                self.bar1.setVisible(False)
                self.bar2.setVisible(False)
                self.t1.setVisible(False)
                self.t2.setVisible(False)
                break 

            # SAVE IMAGE WHEN 's' key is pressed
            if cv2.waitKey(1) & self.logic==1:
                try:
                    cv2.imwrite("Scanned/myImage.png", imgWarpColored)
                    cv2.rectangle(stackedImage, ((int(stackedImage.shape[1] / 2) - 230), int(stackedImage.shape[0] / 2) + 50),
                                (1100, 350), (0, 255, 0), cv2.FILLED)
                    cv2.putText(stackedImage, "Scan Saved", (int(stackedImage.shape[1] / 2) - 200, int(stackedImage.shape[0] / 2)),
                                cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 5, cv2.LINE_AA)
                    self.infoScreen.setText(self.infoScreen.text()+"\n--Das Foto wurde gemacht.")
                    #cv2.imshow('Result', stackedImage)
                    cv2.waitKey(300)

                    if os.path.isfile("Scanned/myImage.png"):
                        paths = gRead.imToPaths("Scanned/myImage.png")
                        outfile = "Scanned/myImage.gcode"
                        gOut.toTextFile(outfile, paths)
                        self.infoScreen.setText(self.infoScreen.text()+"\n--G-Code wurde erstellt.") 
                    count += 1
                except:
                    self.infoScreen.setText(self.infoScreen.text()+"\n--Das Dokument konnte nicht bestimmt werden.")
                    self.infoScreen.setText(self.infoScreen.text()+"\n--Bitte versuche es erneut!")
                self.logic=2
        cap.release() 
        for i in range(1,10):
            cv2.destroyAllWindows()
            cv2.waitKey(1)
        #self.imgLabel.setVisible(False)
        self.sendGcode.setVisible(True)
        self.oriImage.setVisible(True)
        self.logic=0 
    
    def displayImage(self,lbl, img,window=1):
        qformat=QImage.Format_Indexed8

        if len(img.shape)==3:
            if(img.shape[2])==4:
                qformat=QImage.Format_RGBA8888

            else:
                qformat=QImage.Format_RGB888

        img=QImage(img,img.shape[1],img.shape[0],qformat)
        img=img.rgbSwapped()
        lbl.setPixmap(QPixmap.fromImage(img))
        lbl.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


    def takePhotoClicked(self):
        self.logic=1

    def sendGClicked(self):
        self.infoScreen.setText(self.infoScreen.text()+"\n--Der G-Code-Sendevorgang wurde gestartet und Druckvorgang wurde gestartet.\n--\n--\n--")
        self.Port=self.comboBox.currentText()
        self.sendG(self.Port.lower(), "Scanned\myImage.gcode")

    
    def sendG(self, com, file):
        print("sendGCodeClicked")
        print("COM : " , com)
        parser = argparse.ArgumentParser(description='This is a basic gcode sender. http://crcibernetica.com')
        #parser.add_argument('-p','--port',help='Input USB port',required=True)
        #parser.add_argument('-f','--file',help='Gcode file name',required=True)
        args = parser.parse_args()
        args.port=com
        args.file=file
        ## show values ##
        self.infoScreen.setText(self.infoScreen.text()+"\n--USB Port: %s" % args.port)
        self.infoScreen.setText(self.infoScreen.text()+"\n--Gcode file: %s" % args.file)
        print ("USB Port: %s" % args.port )
        print ("Gcode file: %s" % args.file )
        # Open serial port
        #s = serial.Serial('/dev/ttyACM0',115200)
        try:
            s = serial.Serial(args.port, 115200)
            # Open g-code file
            #f = open('/media/UNTITLED/shoulder.g','r');
            try:
                f = open(args.file,'r')
                time.sleep(2)   # Wait for Printrbot to initialize
                s.flushInput()  # Flush startup text in serial input
                a=True
                for line in f:
                    l = self.removeComment(line)
                    l = l.strip() # Strip all EOL characters for streaming
                    if a==True:
                        self.infoScreen.setText(self.infoScreen.text()+"\n--Druckvorgang wurde gestartet.")
                        a=False
                    print(l)
                    if  (l.isspace()==False and len(l)>0) :
                        s.write((l + '\n').encode()) # Send g-code block
                        grbl_out = s.readline() # Wait for response with carriage return
                        print(grbl_out)
                self.infoScreen.setText(self.infoScreen.text()+"\n--Druckvorgang ist fertig.")   
                # Close file and serial port
                f.close()
                s.close()
            except:
                self.infoScreen.setText(self.infoScreen.text()+"\n--Das G-Code-Verzeichnis ist falsch oder der es wurde nicht gefunden.")   
                print("--Das G-Code-Verzeichnis ist falsch oder der es wurde nicht gefunden.")
        except:
            self.infoScreen.setText(self.infoScreen.text()+"\n--Der Zeichenroboter ist nicht angeschlossen oder es ist an den falschen Anschluss angeschlossen.")  
            print("arduino bağlanmadı ya da arduino yanlış porta bağlı.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = main()
    widget.show()
    sys.exit(app.exec_())
    