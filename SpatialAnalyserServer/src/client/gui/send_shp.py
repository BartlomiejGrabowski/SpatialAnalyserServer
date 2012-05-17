# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_shp.ui'
#
# Created: Sat May 12 21:34:57 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
from PyKDE4.kdeui import KLed
sys.path.append("..")
sys.path.append("../../logger")
sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
from Client import Client


class Ui_SendSHP(Client):
    def setupUi(self, SendSHP):
        SendSHP.setObjectName("SendSHP")
        SendSHP.resize(407, 202)
        self.shp_file = QtGui.QLineEdit(SendSHP)
        self.shp_file.setGeometry(QtCore.QRect(20, 60, 251, 27))
        self.shp_file.setObjectName("shp_file")
        self.label = QtGui.QLabel(SendSHP)
        self.label.setGeometry(QtCore.QRect(20, 30, 62, 17))
        self.label.setObjectName("label")
        self.widget = QtGui.QWidget(SendSHP)
        self.widget.setGeometry(QtCore.QRect(300, 10, 95, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shp_select = QtGui.QPushButton(self.widget)
        self.shp_select.setObjectName("shp_select")
        self.verticalLayout.addWidget(self.shp_select)
        self.shp_clear = QtGui.QPushButton(self.widget)
        self.shp_clear.setObjectName("shp_clear")
        self.verticalLayout.addWidget(self.shp_clear)
        self.shp_send = QtGui.QPushButton(self.widget)
        self.shp_send.setObjectName("shp_send")
        self.verticalLayout.addWidget(self.shp_send)
        self.shp_cancel = QtGui.QPushButton(self.widget)
        self.shp_cancel.setObjectName("shp_cancel")
        self.verticalLayout.addWidget(self.shp_cancel)
        self.status_led = KLed(SendSHP)
        self.status_led.setGeometry(QtCore.QRect(70, 180, 16, 16))
        self.status_led.setObjectName("status_led")
        self.shp_status = QtGui.QLabel(SendSHP)
        self.shp_status.setGeometry(QtCore.QRect(20, 180, 51, 17))
        self.shp_status.setObjectName("shp_status")
        self.status_led.setVisible(False)
        self.error_label = QtGui.QLabel(SendSHP)
        self.error_label.setGeometry(QtCore.QRect(20, 90, 251, 17))
        font = QtGui.QFont()
        font.setFamily("gargi")
        self.error_label.setFont(font)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        
        self.retranslateUi(SendSHP)
        QtCore.QObject.connect(self.shp_clear, QtCore.SIGNAL("clicked()"), self.shp_file.clear)
        QtCore.QObject.connect(self.shp_select, QtCore.SIGNAL("clicked()"), self.selectSHP)
        QtCore.QObject.connect(self.shp_cancel, QtCore.SIGNAL("clicked()"), SendSHP,  QtCore.SLOT("close()"))
        QtCore.QObject.connect(self.shp_send, QtCore.SIGNAL("clicked()"), self.gui_client_send_shp_to_postgres)
        QtCore.QMetaObject.connectSlotsByName(SendSHP)
  
    def retranslateUi(self, SendSHP):
        SendSHP.setWindowTitle(QtGui.QApplication.translate("SendSHP", "Send SHP", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SendSHP", "File:", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_select.setText(QtGui.QApplication.translate("SendSHP", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_clear.setText(QtGui.QApplication.translate("SendSHP", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_send.setText(QtGui.QApplication.translate("SendSHP", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_cancel.setText(QtGui.QApplication.translate("SendSHP", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_status.setText(QtGui.QApplication.translate("SendSHP", "Status", None, QtGui.QApplication.UnicodeUTF8))

    def selectSHP(self):       
        fname = QtGui.QFileDialog.getOpenFileName(QtGui.QWidget(), 'Open')
        self.shp_file.setText(fname)
        
    def gui_client_send_shp_to_postgres(self):
        self.fName = self.shp_file.text()
        if self.fName == '':
            self.error_label.setText('First select the .shp file.')
        else: 
            self.ret_code = self.client_send_shp_to_postgres(self.fName)
            if self.ret_code == 0:
                self.status_led.setVisible(True)
    
