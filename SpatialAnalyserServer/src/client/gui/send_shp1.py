# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_shp.ui'
#
# Created: Sun Aug 26 10:52:30 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SendSHP(object):
    def setupUi(self, SendSHP):
        SendSHP.setObjectName("SendSHP")
        SendSHP.resize(407, 393)
        self.shp_file = QtGui.QLineEdit(SendSHP)
        self.shp_file.setGeometry(QtCore.QRect(20, 120, 251, 27))
        self.shp_file.setObjectName("shp_file")
        self.label = QtGui.QLabel(SendSHP)
        self.label.setGeometry(QtCore.QRect(20, 90, 62, 17))
        self.label.setObjectName("label")
        self.layoutWidget = QtGui.QWidget(SendSHP)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 10, 95, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shp_select = QtGui.QPushButton(self.layoutWidget)
        self.shp_select.setObjectName("shp_select")
        self.verticalLayout.addWidget(self.shp_select)
        self.shp_clear = QtGui.QPushButton(self.layoutWidget)
        self.shp_clear.setObjectName("shp_clear")
        self.verticalLayout.addWidget(self.shp_clear)
        self.shp_send = QtGui.QPushButton(self.layoutWidget)
        self.shp_send.setObjectName("shp_send")
        self.verticalLayout.addWidget(self.shp_send)
        self.shp_cancel = QtGui.QPushButton(self.layoutWidget)
        self.shp_cancel.setObjectName("shp_cancel")
        self.verticalLayout.addWidget(self.shp_cancel)
        self.status_led = KLed(SendSHP)
        self.status_led.setGeometry(QtCore.QRect(70, 370, 16, 16))
        self.status_led.setState(QtGui.KLed.Off)
        self.status_led.setShape(QtGui.KLed.Circular)
        self.status_led.setLook(QtGui.KLed.Raised)
        self.status_led.setObjectName("status_led")
        self.shp_status = QtGui.QLabel(SendSHP)
        self.shp_status.setGeometry(QtCore.QRect(20, 370, 50, 17))
        self.shp_status.setObjectName("shp_status")
        self.error_label = QtGui.QLabel(SendSHP)
        self.error_label.setGeometry(QtCore.QRect(20, 150, 251, 17))
        font = QtGui.QFont()
        font.setFamily("gargi")
        self.error_label.setFont(font)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.frame = QtGui.QFrame(SendSHP)
        self.frame.setGeometry(QtCore.QRect(20, 200, 251, 146))
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setBold(False)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 22, 251, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(60, 0, 20, 151))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 62, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 40, 62, 17))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtGui.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.file_info = QtGui.QLabel(self.frame)
        self.file_info.setGeometry(QtCore.QRect(60, 10, 191, 17))
        self.file_info.setText("")
        self.file_info.setObjectName("file_info")
        self.table_info = QtGui.QLabel(self.frame)
        self.table_info.setGeometry(QtCore.QRect(60, 30, 191, 17))
        self.table_info.setText("")
        self.table_info.setObjectName("table_info")
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(0, 50, 251, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtGui.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 80, 251, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtGui.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 110, 251, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 62, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(0, 100, 62, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(0, 130, 62, 17))
        self.label_7.setObjectName("label_7")
        self.host_info = QtGui.QLabel(self.frame)
        self.host_info.setGeometry(QtCore.QRect(70, 70, 171, 17))
        self.host_info.setText("")
        self.host_info.setObjectName("host_info")
        self.ip_info = QtGui.QLabel(self.frame)
        self.ip_info.setGeometry(QtCore.QRect(70, 100, 181, 17))
        self.ip_info.setText("")
        self.ip_info.setObjectName("ip_info")
        self.user_info = QtGui.QLabel(self.frame)
        self.user_info.setGeometry(QtCore.QRect(70, 126, 181, 21))
        self.user_info.setText("")
        self.user_info.setObjectName("user_info")
        self.label_4 = QtGui.QLabel(SendSHP)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 62, 17))
        self.label_4.setObjectName("label_4")
        self.db_table = QtGui.QLineEdit(SendSHP)
        self.db_table.setGeometry(QtCore.QRect(20, 40, 251, 27))
        self.db_table.setObjectName("db_table")
        self.table_error_label = QtGui.QLabel(SendSHP)
        self.table_error_label.setGeometry(QtCore.QRect(20, 70, 251, 17))
        self.table_error_label.setText("")
        self.table_error_label.setObjectName("table_error_label")

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
        self.shp_status.setText(QtGui.QApplication.translate("SendSHP", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SendSHP", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SendSHP", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SendSHP", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("SendSHP", "IP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("SendSHP", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SendSHP", "Table:", None, QtGui.QApplication.UnicodeUTF8))

from PyKDE4.kdeui import KLed
