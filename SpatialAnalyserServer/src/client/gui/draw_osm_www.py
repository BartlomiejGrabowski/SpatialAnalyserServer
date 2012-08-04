# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw_osm_www.ui'
#
# Created: Wed Jun 20 18:36:06 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys

sys.path.append("..")
sys.path.append("../../logger")
sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
sys.path.append("../../../interfaces/projections")

from Client import Client
import draw_osm_web_image

class Ui_DrawOSMFromWeb(Client):
    '''
    Class Ui_DrawOSMImage is class displays window to drawing osm from website. PyQT implementation.
    @author: Bartlomiej Grabowski
    @version: 1.0
    '''
        
        
    def setupUi(self, DrawOSMFromWeb):
        '''
        @brief: This function is used to setup all elements of the main window.
        @see: Ui_DrawOSMFromWeb
        @param DrawOSMFromWeb QtGui.QWidget: Input parameter is QtGui.QWidget.
        @return: This function does not return a value. 
        '''
        self.osmUrl = 'http://api.openstreetmap.org/api/0.6/map'
        DrawOSMFromWeb.setObjectName("DrawOSMFromWeb")
        DrawOSMFromWeb.resize(497, 296)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.confIconsDir+'1344069808_firefox.ico'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DrawOSMFromWeb.setWindowIcon(icon)
        self.frame = QtGui.QFrame(DrawOSMFromWeb)
        self.frame.setGeometry(QtCore.QRect(10, 10, 340, 271))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.www_label = QtGui.QLabel(self.frame)
        self.www_label.setGeometry(QtCore.QRect(10, 10, 41, 17))
        self.www_label.setObjectName("www_label")
        self.www_address_label = QtGui.QLabel(self.frame)
        self.www_address_label.setGeometry(QtCore.QRect(60, 10, 301, 17))
        self.www_address_label.setText("")
        self.www_address_label.setObjectName("www_address_label")
        self.www_address_label.setText(self.osmUrl)
        self.coordinates_label = QtGui.QLabel(self.frame)
        self.coordinates_label.setGeometry(QtCore.QRect(10, 40, 81, 17))
        self.coordinates_label.setObjectName("coordinates_label")
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 60, 301, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.minlon_label = QtGui.QLabel(self.frame)
        self.minlon_label.setGeometry(QtCore.QRect(20, 90, 62, 17))
        self.minlon_label.setObjectName("minlon_label")
        self.maxlot_label = QtGui.QLabel(self.frame)
        self.maxlot_label.setGeometry(QtCore.QRect(20, 130, 62, 17))
        self.maxlot_label.setObjectName("maxlot_label")
        self.minlat_label = QtGui.QLabel(self.frame)
        self.minlat_label.setGeometry(QtCore.QRect(20, 180, 62, 17))
        self.minlat_label.setObjectName("minlat_label")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 220, 62, 17))
        self.label.setObjectName("label")
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(20, 160, 291, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.minlon_input = QtGui.QLineEdit(self.frame)
        self.minlon_input.setGeometry(QtCore.QRect(110, 84, 113, 27))
        self.minlon_input.setObjectName("minlon_input")
        self.maxlon_input = QtGui.QLineEdit(self.frame)
        self.maxlon_input.setGeometry(QtCore.QRect(110, 126, 113, 27))
        self.maxlon_input.setObjectName("maxlon_input")
        self.minlat_input = QtGui.QLineEdit(self.frame)
        self.minlat_input.setGeometry(QtCore.QRect(110, 174, 113, 27))
        self.minlat_input.setObjectName("minlat_input")
        self.maxlat_input = QtGui.QLineEdit(self.frame)
        self.maxlat_input.setGeometry(QtCore.QRect(110, 216, 113, 27))
        self.maxlat_input.setObjectName("maxlat_input")
        self.draw_button = QtGui.QPushButton(DrawOSMFromWeb)
        self.draw_button.setGeometry(QtCore.QRect(370, 10, 91, 27))
        self.draw_button.setObjectName("draw_button")
        self.clear_button = QtGui.QPushButton(DrawOSMFromWeb)
        self.clear_button.setGeometry(QtCore.QRect(370, 50, 91, 27))
        self.clear_button.setObjectName("clear_button")
        self.cancel_button = QtGui.QPushButton(DrawOSMFromWeb)
        self.cancel_button.setGeometry(QtCore.QRect(370, 90, 91, 27))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(DrawOSMFromWeb)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL("clicked()"), DrawOSMFromWeb,  QtCore.SLOT("close()"))
        QtCore.QObject.connect(self.clear_button, QtCore.SIGNAL("clicked()"), self.clearAll)
        QtCore.QObject.connect(self.draw_button, QtCore.SIGNAL("clicked()"), self.showOSMDrawForm)
        QtCore.QMetaObject.connectSlotsByName(DrawOSMFromWeb)

    def retranslateUi(self, DrawOSMFromWeb):
        '''
        @brief: This function is used to translate Qt's items.
        @param DrawOSMFromWeb QWidget: Input parameter is QtGui.QWidget.
        @return: This function does not return a value.
        '''
        
        DrawOSMFromWeb.setWindowTitle(QtGui.QApplication.translate("DrawOSMFromWeb", "Draw OSM file from web", None, QtGui.QApplication.UnicodeUTF8))
        self.www_label.setText(QtGui.QApplication.translate("DrawOSMFromWeb", "www:", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinates_label.setText(QtGui.QApplication.translate("DrawOSMFromWeb", "coordinates:", None, QtGui.QApplication.UnicodeUTF8))
        self.minlon_label.setText(QtGui.QApplication.translate("DrawOSMFromWeb", "minlon:", None, QtGui.QApplication.UnicodeUTF8))
        self.maxlot_label.setText(QtGui.QApplication.translate("DrawOSMFromWeb", "maxlon:", None, QtGui.QApplication.UnicodeUTF8))
        self.minlat_label.setText(QtGui.QApplication.translate("DrawOSMFromWeb", "minlat:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DrawOSMFromWeb", "maxlat:", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_button.setText(QtGui.QApplication.translate("DrawOSMFromWeb", "Draw", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_button.setText(QtGui.QApplication.translate("DrawOSMFromWeb", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate("DrawOSMFromWeb", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        
    def clearAll(self):
        '''
        @brief: This function is used clear all input fields for parameters.
        @param None:
        @return: This function does not return a value.
        '''
        self.maxlat_input.clear()
        self.minlat_input.clear()
        self.maxlon_input.clear()
        self.minlon_input.clear()
        
    def showOSMDrawForm(self):
        '''
        @brief: This function is used to displays form allowing to draw osm files.
        @param None:
        @return: This function does not return a value.
        '''
        
        minlat = self.minlat_input.text()
        maxlat = self.maxlat_input.text()
        minlon = self.minlon_input.text()
        maxlon = self.maxlon_input.text()
        if minlat != '' and maxlat != '' and minlon != '' and maxlon != '':
            #Show OSM draw image form.
            self.DrawOSMImage = QtGui.QWidget()
            self.sh = draw_osm_web_image.Ui_DrawOSMImage(self.osmUrl, minlat, maxlat, minlon, maxlon)
            self.sh.setupUi(self.DrawOSMImage)
            #Show a form that allows draw image from shp file.
            self.DrawOSMImage.show()

