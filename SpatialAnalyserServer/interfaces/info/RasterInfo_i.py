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
            