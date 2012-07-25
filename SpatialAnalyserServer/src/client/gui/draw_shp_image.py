# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw_shp_image.ui'
#
# Created: Mon Jun  4 20:51:50 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import mapnik
import osgeo.ogr
import sys

sys.path.append("..")
sys.path.append("../../logger")
sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
sys.path.append("../../../interfaces/projections")
from Client import Client

class Ui_DrawSHPImage(Client):
    '''
    Class Ui_DrawSHPImage is class displays window to drawing shapefiles. PyQT implementation.
    @author: Bartlomiej Grabowski
    @version: 1.0
    '''
           
    def setupUi(self, DrawSHPImage):
        '''
        @brief: This function is used to setup all elements of the main window.
        @see: Ui_DrawSHPImage
        @param DrawSHPImage QtGui.QWidget: Input parameter is QtGui.QWidget.
        @return: This function does not return a value. 
        '''
        
        DrawSHPImage.setObjectName("DrawSHPImage")
        DrawSHPImage.resize(796, 594)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.confIconsDir+'earthsphere.ico'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DrawSHPImage.setWindowIcon(icon)
        self.conf_shp_image = QtGui.QTabWidget(DrawSHPImage)
        self.conf_shp_image.setGeometry(QtCore.QRect(10, 460, 601, 111))
        self.conf_shp_image.setObjectName("conf_shp_image")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        #Background color combo box.
        self.background_image_color = QtGui.QComboBox(self.tab)
        self.background_image_color.setGeometry(QtCore.QRect(10, 40, 141, 31))
        self.background_image_color.setObjectName("background_image_color")
        
        #Add background colors to combo box.
        self.background_image_color.addItem('green')
        self.background_image_color.addItem('blue')
        self.background_image_color.addItem('red')
        self.background_image_color.addItem('gray')
        self.background_image_color.addItem('yellow')
        self.background_image_color.addItem('white')
        
        self.background_label = QtGui.QLabel(self.tab)
        self.background_label.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.background_label.setObjectName("background_label")
        
        #Polygons color combo box.
        self.polygons_color = QtGui.QComboBox(self.tab)
        self.polygons_color.setGeometry(QtCore.QRect(180, 40, 141, 31))
        self.polygons_color.setObjectName("polygons_color")
        self.polygons_color.addItem('yellow')
        self.polygons_color.addItem('red')
        self.polygons_color.addItem('green')
        self.polygons_color.addItem('white')
        self.polygons_color.addItem('black')
        self.polygons_color.addItem('blue')
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(180, 10, 111, 21))
        self.label.setObjectName("label")
        
        #Lines color combo box.
        self.lines_color = QtGui.QComboBox(self.tab)
        self.lines_color.setGeometry(QtCore.QRect(350, 40, 141, 31))
        self.lines_color.setObjectName("lines_color")
        self.lines_color.addItem('blue')
        self.lines_color.addItem('red')
        self.lines_color.addItem('green')
        self.lines_color.addItem('white')
        self.lines_color.addItem('black')
        self.lines_color.addItem('yellow')
    
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(350, 10, 91, 21))
        self.label_2.setObjectName("label_2")
        self.conf_shp_image.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.projection_label = QtGui.QLabel(self.tab_2)
        self.projection_label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.projection_label.setObjectName("projection_label") 
        #Projection types combo box.
        self.projection_type = QtGui.QComboBox(self.tab_2)
        self.projection_type.setGeometry(QtCore.QRect(10, 40, 171, 31))
        self.projection_type.setObjectName("projection_type")
        #Projection types in combo box.
        self.projection_type.addItem('+proj=latlong +datum=WGS84')
        self.projection_type.addItem('+proj=tmerc +datum=WGS84')
        self.projection_type.addItem('+proj=cc +datum=WGS84')
        self.projection_type.addItem('+proj=merc +datum=WGS84')
        self.projection_type.addItem('+proj=fouc +datum=WGS84')
        
        #QLineEdit with output file name.
        self.out_image_name = QtGui.QLineEdit(self.tab_2)
        self.out_image_name.setGeometry(QtCore.QRect(220, 40, 191, 31))
        self.out_image_name.setObjectName("out_image_name")
        #Set default image name.
        self.out_image_name.setText('out.png')
        
        self.out_image_label = QtGui.QLabel(self.tab_2)
        self.out_image_label.setGeometry(QtCore.QRect(220, 20, 141, 21))
        self.out_image_label.setObjectName("out_image_label")
        
        self.conf_shp_image.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.antialiasing_checkbox = QtGui.QCheckBox(self.tab_3)
        self.antialiasing_checkbox.setGeometry(QtCore.QRect(20, 30, 111, 22))
        self.antialiasing_checkbox.setObjectName("antialiasing_checkbox")
        self.conf_shp_image.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.scale_label = QtGui.QLabel(self.tab_4)
        self.scale_label.setGeometry(QtCore.QRect(10, 10, 62, 17))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.scale_label.setFont(font)
        self.scale_label.setObjectName("scale_label")
        self.scale_x_label = QtGui.QLabel(self.tab_4)
        self.scale_x_label.setGeometry(QtCore.QRect(70, 10, 21, 17))
        self.scale_x_label.setObjectName("scale_x_label")
        self.scale_y_label = QtGui.QLabel(self.tab_4)
        self.scale_y_label.setGeometry(QtCore.QRect(70, 50, 16, 17))
        self.scale_y_label.setObjectName("scale_y_label")
        self.scale_x_input = QtGui.QLineEdit(self.tab_4)
        self.scale_x_input.setGeometry(QtCore.QRect(90, 10, 51, 27))
        self.scale_x_input.setObjectName("scale_x_input")
        self.scale_y_input = QtGui.QLineEdit(self.tab_4)
        self.scale_y_input.setGeometry(QtCore.QRect(90, 40, 51, 27))
        self.scale_y_input.setObjectName("scale_y_input")
        self.rotation_label = QtGui.QLabel(self.tab_4)
        self.rotation_label.setGeometry(QtCore.QRect(190, 10, 62, 17))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.rotation_label.setFont(font)
        self.rotation_label.setObjectName("rotation_label")
        self.angle_label = QtGui.QLabel(self.tab_4)
        self.angle_label.setGeometry(QtCore.QRect(260, 10, 41, 17))
        self.angle_label.setObjectName("angle_label")
        self.angle_input = QtGui.QLineEdit(self.tab_4)
        self.angle_input.setGeometry(QtCore.QRect(310, 10, 51, 27))
        self.angle_input.setObjectName("angle_input")
        self.shear_label = QtGui.QLabel(self.tab_4)
        self.shear_label.setGeometry(QtCore.QRect(400, 10, 51, 17))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.shear_label.setFont(font)
        self.shear_label.setObjectName("shear_label")
        self.shear_x_label = QtGui.QLabel(self.tab_4)
        self.shear_x_label.setGeometry(QtCore.QRect(460, 10, 16, 17))
        self.shear_x_label.setObjectName("shear_x_label")
        self.shear_y_label = QtGui.QLabel(self.tab_4)
        self.shear_y_label.setGeometry(QtCore.QRect(460, 50, 16, 17))
        self.shear_y_label.setObjectName("shear_y_label")
        self.shear_x_input = QtGui.QLineEdit(self.tab_4)
        self.shear_x_input.setGeometry(QtCore.QRect(480, 10, 51, 27))
        self.shear_x_input.setObjectName("shear_x_input")
        self.shear_y_input = QtGui.QLineEdit(self.tab_4)
        self.shear_y_input.setGeometry(QtCore.QRect(480, 40, 51, 27))
        self.shear_y_input.setObjectName("shear_y_input")
        self.line = QtGui.QFrame(self.tab_4)
        self.line.setGeometry(QtCore.QRect(170, 10, 3, 61))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.tab_4)
        self.line_2.setGeometry(QtCore.QRect(380, 10, 3, 61))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.conf_shp_image.addTab(self.tab_4, "")


        self.conf_shp_image.addTab(self.tab_2, "")
        self.shp_image_view = QtGui.QGraphicsView(DrawSHPImage)
        self.shp_image_view.setGeometry(QtCore.QRect(10, 40, 605, 405))
        self.shp_image_view.setObjectName("shp_image_view")
        self.shp_name_label = QtGui.QLabel(DrawSHPImage)
        self.shp_name_label.setGeometry(QtCore.QRect(10, 10, 62, 17))
        self.shp_name_label.setObjectName("shp_name_label")
        self.shp_file_name = QtGui.QLabel(DrawSHPImage)
        self.shp_file_name.setGeometry(QtCore.QRect(70, 10, 300, 17))
        self.shp_file_name.setGeometry(QtCore.QRect(70, 10, 200, 17))
        self.shp_file_name.setText("")
        self.shp_file_name.setObjectName("shp_file_name")
        self.draw_image = QtGui.QPushButton(DrawSHPImage)
        self.draw_image.setGeometry(QtCore.QRect(660, 40, 91, 27))
        self.draw_image.setObjectName("draw_image")
        self.clear_button = QtGui.QPushButton(DrawSHPImage)
        self.clear_button.setGeometry(QtCore.QRect(660, 90, 91, 27))
        self.clear_button.setObjectName("clear_button")
        self.cancel_button = QtGui.QPushButton(DrawSHPImage)
        self.cancel_button.setGeometry(QtCore.QRect(660, 140, 91, 27))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(DrawSHPImage)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL("clicked()"), DrawSHPImage,  QtCore.SLOT("close()"))
        QtCore.QObject.connect(self.draw_image, QtCore.SIGNAL("clicked()"), self.drawSHPFile)
        QtCore.QObject.connect(self.clear_button, QtCore.SIGNAL("clicked()"), self.clearAll)

        self.conf_shp_image.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DrawSHPImage)

    def retranslateUi(self, DrawSHPImage):
        '''
        @brief: This function is used to translate Qt's items.
        @param DrawSHPImage QWidget: Input parameter is QtGui.QWidget.
        @return: This function does not return a value.
        '''
        
        DrawSHPImage.setWindowTitle(QtGui.QApplication.translate("DrawSHPImage", "Draw from SHP", None, QtGui.QApplication.UnicodeUTF8))
        self.background_label.setText(QtGui.QApplication.translate("DrawSHPImage", "Background color", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DrawSHPImage", "Polygons color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DrawSHPImage", "Lines color", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_shp_image.setTabText(self.conf_shp_image.indexOf(self.tab), QtGui.QApplication.translate("DrawSHPImage", "Colors", None, QtGui.QApplication.UnicodeUTF8))
        self.projection_label.setText(QtGui.QApplication.translate("DrawSHPImage", "Projection", None, QtGui.QApplication.UnicodeUTF8))
        self.out_image_label.setText(QtGui.QApplication.translate("DrawSHPImage", "Output image name", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_shp_image.setTabText(self.conf_shp_image.indexOf(self.tab_2), QtGui.QApplication.translate("DrawSHPImage", "Projection", None, QtGui.QApplication.UnicodeUTF8))
        self.antialiasing_checkbox.setText(QtGui.QApplication.translate("DrawSHPImage", "Antialiasing", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_shp_image.setTabText(self.conf_shp_image.indexOf(self.tab_3), QtGui.QApplication.translate("DrawSHPImage", "Antialiasing", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_label.setText(QtGui.QApplication.translate("DrawSHPImage", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_x_label.setText(QtGui.QApplication.translate("DrawSHPImage", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_y_label.setText(QtGui.QApplication.translate("DrawSHPImage", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.rotation_label.setText(QtGui.QApplication.translate("DrawSHPImage", "Rotation", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_label.setText(QtGui.QApplication.translate("DrawSHPImage", "Angle", None, QtGui.QApplication.UnicodeUTF8))
        self.shear_label.setText(QtGui.QApplication.translate("DrawSHPImage", "Shear", None, QtGui.QApplication.UnicodeUTF8))
        self.shear_x_label.setText(QtGui.QApplication.translate("DrawSHPImage", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.shear_y_label.setText(QtGui.QApplication.translate("DrawSHPImage", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_shp_image.setTabText(self.conf_shp_image.indexOf(self.tab_4), QtGui.QApplication.translate("DrawSHPImage", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.shp_name_label.setText(QtGui.QApplication.translate("DrawSHPImage", "SHP file: ", None, QtGui.QApplication.UnicodeUTF8))
        self.draw_image.setText(QtGui.QApplication.translate("DrawSHPImage", "Draw", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_button.setText(QtGui.QApplication.translate("DrawSHPImage", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate("DrawSHPImage", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

    def clearAll(self):
        '''
        @brief: This function is used to clear all QGraphicsView parameters.
        @param None:
        @return: This function does not return a value.
        '''
        
        #Clear scene.
        self.scene.clear()
        #Clear scale coordinates.
        self.scale_x_input.clear()
        self.scale_y_input.clear()
        #Clear angle of rotation.
        self.angle_input.clear()
        #Clear shear coordinates.
        self.shear_x_input.clear()
        self.shear_y_input.clear()
    
        
        
    def drawSHPFile(self):
        '''
        @brief: This function is used to draw picture from shapefile.
        @param None:
        @return: This function does not return a value.
        '''
        
        #Create a map with a given width and height in pixels.
        # Map
        #Fetch projection type.
        self.projection = str(self.projection_type.currentText())
        #Fetch background color.
        self.background = str(self.background_image_color.currentText())
        #Fetch polygons color.
        self.polygon = str(self.polygons_color.currentText())
        #Fetch lines color.
        self.lines = str(self.lines_color.currentText())
        #Fetch output png file name.
        self.output_name = str(self.out_image_name.text())
        #Create new scene.
        self.scene = QtGui.QGraphicsScene()
        #Fetch width of QGraphicsView widget.
        self.x = self.shp_image_view.width() - 5
        #Fetch height of QGraphicsView widget.
        self.y = self.shp_image_view.height() - 5
        #Fetch antialiasing flag.
        self.antialiasing = self.antialiasing_checkbox.isChecked()
        #Fetch scale x coordinate.
        self.scale_x = self.scale_x_input.text()
        #Fetch scale y coordinate.
        self.scale_y = self.scale_y_input.text()
        #Fetch rotation angle.
        self.rotation_angle = self.angle_input.text()
        #Fetch shear x coordinate.
        self.shear_x = self.shear_x_input.text()
        #fetch shear y coordinate.
        self.shear_y = self.shear_y_input.text()
        #Set map size and projection type.
        m = mapnik.Map(self.x,self.y, self.projection)
        print(m.srs)
        #Set background color.
        m.background = mapnik.Color(self.background)

        print(self.confSHPDownloadsLoc+str(self.shp_file_name.text()) + '.shp')
        shapefile = osgeo.ogr.Open(self.confSHPDownloadsLoc+str(self.shp_file_name.text()) + '.shp')
        
        numLayers = shapefile.GetLayerCount()
        
        print "Shapefile contains %d layers" % numLayers
        print
        
        for layerNum in range(numLayers):
            layer = shapefile.GetLayer(layerNum)
            spatialRef = layer.GetSpatialRef().ExportToProj4()
            numFeatures = layer.GetFeatureCount()
            print "Layer %d has spatial references %s" % (layerNum, spatialRef)
            print "Layer %d has %d features: " % (layerNum, numFeatures)
            print
            
        for featureNum in range(numFeatures):
            feature = layer.GetFeature(featureNum)
            featureRef = feature.GetFieldDefnRef(featureNum)
            #print featureRef.GetName()
            #featureName = feature.GetField("NAME")
            #featurePostal = feature.GetField("ADMIN")
            
            
            #print "Feature %d has name %s -> %s" % (featureNum, featureName, featurePostal)
        # Styles

        #Create polygon style.
        polygonStyle = mapnik.Style()
        #Create new rule for polygons.
        rule = mapnik.Rule()
        #rule.filter =mapnik.Expression("[NAME] != 'Russia'")
        #Set polygon color.
        symbol = mapnik.PolygonSymbolizer(mapnik.Color(self.polygon))
        #Append symbol to rule.
        rule.symbols.append(symbol)
        #Append polygon rule to set of rules.
        polygonStyle.rules.append(rule)
        
        
        #Create new outlines rule.
        rule = mapnik.Rule()
        #Set outline color.
        symbol = mapnik.LineSymbolizer(mapnik.Color(self.lines), 0.3)
        rule.symbols.append(symbol)
        polygonStyle.rules.append(rule)
        
        rule = mapnik.Rule()
        symbol = mapnik.LineSymbolizer(mapnik.Color("#000000"), 0.1)
        rule.symbols.append(symbol)
        
        polygonStyle.rules.append(rule)
        
        #Create new label style.
        #labelStyle = mapnik.Style()
        #rule = mapnik.Rule()
        #symbol = mapnik.TextSymbolizer(mapnik.Expression("[NAME]"), "DejaVu Sans Book", 12, mapnik.Color("#000000"))
        #rule.symbols.append(symbol)
        #labelStyle.rules.append(rule)
        
        #Datasource.
        datasource = mapnik.Shapefile(file=self.confSHPDownloadsLoc+str(self.shp_file_name.text()))
        
        # Layers
        polygonLayer = mapnik.Layer("Polygons")
        polygonLayer.datasource = datasource
        polygonLayer.styles.append("PolygonStyle")
        
        #lineLayer = mapnik.Layer("Lines")
        #lineLayer.datasource = datasource
        #lineLayer.styles.append("LineStyle")
        
        #labelLayer = mapnik.Layer("Labels")
        #labelLayer.datasource = datasource
        #labelLayer.styles.append("LabelStyle")

        m.append_style("PolygonStyle", polygonStyle)
        #m.append_style("LineStyle", lineStyle)
        #m.append_style("LabelStyle", labelStyle)
        
        m.layers.append(polygonLayer)
        #m.layers.append(lineLayer)
        #m.layers.append(labelLayer)
        
        # Render
        m.zoom_to_box(polygonLayer.envelope())
        mapnik.render_to_file(m, '/tmp/'+self.output_name)
        
        self.picture = QtGui.QPixmap('/tmp/'+self.output_name)
        self.scene.addItem(QtGui.QGraphicsPixmapItem(self.picture))
        self.shp_image_view.setScene(self.scene)
        #Check if angle of rotation is set. If is not empty, then rotate.
        if not self.rotation_angle.isEmpty():
            self.shp_image_view.rotate(float(self.rotation_angle))
        
        #Check if x and y coordinate of scale are set.
        if not self.scale_x.isEmpty() and not self.scale_y.isEmpty():
            print "scale"
            self.shp_image_view.scale(float(self.scale_x), float(self.scale_y))
            
        #Check if x and y coordinate of shear are set.
        if not self.shear_x.isEmpty() and not self.shear_y.isEmpty():
            print "shear"
            self.shp_image_view.shear(float(self.shear_x), float(self.shear_y))
            
        #Check is antialiasing check box is set.
        if self.antialiasing == True:
            print "antialiasing"
            self.shp_image_view.setRenderHint(QtGui.QPainter.Antialiasing)
        
