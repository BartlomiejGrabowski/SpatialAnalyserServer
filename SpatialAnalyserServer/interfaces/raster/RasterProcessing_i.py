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
        try:
            im = Image.open(raster_file)
            if filter_name == 'BLUR':
                out = im.filter(ImageFilter.BLUR)
            if filter_name == 'CONTOUR':
                out = im.filter(ImageFilter.CONTOUR)
            if filter_name == 'DETAIL':
                out = im.filter(ImageFilter.DETAIL)
            if filter_name == 'EDGE_ENHANCE':
                out = im.filter(ImageFilter.EDGE_ENHANCE)
            if filter_name == 'EDGE_ENHANCE_MORE':
                out = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
            if filter_name == 'EMBOSS':
                out = im.filter(ImageFilter.EMBOSS)
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
    
    def contrast_image(self, raster_file, contrast):
        """ @brief Function adjusts contrast.
            @param raster_file string: Source raster file.
            @param mode_name string: contrast value.
            @return outfile string: Image after adjusting contrast. """
            
        import ImageEnhance
        
        outfile = '/tmp/' + contrast + os.path.basename(raster_file)
        print(outfile)
        try:
            im = Image.open(raster_file)
            enh = ImageEnhance.Contrast(im)
            if contrast == '0':
                enh.enhance(1).save(outfile)
            if contrast == '-10':
                enh.enhance(0.9 + int(contrast)/10).save(outfile)
                return outfile
            enh.enhance(1 + int(contrast)/10).save(outfile)
        except IOError as ex:
            raise Raster.FileException(str(ex))
        except KeyError as ex:
            raise Raster.InternalException(str(ex))      
        return outfile
    
    def brightness_image(self, raster_file, brightness):
        """ @brief Function is used to control the brightness of an image.
            @param raster_file string: Source raster file.
            @param brightness string: brightness value.
            @return outfile string: Function returns brightness enhancer instance. """
            
        import ImageEnhance
        
        outfile = '/tmp/'  + brightness + os.path.basename(raster_file)
        try:
            im = Image.open(raster_file)
            enh = ImageEnhance.Brightness(im)
            enh.enhance(float(brightness)).save(outfile)
        except IOError as ex:
            raise Raster.FileException(str(ex))
        except KeyError as ex:
            raise Raster.InternalException(str(ex))      
        return outfile
    
    def sharpness_image(self, raster_file, sharpness):
        """ @brief Function is used to control the sharpness of an image.
            @param raster_file string: Source raster file. 'sharpness'
            @param sharpness string: sharpness value.
            @return outfile string: Function returns sharpness enhancer instance. """
            
        import ImageEnhance
        
        outfile = '/tmp/' + sharpness + os.path.basename(raster_file)
        try:
            im = Image.open(raster_file)
            enh = ImageEnhance.Sharpness(im)
            enh.enhance(float(sharpness)).save(outfile)
        except IOError as ex:
            raise Raster.FileException(str(ex))
        except KeyError as ex:
            raise Raster.InternalException(str(ex))      
        return outfile
    
    def get_raster_file(self, fileName):
        self.logger.log.info("get_raster_file method invocation.")
    
        try:
            #Convert file content to the list of strings.
            fileContent = open(fileName, 'r').read()
        except IOError as ex:
            self.logger.error("%s exception occurred during opening raster file" % (ex))
            raise Raster.FileNotFound("Error occurred during opening raster file", fileName)
            sys.exit(1)
        return fileContent