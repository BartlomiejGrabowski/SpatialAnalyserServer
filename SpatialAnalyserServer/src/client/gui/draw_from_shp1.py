# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw_from_shp.ui'
#
# Created: Thu May 31 19:47:00 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DrawFromSHPFile(object):
    def setupUi(self, DrawFromSHPFile):
        DrawFromSHPFile.setObjectName("DrawFromSHPFile")
        DrawFromSHPFile.resize(742, 384)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bluesphere.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DrawFromSHPFile.setWindowIcon(icon)
        self.GetFileList = QtGui.QPushButton(DrawFromSHPFile)
        self.GetFileList.setGeometry(QtCore.QRect(460, 30, 93, 27))
        self.GetFileList.setObjectName("GetFileList")
        self.files_table = QtGui.QTableWidget(DrawFromSHPFile)
        self.files_table.setGeometry(QtCore.QRect(10, 30, 411, 321))
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
        self.listWidget.setGeometry(QtCore.QRect(450, 170, 256, 171))
        self.listWidget.setObjectName("listWidget")
        self.label = QtGui.QLabel(DrawFromSHPFile)
        self.label.setGeometry(QtCore.QRect(20, 10, 62, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(DrawFromSHPFile)
        self.label_2.setGeometry(QtCore.QRect(460, 150, 91, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.clear_file_list = QtGui.QPushButton(DrawFromSHPFile)
        self.clear_file_list.setGeometry(QtCore.QRect(460, 70, 93, 27))
        self.clear_file_list.setObjectName("clear_file_list")
        self.cancel_window = QtGui.QPushButton(DrawFromSHPFile)
        self.cancel_window.setGeometry(QtCore.QRect(610, 70, 93, 27))
        self.cancel_window.setObjectName("cancel_window")
        self.draw_file = QtGui.QPushButton(DrawFromSHPFile)
        self.draw_file.setGeometry(QtCore.QRect(610, 30, 93, 27))
        self.draw_file.setObjectName("draw_file")
        self.frame = QtGui.QFrame(DrawFromSHPFile)
        self.frame.setGeometry(QtCore.QRect(442, 140, 271, 211))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(DrawFromSHPFile)
        QtCore.QObject.connect(self.clear_file_list, QtCore.SIGNAL("clicked()"), self.files_table.clearContents)
        QtCore.QMetaObject.connectSlotsByName(DrawFromSHPFile)

    def retranslateUi(self, DrawFromSHPFile):
        DrawFromSHPFile.setWindowTitle(QtGui.QApplication.translate("DrawFromSHPFile", "Draw from SHP", None, QtGui.QApplication.UnicodeUTF8))
        self.GetFileList.setText(QtGui.QApplication.translate("DrawFromSHPFile", "Get file list", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.verticalHeaderItem(0).setText(QtGui.QApplication.translate("DrawFromSHPFile", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DrawFromSHPFile", "File name", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DrawFromSHPFile", "Created", None, QtGui.QApplication.UnicodeUTF8))
        self.files_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("DrawFromSHPFile", "Last Modified", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DrawFromSHPFile", "File list:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DrawFromSHPFile", "Related files:", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_file_list.setText(QtGui.QApplication.translate("DrawFromSHPFile", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_window.setText(QtGui.QApplication.translate("DrawFromSHPFile", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_file.setText(QtGui.QApplication.translate("DrawFromSHPFile", "Draw", None, QtGui.QApplication.UnicodeUTF8))

