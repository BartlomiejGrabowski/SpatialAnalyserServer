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
        
        try:
            dataset = gdal.Open(dataset_path, GA_ReadOnly)
        except Exception as ex:
            self.logger.error('Exception occurred during creating data set.')
            raise Info.DatasetOpenFailed(ex)
            sys.exit(1)
            
        if dataset is None:
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
        