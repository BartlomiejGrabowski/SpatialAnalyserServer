'''
Created on Jul 7, 2012

@author: bartek
'''
import sys
import Info
import Info__POA

sys.path.append("../../src/logger")
from Logger import Logger

try:
    from osgeo import gdal
    from osgeo import osr
    from osgeo.gdalconst import *
except ImportError:
    import gdal
    
class RasterInfo_i(Info__POA.Raster):
    '''
    Implementation Raster interface.
    '''


    def __init__(self):
        #Create logger handler.
        self.logger = Logger("Info Raster", "../../../src/server/main/server.log")
    
    def get_pixel_size(self, dataset_path):
        ''' @brief Function gets pixel size from raster data set.
            @param dataset_path String Path to raster data set source.
            @return: List Function returns raster pixel size (in format: (x, y)).
        '''
        self.logger.log.info("get_pixel_size method invocation.")
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
            
        #(x, y).
        self.pixel_size = list()
        
        geotransform = dataset.GetGeoTransform()
        if geotransform is not None:
            #w-e pixel resolution.
            pixel_x_size = geotransform[1]
            #n-s pixel resolution.
            pixel_y_size = geotransform[5]
            
        #Create Pixel_X_Y_size structure from Info module.
        self.pixel_size = Info.Pixel_X_Y_size(pixel_x_size, pixel_y_size)
        
        return self.pixel_size
    
    def get_driver_name(self, dataset_path):
        ''' @brief Function gets driver name.
            @param dataset_path String Path to raster data set source.
            @return: List Function returns raster driver name (long and short name).
        '''
        
        self.logger.log.info("get_driver_name method invocation.")
        self.driver_name = list()
                
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
        
        try:
            driver_short_name = dataset.GetDriver().ShortName
            driver_long_name = dataset.GetDriver().LongName
            self.driver_name = Info.Driver(driver_short_name, driver_long_name)
        except Exception as ex:
            self.logger.error('Exception occurred during getting driver name.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
            
        return self.driver_name
    
    def get_origin(self, dataset_path):
        ''' @brief Function gets origin of raster data set.
            @param dataset_path String Path to raster data set source.
            @return: Function returns origin. Top left x and top left y points.
        '''
        self.logger.log.info("get_origin method invocation.")
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
            
        #(top left x, top left y).
        self.origin = list()
        
        geotransform = dataset.GetGeoTransform()
        if geotransform is not None:
            #top left x.
            origin_x = geotransform[0]
            #top left y.
            origin_y = geotransform[3]
            
        #Create Origin structure from Info module.
        self.origin = Info.Origin(origin_x, origin_y)
        
        return self.origin
    
    def get_raster_size(self, dataset_path):
        ''' @brief Function gets raster size.
            @param dataset_path String Path to raster data set source.
            @return: Function returns raster size (struct contains x size and y size).
        '''
        self.logger.log.info("get_raster_size method invocation.")
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
            
        #(x, y).
        self.raster_size = list()
        
        raster_size_x = dataset.RasterXSize
        raster_size_y = dataset.RasterYSize
            
        #Create Raster_size structure from Info module.
        self.raster_size = Info.Raster_size(raster_size_x, raster_size_y)
        
        return self.raster_size
    
    def get_projection_info(self, dataset_path):
        ''' @brief Function gets informations about projection.
            @param dataset_path String Path to raster data set source.
            @return: Function returns information about projection.
        '''
        self.logger.log.info("get_projection_info method invocation.")
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
            
        #Get informations about projection.
        Info.projection = dataset.GetProjection()
        
        return Info.projection
    
    def get_raster_bands(self, dataset_path):
        ''' @brief Function gets informations about number of raster bands.
            @param dataset_path String Path to raster data set source.
            @return: Function returns number of raster bands.
        '''
        self.logger.log.info("get_raster_bands method invocation.")
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
            
        #Get number of raster bands.
        Info.raster_bands = dataset.RasterCount
        
        return Info.raster_bands
    
    def get_metadata_list(self, dataset_path):
        ''' @brief Function gets informations about metadata.
            @param dataset_path String Path to raster data set source.
            @return: Function returns list of metadata related to raster source.
        '''
        self.logger.log.info("get_metadata_list method invocation.")
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
            metadata = dataset.GetMetadata_List()
            metadata_list = list()
        
            if metadata is not None and len(metadata) > 0 :
                for item in metadata:
                    metadata_list.append(item)
                    
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
              
        return metadata_list
    
    def get_coordinate_system_info(self, dataset_path):
        ''' @brief Function gets informations about related coordinate system.
            @param dataset_path String Path to raster data set source.
            @return Function returns string that contains information about coordinate system.
        '''
        self.logger.log.info("get_coordinate_system_info method invocation.")
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
            pszProjection = dataset.GetProjectionRef()
            
            #Report projection    
            if pszProjection is not None:

                spatialRef = osr.SpatialReference()
                if spatialRef.ImportFromWkt(pszProjection ) == gdal.CE_None:
                    wkt = spatialRef.ExportToPrettyWkt(False)

                    return wkt
                else:
                    return pszProjection
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
            
    def get_image_structure_info(self, dataset_path):
        ''' @brief Function gets information about image structure.
            @param dataset_path String Path to raster data set source.
            @return Function returns list of strings that contain information about image structure.
        '''
        self.logger.log.info("get_image_structure_info method invocation.")
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
            metadata_list = list()
            #Report IMAGE_STRUCTURE.
            papszMetadata = dataset.GetMetadata_List("IMAGE_STRUCTURE")
            if len(papszMetadata) > 0:
                for metadata in papszMetadata:
                    metadata_list.append(metadata)

        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
            
        return metadata_list
    
    def get_image_corners(self, dataset_path):
        ''' @brief Function gets information about image corners.
            @param dataset_path String Path to raster data set source.
            @return Function returns list of image corners.
        '''
        self.logger.log.info("get_image_corners method invocation.")
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
            pszProjection = dataset.GetGCPProjection()
            self.corner_list = list()
            hTransform = None
            if pszProjection is not None and len(pszProjection) > 0:
                hProj = osr.SpatialReference( pszProjection )
                if hProj is not None:
                    hLatLong = hProj.CloneGeogCS()
    
                if hLatLong is not None:
                    gdal.PushErrorHandler( 'CPLQuietErrorHandler' )
                    hTransform = osr.CoordinateTransformation( hProj, hLatLong )
                    gdal.PopErrorHandler()
                    if gdal.GetLastErrorMsg().find( 'Unable to load PROJ.4 library' ) != -1:
                        hTransform = None
                        
            corner = self.GDALInfoReportCorner(dataset, hTransform, 0.0, 0.0 )
            self.corner_list.append(Info.Coordinate(corner[0], corner[1]))
            
            corner = self.GDALInfoReportCorner(dataset, hTransform, 0.0, dataset.RasterYSize)
            self.corner_list.append(Info.Coordinate(corner[0], corner[1]))
            
            corner = self.GDALInfoReportCorner(dataset, hTransform, dataset.RasterXSize, 0.0)
            self.corner_list.append(Info.Coordinate(corner[0], corner[1]))
            
            corner = self.GDALInfoReportCorner(dataset, hTransform, dataset.RasterXSize, \
                                                dataset.RasterYSize)
            self.corner_list.append(Info.Coordinate(corner[0], corner[1]))
            
            corner = self.GDALInfoReportCorner(dataset, hTransform, dataset.RasterXSize/2.0, \
                                               dataset.RasterYSize/2.0)
            self.corner_list.append(Info.Coordinate(corner[0], corner[1]))
                
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)           
        return self.corner_list            
                    
    def GDALInfoReportCorner(self, hDataset, hTransform, x, y):
        corner = list()
        adfGeoTransform = hDataset.GetGeoTransform()
        if adfGeoTransform is not None:
            dfGeoX = adfGeoTransform[0] + adfGeoTransform[1] * x \
                + adfGeoTransform[2] * y
            dfGeoY = adfGeoTransform[3] + adfGeoTransform[4] * x \
                + adfGeoTransform[5] * y
    
        else:
            corner.append(x)
            corner.append(y)
            return corner
    
        if abs(dfGeoX) < 181 and abs(dfGeoY) < 91:
            corner.append(dfGeoX)
            corner.append(dfGeoY)
    
        else:
            corner.append(dfGeoX)
            corner.append(dfGeoY)
    
        if hTransform is not None:
            pnt = hTransform.TransformPoint(dfGeoX, dfGeoY, 0)
            if pnt is not None:
                corner.append(gdal.DecToDMS( pnt[0], "Long", 2))
                corner.append(gdal.DecToDMS( pnt[1], "Lat", 2))
    
        return corner
