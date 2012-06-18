# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_main.ui'
#
# Created: Sat May 12 22:15:23 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import send_shp
import draw_from_shp
import draw_from_osm
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
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(0,0,800,400)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.send_shp = QtGui.QPushButton(self.centralwidget)
        self.send_shp.setGeometry(QtCore.QRect(630, 40, 93, 27))
        self.send_shp.setObjectName("send_shp")
        self.draw_shp_from_file = QtGui.QPushButton(self.centralwidget)
        self.draw_shp_from_file.setGeometry(QtCore.QRect(630, 80, 93, 27))
        self.draw_shp_from_file.setObjectName("draw_shp_from_file")
        self.draw_osm_from_file = QtGui.QPushButton(self.centralwidget)
        self.draw_osm_from_file.setGeometry(QtCore.QRect(630, 120, 93, 27))
        self.draw_osm_from_file.setObjectName("draw_osm_from_file")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 20, 241, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_server = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        font.setPointSize(14)
        self.label_server.setFont(font)
        self.label_server.setObjectName("label_server")
        self.horizontalLayout.addWidget(self.label_server)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Connect slots and signals.
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.send_shp, QtCore.SIGNAL("clicked()"), self.sendSHP)
        QtCore.QObject.connect(self.draw_shp_from_file, QtCore.SIGNAL("clicked()"), self.drawFromSHPFile)
        QtCore.QObject.connect(self.draw_osm_from_file, QtCore.SIGNAL("clicked()"), self.drawFromOSMFile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        '''
        @brief: This function is used to translate Qt's items.
        @param MainWindow QMainWindow: Input parameter is QtGui.QMainWindow.
        @return: This function does not return a value.
        '''
        
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.send_shp.setText(QtGui.QApplication.translate("MainWindow", "Send SHP", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_shp_from_file.setText(QtGui.QApplication.translate("MainWindow", "Draw SHP", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_osm_from_file.setText(QtGui.QApplication.translate("MainWindow", "Draw OSM", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Connected to:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_server.setText(QtGui.QApplication.translate("MainWindow", "server", None, QtGui.QApplication.UnicodeUTF8))

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