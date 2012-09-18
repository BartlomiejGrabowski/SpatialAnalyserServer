'''
Created on Sep 16, 2012

@author: bartek
'''
import sys
import os
import Raster
import Raster__POA

import pyproj as pyproj

sys.path.append("../../src/logger")
from Logger import Logger

import Image
import ImageFilter

class RasterProcessing_i(Raster__POA.Processing):
    '''
    Implementation Geodetic interface
    '''
    
    def __init__(self):
        #Create logger handler.
        self.logger = Logger("Raster Processing", "../../../src/server/main/server.log")
        
    def image_filter(self, raster_file, filter_name):
        """ @brief Function applies filter on image.
            @param raster_file string: Source raster file.
            @param filter_name string: Filter name.
            @return outfile string: Image after filter applying. """
            
        outfile = '/tmp/' + filter_name + os.path.basename(raster_file)
        print(outfile)
        try:
            im = Image.open(raster_file)
            if filter_name == 'BLUR':
                out = im.convert(ImageFilter.BLUR)
            if filter_name == 'CONTOUR':
                out = im.filter(ImageFilter.CONTOUR)
            if filter_name == 'DETAIL':
                out = im.filter(ImageFilter.DETAIL)
            if filter_name == 'EDGE_ENHANCE':
                out = im.filter(ImageFilter.EDGE_ENHANCE)
            if filter_name == 'EDGE_ENHANCE_MORE':
                out = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
            if filter_name == 'FIND_EDGES':
                out = im.filter(ImageFilter.FIND_EDGES)
            if filter_name == 'SMOOTH':
                out = im.filter(ImageFilter.SMOOTH)
            if filter_name == 'SMOOTH_MORE':
                out = im.filter(ImageFilter.SMOOTH_MORE)
            if filter_name == 'SHARPEN':
                out = im.filter(ImageFilter.SHARPEN)
            if filter_name == 'None':
                return 'None'   
            out.save(outfile)
        except IOError as ex:
            raise Raster.FileException(str(ex))
        except KeyError as ex:
            raise Raster.InternalException(str(ex))      
        return outfile
    
    def convert_image(self, raster_file, mode_name):
        """ @brief Function converts image mode.
            @param raster_file string: Source raster file.
            @param mode_name string: mode name.
            @return outfile string: Image after filter applying. """
            
        outfile = '/tmp/' + mode_name + os.path.basename(raster_file)
        print(outfile)
        try:
            im = Image.open(raster_file)
            if mode_name == 'None':
                return 'None'   
            out = im.convert(mode_name)
            out.save(outfile)
        except IOError as ex:
            raise Raster.FileException(str(ex))
        except KeyError as ex:
            raise Raster.InternalException(str(ex))      
        return outfile