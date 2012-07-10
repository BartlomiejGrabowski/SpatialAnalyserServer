# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geo_services.ui'
#
# Created: Tue Jul 10 17:24:47 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
sys.path.append("..")
sys.path.append("../../logger")
sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
sys.path.append("../../../interfaces/projections")
from Client import Client

class Ui_GeoServices(Client):
    '''
    Class Ui_GeoServices is class displays window to transform input projection to the other. PyQT implementation.
    @author: Bartlomiej Grabowski
    @version: 1.0
    '''
    
    def setupUi(self, GeoServices):
        '''
        @brief: This function is used to setup all elements of the main window.
        @see: Ui_GeoServices
        @param GeoServices QtGui.QWidget: Input parameter is QtGui.QWidget.
        @return: This function does not return a value. 
        '''
        
        GeoServices.setObjectName("GeoServices")
        GeoServices.resize(937, 617)
        self.services_tab = QtGui.QTabWidget(GeoServices)
        self.services_tab.setGeometry(QtCore.QRect(0, 0, 931, 571))
        self.services_tab.setObjectName("services_tab")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.fwd_group = QtGui.QGroupBox(self.tab)
        self.fwd_group.setGeometry(QtCore.QRect(10, 10, 291, 521))
        self.fwd_group.setAutoFillBackground(False)
        self.fwd_group.setFlat(False)
        self.fwd_group.setCheckable(False)
        self.fwd_group.setObjectName("fwd_group")
        self.fwd_frame = QtGui.QFrame(self.fwd_group)
        self.fwd_frame.setGeometry(QtCore.QRect(0, 20, 281, 501))
        self.fwd_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fwd_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.fwd_frame.setObjectName("fwd_frame")
        self.fwd_ok = QtGui.QPushButton(self.fwd_frame)
        self.fwd_ok.setGeometry(QtCore.QRect(180, 470, 91, 27))
        self.fwd_ok.setObjectName("fwd_ok")
        self.fwd_clear_all = QtGui.QPushButton(self.fwd_frame)
        self.fwd_clear_all.setGeometry(QtCore.QRect(10, 470, 91, 27))
        self.fwd_clear_all.setObjectName("fwd_clear_all")
        self.label = QtGui.QLabel(self.fwd_frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.label.setObjectName("label")
        self.label_4 = QtGui.QLabel(self.fwd_frame)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 81, 17))
        self.label_4.setObjectName("label_4")
        self.fwd_lons_input = QtGui.QLineEdit(self.fwd_frame)
        self.fwd_lons_input.setGeometry(QtCore.QRect(140, 40, 113, 27))
        self.fwd_lons_input.setObjectName("fwd_lons_input")
        self.label_5 = QtGui.QLabel(self.fwd_frame)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 81, 17))
        self.label_5.setObjectName("label_5")
        self.fwd_lat_input = QtGui.QLineEdit(self.fwd_frame)
        self.fwd_lat_input.setGeometry(QtCore.QRect(140, 80, 113, 27))
        self.fwd_lat_input.setObjectName("fwd_lat_input")
        self.label_6 = QtGui.QLabel(self.fwd_frame)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 81, 17))
        self.label_6.setObjectName("label_6")
        self.fwd_az_input = QtGui.QLineEdit(self.fwd_frame)
        self.fwd_az_input.setGeometry(QtCore.QRect(140, 120, 113, 27))
        self.fwd_az_input.setObjectName("fwd_az_input")
        self.label_7 = QtGui.QLabel(self.fwd_frame)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 81, 17))
        self.label_7.setObjectName("label_7")
        self.fwd_dist_input = QtGui.QLineEdit(self.fwd_frame)
        self.fwd_dist_input.setGeometry(QtCore.QRect(140, 160, 113, 27))
        self.fwd_dist_input.setObjectName("fwd_dist_input")
        self.label_8 = QtGui.QLabel(self.fwd_frame)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 71, 17))
        self.label_8.setObjectName("label_8")
        self.fwd_output = QtGui.QTextEdit(self.fwd_frame)
        self.fwd_output.setGeometry(QtCore.QRect(10, 250, 261, 201))
        self.fwd_output.setObjectName("fwd_output")
        self.inv_group = QtGui.QGroupBox(self.tab)
        self.inv_group.setGeometry(QtCore.QRect(320, 10, 281, 521))
        self.inv_group.setObjectName("inv_group")
        self.inv_frame = QtGui.QFrame(self.inv_group)
        self.inv_frame.setGeometry(QtCore.QRect(0, 20, 281, 501))
        self.inv_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.inv_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.inv_frame.setObjectName("inv_frame")
        self.inv_ok = QtGui.QPushButton(self.inv_frame)
        self.inv_ok.setGeometry(QtCore.QRect(180, 470, 91, 27))
        self.inv_ok.setObjectName("inv_ok")
        self.inv_clear_all = QtGui.QPushButton(self.inv_frame)
        self.inv_clear_all.setGeometry(QtCore.QRect(10, 470, 91, 27))
        self.inv_clear_all.setObjectName("inv_clear_all")
        self.label_2 = QtGui.QLabel(self.inv_frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.label_2.setObjectName("label_2")
        self.label_9 = QtGui.QLabel(self.inv_frame)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 110, 17))
        self.label_9.setObjectName("label_9")
        self.inv_e_lons_input = QtGui.QLineEdit(self.inv_frame)
        self.inv_e_lons_input.setGeometry(QtCore.QRect(140, 120, 113, 27))
        self.inv_e_lons_input.setObjectName("inv_e_lons_input")
        self.label_10 = QtGui.QLabel(self.inv_frame)
        self.label_10.setGeometry(QtCore.QRect(10, 170, 101, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(self.inv_frame)
        self.label_11.setGeometry(QtCore.QRect(10, 130, 101, 17))
        self.label_11.setObjectName("label_11")
        self.inv_e_lat_input = QtGui.QLineEdit(self.inv_frame)
        self.inv_e_lat_input.setGeometry(QtCore.QRect(140, 160, 113, 27))
        self.inv_e_lat_input.setObjectName("inv_e_lat_input")
        self.label_12 = QtGui.QLabel(self.inv_frame)
        self.label_12.setGeometry(QtCore.QRect(10, 90, 101, 17))
        self.label_12.setObjectName("label_12")
        self.inv_s_lons_input = QtGui.QLineEdit(self.inv_frame)
        self.inv_s_lons_input.setGeometry(QtCore.QRect(140, 40, 113, 27))
        self.inv_s_lons_input.setObjectName("inv_s_lons_input")
        self.inv_s_lat_input = QtGui.QLineEdit(self.inv_frame)
        self.inv_s_lat_input.setGeometry(QtCore.QRect(140, 80, 113, 27))
        self.inv_s_lat_input.setObjectName("inv_s_lat_input")
        self.inv_output = QtGui.QTextEdit(self.inv_frame)
        self.inv_output.setGeometry(QtCore.QRect(10, 250, 261, 201))
        self.inv_output.setObjectName("inv_output")
        self.label_13 = QtGui.QLabel(self.inv_frame)
        self.label_13.setGeometry(QtCore.QRect(10, 230, 71, 17))
        self.label_13.setObjectName("label_13")
        self.inter_group = QtGui.QGroupBox(self.tab)
        self.inter_group.setGeometry(QtCore.QRect(630, 10, 281, 521))
        self.inter_group.setObjectName("inter_group")
        self.inter_frame = QtGui.QFrame(self.inter_group)
        self.inter_frame.setGeometry(QtCore.QRect(0, 20, 281, 501))
        self.inter_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.inter_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.inter_frame.setObjectName("inter_frame")
        self.inter_ok = QtGui.QPushButton(self.inter_frame)
        self.inter_ok.setGeometry(QtCore.QRect(180, 470, 91, 27))
        self.inter_ok.setObjectName("inter_ok")
        self.inter_clear_all = QtGui.QPushButton(self.inter_frame)
        self.inter_clear_all.setGeometry(QtCore.QRect(10, 470, 91, 27))
        self.inter_clear_all.setObjectName("inter_clear_all")
        self.label_3 = QtGui.QLabel(self.inter_frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.label_3.setObjectName("label_3")
        self.label_14 = QtGui.QLabel(self.inter_frame)
        self.label_14.setGeometry(QtCore.QRect(10, 90, 101, 17))
        self.label_14.setObjectName("label_14")
        self.inter_e_lat_input = QtGui.QLineEdit(self.inter_frame)
        self.inter_e_lat_input.setGeometry(QtCore.QRect(140, 160, 113, 27))
        self.inter_e_lat_input.setObjectName("inter_e_lat_input")
        self.label_15 = QtGui.QLabel(self.inter_frame)
        self.label_15.setGeometry(QtCore.QRect(10, 50, 110, 17))
        self.label_15.setObjectName("label_15")
        self.inter_s_lat_input = QtGui.QLineEdit(self.inter_frame)
        self.inter_s_lat_input.setGeometry(QtCore.QRect(140, 80, 113, 27))
        self.inter_s_lat_input.setObjectName("inter_s_lat_input")
        self.label_16 = QtGui.QLabel(self.inter_frame)
        self.label_16.setGeometry(QtCore.QRect(10, 130, 101, 17))
        self.label_16.setObjectName("label_16")
        self.inter_s_lons_input = QtGui.QLineEdit(self.inter_frame)
        self.inter_s_lons_input.setGeometry(QtCore.QRect(140, 40, 113, 27))
        self.inter_s_lons_input.setObjectName("inter_s_lons_input")
        self.label_17 = QtGui.QLabel(self.inter_frame)
        self.label_17.setGeometry(QtCore.QRect(10, 170, 101, 17))
        self.label_17.setObjectName("label_17")
        self.inter_e_lons_input = QtGui.QLineEdit(self.inter_frame)
        self.inter_e_lons_input.setGeometry(QtCore.QRect(140, 120, 113, 27))
        self.inter_e_lons_input.setObjectName("inter_e_lons_input")
        self.inter_nop_input = QtGui.QLineEdit(self.inter_frame)
        self.inter_nop_input.setGeometry(QtCore.QRect(140, 200, 113, 27))
        self.inter_nop_input.setObjectName("inter_nop_input")
        self.label_18 = QtGui.QLabel(self.inter_frame)
        self.label_18.setGeometry(QtCore.QRect(10, 210, 121, 17))
        self.label_18.setObjectName("label_18")
        self.inter_output = QtGui.QTextEdit(self.inter_frame)
        self.inter_output.setGeometry(QtCore.QRect(10, 250, 261, 201))
        self.inter_output.setObjectName("inter_output")
        self.label_19 = QtGui.QLabel(self.inter_frame)
        self.label_19.setGeometry(QtCore.QRect(10, 230, 71, 17))
        self.label_19.setObjectName("label_19")
        self.services_tab.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.services_tab.addTab(self.tab_2, "")
        self.exit_btn = QtGui.QPushButton(GeoServices)
        self.exit_btn.setGeometry(QtCore.QRect(820, 580, 91, 27))
        self.exit_btn.setObjectName("pushButton")

        self.retranslateUi(GeoServices)
        QtCore.QObject.connect(self.exit_btn , QtCore.SIGNAL("clicked()"), GeoServices, QtCore.SLOT("close()"))
        QtCore.QObject.connect(self.fwd_ok, QtCore.SIGNAL("clicked()"), self.doForwardTransformation)
        QtCore.QObject.connect(self.fwd_clear_all, QtCore.SIGNAL("clicked()"), self.clearFwdFrame)
        QtCore.QObject.connect(self.inv_ok, QtCore.SIGNAL("clicked()"), self.doInvertTransformation)
        QtCore.QObject.connect(self.inv_clear_all, QtCore.SIGNAL("clicked()"), self.clearInvFrame)
        QtCore.QObject.connect(self.inter_ok, QtCore.SIGNAL("clicked()"), self.calculateInterPoints)
        QtCore.QObject.connect(self.inter_clear_all, QtCore.SIGNAL("clicked()"), self.clearInterFrame)
        self.services_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GeoServices)

    def retranslateUi(self, GeoServices):
        GeoServices.setWindowTitle(QtGui.QApplication.translate("GeoServices", "Geo-services", None, QtGui.QApplication.UnicodeUTF8))
        self.fwd_group.setTitle(QtGui.QApplication.translate("GeoServices", "Forward transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.fwd_ok.setText(QtGui.QApplication.translate("GeoServices", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.fwd_clear_all.setText(QtGui.QApplication.translate("GeoServices", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GeoServices", "Input parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("GeoServices", "Longitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("GeoServices", "Latitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("GeoServices", "Azimuth:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("GeoServices", "Distance:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("GeoServices", "Result:", None, QtGui.QApplication.UnicodeUTF8))
        self.inv_group.setTitle(QtGui.QApplication.translate("GeoServices", "Invert transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.inv_ok.setText(QtGui.QApplication.translate("GeoServices", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.inv_clear_all.setText(QtGui.QApplication.translate("GeoServices", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GeoServices", "Input parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("GeoServices", "Start longitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("GeoServices", "End latitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("GeoServices", "End longitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("GeoServices", "Start latitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("GeoServices", "Result:", None, QtGui.QApplication.UnicodeUTF8))
        self.inter_group.setTitle(QtGui.QApplication.translate("GeoServices", "Intermediate points", None, QtGui.QApplication.UnicodeUTF8))
        self.inter_ok.setText(QtGui.QApplication.translate("GeoServices", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.inter_clear_all.setText(QtGui.QApplication.translate("GeoServices", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GeoServices", "Input parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("GeoServices", "Start latitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("GeoServices", "Start longitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("GeoServices", "End longitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("GeoServices", "End latitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("GeoServices", "Number of points:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("GeoServices", "Result:", None, QtGui.QApplication.UnicodeUTF8))
        self.services_tab.setTabText(self.services_tab.indexOf(self.tab), QtGui.QApplication.translate("GeoServices", "Projection transformations", None, QtGui.QApplication.UnicodeUTF8))
        self.services_tab.setTabText(self.services_tab.indexOf(self.tab_2), QtGui.QApplication.translate("GeoServices", "Raster properties", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_btn.setText(QtGui.QApplication.translate("GeoServices", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

    def doForwardTransformation(self):
        ''' 
        @brief This function is used to compute forward transformation.
        @param None
        @return This function does not return a value. 
        '''
        try:
            longitude = float(self.fwd_lons_input.text())
            latitude = float(self.fwd_lat_input.text())
            azimuth = float(self.fwd_az_input.text())
            distance = float(self.fwd_dist_input.text())
            #Compute forward transformation.
            self.fwd_transformation = self.client_get_fwd_transformation(longitude, latitude, azimuth, distance)
            #First of all clear text edit.
            self.fwd_output.clear()
            self.fwd_output.append('Transformation results')
            self.fwd_output.append('\n')
            self.fwd_output.append('End longitude: %s' % (self.fwd_transformation.end_longitude))
            self.fwd_output.append('End latitude: %s' % (self.fwd_transformation.end_latitude))
            self.fwd_output.append('Back azimuth: %s' % (self.fwd_transformation.back_azimuth))
        except ValueError:
            err_type, err_value, err_traceback = sys.exc_info()
            print('Error type: %s' % (err_type))
            print('Error value: %s' % (err_value))
            print('Error traceback: %s' % (err_traceback))
       
    def clearFwdFrame(self):
        '''
        @brief This function is used clear all input fields.
        @param None
        @return This function does not return a value.
        '''
        self.fwd_lat_input.clear()
        self.fwd_lons_input.clear()
        self.fwd_az_input.clear()
        self.fwd_dist_input.clear()
        self.fwd_output.clear()
        
    def doInvertTransformation(self):
        ''' 
        @brief This function is used to compute invert transformation.
        @param None
        @return This function does not return a value. 
        '''
        try:
            start_longitude = float(self.inv_s_lons_input.text())
            start_latitude = float(self.inv_s_lat_input.text())
            end_longitude = float(self.inv_e_lons_input.text())
            end_latitude = float(self.inv_e_lat_input.text())
            print('start long: %s' % (start_longitude))
            print('start lat: %s' % (start_latitude))
            print('end long: %s' % (end_longitude))
            print('end lat: %s' % (end_latitude))
            #Compute forward transformation.
            self.inv_transformation = self.client_get_inv_transformation(start_longitude, start_latitude, 
                                                                        end_longitude, end_latitude)
            #First of all clear text edit.
            self.inv_output.clear()
            self.inv_output.append('Transformation results')
            self.inv_output.append('\n')
            self.inv_output.append('Azimuth: %s' % (self.inv_transformation.trans_azimuth))
            self.inv_output.append('Back azimuth: %s' % (self.inv_transformation.back_azimuth))
            self.inv_output.append('Distance: %s' % (self.inv_transformation.dist))
        except ValueError:
            err_type, err_value, err_traceback = sys.exc_info()
            print('Error type: %s' % (err_type))
            print('Error value: %s' % (err_value))
            print('Error traceback: %s' % (err_traceback))    
        
    def clearInvFrame(self):
        '''
        @brief This function is used clear all input fields.
        @param None
        @return This function does not return a value.
        '''
        self.inv_s_lons_input.clear()
        self.inv_s_lat_input.clear()
        self.inv_e_lons_input.clear()
        self.inv_e_lat_input.clear()
        self.inv_output.clear()
        
    def calculateInterPoints(self):
        ''' 
        @brief This function is used to calculate intetmediate points.
        @param None
        @return This function does not return a value. 
        '''
        try:
            start_longitude = float(self.inter_s_lons_input.text())
            start_latitude = float(self.inter_s_lat_input.text())
            end_longitude = float(self.inter_e_lons_input.text())
            end_latitude = float(self.inter_e_lat_input.text())
            nop = int(self.inter_nop_input.text())
            print(start_longitude)
            print(start_latitude)
            print(end_longitude)
            print(end_latitude)
            print(nop)
            #Compute forward transformation.
            self.intermediate_points = self.client_get_intermediate_points(start_longitude, start_latitude, 
                                                                        end_longitude, end_latitude, nop)
            #First of all clear text edit.
            self.inter_output.clear()
            self.inter_output.append('Intermediate points:')
            self.inter_output.append('\n')
            for point in self.intermediate_points:
                self.inter_output.append('(%s, %s)' % (point.end_longitude, point.end_latitude))
        except ValueError:
            err_type, err_value, err_traceback = sys.exc_info()
            print('Error type: %s' % (err_type))
            print('Error value: %s' % (err_value))
            print('Error traceback: %s' % (err_traceback))    
        
    def clearInterFrame(self):
        '''
        @brief This function is used clear all input fields.
        @param None
        @return This function does not return a value.
        '''
        self.inter_s_lons_input.clear()
        self.inter_s_lat_input.clear()
        self.inter_e_lons_input.clear()
        self.inter_e_lat_input.clear()
        self.inter_nop_input.clear()
        self.inter_output.clear()              
        
