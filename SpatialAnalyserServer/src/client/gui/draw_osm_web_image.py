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
from PyQt4.pyqtconfig import QtCoreModuleMakefile

sys.path.append("..")
sys.path.append("../../logger")
sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
sys.path.append("../../../interfaces/projections")

from Client import Client

class Ui_DrawOSMImage(Client):
    '''
    Class Ui_DrawOSMImage is class displays window to drawing osm from website. PyQT implementation.
    @author: Bartlomiej Grabowski
    @version: 1.0
    '''
    
    def __init__(self, osmUrl, minlat, maxlat, minlon, maxlon):
        #Fill input parameters.
        self.osmUrl = str(osmUrl)
        self.minlat = str(minlat)
        self.maxlat = str(maxlat)
        self.minlon = str(minlon)
        self.maxlon = str(maxlon)
        
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
        icon.addPixmap(QtGui.QPixmap('icons/1344069808_firefox.ico'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DrawOSMImage.setWindowIcon(icon)
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
        QtCore.QObject.connect(self.draw_image_button, QtCore.SIGNAL("clicked()"), self.drawOSMWeb)
        QtCore.QObject.connect(self.cancel_window_button, QtCore.SIGNAL("clicked()"), DrawOSMImage,  QtCore.SLOT("close()"))
        QtCore.QObject.connect(self.clear_image_button, QtCore.SIGNAL("clicked()"), self.clearImage)
        QtCore.QMetaObject.connectSlotsByName(DrawOSMImage)

    def retranslateUi(self, DrawOSMImage):
        '''
        @brief: This function is used to translate Qt's items.
        @param DrawOSMImage QWidget: Input parameter is QtGui.QWidget.
        @return: This function does not return a value.
        '''
        
        DrawOSMImage.setWindowTitle(QtGui.QApplication.translate("DrawOSMImage", "Draw OSM image from Web", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_image_button.setText(QtGui.QApplication.translate("DrawOSMImage", "Draw", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_image_button.setText(QtGui.QApplication.translate("DrawOSMImage", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_window_button.setText(QtGui.QApplication.translate("DrawOSMImage", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        
 
        
    def fillHighwayColor(self, lineStyle, kind, color, thickness):
        '''
        @brief: This function is used to fill highways color.
        @param lineStyle mapnik.Style: Input parameter is mapnik style.
        @param kind string: Input parameter is kind of highway.
        @param color string: Input parameters is highway color.
        @param thickness float: Input parameter is line thickness.  
        @return: This function does not return a value.
        '''
        
        rule = mapnik.Rule()
        rule.filter = mapnik.Expression("[highway] = '%s'" % (kind))
        #Set outline color.
        #symbol = mapnik.LineSymbolizer(mapnik.Color(color), thickness)
        l = mapnik.LineSymbolizer()
        s = mapnik.Stroke(mapnik.Color(color), thickness)
        
        if kind == 'path' or kind == 'tram':
            s.add_dash(2.5, 1.5)
            
        l.stroke = s
        rule.symbols.append(l)
        lineStyle.rules.append(rule)

        
        symbol = mapnik.TextSymbolizer(mapnik.Expression("[name]"), 'DejaVu Sans Book', 10, mapnik.Color('black'))
        #symbol.properties.label_placement = mapnik.label_placement.LINE_PLACEMENT
        #symbol.properties.label_position_tolerance = mapnik.label_placement.INTERIOR_PLACEMENT
        
        rule.symbols.append(symbol)
        lineStyle.rules.append(rule)
        
    def fillLanduseColor(self, polygonStyle, kind, color):
        '''
        @brief: This function is used to fill lands color.
        @param lineStyle mapnik.Style: Input parameter is mapnik style.
        @param kind string: Input parameter is kind of land.
        @param color string: Input parameters is land color. 
        @return: This function does not return a value.
        '''
        
        rule = mapnik.Rule()
        rule.filter = mapnik.Expression("[landuse] = '%s'" % (kind))
        #Set polygon's color.
        symbol = mapnik.PolygonSymbolizer(mapnik.Color(color))
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
        symbol = mapnik.TextSymbolizer(mapnik.Expression("[name]"), 'DejaVu Sans Book', 10, mapnik.Color('black'))
        
        
        #symbol.label_placement = mapnik.label_placement.LINE_PLACEMENT
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)

        
    def fillLaisureColor(self, polygonStyle, kind, color):
        '''
        @brief: This function is used to fill laisure color.
        @param lineStyle mapnik.Style: Input parameter is mapnik style.
        @param kind string: Input parameter is kind of laisure.
        @param color string: Input parameters is laisure color. 
        @return: This function does not return a value.
        '''
        
        
        rule = mapnik.Rule()
        rule.filter = mapnik.Expression("[laisure] = '%s'" % (kind))
        #Set polygon's color.
        symbol = mapnik.PolygonSymbolizer(mapnik.Color(color))
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
    def fillBuildingColor(self, polygonStyle, kind, color):
        '''
        @brief: This function is used to fill building color.
        @param lineStyle mapnik.Style: Input parameter is mapnik style.
        @param kind string: Input parameter is kind of building.
        @param color string: Input parameters is building color. 
        @return: This function does not return a value.
        '''
        
        
        rule = mapnik.Rule()
        rule.filter = mapnik.Expression("[building] = '%s'" % (kind))
        #Set polygon's color.
        symbol = mapnik.PolygonSymbolizer(mapnik.Color(color))
        #symbol.fill.color = 'black'
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
        symbol = mapnik.TextSymbolizer(mapnik.Expression("[name]"), 'DejaVu Sans Book', 10, mapnik.Color('black'))
        
        #symbol.label_placement = mapnik.label_placement.LINE_PLACEMENT
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
    def fillNaturalColor(self, polygonStyle, kind, color):
        '''
        @brief: This function is used to fill natural color.
        @param lineStyle mapnik.Style: Input parameter is mapnik style.
        @param kind string: Input parameter is kind of natural.
        @param color string: Input parameters is natural color. 
        @return: This function does not return a value.
        '''
        
        rule = mapnik.Rule()
        rule.filter = mapnik.Expression("[natural] = '%s'" % (kind))
        #Set polygon's color.
        symbol = mapnik.PolygonSymbolizer(mapnik.Color(color))
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
    def fillRailwayColor(self, lineStyle, kind, color, thickness):
        '''
        @brief: This function is used to fill railways color.
        @param lineStyle mapnik.Style: Input parameter is mapnik style.
        @param kind string: Input parameter is kind of railway.
        @param color string: Input parameters is railway color.
        @param thickness float: Input parameter is line thickness.  
        @return: This function does not return a value.
        '''
        
        rule = mapnik.Rule()
        rule.filter = mapnik.Expression("[railway] = '%s'" % (kind))
        #Set outline color.
        #symbol = mapnik.LineSymbolizer(mapnik.Color(color), thickness)
        l = mapnik.LineSymbolizer()
        s = mapnik.Stroke(mapnik.Color(color), thickness)

        s.add_dash(8.0, 8.0)
            
        l.stroke = s
        rule.symbols.append(l)
        lineStyle.rules.append(rule)

        
        symbol = mapnik.TextSymbolizer(mapnik.Expression("[name]"), 'DejaVu Sans Book', 10, mapnik.Color('black'))
        
        rule.symbols.append(symbol)
        lineStyle.rules.append(rule)
        
    def fillWaterwayColor(self, polygonStyle, kind, color):
        '''
        @brief: This function is used to fill waterways color.
        @param lineStyle mapnik.Style: Input parameter is mapnik style.
        @param kind string: Input parameter is kind of waterway.
        @param color string: Input parameters is waterway color. 
        @return: This function does not return a value.
        '''
        
        
        rule = mapnik.Rule()
        rule.filter = mapnik.Expression("[waterway] = '%s'" % (kind))
        #Set polygon's color.
        symbol = mapnik.PolygonSymbolizer(mapnik.Color(color))
        #symbol.fill.color = 'black'
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
        symbol = mapnik.TextSymbolizer(mapnik.Expression("[name]"), 'DejaVu Sans Book', 10, mapnik.Color('black'))
        
        #symbol.label_placement = mapnik.label_placement.LINE_PLACEMENT
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
    def fillPlaceColor(self, polygonStyle, kind, color):
        '''
        @brief: This function is used to fill places color.
        @param lineStyle mapnik.Style: Input parameter is mapnik style.
        @param kind string: Input parameter is kind of place.
        @param color string: Input parameters is place color. 
        @return: This function does not return a value.
        '''
        
        
        rule = mapnik.Rule()
        rule.filter = mapnik.Expression("[place] = '%s'" % (kind))
        #Set polygon's color.
        symbol = mapnik.PolygonSymbolizer(mapnik.Color(color))
        #symbol.fill.color = 'black'
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
        symbol = mapnik.TextSymbolizer(mapnik.Expression("[name]"), 'DejaVu Sans Book', 10, mapnik.Color('black'))
        
        #symbol.label_placement = mapnik.label_placement.LINE_PLACEMENT
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
        
    def drawOSMWeb(self):
        '''
        @brief: This function is used to draw picture from osm file.
        @param None:
        @return: This function does not return a value.
        '''
        
        #Create new scene.
        self.scene = QtGui.QGraphicsScene()
        #Fetch width of QGraphicsView widget.
        self.x = self.osm_image_view.width() - 5
        #Fetch height of QGraphicsView widget.
        self.y = self.osm_image_view.height() - 5
        
        #Set map size and projection type.
        m = mapnik.Map(self.x,self.y, "+proj=latlong +datum=WGS84")
        
        #Set background color.
        m.background = mapnik.Color('#F8F8F8')
        
        # Styles

        #Create polygon style.
        polygonStyle = mapnik.Style()
        #Create new rule for polygons.
        
        #PLACES.
        
        #Coloring suburbs.
        self.fillPlaceColor(polygonStyle, 'suburb', 'white')
        
        #NATURALS.
        
        #Coloring water.
        self.fillNaturalColor(polygonStyle, 'water', 'lightblue')
        
        #Coloring marshes.
        self.fillNaturalColor(polygonStyle, 'marsh', 'blue')
        
        #Coloring beaches.
        self.fillNaturalColor(polygonStyle, 'beach', '#FFFF66')
        
        #Coloring lands.
        self.fillNaturalColor(polygonStyle, 'land', '#CCCC99')
        
        #Coloring coastlines.
        self.fillNaturalColor(polygonStyle, 'coastline', '#8BCCE5')
        
        #Coloring scrubs.
        self.fillNaturalColor(polygonStyle, 'scrub', '#99EE9C')
        
        #Coloring woods.
        self.fillNaturalColor(polygonStyle, 'wood', '#99DB9C')
        
        #Coloring heaths.
        self.fillNaturalColor(polygonStyle, 'heath', '#EFEDA5')
        
        #Coloring fells.
        self.fillNaturalColor(polygonStyle, 'fell', '#CDDB69')
        
        
        #WATERWAYS.
        
        #Coloring rivers.
        self.fillWaterwayColor(polygonStyle, 'river', 'lightblue')
        
        #Coloring drains.
        self.fillWaterwayColor(polygonStyle, 'drain', 'lightblue')        
        
        #Coloring streams.
        self.fillWaterwayColor(polygonStyle, 'stream', 'lightblue')
        
        #Coloring canals.
        self.fillWaterwayColor(polygonStyle, 'canal', 'lightblue')
        
        #Coloring riverbanks.
        self.fillWaterwayColor(polygonStyle, 'riverbank', 'lightblue')
        
        
        #Coloring forests.
        self.fillLanduseColor(polygonStyle, 'forest', '#CFECA8')
        
        #Coloring residentials.
        self.fillLanduseColor(polygonStyle, 'residential', '#DCDCDC')
        
        #Coloring constructions.
        self.fillLanduseColor(polygonStyle, 'construction', '#CCCCCC')
        
        #Coloring grasses.
        self.fillLanduseColor(polygonStyle, 'grass', '#28d25c')
        
        #Coloring industrials.
        self.fillLanduseColor(polygonStyle, 'industrial', '#FEADB8')
        
        #Coloring retails.
        self.fillLanduseColor(polygonStyle, 'retail', '#F0DADA')
        
        #Coloring cemeteries.
        self.fillLanduseColor(polygonStyle, 'cemetery', '#A9CAAE')
        
        #Coloring allotments.
        self.fillLanduseColor(polygonStyle, 'allotments', '#C8B084')
             
        
        #BUILDINGS.
        
        #Coloring blocks.
        self.fillBuildingColor(polygonStyle, 'residential', '#F3D6B6')
        
        #Coloring any.
        self.fillBuildingColor(polygonStyle, '*', '#6B5B8E')
        
        
        #Coloring parks.
        self.fillLaisureColor(polygonStyle, 'park', '#00CC99')
        
        #Coloring commons.
        self.fillLaisureColor(polygonStyle, 'common', '#CFECA8')
        
        
        #Create new outlines style.
        lineStyle = mapnik.Style()

        #Coloring primary highways.
        self.fillHighwayColor(lineStyle, 'primary', '#FF3333', 4.0)
        
        #Coloring primary link highways.
        self.fillHighwayColor(lineStyle, 'primary_link', '#FF3333', 4.0)
        
        #Coloring secondary highways.
        self.fillHighwayColor(lineStyle, 'secondary', '#FF9966', 2.0)
        
        #Coloring secondary link highways.
        self.fillHighwayColor(lineStyle, 'secondary_link', '#FF9966', 2.0)
        
        #Coloring motorway highways.
        self.fillHighwayColor(lineStyle, 'motorway', '#33CCFF', 4.0)    

        #Coloring motorway link highways.
        self.fillHighwayColor(lineStyle, 'motorway_link', '#3366FF', 4.0)
        
        #Coloring trunk highways.
        self.fillHighwayColor(lineStyle, 'trunk', '#339900', 2.0)    

        #Coloring trunk link highways.
        self.fillHighwayColor(lineStyle, 'trunk_link', '#33FF66', 2.0)
        
        #Coloring trietary highways.
        self.fillHighwayColor(lineStyle, 'trietary', '#FFFF99', 2.0)    

        #Coloring trietary link highways.
        self.fillHighwayColor(lineStyle, 'trietary_link', '#FFFF99', 2.0)
        
        #Coloring living_street highways.
        self.fillHighwayColor(lineStyle, 'living_street', '#FF6666', 2.0)    

        #Coloring pedestrian highways.
        self.fillHighwayColor(lineStyle, 'pedestrian', '#FFCFA4', 7.0)
        
        #Coloring residential highways.
        self.fillHighwayColor(lineStyle, 'residential', '#C6C6FF', 3.0)    

        #Coloring unclassified highways.
        self.fillHighwayColor(lineStyle, 'unclassified', '#EEEECE', 3.0)
        
        #Coloring rest_area highways.
        self.fillHighwayColor(lineStyle, 'rest_area', '#D1A0A0', 10.0)    

        #Coloring traffic_signals highways.
        self.fillHighwayColor(lineStyle, 'traffic_signals', '#D73E68', 2.0)
        
        #Coloring crossing highways.F3D6B6
        self.fillHighwayColor(lineStyle, 'crossing', '#1F88A7', 6.0)    

        #Coloring path highways.
        self.fillHighwayColor(lineStyle, 'path', '#C27E3A', 2.0)
        
        #Coloring cycle_way highways.
        self.fillHighwayColor(lineStyle, 'cycle_way', '#29AFD6', 2.0)    

        #Coloring bridleway highways.
        self.fillHighwayColor(lineStyle, 'bridleway', '#4A9586', 1.5)
        
        #Coloring footway highways.
        self.fillHighwayColor(lineStyle, 'footway', '#B05F3C', 1.5)
        
        
        #RAILWAYS
        
        #Coloring tram highways.
        self.fillRailwayColor(lineStyle, 'tram', 'black', 1.5)
        
        #Coloring rail highways.
        self.fillRailwayColor(lineStyle, 'rail', 'gray', 2.0)
        
        #Datasource.
        #bounds = self.minlon + ', ' + self.minlat + ', ' + self.maxlon + ', ' + self.maxlat
        #print bounds
        #print self.osmUrl
        bounds = "%s,%s,%s,%s" % (self.minlon, self.minlat, self.maxlon, self.maxlat)
        datasource = mapnik.Osm(url=self.osmUrl, bbox=bounds)
        
        # Layers
        polygonLayer = mapnik.Layer("Polygons")
        polygonLayer.datasource = datasource
        polygonLayer.styles.append("PolygonStyle")
        
        #labelLayer = mapnik.Layer("Labels")
        #labelLayer.datasource = datasource
        #labelLayer.styles.append("LabelStyle")
        
        lineLayer = mapnik.Layer("Lines")
        lineLayer.datasource = datasource
        lineLayer.styles.append("LineStyle")

        m.append_style("PolygonStyle", polygonStyle)
        m.append_style("LineStyle", lineStyle)
        #m.append_style("LabelStyle", labelStyle)
        
        
        m.layers.append(polygonLayer)
        m.layers.append(lineLayer)
        #m.layers.append(labelLayer)
        
        m.zoom_to_box(mapnik.Box2d(176.193,-38.172,176.276,-38.108))
        mapnik.render_to_file(m, '/tmp/'+ 'out' + '.png')
        
        self.picture = QtGui.QPixmap('/tmp/'+ 'out' + '.png')
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.osm_image_view.setScene(self.scene)
        
    def clearImage(self):
        '''Remove all elements from scene.'''
        self.scene.clear()


