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
import numpy as np
import imutils
import serial
import time
import argparse


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setFixedSize(1000, 600)
        call=uic.loadUi('form.ui',self)
        call.camOn.clicked.connect(self.camClicked)
        call.sendGcode.connect(self.sendGClicked)
        call.camOn.setVisible(False)
        call.sendGcode.setVisible(False)

    def sendGClicked(self):
        print("sendGCodeClicked")
        parser = argparse.ArgumentParser(description='This is a basic gcode sender. http://crcibernetica.com')
        parser.add_argument('-p','--port',help='Input USB port',required=True)
        parser.add_argument('-f','--file',help='Gcode file name',required=True)
        args = parser.parse_args()
        
        ## show values ##
        print ("USB Port: %s" % args.port )
        print ("Gcode file: %s" % args.file )
        # Open serial port
        #s = serial.Serial('/dev/ttyACM0',115200)
        s = serial.Serial(args.port,9600)

        
        # Open g-code file
        #f = open('/media/UNTITLED/shoulder.g','r');
        f = open(args.file,'r')
        # Wake up 
        #s.write("\r\n\r\n") # Hit enter a few times to wake the Printrbot
        time.sleep(2)   # Wait for Printrbot to initialize
        s.flushInput()  # Flush startup text in serial input
        
        # Stream g-code
        for line in f:
            l = self.removeComment(line)
            l = l.strip() # Strip all EOL characters for streaming
            print(l)
            if  (l.isspace()==False and len(l)>0) :
                s.write((l + '\n').encode()) # Send g-code block
                print('dd')
                grbl_out = s.readline() # Wait for response with carriage return
                print(grbl_out)
        
        # Wait here until printing is finished to close serial port and file.
        input("  Press <Enter> to exit.")
        
        # Close file and serial port
        f.close()
        s.close()

    def removeComment(string):
        if (string.find(';')==-1):
            return string
        else:
            return string[:string.index(';')]


    def camClicked(self):
        print("camClicked")
        self.logic=0
        count=0
        oriImg=self.oriImage.setVisible(True)
        print("Cam ON")
        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        kernel = np.ones((5,5), np.uint8)

        while True:
           
            ret, img = cam.read()
            gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray_frame, (5,5), 0)
            canny = cv2.Canny(blur , 70, 200)
            self.oriImg.displayImage(img,1)
            self.workedImage.displayImage(canny,1)
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
            print("Die Kanten wird erkannt.")
            #cv2.drawContours(frame, [screenCnt], -1, (0, 0, 255), 4)
            frame_resized_3 = cv2.resize(img, (500, 400))
            #cv2.imshow("Die Kanten", frame_resized_3)

            #warped = four_point_transform(frame, screenCnt.reshape(4, 2))
            #warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
            #T = threshold_local(warped, 11, offset=10, method="gaussian")
            #warped = (warped > T).astype("uint8") * 255

            #cv2.imshow("Scanned", imutils.resize(warped, height=400))

            if not ret:
                break

            k=cv2.waitKey(1)

            if self.logic==2:
                print("Cam OFF")
                break                
            
            if self.logic==1:
                print("Image "+str(count)+"saved")
                file= os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+'/'+str(count)+'.png'
                cv2.imwrite(file, img)
                
                count +=1
                self.logic=2

        cam.release() 
        for i in range(1,10):
            cv2.destroyAllWindows()
            cv2.waitKey(1)
        self.imgLabel.setVisible(False)
        self.sendGcode.setVisible(True)
        self.oriImage.setVisible(True)
        self.logic=0    

        QListWidget *comPortsList = new QListWidget(); #list
        QListWidgetItem *comPort = new QListWidgetItem();  #listitem
        comPortsList->setItemWidget(comPort,new QRadioButton("Com1"));

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = main()
    widget.show()
    sys.exit(app.exec_())
