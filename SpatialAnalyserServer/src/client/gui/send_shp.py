# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_shp.ui'
#
# Created: Sat May 12 21:34:57 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SendSHP(object):
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

        self.retranslateUi(SendSHP)
        QtCore.QObject.connect(self.shp_clear, QtCore.SIGNAL("clicked()"), self.shp_file.clear)
        QtCore.QMetaObject.connectSlotsByName(SendSHP)

    def retranslateUi(self, SendSHP):
        SendSHP.setWindowTitle(QtGui.QApplication.translate("SendSHP", "Send SHP", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SendSHP", "File:", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_select.setText(QtGui.QApplication.translate("SendSHP", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_clear.setText(QtGui.QApplication.translate("SendSHP", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_send.setText(QtGui.QApplication.translate("SendSHP", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_cancel.setText(QtGui.QApplication.translate("SendSHP", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

