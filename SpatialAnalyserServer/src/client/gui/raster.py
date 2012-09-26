# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raster.ui'
#
# Created: Sun Sep 16 18:26:58 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Image
import sys
import os
sys.path.append("..")
sys.path.append("../../logger")
sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
sys.path.append("../../../interfaces/projections")
sys.path.append("../../../interfaces/raster")
from Client import Client

class Ui_FileProcessing(Client):
    
    def __init__(self, rasterFile):
        Client.__init__(self)
        self.file = rasterFile
        try:
            self.image = Image.open(str(self.file))
        except IOError as ex:
            sys.stderr.write(str(ex))

    def setupUi(self, FileProcessing):
        FileProcessing.setObjectName("FileProcessing")
        FileProcessing.resize(929, 784)
        FileProcessing.setFixedHeight(784)
        FileProcessing.setFixedWidth(929)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.confIconsDir+'1344071416_statistics.ico'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        FileProcessing.setWindowIcon(icon)
        self.image_view = QtGui.QGraphicsView(FileProcessing)
        self.image_view.setGeometry(QtCore.QRect(10, 40, 761, 541))
        self.image_view.setObjectName("image_view")
        self.label = QtGui.QLabel(FileProcessing)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 17))
        self.label.setObjectName("label")
        self.file_label = QtGui.QLabel(FileProcessing)
        self.file_label.setGeometry(QtCore.QRect(50, 10, 750, 17))
        self.file_label.setText("")
        self.file_label.setObjectName("file_label")
        self.label_2 = QtGui.QLabel(FileProcessing)
        self.label_2.setGeometry(QtCore.QRect(780, 40, 62, 17))
        self.label_2.setObjectName("label_2")
        self.format_label = QtGui.QLabel(FileProcessing)
        self.format_label.setGeometry(QtCore.QRect(780, 60, 141, 21))
        self.format_label.setText("")
        self.format_label.setObjectName("format_label")
        self.label_3 = QtGui.QLabel(FileProcessing)
        self.label_3.setGeometry(QtCore.QRect(780, 100, 62, 17))
        self.label_3.setObjectName("label_3")
        self.size_label = QtGui.QLabel(FileProcessing)
        self.size_label.setGeometry(QtCore.QRect(780, 120, 141, 21))
        self.size_label.setText("")
        self.size_label.setObjectName("size_label")
        self.label_4 = QtGui.QLabel(FileProcessing)
        self.label_4.setGeometry(QtCore.QRect(780, 160, 62, 17))
        self.label_4.setObjectName("label_4")
        self.mode_label = QtGui.QLabel(FileProcessing)
        self.mode_label.setGeometry(QtCore.QRect(780, 180, 141, 21))
        self.mode_label.setText("")
        self.mode_label.setObjectName("mode_label")
        self.label_6 = QtGui.QLabel(FileProcessing)
        self.label_6.setGeometry(QtCore.QRect(780, 220, 62, 17))
        self.label_6.setObjectName("label_6")
        self.palette_label = QtGui.QLabel(FileProcessing)
        self.palette_label.setGeometry(QtCore.QRect(780, 240, 141, 21))
        self.palette_label.setText("")
        self.palette_label.setObjectName("palette_label")
        self.label_7 = QtGui.QLabel(FileProcessing)
        self.label_7.setGeometry(QtCore.QRect(780, 280, 62, 17))
        self.label_7.setObjectName("label_7")
        self.info_label = QtGui.QLabel(FileProcessing)
        self.info_label.setGeometry(QtCore.QRect(780, 300, 141, 21))
        self.info_label.setText("")
        self.info_label.setObjectName("info_label")
        self.info_label2 = QtGui.QLabel(FileProcessing)
        self.info_label2.setGeometry(QtCore.QRect(780, 320, 141, 21))
        self.info_label2.setText("")
        self.info_label2.setObjectName("info_label2")
        self.label_5 = QtGui.QLabel(FileProcessing)
        self.label_5.setGeometry(QtCore.QRect(10, 590, 51, 17))
        self.label_5.setObjectName("label_5")
        self.filter_box = QtGui.QComboBox(FileProcessing)
        self.filter_box.setGeometry(QtCore.QRect(10, 610, 171, 31))
        self.filter_box.setObjectName("filter_box")
        self.label_8 = QtGui.QLabel(FileProcessing)
        self.label_8.setGeometry(QtCore.QRect(200, 590, 51, 17))
        self.label_8.setObjectName("label_8")
        self.mode_box = QtGui.QComboBox(FileProcessing)
        self.mode_box.setGeometry(QtCore.QRect(200, 610, 171, 31))
        self.mode_box.setObjectName("mode_box")
        self.label_9 = QtGui.QLabel(FileProcessing)
        self.label_9.setGeometry(QtCore.QRect(390, 590, 61, 17))
        self.label_9.setObjectName("label_9")
        self.contrast_box = QtGui.QComboBox(FileProcessing)
        self.contrast_box.setGeometry(QtCore.QRect(390, 610, 171, 31))
        self.contrast_box.setObjectName("contrast_box")
        self.label_10 = QtGui.QLabel(FileProcessing)
        self.label_10.setGeometry(QtCore.QRect(10, 660, 70, 17))
        self.label_10.setObjectName("label_10")
        self.brightness_box = QtGui.QComboBox(FileProcessing)
        self.brightness_box.setGeometry(QtCore.QRect(10, 680, 171, 31))
        self.brightness_box.setObjectName("brightness_box")
        self.label_11 = QtGui.QLabel(FileProcessing)
        self.label_11.setGeometry(QtCore.QRect(200, 660, 70, 17))
        self.label_11.setObjectName("label_11")
        self.sharpness_box = QtGui.QComboBox(FileProcessing)
        self.sharpness_box.setGeometry(QtCore.QRect(200, 680, 171, 31))
        self.sharpness_box.setObjectName("sharpness_box")
        self.ok_button = QtGui.QPushButton(FileProcessing)
        self.ok_button.setGeometry(QtCore.QRect(820, 740, 91, 27))
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtGui.QPushButton(FileProcessing)
        self.cancel_button.setGeometry(QtCore.QRect(710, 740, 91, 27))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(FileProcessing)
        QtCore.QMetaObject.connectSlotsByName(FileProcessing)
        
        #Fill image attributes.
        self.file_label.setText(self.file)
        self.size_label.setText(str(self.image.size))
        self.mode_label.setText(self.image.mode)
        self.format_label.setText(self.image.format)
        if self.image.palette != None:
            self.palette_label.setText(str(self.image.palette))
        else:
            self.palette_label.setText("None")
            
        if self.image.info['compression'] != None:
            self.info_label.setText("compression: %s" % (self.image.info['compression']))
        if self.image.info['dpi'] != None:
            self.info_label2.setText("dpi: %s" % (str(self.image.info['dpi'])))
        
        #Fill filter box.
        self.filter_box.addItem('None')
        self.filter_box.addItem('BLUR')
        self.filter_box.addItem('CONTOUR')
        self.filter_box.addItem('DETAIL')
        self.filter_box.addItem('EDGE_ENHANCE')
        self.filter_box.addItem('EDGE_ENHANCE_MORE')
        self.filter_box.addItem('EMBOSS')
        self.filter_box.addItem('FIND_EDGES')
        self.filter_box.addItem('SMOOTH')
        self.filter_box.addItem('SMOOTH_MORE')
        self.filter_box.addItem('SHARPEN')
        
        #Fill mode box.
        self.mode_box.addItem('None')
        self.mode_box.addItem('RGB')
        self.mode_box.addItem('RGBA')
        self.mode_box.addItem('CMYK')
        self.mode_box.addItem('1')
        self.mode_box.addItem('L')
        self.mode_box.addItem('P')
        self.mode_box.addItem('YCbCr')
        self.mode_box.addItem('I')
        self.mode_box.addItem('F')
        
        #Fill contrast box.
        contrast_list = [-90, -80, -70, -60, -50, -40, 
                         -30, -20, -10, 0, 10, 20, 30, 
                         40, 50, 60, 70, 80, 90]
        for i in contrast_list:
            self.contrast_box.addItem(str(i))
        self.contrast_box.setCurrentIndex(9)
        
        #Fill brightness box.
        brightness_list = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0,
                           1.2, 1.4, 1.6, 1.8, 2.0]
        for i in brightness_list:
            self.brightness_box.addItem(str(i))
        self.brightness_box.setCurrentIndex(5)
        
        #Fill sharpness box.
        sharpness_list = [-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0,
                          3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        for i in sharpness_list:
            self.sharpness_box.addItem(str(i))
        self.sharpness_box.setCurrentIndex(6)
        
        #Display image on scene.
        self.scene = QtGui.QGraphicsScene()
        self.picture = QtGui.QPixmap(self.file)
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.image_view.setScene(self.scene)
        
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL("clicked()"), self.allProcessing)
        QtCore.QObject.connect(self.filter_box, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.filterProcessing)
        QtCore.QObject.connect(self.mode_box, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.modeProcessing)
        QtCore.QObject.connect(self.contrast_box, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.contrastProcessing)
        QtCore.QObject.connect(self.brightness_box, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.brightnessProcessing)
        QtCore.QObject.connect(self.sharpness_box, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.sharpnessProcessing)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL("clicked()"), FileProcessing, QtCore.SLOT("close()"))

        
    def retranslateUi(self, FileProcessing):
        FileProcessing.setWindowTitle(QtGui.QApplication.translate("FileProcessing", "File processing", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FileProcessing", "File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FileProcessing", "Format:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FileProcessing", "Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Fistr(self.filter_box.currentText())leProcessing", "Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("FileProcessing", "Palette:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("FileProcessing", "Info:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FileProcessing", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("FileProcessing", "Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("FileProcessing", "Contrast:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("FileProcessing", "Brightness:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("FileProcessing", "Sharpness:", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_button.setText(QtGui.QApplication.translate("FileProcessing", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate("FileProcessing", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        
    def downloadFile(self, fileName):
        '''
        @brief: This function is used to download file from server.
        @param fileName string: Input parameter is file name. 
        @return: This function does not return a value. Returns 1 if error occurred.
        '''
    
        #Get file content to string.
        fileContent = self.client_get_raster_file(fileName)
        try:
            #Create file in downloads directory. Name of file is the same as the name on server.
            out_file = open(fileName, 'w')
            #Write list of strings into file.
            out_file.writelines(fileContent)
            #Close the file.
            out_file.close()
        except IOError as ex:
            self.logger.log.error("%s exception occurred during open %s file" % (ex, fileName))
            return 1 
        
    def filterProcessing(self, index):
        if self.filter_box.currentText() != 'None':
            out = self.client_image_filter(str(self.file), str(index))
        else:
            out = self.file
        
        #self.downloadFile(out)
        
        #Display image on scene.
        self.scene = QtGui.QGraphicsScene()
        self.picture = QtGui.QPixmap(out) 
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.image_view.setScene(self.scene)
        
        
    def modeProcessing(self, index):
        if self.mode_box.currentText() != 'None':
            if self.filter_box.currentText() != 'None':
                filterFile = '/tmp/' + self.filter_box.currentText() + os.path.basename(str(self.file))
                out = self.client_convert_image(str(filterFile), str(self.mode_box.currentText()))
                self.mode_label.setText(str(self.mode_box.currentText()))
            else:
                out = self.client_convert_image(str(self.file), str(self.mode_box.currentText()))
                self.mode_label.setText(str(self.mode_box.currentText()))
        else:
            if self.filter_box.currentText() != 'None':
                filterFile = '/tmp/' + self.filter_box.currentText() + os.path.basename(str(self.file))
                out = self.client_convert_image(str(filterFile), str(self.mode_box.currentText()))
                self.mode_label.setText(str(self.mode_box.currentText()))
            else:
                out = self.file
        
        #self.downloadFile(out)
        
        #Display image on scene.
        self.scene = QtGui.QGraphicsScene()
        self.picture = QtGui.QPixmap(out)
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.image_view.setScene(self.scene)
        
    def contrastProcessing(self, index):
        if self.contrast_box.currentText() != '0' \
            and self.filter_box.currentText() != 'None' \
                and  self.mode_box.currentText() != 'None':
            modeFile = '/tmp/' + self.mode_box.currentText() + self.filter_box.currentText() + os.path.basename(str(self.file))
            print(modeFile)
            out = self.client_contrast_image(str(modeFile), str(self.contrast_box.currentText()))
            
        if self.contrast_box.currentText() != '0' \
            and self.filter_box.currentText() != 'None' \
                and  self.mode_box.currentText() == 'None':
            filterFile = '/tmp/' + self.filter_box.currentText() + os.path.basename(str(self.file))
            out = self.client_contrast_image(str(filterFile), str(self.contrast_box.currentText()))
            
        if self.contrast_box.currentText() != '0' \
            and self.filter_box.currentText() == 'None' \
                and  self.filter_box.currentText() == 'None':
            contrastFile = '/tmp/' + self.contrast_box.currentText() + os.path.basename(str(self.file))
            out = self.client_contrast_image(str(contrastFile), str(self.contrast_box.currentText()))
            
        if self.contrast_box.currentText() == '0':
            out = self.file
    
        #self.downloadFile(out)
            
        #Display image on scene.
        self.scene = QtGui.QGraphicsScene()
        self.picture = QtGui.QPixmap(out)
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.image_view.setScene(self.scene)
        
    def brightnessProcessing(self, index):
        if self.brightness_box.currentText() != '1.0':
            if self.contrast_box.currentText() != '0' \
                and self.filter_box.currentText() != 'None' \
                and  self.mode_box.currentText() != 'None':
                    contrastFile = '/tmp/' + self.contrast_box.currentText() + self.mode_box.currentText() + self.filter_box.currentText() + os.path.basename(str(self.file))
                    out = self.client_brightness_image(str(contrastFile), str(self.brightness_box.currentText()))
                    
        if self.brightness_box.currentText() != '1.0':
            if self.contrast_box.currentText() == '0' \
                and self.filter_box.currentText() != 'None' \
                and  self.mode_box.currentText() != 'None':
                    modeFile = '/tmp/' + self.mode_box.currentText() + self.filter_box.currentText() + os.path.basename(str(self.file))
                    out = self.client_brightness_image(str(modeFile), str(self.brightness_box.currentText()))
                    
        if self.brightness_box.currentText() != '1.0':
            if self.contrast_box.currentText() == '0' \
                and self.filter_box.currentText() != 'None' \
                and  self.mode_box.currentText() == 'None':
                    filterFile = '/tmp/' + self.filter_box.currentText() + os.path.basename(str(self.file))
                    out = self.client_brightness_image(str(filterFile), str(self.brightness_box.currentText()))
                    
        if self.brightness_box.currentText() != '1.0':
            if self.contrast_box.currentText() == '0' \
                and self.filter_box.currentText() == 'None' \
                and  self.mode_box.currentText() == 'None':
                    out = self.client_brightness_image(str(self.file), str(self.brightness_box.currentText()))
                    
        if self.brightness_box.currentText() == '1.0':
            if self.contrast_box.currentText() == '0' \
                and self.filter_box.currentText() == 'None' \
                and  self.mode_box.currentText() == 'None':
                    out = self.file
            
        #self.downloadFile(out)
            
        #Display image on scene.
        self.scene = QtGui.QGraphicsScene()
        self.picture = QtGui.QPixmap(out)
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.image_view.setScene(self.scene)
    
    def sharpnessProcessing(self):
        if self.sharpness_box.currentText() != '1.0':
            if self.brightness_box.currentText() != '1.0':
                if self.contrast_box.currentText() != '0' \
                    and self.filter_box.currentText() != 'None' \
                    and  self.mode_box.currentText() != 'None':
                        brightnessFile = '/tmp/' + self.brightness_box.currentText() + self.contrast_box.currentText() + self.mode_box.currentText() \
                         + self.filter_box.currentText() + os.path.basename(str(self.file))
                        out = self.client_sharpness_image(str(brightnessFile), str(self.sharpness_box.currentText()))
                        
        if self.sharpness_box.currentText() != '1.0':
            if self.brightness_box.currentText() == '1.0':
                if self.contrast_box.currentText() != '0' \
                    and self.filter_box.currentText() != 'None' \
                    and  self.mode_box.currentText() != 'None':
                        contrastFile = '/tmp/' + self.contrast_box.currentText() + self.mode_box.currentText() \
                         + self.filter_box.currentText() + os.path.basename(str(self.file))
                        out = self.client_sharpness_image(str(contrastFile), str(self.sharpness_box.currentText()))
                        
        if self.sharpness_box.currentText() != '1.0':
            if self.brightness_box.currentText() == '1.0':
                if self.contrast_box.currentText() == '0' \
                    and self.filter_box.currentText() != 'None' \
                    and  self.mode_box.currentText() != 'None':
                        modeFile = '/tmp/' + self.mode_box.currentText() \
                         + self.filter_box.currentText() + os.path.basename(str(self.file))
                        out = self.client_sharpness_image(str(modeFile), str(self.sharpness_box.currentText()))
                        
        if self.sharpness_box.currentText() != '1.0':
            if self.brightness_box.currentText() == '1.0':
                if self.contrast_box.currentText() == '0' \
                    and self.filter_box.currentText() != 'None' \
                    and  self.mode_box.currentText() == 'None':
                        filterFile = '/tmp/' + self.filter_box.currentText() + os.path.basename(str(self.file))
                        out = self.client_sharpness_image(str(filterFile), str(self.sharpness_box.currentText()))
                        
        if self.sharpness_box.currentText() != '1.0':
            if self.brightness_box.currentText() == '1.0':
                if self.contrast_box.currentText() == '0' \
                    and self.filter_box.currentText() == 'None' \
                    and  self.mode_box.currentText() == 'None':
                        out = self.client_sharpness_image(str(self.file), str(self.sharpness_box.currentText()))
            
        if self.sharpness_box.currentText() == '1.0':
            out = self.file
        
        #self.downloadFile(out)
        
        #Display image on scene.
        self.scene = QtGui.QGraphicsScene()
        self.picture = QtGui.QPixmap(out)
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.image_view.setScene(self.scene)
        
    def allProcessing(self):
        self.image = 'out.png'
        self.pixmap = QtGui.QPixmap(QtGui.QPixmap.grabWidget(self.image_view))
        self.pixmap.save(self.image)
        
            
        