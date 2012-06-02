'''
Created on Apr 29, 2012

@author: bartek
'''

import SHP__POA
import SHP
import psycopg2
import os.path
from osgeo import ogr
import sys
import CORBA

sys.path.append("../../src/logger")
from Logger import Logger

sys.path.append("../../database/postgres")
from Basic import PostgresBasic

class ShpToDB_i(SHP__POA.ShpToDB):
    '''
    Implementation of ShpToDB servant.
    '''
        
    def __init__(self):
        '''
        Initialize logging handler.
        '''
        self.logger = Logger("ShpToDB", "../../../src/server/main/server.log")
        
    def send_shp_to_postgres(self, shpFile, tableName):
        pb = PostgresBasic()
        self.logger.log.info("Connecting to %s database" % (pb.db))
        try:
            connection = pb.connectToDatabase()
        except psycopg2.OperationalError as ex:
            self.logger.log.error("%s exception occurred during connection to %s database" % (ex, pb.db))
            raise SHP.CannotConnectToDB("Cannot connect to database", pb.db )
            sys.exit(1)
            
        cursor = connection.cursor()
    
        cursor.execute('DROP TABLE IF EXISTS %s' % (tableName))
        cursor.execute("""CREATE TABLE %s (
                           id    SERIAL,
                           level    INTEGER,
                           PRIMARY KEY (id))""" % (tableName))
        cursor.execute("CREATE INDEX levelIndex ON %s (level)" % (tableName))
        cursor.execute("SELECT AddGeometryColumn('%s', 'geom', 4326, 'POLYGON', 2)" % (tableName))
        cursor.execute("CREATE INDEX geomIndex ON %s USING GIST (geom)" % (tableName))
        
        self.logger.log.info("Opening %s shapefile" % (shpFile))
        shapefile = ogr.Open(shpFile)
        try:
            layer = shapefile.GetLayer(0)
            level = 1
            for i in range(layer.GetFeatureCount()):
                feature = layer.GetFeature(i)
                geometry = feature.GetGeometryRef()
                wkt = geometry.ExportToWkt()
                cursor.execute("INSERT INTO %s (level, geom)" % (tableName) + "VALUES (%s, ST_GeomFromText(%s, 4326))"
                           ,(level, wkt))
        except AttributeError as ex:
            self.logger.log.error("Error occurred during open %s file. %s" % (shpFile, ex))
            raise SHP.FileDoesNotExist("File does not exist", shpFile)
            sys.exit(1)
        
        connection.commit()
        
        #Run VACUUM ANALYZE command so that PostGIS cat gather statistics to help it optimize database.
        old_level = connection.isolation_level
        connection.set_isolation_level(0)
        cursor.execute("VACUUM ANALYZE")
        connection.set_isolation_level(old_level)
        
    
    def send_wbd_to_postgres(self, shpFile):
        pb = PostgresBasic()
        self.logger.log.info("Connecting to %s database" % (pb.db))
        try:
            connection = pb.connectToDatabase()
        except psycopg2.OperationalError as ex:
            self.logger.log.error("%s exception occurred during connection to %s database" % (ex, pb.db))
            raise SHP.CannotConnectToDB("Cannot connect to database", pb.db )
            sys.exit(1)
            
        cursor = connection.cursor()
        
        cursor.execute("DROP TABLE IF EXISTS countries")
        cursor.execute("""
                    CREATE TABLE countries (
                        id SERIAL,
                        name VARCHAR(255),
                        PRIMARY KEY (id))
                        """)
        cursor.execute("SELECT AddGeometryColumn('countries', 'outline', 4326, 'POLYGON', 2)")
        cursor.execute("CREATE INDEX countryIndex ON countries USING GIST(outline)")

        connection.commit()
        
        cursor.execute("DELETE FROM countries")

        try:
            self.logger.log.info("Opening %s shapefile" % (shpFile))
            shapefile = ogr.Open(shpFile)
            layer = shapefile.GetLayer(0)
            for i in range(layer.GetFeatureCount()):
                feature = layer.GetFeature(i)
                name = feature.GetField("NAME").decode("Latin-1")
                wkt = feature.GetGeometryRef().ExportToWkt()
            cursor.execute("INSERT INTO countries (name,outline) " +
                           "VALUES (%s, ST_PolygonFromText(%s, " +
                           "4326))", (name.encode("utf8"), wkt))
        except AttributeError as ex:
            self.logger.log.error("Error occurred during open %s file. %s" % (shpFile, ex))
            raise SHP.FileDoesNotExist("File does not exist", shpFile)
            sys.exit(1)
            
        connection.commit()

            