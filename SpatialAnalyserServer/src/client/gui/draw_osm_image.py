# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw_osm_image.ui'
#
# Created: Sat Jun 16 18:58:04 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import mapnik
import osgeo.ogr
import re
import xml.sax.handler
import sys
from numpy.lib.shape_base import tile

sys.path.append("..")
sys.path.append("../../logger")
sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
sys.path.append("../../../interfaces/projections")
from Client import Client

class Ui_DrawOSMImage(Client):
    '''
    Class Ui_DrawOSMImage is class displays window to drawing osm files. PyQT implementation.
    @author: Bartlomiej Grabowski
    @version: 1.0
    '''
    
    def setupUi(self, DrawOSMImage):
        '''
        @brief: This function is used to setup all elements of the main window.
        @see: Ui_DrawOSMImage
        @param DrawOSMImage QtGui.QWidget: Input parameter is QtGui.QWidget.
        @return: This function does not return a value. 
        '''
        
        DrawOSMImage.setObjectName("DrawOSMImage")
        DrawOSMImage.resize(1024, 768)
        DrawOSMImage.setFixedHeight(768)
        DrawOSMImage.setFixedWidth(1024)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.confIconsDir+'1344068657_image.ico'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DrawOSMImage.setWindowIcon(icon)
        self.osm_name_label = QtGui.QLabel(DrawOSMImage)
        self.osm_name_label.setGeometry(QtCore.QRect(20, 10, 62, 17))
        self.osm_name_label.setObjectName("osm_name_label")
        self.file_name_label = QtGui.QLabel(DrawOSMImage)
        self.file_name_label.setGeometry(QtCore.QRect(90, 10, 351, 17))
        self.file_name_label.setText("")
        self.file_name_label.setObjectName("file_name_label")
        self.osm_image_view = QtGui.QGraphicsView(DrawOSMImage)
        self.osm_image_view.setGeometry(QtCore.QRect(20, 40, 801, 591))
        self.osm_image_view.setObjectName("osm_image_view")
        self.draw_image_button = QtGui.QPushButton(DrawOSMImage)
        self.draw_image_button.setGeometry(QtCore.QRect(880, 40, 91, 27))
        self.draw_image_button.setObjectName("draw_image_button")
        self.clear_image_button = QtGui.QPushButton(DrawOSMImage)
        self.clear_image_button.setGeometry(QtCore.QRect(880, 80, 91, 27))
        self.clear_image_button.setObjectName("clear_image_button")
        self.cancel_window_button = QtGui.QPushButton(DrawOSMImage)
        self.cancel_window_button.setGeometry(QtCore.QRect(880, 120, 91, 27))
        self.cancel_window_button.setObjectName("cancel_window_button")

        self.retranslateUi(DrawOSMImage)
        QtCore.QObject.connect(self.draw_image_button, QtCore.SIGNAL("clicked()"), self.drawOSMFile1)
        QtCore.QObject.connect(self.cancel_window_button, QtCore.SIGNAL("clicked()"), DrawOSMImage,  QtCore.SLOT("close()"))
        QtCore.QObject.connect(self.clear_image_button, QtCore.SIGNAL("clicked()"), self.clearImage)
        QtCore.QMetaObject.connectSlotsByName(DrawOSMImage)

    def retranslateUi(self, DrawOSMImage):
        '''
        @brief: This function is used to translate Qt's items.
        @param DrawOSMImage QWidget: Input parameter is QtGui.QWidget.
        @return: This function does not return a value.
        '''
        
        DrawOSMImage.setWindowTitle(QtGui.QApplication.translate("DrawOSMImage", "Draw OSM image", None, QtGui.QApplication.UnicodeUTF8))
        self.osm_name_label.setText(QtGui.QApplication.translate("DrawOSMImage", "OSM file: ", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_image_button.setText(QtGui.QApplication.translate("DrawOSMImage", "Draw", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_image_button.setText(QtGui.QApplication.translate("DrawOSMImage", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_window_button.setText(QtGui.QApplication.translate("DrawOSMImage", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        
 
     
     
     
    #############################################################
     
     
     
    def render(self, myMap):
     
     
     
        # make dictionary of node IDs
        nodes = {}
        for node in myMap['node']:
            nodes[node['id']] = node
             
        ways = {}
        for way in myMap['way']:
            ways[way['id']]=way
     
     
        import pylab as p
     
     
        renderingRules = {
            'primary': dict(
                    linestyle       = '-',
                    linewidth       = 6,
                    color           ='#ee82ee',
                    zorder          = -1,
                    ),
            'primary_link': dict(
                    linestyle       = '-',
                    linewidth       = 6,
                    color           = '#da70d6',
                    zorder          = -1,           
                    ),
            'secondary': dict(
                    linestyle       = '-',
                    linewidth       = 6,
                    color           = '#d8bfd8',
                    zorder          = -2,           
                    ),
            'secondary_link': dict(
                    linestyle       = '-',
                    linewidth       = 6,
                    color           = '#d8bfd8',
                    zorder          = -2,           
                    ),
            'tertiary': dict(
                    linestyle       = '-',
                    linewidth       = 4,
                    color           = (0.0,0.0,0.7),
                    zorder          = -3,           
                    ),
            'tertiary_link': dict(
                    linestyle       = '-',
                    linewidth       = 4,
                    color           = (0.0,0.0,0.7),
                    zorder          = -3,           
                    ),
            'residential': dict(
                    linestyle       = '-',
                    linewidth       = 1,
                    color           = (0.1,0.1,0.1),
                    zorder          = -99,           
                    ),           
            'unclassified': dict(
                    linestyle       = ':',
                    linewidth       = 1,
                    color           = (0.5,0.5,0.5),
                    zorder          = -1,           
                    ),
            'default': dict(
                    linestyle       = '-',
                    linewidth       = 3,
                    color           = 'b',
                    zorder          = -1,           
                    ),
            }
                             
     
        # get bounds from OSM data           
        minX = float(myMap['bounds']['minlon'])
        maxX = float(myMap['bounds']['maxlon'])
        minY = float(myMap['bounds']['minlat'])
        maxY = float(myMap['bounds']['maxlat'])
     
     
     
        fig = p.figure()
         
        # by setting limits before hand, plotting is about 3 times faster
        ax = fig.add_subplot(111,autoscale_on=False,xlim=(minX,maxX),ylim=(minY,maxY))
         
        for idx,nodeID in enumerate(ways.keys()):
            wayTags         = ways[nodeID]['tag']
            if not wayTags==None:
                hwyTypeList  = [d['v'] for d in wayTags if d['k']=='highway']
                if len(hwyTypeList)>0:
                        wayType = hwyTypeList[0] 
                else:
                        wayType = None
            else:
                wayType = None
            try:
                if wayType in ['primary','primary_link',
                                'unclassified',
                                'secondary','secondary_link',
                                'tertiary','tertiary_link',
                                'residential',
                                'trunk','trunk_link',
                                'motorway','motorway_link',
                                ]:
                    oldX = None
                    oldY = None
                     
                    if wayType in renderingRules.keys():
                        thisRendering = renderingRules[wayType]
                    else:
                        thisRendering = renderingRules['default']
                         
                    for nCnt,nID in enumerate(ways[nodeID]['nd']):
                        y = float(nodes[nID['ref']]['lat'])
                        x = float(nodes[nID['ref']]['lon'])
                        if oldX == None:
                            pass
                        else:
                            p.plot([oldX,x],[oldY,y],
                                marker          = '',
                                linestyle       = thisRendering['linestyle'],
                                linewidth       = thisRendering['linewidth'],
                                color           = thisRendering['color'],
                                solid_capstyle  = 'round',
                                solid_joinstyle = 'round',
                                zorder          = thisRendering['zorder'],
                                )
                        oldX = x
                        oldY = y
                            
            except KeyError:
                pass
               
        p.show()
 
 
 
 
########################################
    def drawOSMFile(self):
        '''
        @brief: This function is used to draw picture from osm file.
        @param None:
        @return: This function does not return a value.
        '''
        
        src = file(self.confOSMDownloadsLoc+str(self.file_name_label.text())+'.osm')
        myMap = self.xml2obj(src)
        self.render(myMap)
        
        
    def drawOSMFile1(self):
        '''
        @brief: This function is used to draw picture from osm file.
        @param None:
        @return: This function does not return a value.
        '''
        
        import time
        
        #Create new scene.
        self.scene = QtGui.QGraphicsScene()
        #Fetch width of QGraphicsView widget.
        self.x = self.osm_image_view.width() - 5
        #Fetch height of QGraphicsView widget.
        self.y = self.osm_image_view.height() - 5
        
        start_timestamp_c = time.time()
        
        self.ostOutFile = self.client_draw_osm_file(str(self.file_name_label.text())+'.osm', long(self.x), long(self.y))       

        self.downloadFile(self.confOSMDownloadsLoc, self.ostOutFile)
        
        stop_timestamp_c = time.time()
        
        print(":::::::::::::::Client timestamps difference: %s" % (stop_timestamp_c - start_timestamp_c))
        
        self.picture = QtGui.QPixmap(self.confOSMDownloadsLoc + str(self.file_name_label.text()) + '.osm' + '.png')
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.osm_image_view.setScene(self.scene)
        
        
    def downloadFile(self, destDir, fileName):
        '''
        @brief: This function is used to download file from server.
        @param destDir string: Input parameter is destination directory.
        @param fileName string: Input parameter is file name. 
        @return: This function does not return a value. Returns 1 if error occurred.
        '''
        
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
 
    def clearImage(self):
        '''Remove all elements from scene.'''
        self.scene.clear()



