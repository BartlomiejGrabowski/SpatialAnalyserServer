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
        self.raster_properties_text = QtGui.QTextBrowser(self.tab_2)
        self.raster_properties_text.setGeometry(QtCore.QRect(8, 90, 911, 441))
        self.raster_properties_text.setObjectName("raster_properties_text")
        self.select_file_btn = QtGui.QPushButton(self.tab_2)
        self.select_file_btn.setGeometry(QtCore.QRect(120, 30, 91, 27))
        self.select_file_btn.setObjectName("select_file_btn")
        self.get_info_btn = QtGui.QPushButton(self.tab_2)
        self.get_info_btn.setGeometry(QtCore.QRect(10, 30, 91, 27))
        self.get_info_btn.setObjectName("get_info_btn")
        self.get_info_btn.setEnabled(False)
        self.path_to_file = QtGui.QLineEdit(self.tab_2)
        self.path_to_file.setGeometry(QtCore.QRect(307, 30, 611, 27))
        self.path_to_file.setObjectName("path_to_file")
        self.label_20 = QtGui.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(260, 40, 41, 17))
        self.label_20.setObjectName("label_20")
        self.services_tab.addTab(self.tab_2, "")
        self.label_21 = QtGui.QLabel(GeoServices)
        self.label_21.setGeometry(QtCore.QRect(10, 590, 62, 17))
        self.label_21.setObjectName("label_21")
        self.status_label = QtGui.QLabel(GeoServices)
        self.status_label.setGeometry(QtCore.QRect(80, 590, 711, 17))
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 511))
        self.groupBox.setObjectName("groupBox")
        self.input_proj_frame = QtGui.QFrame(self.groupBox)
        self.input_proj_frame.setGeometry(QtCore.QRect(10, 20, 371, 471))
        self.input_proj_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.input_proj_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.input_proj_frame.setObjectName("input_proj_frame")
        self.label_22 = QtGui.QLabel(self.input_proj_frame)
        self.label_22.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.label_22.setObjectName("label_22")
        self.input_projection_input = QtGui.QComboBox(self.input_proj_frame)
        self.input_projection_input.setGeometry(QtCore.QRect(130, 10, 231, 31))
        self.input_projection_input.setObjectName("input_projection_input")
        self.label_23 = QtGui.QLabel(self.input_proj_frame)
        self.label_23.setGeometry(QtCore.QRect(10, 60, 120, 20))
        self.label_23.setObjectName("label_23")
        self.output_projection_input = QtGui.QComboBox(self.input_proj_frame)
        self.output_projection_input.setGeometry(QtCore.QRect(130, 50, 231, 31))
        self.output_projection_input.setObjectName("output_projection_input")
        self.label_24 = QtGui.QLabel(self.input_proj_frame)
        self.label_24.setGeometry(QtCore.QRect(10, 190, 111, 17))
        self.label_24.setObjectName("label_24")
        self.coor_x_input = QtGui.QLineEdit(self.input_proj_frame)
        self.coor_x_input.setGeometry(QtCore.QRect(130, 180, 113, 27))
        self.coor_x_input.setObjectName("coor_x_input")
        self.coor_y_input = QtGui.QLineEdit(self.input_proj_frame)
        self.coor_y_input.setGeometry(QtCore.QRect(130, 230, 113, 27))
        self.coor_y_input.setObjectName("coor_y_input")
        self.label_25 = QtGui.QLabel(self.input_proj_frame)
        self.label_25.setGeometry(QtCore.QRect(10, 240, 111, 17))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtGui.QLabel(self.input_proj_frame)
        self.label_26.setGeometry(QtCore.QRect(10, 290, 111, 17))
        self.label_26.setObjectName("label_26")
        self.coor_z_input = QtGui.QLineEdit(self.input_proj_frame)
        self.coor_z_input.setGeometry(QtCore.QRect(130, 280, 113, 27))
        self.coor_z_input.setObjectName("coor_z_input")
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 10, 391, 511))
        self.groupBox_2.setObjectName("groupBox_2")
        self.output_proj_frame = QtGui.QFrame(self.groupBox_2)
        self.output_proj_frame.setGeometry(QtCore.QRect(10, 20, 371, 471))
        self.output_proj_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.output_proj_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.output_proj_frame.setObjectName("output_proj_frame")
        self.coor_output = QtGui.QTextEdit(self.output_proj_frame)
        self.coor_output.setGeometry(QtCore.QRect(10, 10, 351, 231))
        self.coor_output.setObjectName("coor_output")
        self.services_tab.addTab(self.tab_3, "")
        self.label_27 = QtGui.QLabel(self.input_proj_frame)
        self.label_27.setGeometry(QtCore.QRect(10, 320, 241, 17))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtGui.QLabel(self.input_proj_frame)
        self.label_28.setGeometry(QtCore.QRect(10, 360, 62, 17))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtGui.QLabel(self.input_proj_frame)
        self.label_29.setGeometry(QtCore.QRect(10, 380, 62, 17))
        self.label_29.setObjectName("label_29")
        self.input_proj_desc = QtGui.QLabel(self.input_proj_frame)
        self.input_proj_desc.setGeometry(QtCore.QRect(50, 360, 311, 17))
        self.input_proj_desc.setText("")
        self.input_proj_desc.setObjectName("input_proj_desc")
        self.output_proj_desc = QtGui.QLabel(self.input_proj_frame)
        self.output_proj_desc.setGeometry(QtCore.QRect(60, 380, 311, 17))
        self.output_proj_desc.setText("")
        self.output_proj_desc.setObjectName("output_proj_desc")
        self.convert_projection_btn = QtGui.QPushButton(self.input_proj_frame)
        self.convert_projection_btn.setGeometry(QtCore.QRect(260, 430, 91, 27))
        self.convert_projection_btn.setObjectName("convert_projection_btn")
        self.label_30 = QtGui.QLabel(self.input_proj_frame)
        self.label_30.setGeometry(QtCore.QRect(10, 100, 120, 20))
        self.label_30.setObjectName("label_30")
        self.ellipsoid_input = QtGui.QComboBox(self.input_proj_frame)
        self.ellipsoid_input.setGeometry(QtCore.QRect(130, 90, 231, 31))
        self.ellipsoid_input.setObjectName("ellipsoid_input")
        self.additional_param_input = QtGui.QLineEdit(self.input_proj_frame)
        self.additional_param_input.setGeometry(QtCore.QRect(130, 130, 113, 27))
        self.additional_param_input.setObjectName("additional_param_input")
        self.label_31 = QtGui.QLabel(self.input_proj_frame)
        self.label_31.setGeometry(QtCore.QRect(10, 140, 121, 17))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtGui.QLabel(self.input_proj_frame)
        self.label_32.setGeometry(QtCore.QRect(10, 400, 62, 17))
        self.label_32.setObjectName("label_32")
        self.ellipsoid_desc = QtGui.QLabel(self.input_proj_frame)
        self.ellipsoid_desc.setGeometry(QtCore.QRect(70, 400, 291, 20))
        self.ellipsoid_desc.setText("")
        self.ellipsoid_desc.setObjectName("ellipsoid_desc")
        

        self.retranslateUi(GeoServices)
        QtCore.QObject.connect(self.exit_btn , QtCore.SIGNAL("clicked()"), GeoServices, QtCore.SLOT("close()"))
        QtCore.QObject.connect(self.fwd_ok, QtCore.SIGNAL("clicked()"), self.doForwardTransformation)
        QtCore.QObject.connect(self.fwd_clear_all, QtCore.SIGNAL("clicked()"), self.clearFwdFrame)
        QtCore.QObject.connect(self.inv_ok, QtCore.SIGNAL("clicked()"), self.doInvertTransformation)
        QtCore.QObject.connect(self.inv_clear_all, QtCore.SIGNAL("clicked()"), self.clearInvFrame)
        QtCore.QObject.connect(self.inter_ok, QtCore.SIGNAL("clicked()"), self.calculateInterPoints)
        QtCore.QObject.connect(self.inter_clear_all, QtCore.SIGNAL("clicked()"), self.clearInterFrame)
        QtCore.QObject.connect(self.select_file_btn, QtCore.SIGNAL("clicked()"), self.selectRasterFile)
        QtCore.QObject.connect(self.get_info_btn, QtCore.SIGNAL("clicked()"), self.getRasterFileInfo)
        QtCore.QObject.connect(self.input_projection_input, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.getCurrentInDesc)
        QtCore.QObject.connect(self.output_projection_input, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.getCurrentOutDesc)
        QtCore.QObject.connect(self.ellipsoid_input, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.getCurrentEllpsDesc)
        QtCore.QObject.connect(self.convert_projection_btn, QtCore.SIGNAL("clicked()"), self.convertProjection)
        self.services_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GeoServices)
        
        #Fill all combo boxes the data.
        projections = self.client_get_projection_list()
        self.projection_search = dict()
        for projection in projections:
            self.projection_search.update({projection.proj_name : projection.proj_desc})
            self.input_projection_input.addItem(projection.proj_name)
            self.output_projection_input.addItem(projection.proj_name)
            
        ellipsoids = self.client_get_ellipsoid_list()
        self.ellipsoid_search = dict()
        for ellipsoid in ellipsoids:
            self.ellipsoid_search.update({ellipsoid.ellps_name : ellipsoid.ellps_desc})
            self.ellipsoid_input.addItem(ellipsoid.ellps_name)
            
         
        #Set initial projection description.    
        self.input_proj_desc.setText(self.projection_search[str(self.input_projection_input.currentText())])
        self.output_proj_desc.setText(self.projection_search[str(self.output_projection_input.currentText())])
        
        #Set initial ellipsoid description.
        self.ellipsoid_desc.setText(self.ellipsoid_search[str(self.ellipsoid_input.currentText())])
                

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
        self.select_file_btn.setText(QtGui.QApplication.translate("GeoServices", "Select File", None, QtGui.QApplication.UnicodeUTF8))
        self.get_info_btn.setText(QtGui.QApplication.translate("GeoServices", "Get info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("GeoServices", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("GeoServices", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("GeoServices", "Input pramterers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("GeoServices", "Input projection:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("GeoServices", "Output projection:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("GeoServices", "Coordinate X:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("GeoServices", "Coordinate Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("GeoServices", "Coordinate Z:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("GeoServices", "Brief description of the projection:", None, QtGui.QApplication.UnicodeUTF8))
        self.convert_projection_btn.setText(QtGui.QApplication.translate("GeoServices", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("GeoServices", "Input:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("GeoServices", "Output:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("GeoServices", "Ellipsoid:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("GeoServices", "Additional param:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("GeoServices", "Ellipsoid:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("GeoServices", "Output parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.services_tab.setTabText(self.services_tab.indexOf(self.tab_3), QtGui.QApplication.translate("GeoServices", "Change transformation", None, QtGui.QApplication.UnicodeUTF8))

    def getCurrentInDesc(self, curr_item):
        '''
        @brief This function is used to update projection description.
        @param curr_item QString.
        @return This function does not return a value.
        '''
        self.input_proj_desc.setText(self.projection_search[str(curr_item)])
        
    def getCurrentOutDesc(self, curr_item):
        '''
        @brief This function is used to update projection description.
        @param curr_item QString.
        @return This function does not return a value.
        '''
        self.output_proj_desc.setText(self.projection_search[str(curr_item)])
        
    def getCurrentEllpsDesc(self, curr_item):
        '''
        @brief This function is used to update ellipsoid description.
        @param curr_item QString.
        @return This function does not return a value.
        '''
        self.ellipsoid_desc.setText(self.ellipsoid_search[str(curr_item)])
      
    def convertProjection(self):
        '''
        @brief This function is used to convert one projection to another.
        @param None.
        @return This function does not return a value.
        '''
        try:
            x = float(self.coor_x_input.text())
            y = float(self.coor_y_input.text())
            if self.coor_z_input is None:
                z = 0
                self.status_label.setText('Coordinate \'Z\' will be set automatically to a value 0.')
            else:
                z = float(self.coor_z_input.text())
            in_projection = str(self.input_projection_input.currentText())
            out_projection = str(self.output_projection_input.currentText())
            ellipsoid = str(self.ellipsoid_input.currentText())
            params = str(self.additional_param_input.text())
            
            if not params is '':
                self.new_coordinate_system = self.client_transform_coordinate_systems(in_projection+':'+params,
                                                                                      out_projection+':'+params,
                                                                                      x, y, 0, ellipsoid)
            else:
                #Convert transformation.
                self.new_coordinate_system =  self.client_transform_coordinate_systems(in_projection, out_projection,
                                                                                   x, y, 0, ellipsoid)
            
            #Fill output field.
            self.coor_output.clear()
            self.coor_output.append("<font color='blue'>%s -> %s</font>" % (in_projection, out_projection))
            self.coor_output.append("<font color='green'>Coordinate X:</font> %s" % (self.new_coordinate_system.x2))
            self.coor_output.append("<font color='green'>Coordinate Y:</font> %s" % (self.new_coordinate_system.y2))
            self.coor_output.append("<font color='green'>Coordinate Z:</font> %s" % (self.new_coordinate_system.z2))
            self.status_label.setText('OK')
        except (ValueError, RuntimeError):
            err_type, err_value, err_traceback = sys.exc_info()
            print('Error type: %s' % (err_type))
            print('Error value: %s' % (err_value))
            print('Error traceback: %s' % (err_traceback))
            self.status_label.setText('Error: %s' % (err_value)) 
        
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
            self.status_label.setText('OK')
        except ValueError:
            err_type, err_value, err_traceback = sys.exc_info()
            print('Error type: %s' % (err_type))
            print('Error value: %s' % (err_value))
            print('Error traceback: %s' % (err_traceback))
            self.status_label.setText('Error: %s' % (err_value))
       
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
            self.status_label.setText('OK')
        except ValueError:
            err_type, err_value, err_traceback = sys.exc_info()
            print('Error type: %s' % (err_type))
            print('Error value: %s' % (err_value))
            print('Error traceback: %s' % (err_traceback))
            self.status_label.setText('Error: %s' % (err_value))  
        
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
            self.status_label.setText('OK')
        except ValueError:
            err_type, err_value, err_traceback = sys.exc_info()
            print('Error type: %s' % (err_type))
            print('Error value: %s' % (err_value))
            print('Error traceback: %s' % (err_traceback))
            self.status_label.setText('Error: %s' % (err_value))   
        
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
        
        
    def selectRasterFile(self):
        '''
        @brief This function is used to select input raster file.
        @param None
        @return This function does not return a value.
        '''     
        fname = QtGui.QFileDialog.getOpenFileName(QtGui.QWidget(), 'Open')
        if not fname.isEmpty(): 
            self.path_to_file.setText(fname)
            self.get_info_btn.setEnabled(True)
            
    def getRasterFileInfo(self):
        '''
        @brief This function is used to fetch raster file properties.
        Shows them on the QTextBrowser.
        @param None
        @return This function does not return a value.
        ''' 
        raster_file_name = os.path.basename(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Raster file name:</font> %s" % (raster_file_name))
        
        #driver name.
        driver_name = self.client_get_driver_name(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Short driver name:</font> %s" % (driver_name.short_name))
        self.raster_properties_text.append("<font color='green'>Long driver name:</font> %s" % (driver_name.long_name))
        
        #raster size.
        raster_size = self.client_get_raster_size(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Raster x size:</font> %s" % (raster_size.x_size))
        self.raster_properties_text.append("<font color='green'>Raster y size:</font> %s" % (raster_size.y_size))
        
        #pixel size.
        pixel_size = self.client_get_pixel_size(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Pixel x size:</font> %s" % (pixel_size.x_size))
        self.raster_properties_text.append("<font color='green'>Pixel y size:</font> %s" % (pixel_size.y_size))
        
        #origin
        origin = self.client_get_origin(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Origin x:</font> %s" % (origin.top_left_x))
        self.raster_properties_text.append("<font color='green'>Origin y:</font> %s" % (origin.top_left_y))
        
        #projection
        projection = self.client_get_projection_info(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Projection:</font> %s" % (projection))
        
        #raster bands.
        raster_bands = self.client_get_raster_bands(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Number of raster bands:</font> %s" % (raster_bands))
        
        #metadata list
        metadata_list = self.client_get_metadata_list(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Metadata:</font>")
        for metadata in metadata_list:
            self.raster_properties_text.append('\t%s' % (metadata))
            
        #coordinate system.
        coordinate_system = self.client_get_coordinate_system_info(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Coordinate system:</font> %s" % (coordinate_system))
        
        #image structure.
        image_structure = self.client_get_image_structure_info(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Image structure:</font>")
        for item in image_structure:
            self.raster_properties_text.append('\t%s' % (item))
            
        #image corners.
        corner_list = self.client_get_image_corners(str(self.path_to_file.text()))
        self.raster_properties_text.append("<font color='green'>Corner list:</font>")
        self.raster_properties_text.append('\tUpper Left: (%s, %s)' \
                                            % (corner_list[0].x, corner_list[0].y))
        self.raster_properties_text.append('\tLower Left: (%s, %s)' \
                                            % (corner_list[1].x, corner_list[1].y))
        self.raster_properties_text.append('\tUpper Right: (%s, %s)' \
                                            % (corner_list[2].x, corner_list[2].y))
        self.raster_properties_text.append('\tUpper Right: (%s, %s)' \
                                            % (corner_list[3].x, corner_list[3].y))
        self.raster_properties_text.append('\tCenter: (%s, %s)' \
                                            % (corner_list[4].x, corner_list[4].y))