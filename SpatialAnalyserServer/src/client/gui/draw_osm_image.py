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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.confIconsDir+'earthsphere.ico'), QtGui.QIcon.Normal, QtGui.QIcon.On)
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
        
 
    def xml2obj(self, src):
        """
        @brief: A simple function to converts XML data into native Python object.
        @param src string: Input parameter is a path to xml file.
        @return: xml object. 
        """
     
        non_id_char = re.compile('[^_0-9a-zA-Z]')
        def _name_mangle(name):
            return non_id_char.sub('_', name)
     
        class DataNode(object):
            def __init__(self):
                self._attrs = {}    # XML attributes and child elements
                self.data = None    # child text data
            def __len__(self):
                # treat single element as a list of 1
                return 1
            def __getitem__(self, key):
                if isinstance(key, basestring):
                    return self._attrs.get(key,None)
                else:
                    return [self][key]
            def __contains__(self, name):
                return self._attrs.has_key(name)
            def __nonzero__(self):
                return bool(self._attrs or self.data)
            def __getattr__(self, name):
                if name.startswith('__'):
                    # need to do this for Python special methods???
                    raise AttributeError(name)
                return self._attrs.get(name,None)
            def _add_xml_attr(self, name, value):
                if name in self._attrs:
                    # multiple attribute of the same name are represented by a list
                    children = self._attrs[name]
                    if not isinstance(children, list):
                        children = [children]
                        self._attrs[name] = children
                    children.append(value)
                else:
                    self._attrs[name] = value
            def __str__(self):
                return self.data or ''
            def __repr__(self):
                items = sorted(self._attrs.items())
                if self.data:
                    items.append(('data', self.data))
                return u'{%s}' % ', '.join([u'%s:%s' % (k,repr(v)) for k,v in items])
     
        class TreeBuilder(xml.sax.handler.ContentHandler):
            def __init__(self):
                self.stack = []
                self.root = DataNode()
                self.current = self.root
                self.text_parts = []
            def startElement(self, name, attrs):
                self.stack.append((self.current, self.text_parts))
                self.current = DataNode()
                self.text_parts = []
                # xml attributes --> python attributes
                for k, v in attrs.items():
                    self.current._add_xml_attr(_name_mangle(k), v)
            def endElement(self, name):
                text = ''.join(self.text_parts).strip()
                if text:
                    self.current.data = text
                if self.current._attrs:
                    obj = self.current
                else:
                    # a text only node is simply represented by the string
                    obj = text or ''
                self.current, self.text_parts = self.stack.pop()
                self.current._add_xml_attr(_name_mangle(name), obj)
            def characters(self, content):
                self.text_parts.append(content)
     
        builder = TreeBuilder()
        if isinstance(src,basestring):
            xml.sax.parseString(src, builder)
        else:
            xml.sax.parse(src, builder)
        return builder.root._attrs.values()[0]
     
     
     
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
        
    def drawOSMFile1(self):
        '''
        @brief: This function is used to draw picture from osm file.
        @param None:
        @return: This function does not return a value.
        '''
        
        src = file(self.confOSMDownloadsLoc+str(self.file_name_label.text())+'.osm')
        myMap = self.xml2obj(src)
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

        #osm = osgeo.ogr.Open(self.confOSMDownloadsLoc+str(self.shp_file_name.text()) + '.osm')
        
        # Styles

        #Create polygon style.
        polygonStyle = mapnik.Style()
        #Create new rule for polygons.
        
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
        

        
        #LANDUSES.
        
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
        
        #Create new label style.
        #labelStyle = mapnik.Style()
        #rule = mapnik.Rule()
        #symbol = mapnik.TextSymbolizer(mapnik.Expression("[way]"), "DejaVu Sans Book", 12, mapnik.Color("#093123"))
        #rule.symbols.append(symbol)
        #labelStyle.rules.append(rule)
        
        #Datasource.
        datasource = mapnik.Osm(file=self.confOSMDownloadsLoc+str(self.file_name_label.text())+'.osm')
        
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
           
           
        ways = {}
        for way in myMap['way']:
            ways[way['id']]=way
            
        for idx,nodeID in enumerate(ways.keys()):
            wayTags = ways[nodeID]['tag']
            if not wayTags==None:
                hwyTypeList  = [d['v'] for d in wayTags if d['k']=='addr:street']
                if len(hwyTypeList)>0:
                        wayName = hwyTypeList[0] 
                else:
                        wayName = None
            else:
                wayName = None
        
        # get bounds from OSM data           
        minX = float(myMap['bounds']['minlon'])
        maxX = float(myMap['bounds']['maxlon'])
        minY = float(myMap['bounds']['minlat'])
        maxY = float(myMap['bounds']['maxlat'])
        
        m.zoom_to_box(mapnik.Box2d(minX, minY, maxX, maxY ))
        mapnik.render_to_file(m, '/tmp/'+str(self.file_name_label.text()) + '.png')
        
        self.picture = QtGui.QPixmap('/tmp/'+self.file_name_label.text() + '.png')
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.osm_image_view.setScene(self.scene)
        



