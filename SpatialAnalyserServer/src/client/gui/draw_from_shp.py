# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw_from_shp.ui'
#
# Created: Mon May 28 21:00:54 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import string
from PyQt4 import QtCore, QtGui
sys.path.append("..")
sys.path.append("../../logger")
sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
from Client import Client

class Ui_DrawFromSHPFile(Client):
    def setupUi(self, DrawFromSHPFile):
        DrawFromSHPFile.setObjectName("DrawFromSHPFile")
        DrawFromSHPFile.resize(742, 571)
        self.get_file_list = QtGui.QPushButton(DrawFromSHPFile)
        self.get_file_list.setGeometry(QtCore.QRect(575, 10, 93, 27))
        self.get_file_list.setObjectName("GetFileList")
        self.files_table = QtGui.QTableWidget(DrawFromSHPFile)
        self.files_table.setGeometry(QtCore.QRect(10, 10, 425, 300))
        self.files_table.setMouseTracking(False)
        self.files_table.setAutoFillBackground(False)
        self.files_table.setObjectName("files_table")
        self.files_table.setColumnCount(3)
        self.files_table.setRowCount(0)
        self.files_table.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
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
        self.related_files_list = QtGui.QListWidget(DrawFromSHPFile)
        self.related_files_list.setGeometry(QtCore.QRect(10, 370, 250, 100))
        self.related_files_list.setObjectName("related_files_list")
        #self.draw_file = QtGui.QPushButton(DrawFromSHPFile)
        #self.draw_file.setGeometry(QtCore.QRect(430, 37, 93, 27))
        #self.draw_file.setAutoFillBackground(False)
        #self.draw_file.setDefault(False)
        #self.draw_file.setFlat(False)
        #self.draw_file.setObjectName("draw_file")

        self.retranslateUi(DrawFromSHPFile)
        QtCore.QObject.connect(self.get_file_list, QtCore.SIGNAL("clicked()"), self.getSHPFileList)
        QtCore.QObject.connect(self.files_table, QtCore.SIGNAL("cellClicked(int, int)"), self.selectRowByCell)
        QtCore.QMetaObject.connectSlotsByName(DrawFromSHPFile)

    def retranslateUi(self, DrawFromSHPFile):
        DrawFromSHPFile.setWindowTitle(QtGui.QApplication.translate("DrawFromSHPFile", "Draw from SHP", None, QtGui.QApplication.UnicodeUTF8))
        self.get_file_list.setText(QtGui.QApplication.translate("DrawFromSHPFile", "Get file list", None, QtGui.QApplication.UnicodeUTF8))
        #self.files_table.verticalHeaderItem(0).setText(QtGui.QApplication.translate("DrawFromSHPFile", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DrawFromSHPFile", "File name", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DrawFromSHPFile", "Created", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("DrawFromSHPFile", "Last Modified", None, QtGui.QApplication.UnicodeUTF8))
        #self.draw_file.setText(QtGui.QApplication.translate("DrawFromSHPFile", "Draw", None, QtGui.QApplication.UnicodeUTF8))
        
    def getSHPFileList(self):
        self.outList = self.client_get_shp_file_list()
        self.rows = 0
        for i in self.outList:
            #First fill the table.
            self.files_table.insertRow(self.rows)
            #Add file name item.
            item = QtGui.QTableWidgetItem()
            item.setText(i.fName)
            self.files_table.setItem(self.rows, 0, item)
            #Add file created item.
            item = QtGui.QTableWidgetItem()
            item.setText(i.cTime)
            self.files_table.setItem(self.rows, 1, item)
            #Add last modified item.
            item = QtGui.QTableWidgetItem()
            item.setText(i.lModified)
            self.files_table.setItem(self.rows, 2, item)

            self.rows += 1 

    def addFileIntoList(self, filesList, fileName ):
        fileItem = QtGui.QListWidgetItem()
        fileItem.setText(fileName)
        #fileItem.setBackground(QtGui.QBrush(QtCore.Qt.Dense7Pattern))
        fileItem.setTextColor(QtGui.QColor(QtCore.Qt.blue))
        filesList.addItem(fileItem)
        
    def selectRowByCell(self, x, y):
        #First deselect all rows. Clear earlier selections.
        self.files_table.clearSelection()
        item = QtGui.QTableWidgetItem()
        #Get row number after the cell has been selected.
        row = self.files_table.row(self.files_table.item(x, y))
        #Get file name from table row.
        fileName = self.files_table.item(row, 0).text()
        #Find related files.
        relatedFiles = list()
        #If list is not empty, then clear list.
        if self.related_files_list.count() != 0:
            self.related_files_list.clear()
        for f in self.outList:
            if f.fName.split(".")[0] == fileName.split(".")[0]:
                #If founded related file, then append file to related list
                relatedFiles.append(f.fName)
                #We are founding file in the table,
                relatedItem = self.files_table.findItems(f.fName, QtCore.Qt.MatchExactly)
                #If founded, then get row number.
                relatedRow = self.files_table.row(relatedItem[0])
                #Select row.
                self.files_table.selectRow(relatedRow)
                #Add file to file related list.
                self.addFileIntoList(self.related_files_list, f.fName)
