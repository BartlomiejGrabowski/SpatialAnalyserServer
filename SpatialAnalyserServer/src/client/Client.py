'''
Created on Apr 28, 2012

@author: bartek
'''
import sys
import os
from omniORB import CORBA
import CosNaming

#sys.path.append("../logger")
from Logger import Logger


import DB
import SHP
import SHPDraw
import Info
import Projection
import xml.etree.ElementTree as ET

class Client(object):
    '''
    Class Client is a major client side class.
    @author: Bartlomiej Grabowski
    @version: 1.0
    '''

    def __init__(self):
        '''
        Client constructor. The constructor takes the initialization 
        of CORBA main facilities such as reference to NameService and configuration parameters.
        '''
        
        self.logger = Logger("Client", "../client.log")
        #Initialize the ORB.
        self.logger.log.info("Initialize the ORB")
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        #Obtain a reference to the root naming context.
        self.logger.log.info("Obtain a reference to the root naming context")
        #Resolve initial reference.
        self.obj = orb.resolve_initial_references("NameService")
        #Narrow to root context.
        self.rootContext = self.obj._narrow(CosNaming.NamingContext)
        
        if self.rootContext is None:
            self.logger.log.error("Failed to narrow the root naming context")
            sys.exit(1)
            
        #Retrieving xml configuration file.
        self.logger.log.info("Retrieving configuration data from XML file.")
        #Open xml configuration file.
        configurationFile = ET.parse('../conf/clientConf.xml')
        doc = configurationFile.getroot()
        
        downloadsConf = doc.find('SHPDownloadDir')

        #Fetch location of shp download folder.
        self.confSHPDownloadsLoc = downloadsConf.find('Location').text
        #Fetch flush download directory flag.
        self.confSHPDownloadsFlush = downloadsConf.find('FlushContent').text 
        
        downloadsConf = doc.find('OSMDownloadDir')
        #Fetch location of osm download folder.
        self.confOSMDownloadsLoc = downloadsConf.find('Location').text
        #Fetch flush download directory flag.
        self.confOSMDownloadsFlush = downloadsConf.find('FlushContent').text

        #Fetch location of downloads folder.
        self.confSHPDownloadsLoc = downloadsConf.find('Location').text
        #Fetch flush downloads directory flag.
        self.confSHPDownloadsFlush = downloadsConf.find('FlushContent').text 
        
        contextConf = doc.find('NamingContext')
        #Fetch server context name.
        self.confServerContext = contextConf.find('ServerContext').text
        #Fetch object context name,
        self.confObjectContext = contextConf.find('ObjectContext').text
        
        #Interfaces XML TAG.
        interfacesConf = doc.find('Interfaces')
        
        #SHP INTERFACE.
        shpConf = interfacesConf.find('SHP')
        #Fetch ID.
        self.confSHPIntID = shpConf.find('ID').text
        #Fetch kind of interface.
        self.confSHPIntKind = shpConf.find('Kind').text

        self.confSHPIntID = shpConf.find('ID')
        #Fetch kind of interface.
        self.confSHPIntKind = shpConf.find('Kind')
        
        #SHPDraw INTERFACE.
        shpDrawConf = interfacesConf.find('ShpDraw')
        #Fetch ID from interface.
        self.confSHPDrawIntID = shpDrawConf.find('ID').text
        #Fetch kind of interface.
        self.confSHPDrawIntKind = shpDrawConf.find('Kind').text
        
        #Geodetic INTERFACE.
        geodeticConf = interfacesConf.find('Geodetic')
        #Fetch ID from interface.
        self.confGeodeticIntID = geodeticConf.find('ID').text
        #Fetch kind of interface.
        self.confGeodeticIntKind = geodeticConf.find('Kind').text
        
        #Raster INTERFACE.
        rasterConf = interfacesConf.find('Raster')
        #Fetch ID from interface.
        self.confRasterIntID = rasterConf.find('ID').text
        #Fetch kind of interface.
        self.confRasterIntKind = rasterConf.find('Kind').text
        
        #Images XML TAG.
        iconsDirConf = doc.find('IconsDir')
        #Fetch images location directory.
        self.confIconsDir = iconsDirConf.find('Location').text
        
        
    def get_reference_to_obj(self, prefix, postfix):
        '''
        @brief: This function is used to get reference to object.
        @see: Client
        @param prefix string: Input parameter is a object id.
        @param postfix string: Input parameter is a kind of object.
        @return: CORBA object.  
        '''
        
        self.logger.log.info("Getting reference to %s.%s object" % (prefix, postfix))
        name = [CosNaming.NameComponent(self.confServerContext, self.confObjectContext), CosNaming.NameComponent(prefix, postfix)]
        try:
            self.obj = self.rootContext.resolve(name)            
        except CosNaming.NamingContext.NotFound, ex:
            self.logger.log.error("Name not found. Error: %s" % (ex))
            sys.exit(1)       
        return self.obj
    
    def client_send_shp_to_postgres(self, fileName, tabName):
        '''
        @brief: This function is used to send shapefile to Postgres database.
        @see: Client
        @param fileName string: Input parameter is a shapefile name.
        @param tabName string: Input parameter is a table name in database.
        @return: int Returns 0 if successful.  
        '''
        
        client = Client()
        
        #Get reference to object. 

        obj = client.get_reference_to_obj(self.confSHPIntID, self.confSHPIntKind)
        
        client.logger.log.info("Narrowing to SHP.ShpToDB reference")
        
        #Narrow reference to ShpToDB interface.
        shpRef = obj._narrow(SHP.ShpToDB)
        
        #If reference is null, then exit with status 1.
        if shpRef is None:
            client.logger.log.error("Object reference is no an SHP::ShpToDB")
            sys.exit(1)       
        try:
            client.logger.log.info("Calling send_shp_to_postgres() function")
            #Call send_shp_to_postgres function from shp_to_db.idl file.
            shpRef.send_shp_to_postgres(fileName, tabName)
            return 0
        except SHP.FileDoesNotExist as ex:
            client.logger.log.error("%s. %s" % (ex.reason, ex.fileName))
            return 1
        except SHP.CannotConnectToDB as ex:
            client.logger.log.error("%s. %s" % (ex.reason, ex.dbName))
            return 1
            
    def client_send_wbd_to_postgres(self, fileName):
        '''
        @brief: This function is used to send shapefile (world border dataset) to Postgres database.
        @see: Client
        @param fileName string: Input parameter is a shapefile name.
        @return: int Returns 0 if successful.  
        '''
        
        client = Client()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confSHPIntID, self.confSHPIntKind)
        
        client.logger.log.info("Narrowing to SHP.ShpToDB reference")
        #Narrow reference to ShpToDB interface.
        shpRef = obj._narrow(SHP.ShpToDB)
        if shpRef is None:
            client.logger.log.error("Object reference is no an SHP::ShpToDB")
            sys.exit(1)
        try:
            srcFile = os.path.join(sys.path[0], "../../data_files/TM_WORLD_BORDERS-0.3", "TM_WORLD_BORDERS-0.3.shp")
            client.logger.log.info("Calling send_wbd_to_postgres() function")
            #Call send_wbd_to_postgres function from shp_to_db.idl file.
            shpRef.send_wbd_to_postgres(srcFile)
            return 0
        except SHP.FileDoesNotExist as ex:
            client.logger.log.error("%s. %s" % (ex.reason, ex.fileName))
            return 1
        except SHP.CannotConnectToDB as ex:
            client.logger.log.error("%s. %s" % (ex.reason, ex.dbName))
            return 1
        
    def client_get_shp_file_list(self):
        '''
        @brief: This function is used to get shapefile list from server.
        @see: Client
        @param None:
        @return: list Returns built-in Python's list() or 1 if error occurred. 
        '''
        
        client = Client()
        #Output list.
        self.outList = list()

        #Get reference to object.

        obj = client.get_reference_to_obj(self.confSHPDrawIntID, self.confSHPDrawIntKind)
        
        client.logger.log.info("Narrowing reference to SHPDraw.Basic reference")
        #Narrow reference to Basic interface.
        shpLstObj = obj._narrow(SHPDraw.Basic)
        if shpLstObj is None:
            client.logger.log.error("Object reference is no an SHPDraw::Basic")
            sys.exit(1)
        try:
            self.outList = shpLstObj.get_shp_file_list()
            return self.outList
        except SHPDraw.UnknownInternalError as ex:
            client.logger.log.error("%s." % (ex.reason))
            return 1
        
    def client_get_shp_file_content(self, fileName):        
        '''
        @brief: This function is used to get shapefile content from server.
        @see: Client
        @param fileName string: Input parameter is a shapefile name.
        @return: sequence<octet> Returns octet sequence or 1 if error occurred. 
        '''
        
        client = Client()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confSHPDrawIntID, self.confSHPDrawIntKind)
        
        client.logger.log.info("Narrowing reference to SHPDraw.Basic reference")
        #Narrow reference to Basic interface.
        shpLstObj = obj._narrow(SHPDraw.Basic)
        if shpLstObj is None:
            client.logger.log.error("Object reference is no an SHPDraw::Basic")
            sys.exit(1)
        try:
            #Call get_shp_file_content from shp_draw.idl file.
            fileContent = shpLstObj.get_shp_file_content(fileName)
            return fileContent
        except SHPDraw.FileNotFound as ex:
            client.logger.log.error("%s.File: %s" % (ex.reason, ex.fileName))
            return 1
        
    def client_get_osm_file_list(self):
        '''
        @brief: This function is used to get osm(OpenStreetMap) file list from server.
        @see: Client
        @param None:
        @return: list Returns built-in Python's list() or 1 if error occurred. 
        '''
        
        client = Client()
        #Output list.
        self.outList = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confSHPDrawIntID, self.confSHPDrawIntKind)
        
        client.logger.log.info("Narrowing reference to SHPDraw.Basic reference")
        #Narrow reference to Basic interface.
        osmLstObj = obj._narrow(SHPDraw.Basic)
        if osmLstObj is None:
            client.logger.log.error("Object reference is no an SHPDraw::Basic")
            sys.exit(1)
        try:
            #Call get_osm_file_list function from shp_draw.idl file.
            self.outList = osmLstObj.get_osm_file_list()
            return self.outList
        except SHPDraw.UnknownInternalError as ex:
            client.logger.log.error("%s." % (ex.reason))
            return 1
        
    def client_get_osm_file_content(self, fileName):
        '''
        @brief: This function is used to get osm(OpenStreetMap) file content from server.
        @see: Client
        @param fileName string: Input parameter is a osm file name.
        @return: sequence<octet> Returns octet sequence or 1 if error occurred. 
        '''
        
        client = Client()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confSHPDrawIntID, self.confSHPDrawIntKind)
        
        client.logger.log.info("Narrowing reference to SHPDraw.Basic reference")
        #Narrow reference to Basic interface.
        osmLstObj = obj._narrow(SHPDraw.Basic)
        if osmLstObj is None:
            client.logger.log.error("Object reference is no an SHPDraw::Basic")
            sys.exit(1)
        try:
            #Call get_osm_file_content function from shp_draw.idl file.
            fileContent = osmLstObj.get_osm_file_content(fileName)
            return fileContent
        except SHPDraw.FileNotFound as ex:
            client.logger.log.error("%s.File: %s" % (ex.reason, ex.fileName))
            return 1

    def client_get_fwd_transformation(self, lons, lats, az, dist):
        '''
        @brief: This function is used to get forward transformation.
        @see: Client
        @param lons float: Input parameter is longitude value.
        @param lats float: Input parameter is latitude value.
        @param az float: Input parameter is azimuth value.
        @param dist float: Input parameter is distance value.
        @return: Returns longitudes, latitudes and back azimuths or 1 if error occurred.
        '''
        client = Client()
        
        #Forward transformation.
        self.fwdTransformation = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confGeodeticIntID, self.confGeodeticIntKind)
        
        client.logger.log.info("Narrowing reference to Projection.Geodetic reference")
        #Narrow reference to Geodetic interface.
        geodeticObj = obj._narrow(Projection.Geodetic)
        if geodeticObj is None:
            client.logger.log.error("Object reference is no an Projection::Geodetic")
            sys.exit(1)
        try:
            self.fwdTransformation = geodeticObj.get_fwd_transformation(lons, lats, az, dist)
            return self.fwdTransformation
        except Projection.ArgumentsNotInOrder as ex:
            client.logger.log.error(ex.reason)
            return 1
        
    def client_get_inv_transformation(self, lons1, lats1, lons2, lats2):
        '''
        @brief: This function is used to get inverse transformation.
        @see: Client
        @param lons1 float: Input parameter is start longitude value.
        @param lats1 float: Input parameter is start latitude value.
        @param lons2 float: Input parameter is end longitude value.
        @param lats2 float: Input parameter is end latitude value.
        @return: Returns forward and back azimuths, plus distances between initial points or 1 if error occurred.
        '''
        client = Client()
        
        #Forward transformation.
        self.invTransformation = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confGeodeticIntID, self.confGeodeticIntKind)
        
        client.logger.log.info("Narrowing reference to Projection.Geodetic reference")
        #Narrow reference to Geodetic interface.
        geodeticObj = obj._narrow(Projection.Geodetic)
        if geodeticObj is None:
            client.logger.log.error("Object reference is no an Projection::Geodetic")
            sys.exit(1)
        try:
            self.invTransformation = geodeticObj.get_inv_transformation(lons1, lats1, lons2, lats2)
            print(self.invTransformation.trans_azimuth)
            print(self.invTransformation.back_azimuth)
            print(self.invTransformation.dist)
            return self.invTransformation
        except Projection.ArgumentsNotInOrder as ex:
            client.logger.log.error(ex.reason)
            return 1
        
    def client_get_intermediate_points(self, lons1, lats1, lons2, lats2, npts):
        '''
        @brief: This function is used to get forward transformation.
        @see: Client
        @param lons1 float: Input parameter is start longitude value.
        @param lats1 float: Input parameter is start latitude value.
        @param lons2 float: Input parameter is end longitude value.
        @param lats2 float: Input parameter is end latitude value.
        @param npts integer: Input parameter is a number of points between start and end point. 
        @return: returns a list of longitude/latitude pairs describing npts or 1 if error occurred.
        '''
        client = Client()
        
        #Forward transformation.
        self.nptsList = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confGeodeticIntID, self.confGeodeticIntKind)
        
        client.logger.log.info("Narrowing reference to Projection.Geodetic reference")
        #Narrow reference to Geodetic interface.
        geodeticObj = obj._narrow(Projection.Geodetic)
        if geodeticObj is None:
            client.logger.log.error("Object reference is no an Projection::Geodetic")
            sys.exit(1)
        try:
            self.nptsList = geodeticObj.get_intermediate_points(lons1, lats1, lons2, lats2, npts)
            return self.nptsList
        except Projection.ArgumentsNotInOrder as ex:
            client.logger.log.error(ex.reason)
            return 1
        
    def client_get_projection_list(self):
        '''
        @brief: This function is used to get projection list.
        @see: Client
        @param: Function takes no input parameters.
        @return: returns a list of projection or 1 if error occurred.
        '''
        client = Client()
        
        self.projectionList = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confGeodeticIntID, self.confGeodeticIntKind)
        
        client.logger.log.info("Narrowing reference to Projection.Geodetic reference")
        #Narrow reference to Geodetic interface.
        geodeticObj = obj._narrow(Projection.Geodetic)
        if geodeticObj is None:
            client.logger.log.error("Object reference is no an Projection::Geodetic")
            sys.exit(1)
            
        self.projectionList = geodeticObj.get_projection_list()

        return self.projectionList
    
    def client_get_ellipsoid_list(self):
        '''
        @brief: This function is used to get ellipsoid list.
        @see: Client
        @param: Function takes no input parameters.
        @return: returns a list of ellipsoid or 1 if error occurred.
        '''
        client = Client()
        
        self.ellipsoidList = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confGeodeticIntID, self.confGeodeticIntKind)
        
        client.logger.log.info("Narrowing reference to Projection.Geodetic reference")
        #Narrow reference to Geodetic interface.
        geodeticObj = obj._narrow(Projection.Geodetic)
        if geodeticObj is None:
            client.logger.log.error("Object reference is no an Projection::Geodetic")
            sys.exit(1)
            
        self.ellipsoidList = geodeticObj.get_ellipsoid_list()

        return self.ellipsoidList
    
    def client_transform_coordinate_systems(self, in_projection, out_projection, x1, y1, z1=0):
        '''
        @brief: This function is used to get coordinate system after transform from another.
        @see: Client
        @param: Function takes no input parameters.
        @return: returns x2,y2,z2 in the coordinate system defined by out_projection.
        '''
        client = Client()
        
        self.output_coordinates = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confGeodeticIntID, self.confGeodeticIntKind)
        
        client.logger.log.info("Narrowing reference to Projection.Geodetic reference")
        #Narrow reference to Geodetic interface.
        geodeticObj = obj._narrow(Projection.Geodetic)
        if geodeticObj is None:
            client.logger.log.error("Object reference is no an Projection::Geodetic")
            sys.exit(1)
        try:    
            self.output_coordinates = geodeticObj.transform_coordinate_systems(in_projection, out_projection, x1, y1, z1)
            return self.output_coordinates
        except Projection.ArgumentsNotInOrder as ex:
            client.logger.log.error(ex.reason)
            return 1
        
    def client_get_pixel_size(self, dataset_path):
        ''' 
        @brief Function gets pixel size from raster data set.
        @param dataset_path String Path to raster data set source.
        @return: List Function returns raster pixel size (in format: (x, y)).
        '''
        client = Client()
        
        self.pixel_size = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.pixel_size = rasterObj.get_pixel_size(dataset_path)
            return self.pixel_size
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        
    def client_get_driver_name(self, dataset_path):
        ''' @brief Function gets driver name.
            @param dataset_path String Path to raster data set source.
            @return: List Function returns raster driver name (long and short name).
        '''
        
        client = Client()
        
        self.driver_name = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.driver_name = rasterObj.get_driver_name(dataset_path)
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        return self.driver_name
    
    def client_get_origin(self, dataset_path):
        ''' @brief Function gets origin of raster data set.
            @param dataset_path String Path to raster data set source.
            @return: Function returns origin. Top left x and top left y points.
        '''
        
        client = Client()
        
        self.origin = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.origin = rasterObj.get_origin(dataset_path)
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        return self.origin
    
    def client_get_raster_size(self, dataset_path):
        ''' @brief Function gets raster size.
            @param dataset_path String Path to raster data set source.
            @return: Function returns raster size (struct contains x size and y size).
        '''
        
        client = Client()
        
        self.raster_size = list()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.raster_size = rasterObj.get_raster_size(dataset_path)
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        return self.raster_size
    
    def client_get_projection_info(self, dataset_path):
        ''' @brief Function gets informations about projection.
            @param dataset_path String Path to raster data set source.
            @return: Function returns information about projection.
        '''
        
        client = Client()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.projection_info = rasterObj.get_projection_info(dataset_path)
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        return self.projection_info
    
    def client_get_raster_bands(self, dataset_path):
        ''' @brief Function gets informations about number of raster bands.
            @param dataset_path String Path to raster data set source.
            @return: Function returns number of raster bands.
        '''
        
        client = Client()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.raster_bands = rasterObj.get_raster_bands(dataset_path)
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        return self.raster_bands
    
    def client_get_metadata_list(self, dataset_path):
        ''' @brief Function gets informations about metadata.
            @param dataset_path String Path to raster data set source.
            @return: Function returns list of metadata related to raster source.
        '''
        
        client = Client()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.metadata_list = rasterObj.get_metadata_list(dataset_path)
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        return self.metadata_list
    
    def client_get_coordinate_system_info(self, dataset_path):
        ''' @brief Function gets informations about related coordinate system.
            @param dataset_path String Path to raster data set source.
            @return Function returns string that contains information about coordinate system.
        '''
        
        client = Client()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.coordinate_system = rasterObj.get_coordinate_system_info(dataset_path)
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        return self.coordinate_system
    
    def client_get_image_structure_info(self, dataset_path):
        ''' @brief Function gets information about image structure.
            @param dataset_path String Path to raster data set source.
            @return Function returns list of strings that contain information about image structure.
        '''
        
        client = Client()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.metadata_list = rasterObj.get_image_structure_info(dataset_path)
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        return self.metadata_list
    
        
    def client_get_image_corners(self, dataset_path):
        ''' @brief Function gets information about image corners.
            @param dataset_path String Path to raster data set source.
            @return Function returns list of image corners.
        '''
        
        client = Client()
        
        #Get reference to object.
        obj = client.get_reference_to_obj(self.confRasterIntID, self.confRasterIntKind)
        
        client.logger.log.info("Narrowing reference to Info.Raster reference")
        #Narrow reference to Raster interface.
        rasterObj = obj._narrow(Info.Raster)
        if rasterObj is None:
            client.logger.log.error("Object reference is no an Info::Raster")
            sys.exit(1)
        try:
            self.corner_list = rasterObj.get_image_corners(dataset_path)
        except Info.DatasetOpenFailed as ex:
            client.logger.log.error(ex.reason)
            return 1
        return self.corner_list