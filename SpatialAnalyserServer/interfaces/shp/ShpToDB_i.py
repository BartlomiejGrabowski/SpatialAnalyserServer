'''
Created on Apr 29, 2012

@author: bartek
'''

import SHP__POA
import psycopg2
import os.path
from osgeo import ogr

class ShpToDB_i(SHP__POA.ShpToDB):
    '''
    classdocs
    '''
        
    def __init__(self):
        '''
        Constructor
        '''
    def send_shp_to_postgres(self, shpFile, tableName):
        conn = b.connectToDatabase("shp_database", "postgres", "postgres")
        connection = psycopg2.connect(database="shp_database", user="postgres", password="postgres")
        cursor = connection.cursor()
    
        cursor.execute('DROP TABLE IF EXISTS %s' % (tableName))
        cursor.execute("""CREATE TABLE %s (
                           id    SERIAL,
                           level    INTEGER,
                           PRIMARY KEY (id))""" % (tableName))
        cursor.execute("CREATE INDEX levelIndex ON %s (level)" % (tableName))
        cursor.execute("SELECT AddGeometryColumn('%s', 'geom', 4326, 'POLYGON', 2)" % (tableName))
        cursor.execute("CREATE INDEX geomIndex ON %s USING GIST (geom)" % (tableName))
        
        
        shapefile = ogr.Open(shpFile)
        layer = shapefile.GetLayer(0)
        level = 1
        for i in range(layer.GetFeatureCount()):
            feature = layer.GetFeature(i)
            geometry = feature.GetGeometryRef()
            wkt = geometry.ExportToWkt()
            
            cursor.execute("INSERT INTO %s (level, geom)" % (tableName) + "VALUES (%s, ST_GeomFromText(%s, 4326))"
                           ,(level, wkt))
        connection.commit()
        
            