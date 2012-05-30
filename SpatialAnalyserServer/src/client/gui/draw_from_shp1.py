# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw_from_shp.ui'
#
# Created: Wed May 30 21:47:58 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DrawFromSHPFile(object):
    def setupUi(self, DrawFromSHPFile):
        DrawFromSHPFile.setObjectName("DrawFromSHPFile")
        DrawFromSHPFile.resize(742, 571)
        self.GetFileList = QtGui.QPushButton(DrawFromSHPFile)
        self.GetFileList.setGeometry(QtCore.QRect(570, 10, 93, 27))
        self.GetFileList.setObjectName("GetFileList")
        self.files_table = QtGui.QTableWidget(DrawFromSHPFile)
        self.files_table.setGeometry(QtCore.QRect(10, 10, 411, 321))
        self.files_table.setMouseTracking(False)
        self.files_table.setAutoFillBackground(False)
        self.files_table.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.files_table.setObjectName("files_table")
        self.files_table.setColumnCount(3)
        self.files_table.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.files_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.files_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.files_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.files_table.setHorizontalHeaderItem(2, item)
        self.files_table.horizontalHeader().setCascadingSectionResizes(False)
        self.files_table.horizontalHeader().setDefaultSectionSize(127)
        self.listWidget = QtGui.QListWidget(DrawFromSHPFile)
        self.listWidget.setGeometry(QtCore.QRect(10, 370, 256, 192))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(DrawFromSHPFile)
        QtCore.QMetaObject.connectSlotsByName(DrawFromSHPFile)

    def retranslateUi(self, DrawFromSHPFile):
        DrawFromSHPFile.setWindowTitle(QtGui.QApplication.translate("DrawFromSHPFile", "Draw from SHP", None, QtGui.QApplication.UnicodeUTF8))
        self.GetFileList.setText(QtGui.QApplication.translate("DrawFromSHPFile", "Get file list", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.verticalHeaderItem(0).setText(QtGui.QApplication.translate("DrawFromSHPFile", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DrawFromSHPFile", "File name", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DrawFromSHPFile", "Created", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("DrawFromSHPFile", "Last Modified", None, QtGui.QApplication.UnicodeUTF8))

