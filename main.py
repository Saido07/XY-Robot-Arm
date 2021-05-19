# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from typing import overload

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
import numpy as np
import imutils
import serial
import time
import argparse
import serial.tools.list_ports
import winreg
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
        self.Port=self.comboBox.currentText()

    def refreshPortClicked(self):
        self.serial_ports()
        self.Port=self.comboBox.currentText()

    def serial_ports(self) -> list:
        self.comboBox.clear()
        path = 'HARDWARE\DEVICEMAP\SERIALCOMM'
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)

        ports = []

        for i in itertools.count():
            try:
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
        count=0
        self.oriImage.setVisible(True)
        self.workedImage.setVisible(True)
        self.camOn.setVisible(False)
        self.sendGcode.setVisible(False)
        self.takePhoto.setVisible(True)
        print("Cam ON")
        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        kernel = np.ones((5,5), np.uint8)

        while True:
           
            ret, img = cam.read()
            gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray_frame, (5,5), 0)
            canny = cv2.Canny(blur , 70, 200)
            cv2.waitKey()

            cnts = cv2.findContours(canny.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

            for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.03 * peri, True)
                if len(approx) == 4:
                    screenCnt = approx
                    break
            normal=-1
            k=cv2.waitKey(1)
            ori=cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 4)
            try:
                self.displayImage(self.oriImage,ori,1)
                #cv2.imshow("Die Kanten", frame_resized_3)
                warped = four_point_transform(img, screenCnt.reshape(4, 2))
                warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
                T = threshold_local(warped, 11, offset=10, method="gaussian")
                warped = (warped > T).astype("uint8") * 255
                self.displayImage(self.workedImage,warped,1)
                normal=0
            except:
                self.displayImage(self.oriImage,img,1)
                self.displayImage(self.workedImage,canny,1)
                normal=1

            if not ret:
                break


            if self.logic==2:
                print("Cam OFF")
                self.camOn.setVisible(True)
                self.sendGcode.setVisible(True)
                self.takePhoto.setVisible(False)
                break                
            
            if self.logic==1:
                self.infoScreen.setText(self.infoScreen.text()+"\n--Das Foto wurde gemacht.") 
                if normal==0:
                    cv2.imwrite('myImage.png',warped)
                    self.displayImage(self.oriImage,cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 4),1)
                    self.displayImage(self.workedImage,cv2.imread('myImage.png'),1)
                elif normal==1:
                    cv2.imwrite('myImage.png',canny)
                    self.displayImage(self.oriImage,img,1)
                    self.displayImage(self.workedImage,cv2.imread('myImage.png'),1)
                self.logic=2
                normal=-1

        cam.release() 
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
        self.sendG(self.Port.lower(), "gCodes\deneme.g")
        self.infoScreen.setText(self.infoScreen.text()+"\n--Der G-Code-Sendevorgang wurde gestartet und Druckvorgang wurde gestartet.\n--\n--\n--")
    
    def sendG(self, com, file):
        print("sendGCodeClicked")
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
            s = serial.Serial(args.port,9600)
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