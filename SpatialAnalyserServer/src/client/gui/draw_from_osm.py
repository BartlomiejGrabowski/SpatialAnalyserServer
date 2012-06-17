'''
Created on Jun 16, 2012

@author: bartek
'''
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
import mapnik
sys.path.append("..")
sys.path.append("../../logger")
sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
from Client import Client
import draw_osm_image

class Ui_DrawFromOSMFile(Client):        
    def setupUi(self, DrawFromOSMFile):
        DrawFromOSMFile.setObjectName("DrawFromOSMFile")
        DrawFromOSMFile.resize(742, 384)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.confIconsDir+'earthsphere.ico'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DrawFromOSMFile.setWindowIcon(icon)
        self.get_file_list = QtGui.QPushButton(DrawFromOSMFile)
        self.get_file_list.setGeometry(QtCore.QRect(460, 30, 93, 27))
        self.get_file_list.setObjectName("GetFileList")
        self.files_table = QtGui.QTableWidget(DrawFromOSMFile)
        self.files_table.setGeometry(QtCore.QRect(10, 30, 411, 321))
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
        self.related_files_list = QtGui.QListWidget(DrawFromOSMFile)
        self.related_files_list.setGeometry(QtCore.QRect(450, 170, 256, 171))
        self.related_files_list.setObjectName("related_files_list")
        self.label = QtGui.QLabel(DrawFromOSMFile)
        self.label.setGeometry(QtCore.QRect(20, 10, 62, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(DrawFromOSMFile)
        self.label_2.setGeometry(QtCore.QRect(460, 150, 91, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.clear_file_list = QtGui.QPushButton(DrawFromOSMFile)
        self.clear_file_list.setGeometry(QtCore.QRect(460, 70, 93, 27))
        self.clear_file_list.setObjectName("clear_file_list")
        self.cancel_window = QtGui.QPushButton(DrawFromOSMFile)
        self.cancel_window.setGeometry(QtCore.QRect(610, 70, 93, 27))
        self.cancel_window.setObjectName("cancel_window")
        self.draw_file = QtGui.QPushButton(DrawFromOSMFile)
        self.draw_file.setGeometry(QtCore.QRect(610, 30, 93, 27))
        self.draw_file.setObjectName("draw_file")
        self.frame = QtGui.QFrame(DrawFromOSMFile)
        self.frame.setGeometry(QtCore.QRect(442, 140, 271, 211))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.retranslateUi(DrawFromOSMFile)
        QtCore.QObject.connect(self.get_file_list, QtCore.SIGNAL("clicked()"), self.getOSMFileList)
        QtCore.QObject.connect(self.draw_file, QtCore.SIGNAL("clicked()"), self.showOSMDrawForm)
        QtCore.QObject.connect(self.files_table, QtCore.SIGNAL("cellClicked(int, int)"), self.selectRelatedRowsByCell)
        QtCore.QObject.connect(self.clear_file_list, QtCore.SIGNAL("clicked()"), self.flushDataRecords)
        QtCore.QObject.connect(self.cancel_window, QtCore.SIGNAL("clicked()"), DrawFromOSMFile,  QtCore.SLOT("close()"))
        QtCore.QMetaObject.connectSlotsByName(DrawFromOSMFile)

    def retranslateUi(self, DrawFromOSMFile):
        DrawFromOSMFile.setWindowTitle(QtGui.QApplication.translate("DrawFromOSMFile", "Draw from OSM", None, QtGui.QApplication.UnicodeUTF8))
        self.get_file_list.setText(QtGui.QApplication.translate("DrawFromOSMFile", "Get file list", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DrawFromOSMFile", "File name", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DrawFromOSMFile", "Created", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("DrawFromOSMFile", "Last Modified", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DrawFromOSMFile", "File list:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DrawFromOSMFile", "Related files:", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_file_list.setText(QtGui.QApplication.translate("DrawFromOSMFile", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_window.setText(QtGui.QApplication.translate("DrawFromOSMFile", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_file.setText(QtGui.QApplication.translate("DrawFromOSMFile", "Draw", None, QtGui.QApplication.UnicodeUTF8))

    def flushDataRecords(self):
        self.files_table.clear()
        self.related_files_list.clear()
        self.getListFlag = 0
        
    def getOSMFileList(self):
        self.outList = self.client_get_osm_file_list()
        self.getListFlag = 1
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
        fileItem.setBackground(QtGui.QBrush(QtCore.Qt.Dense7Pattern))
        fileItem.setTextColor(QtGui.QColor(QtCore.Qt.blue))
        fileItem.setIcon(QtGui.QIcon(QtGui.QPixmap(self.confIconsDir+'shpfile.ico')))
        filesList.addItem(fileItem)
        
    def selectRelatedRowsByCell(self, x, y):
        #To avoid getting value from empty cells.
        if self.getListFlag == 1:
            #First deselect all rows. Clear earlier selections.
            self.files_table.clearSelection()
            item = QtGui.QTableWidgetItem()
            #Get row number after the cell has been selected.
            row = self.files_table.row(self.files_table.item(x, y))
            #Get file name from table row.
            fileName = self.files_table.item(row, 0).text()
            #Find related files.
            self.relatedFiles = list()
            #If list is not empty, then clear list.
            #if self.related_files_list.count() != 0:
            self.related_files_list.clear()
            for f in self.outList:
                if f.fName.split(".")[0] == fileName.split(".")[0]:
                    #If founded related file, then append file to related list
                    self.relatedFiles.append(f.fName)
                    #We are founding file in the table,
                    relatedItem = self.files_table.findItems(f.fName, QtCore.Qt.MatchExactly)
                    #If founded, then get row number.
                    relatedRow = self.files_table.row(relatedItem[0])
                    #Select row.
                    self.files_table.selectRow(relatedRow)
                    #Add file to file related list.
                    self.addFileIntoList(self.related_files_list, f.fName)
               
    def showOSMDrawForm(self):
        #Loop thru related files list.
        for fileName in self.relatedFiles:
            self.downloadFile(self.confOSMDownloadsLoc, fileName)

        #Show OSM draw image form.
        self.DrawOSMImage = QtGui.QWidget()
        self.sh = draw_osm_image.Ui_DrawOSMImage()
        self.sh.setupUi(self.DrawOSMImage)
        #Get first part (without extension) of file name and set as a label text.
        self.sh.file_name_label.setText(self.relatedFiles[0].split('.')[0])
        #Show a form that allows draw image from shp file.
        self.DrawOSMImage.show()
        
        
    def downloadFile(self, destDir, fileName):
        #Redirect stdout to /dev/null.
        #f = open(os.devnull, 'w')
        #sys.stdout = f
        #Get file content to string.
        fileContent = self.client_get_osm_file_content(fileName)
        try:
            #Create file in downloads directory. Name of file is the same as the name on server.
            out_file = open("%s/%s" % (destDir, fileName), 'w')
            #Write list of strings into file.
            out_file.writelines(fileContent)
            #Close the file.
            out_file.close()
        except IOError as ex:
            self.logger.log.error("%s exception occurred during open %s/%s file" % (ex, destDir, fileName))
            return 1 