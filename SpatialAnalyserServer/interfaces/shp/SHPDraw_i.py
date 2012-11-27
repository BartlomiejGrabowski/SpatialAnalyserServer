'''
Created on May 26, 2012

@author: bartek
'''

import sys
import os
import time
import mapnik
import re
import xml.sax.handler

import SHPDraw
import SHPDraw__POA
import CORBA

sys.path.append("../../src/logger")
from Logger import Logger
import xml.etree.ElementTree as ET

class SHPDraw_i(SHPDraw__POA.Basic):
    '''
    Implementation of SHPDraw servant.
    '''
    
    def __init__(self):
        self.logger = Logger("SHPDraw Basic", "../../../src/server/main/server.log")
        #Open xml configuration file.
        configurationFile = ET.parse('../conf/serverConf.xml')
        doc = configurationFile.getroot()
        shpDirConf = doc.find('SHPFilesDirectory')
        #Fetch location of downloads folder.
        self.confSHPDirLocation = shpDirConf.find('Location').text
        
        osmDirConf = doc.find('OSMFilesDirectory')
        #Fetch location of downloads folder.
        self.confOSMDirLocation = osmDirConf.find('Location').text

        # Remove old files in osm directory.
        for filename in sorted(os.listdir(self.confOSMDirLocation)):
            if re.match(r'.+(osm)$', filename) == None:
                os.unlink(self.confOSMDirLocation + '/' + filename)
        
    def get_shp_file_list(self):
        self.logger.log.info("get_shp_file_list method invocation.")
        outFileList = list()
        try:
            for filename in sorted(os.listdir(self.confSHPDirLocation)):
                #Creating new file object.
                fileObj = SHPDraw.File(filename, time.ctime(os.path.getmtime(self.confSHPDirLocation+'/'+filename)),
                time.ctime(os.path.getctime(self.confSHPDirLocation+'/'+filename)))
                #Append file object to the result list.   
                outFileList.append(fileObj)
        except OSError as ex:
            self.logger.log.error("%s exception occurred during creating shp file list" % (ex))
            raise SHPDraw.UnknownInternalError("Error occurred during creating shp file list")
            sys.exit(1)
        return outFileList
    
    def get_shp_file_content(self, shpFileName):
        self.logger.log.info("get_shp_file_content method invocation.")
        absPath = self.confSHPDirLocation+'/'+shpFileName
        try:
            #Convert file content to the list of strings.
            fileContent = open(absPath, 'r').read()
        except IOError as ex:
            self.logger.log.error("%s exception occurred during opening shp file" % (ex))
            raise SHPDraw.FileNotFound("Error occurred during openinf shp file", absPath)
            sys.exit(1)
        return fileContent
    
    def get_osm_file_list(self):
        self.logger.log.info("get_osm_file_list method invocation.")
        outFileList = list()
        try:
            for filename in sorted(os.listdir(self.confOSMDirLocation)):
                if re.match(r'.+(osm)$', filename) != None:
                    #Creating new file object.
                    fileObj = SHPDraw.File(filename, time.ctime(os.path.getmtime(self.confOSMDirLocation+'/'+filename)),
                    time.ctime(os.path.getctime(self.confOSMDirLocation+'/'+filename)))
                    #Append file object to the result list.   
                    outFileList.append(fileObj)
        except OSError as ex:
            self.logger.log.error("%s exception occurred during creating osm file list" % (ex))
            raise SHPDraw.UnknownInternalError("Error occurred during creating osm file list")
            sys.exit(1)
        return outFileList
    
    def get_osm_file_content(self, osmFileName):
        self.logger.log.info("get_osm_file_content method invocation.")
        absPath = self.confOSMDirLocation+'/'+osmFileName
        try:
            #Convert file content to the list of strings.
            fileContent = open(absPath, 'r').read()
        except IOError as ex:
            self.logger.log.error("%s exception occurred during opening osm file" % (ex))
            raise SHPDraw.FileNotFound("Error occurred during openinf osm file", absPath)
            sys.exit(1)
        return fileContent
    
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

    def draw_osm_file(self, osmFileName, width, height):
        '''
        @brief: This function is used to draw picture from osm file.
        @param osmFileName: string Path to OSM file.
        @param width: long Width picture.
        @param height: long Height picture.
        @return: This function returns file name string.
        '''
        
        import time
        
        start_timestamp = time.time()
        
        print(":::::::::Start timestamp: %s" % (start_timestamp))
        
        #Draw image when not exist.
        if os.path.exists(self.confOSMDirLocation+'/'+osmFileName + '.png') != True:
        
            self.logger.log.info("draw_osm_file_content method invocation.")
            absPath = self.confOSMDirLocation+'/'+osmFileName
            try:
                src = file(absPath)
                myMap = self.xml2obj(src)
    
                #Fetch width of QGraphicsView widget.
                self.x = width - 5
                #Fetch height of QGraphicsView widget.
                self.y = height - 5
                
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
                datasource = mapnik.Osm(file=absPath)
                
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
                mapnik.render_to_file(m, self.confOSMDirLocation + '/' + str(osmFileName) + '.png')
            except IOError as ex:
                self.logger.log.error("%s exception occurred during drawing osm file" % (ex))
                raise SHPDraw.FileNotFound("Error occurred during drawing osm file", absPath)
                sys.exit(1)

            stop_timestamp = time.time()
            print(":::::::::Stop timestamp: %s" % (stop_timestamp - start_timestamp))
        return str(osmFileName) + '.png'