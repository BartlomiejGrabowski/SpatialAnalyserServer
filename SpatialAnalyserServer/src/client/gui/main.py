# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Aug  4 11:21:45 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import send_shp
import draw_from_shp
import draw_from_osm
import draw_osm_www
import geo_services
import geo
import about

import sys
sys.path.append("../../../interfaces/info")
sys.path.append("../../../interfaces/projections")
sys.path.append("../../../interfaces/geo")

from Client import Client

class Ui_MainWindow(Client):
    '''
    Class Ui_MainWindow is a major class representing the
    main window of SpatialAnalyser application. PyQT implementation.
    @author: Bartlomiej Grabowski
    @version: 1.0
    '''
    
    def setupUi(self, MainWindow):
        '''
        @brief: This function is used to setup all elements of the main window.
        @see: Ui_MainWindow
        @param MainWindow QMainWindow: Input parameter is QtGui.QMainWindow.
        @return: This function does not return a value. 
        '''
        MainWindow.setObjectName("Geospatial")
        MainWindow.resize(800, 574)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/1344068492_icons.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setFixedHeight(574)
        MainWindow.setFixedWidth(800)
        #self.centralwidget.setMaximumSize(801, 575)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 231, 481))
        self.frame.setMouseTracking(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.frame.setPalette(palette)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 60, 230, 3))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.send_shp_btn = QtGui.QCommandLinkButton(self.frame)
        self.send_shp_btn.setGeometry(QtCore.QRect(0, 0, 231, 61))
        self.send_shp_btn.setMouseTracking(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.send_shp_btn.setPalette(palette)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/1344068458_db_comit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_shp_btn.setIcon(icon1)
        self.send_shp_btn.setIconSize(QtCore.QSize(32, 32))
        self.send_shp_btn.setObjectName("send_shp_btn")
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 120, 230, 3))
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(0, 180, 230, 3))
        self.line_3.setFrameShadow(QtGui.QFrame.Plain)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtGui.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 240, 230, 3))
        self.line_4.setFrameShadow(QtGui.QFrame.Plain)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.draw_shp_btn = QtGui.QCommandLinkButton(self.frame)
        self.draw_shp_btn.setGeometry(QtCore.QRect(0, 60, 231, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.draw_shp_btn.setPalette(palette)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/1344068568_agt_internet.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.draw_shp_btn.setIcon(icon2)
        self.draw_shp_btn.setIconSize(QtCore.QSize(32, 32))
        self.draw_shp_btn.setObjectName("draw_shp_btn")
        self.draw_osm_btn = QtGui.QCommandLinkButton(self.frame)
        self.draw_osm_btn.setGeometry(QtCore.QRect(0, 120, 231, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.draw_osm_btn.setPalette(palette)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/1344068657_image.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.draw_osm_btn.setIcon(icon3)
        self.draw_osm_btn.setIconSize(QtCore.QSize(32, 32))
        self.draw_osm_btn.setObjectName("draw_osm_btn")
        self.draw_web_osm_btn = QtGui.QCommandLinkButton(self.frame)
        self.draw_web_osm_btn.setGeometry(QtCore.QRect(0, 180, 231, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.draw_web_osm_btn.setPalette(palette)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/1344069808_firefox.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.draw_web_osm_btn.setIcon(icon4)
        self.draw_web_osm_btn.setIconSize(QtCore.QSize(32, 32))
        self.draw_web_osm_btn.setObjectName("draw_web_osm_btn")
        self.line_5 = QtGui.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 300, 230, 3))
        self.line_5.setFrameShadow(QtGui.QFrame.Plain)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtGui.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(0, 360, 230, 3))
        self.line_6.setFrameShadow(QtGui.QFrame.Plain)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.geo_comp_btn = QtGui.QCommandLinkButton(self.frame)
        self.geo_comp_btn.setGeometry(QtCore.QRect(0, 240, 231, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.geo_comp_btn.setPalette(palette)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/1344071416_statistics.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.geo_comp_btn.setIcon(icon5)
        self.geo_comp_btn.setIconSize(QtCore.QSize(32, 32))
        self.geo_comp_btn.setObjectName("geo_comp_btn")
        self.geo_calc_btn = QtGui.QCommandLinkButton(self.frame)
        self.geo_calc_btn.setGeometry(QtCore.QRect(0, 300, 231, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.geo_calc_btn.setPalette(palette)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/1344067877_Calculator.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.geo_calc_btn.setIcon(icon6)
        self.geo_calc_btn.setIconSize(QtCore.QSize(32, 32))
        self.geo_calc_btn.setObjectName("geo_calc_btn")
        self.line_7 = QtGui.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(0, 420, 230, 3))
        self.line_7.setFrameShadow(QtGui.QFrame.Plain)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.about_btn = QtGui.QCommandLinkButton(self.frame)
        self.about_btn.setGeometry(QtCore.QRect(0, 360, 231, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.about_btn.setPalette(palette)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/1344071649_consulting.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_btn.setIcon(icon7)
        self.about_btn.setIconSize(QtCore.QSize(32, 32))
        self.about_btn.setObjectName("about_btn")
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(230, 0, 571, 481))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.send_shp_btn, QtCore.SIGNAL("clicked()"), self.sendSHP)
        QtCore.QObject.connect(self.draw_shp_btn, QtCore.SIGNAL("clicked()"), self.drawFromSHPFile)
        QtCore.QObject.connect(self.draw_osm_btn, QtCore.SIGNAL("clicked()"), self.drawFromOSMFile)
        QtCore.QObject.connect(self.draw_web_osm_btn, QtCore.SIGNAL("clicked()"), self.drawFromOSMWeb)
        QtCore.QObject.connect(self.geo_comp_btn, QtCore.SIGNAL("clicked()"), self.showGeoService)
        QtCore.QObject.connect(self.geo_calc_btn, QtCore.SIGNAL("clicked()"), self.showGeoService2)
        QtCore.QObject.connect(self.about_btn, QtCore.SIGNAL("clicked()"), self.showAbout)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.send_shp_btn.setText(QtGui.QApplication.translate("MainWindow", "Send SHP File", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_shp_btn.setText(QtGui.QApplication.translate("MainWindow", "Draw SHP file", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_osm_btn.setText(QtGui.QApplication.translate("MainWindow", "Draw OSM file", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_web_osm_btn.setText(QtGui.QApplication.translate("MainWindow", "Draw OSM file from web", None, QtGui.QApplication.UnicodeUTF8))
        self.geo_comp_btn.setText(QtGui.QApplication.translate("MainWindow", "Geodetic computations", None, QtGui.QApplication.UnicodeUTF8))
        self.geo_calc_btn.setText(QtGui.QApplication.translate("MainWindow", "Geospatial calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.about_btn.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

    def sendSHP(self):
        '''
        @brief: This function is used to show form to send shapefiles to the Postgres database.
        @param None:
        @return: This function does not return a value.
        '''
        
        #Create new form,
        self.Form = QtGui.QWidget()
        #Create new Qt class.
        self.sh = send_shp.Ui_SendSHP()
        #Setup form.
        self.sh.setupUi(self.Form)
        self.Form.show()
        
    def drawFromSHPFile(self):
        '''
        @brief: This function is used to show form to drawing shapefiles.
        @param None:
        @return: This function does not return a value.
        '''
        
        self.DrawFromSHPFile = QtGui.QWidget()
        self.sh = draw_from_shp.Ui_DrawFromSHPFile()
        self.sh.setupUi(self.DrawFromSHPFile)
        self.DrawFromSHPFile.show()
        
    def drawFromOSMFile(self):
        '''
        @brief: This function is used to show form to drawing osm(OpenStreetMap) files.
        @param None:
        @return: This function does not return a value.
        '''
        
        self.DrawFromOSMFile = QtGui.QWidget()
        self.sh = draw_from_osm.Ui_DrawFromOSMFile()
        self.sh.setupUi(self.DrawFromOSMFile)
        self.DrawFromOSMFile.show()
        
    def drawFromOSMWeb(self):
        '''
        @brief: This function is used to show form to drawing osm(OpenStreetMap) from www.
        @param None:
        @return: This function does not return a value.
        '''
        
        self.DrawFromOSMWeb = QtGui.QWidget()
        self.sh = draw_osm_www.Ui_DrawOSMFromWeb()
        self.sh.setupUi(self.DrawFromOSMWeb)
        self.DrawFromOSMWeb.show()
        
    def showGeoService(self):
        '''
        @brief: This function is used to show form to transforming some geodetic projection to the other.
        @param None:
        @return: This function does not return a value.
        '''
        
        self.ShowGeoService = QtGui.QWidget()
        self.sh = geo_services.Ui_GeoServices()
        self.sh.setupUi(self.ShowGeoService)
        self.ShowGeoService.show()
        
    def showGeoService2(self):
        '''
        @brief: This function is used to show form allows compute some geo-spatial data.
        @param None:
        @return: This function does not return a value.
        '''
        
        self.ShowGeoService2 = QtGui.QWidget()
        self.sh = geo.Ui_GeoBasic()
        self.sh.setupUi(self.ShowGeoService2)
        self.ShowGeoService2.show()
        
    def showAbout(self):
        '''
        @brief: This function is used to show about window.
        @param None:
        @return: This function does not return a value.
        '''
        
        self.ShowAbout = QtGui.QWidget()
        self.sh = about.Ui_Form()
        self.sh.setupUi(self.ShowAbout)
        self.ShowAbout.show()
