'''
Created on May 26, 2012

@author: bartek
'''

import sys
import os
import time

import SHPDraw
import SHPDraw__POA
import CORBA

sys.path.append("../../src/logger")
from Logger import Logger


class SHPDraw_i(SHPDraw__POA.Basic):
    '''
    Implementation of SHPDraw servant.
    '''
    
    def __init__(self):
        self.logger = Logger("SHPDraw Basic")
        self.dirLocation = "../../../data_files/gshhs";
        
    def get_shp_file_list(self):
        outFileList = list()
        for filename in sorted(os.listdir(self.dirLocation)):
            fileObj = SHPDraw.File(filename, time.ctime(os.path.getmtime(self.dirLocation+'/'+filename)),
            time.ctime(os.path.getctime(self.dirLocation+'/'+filename)))
            #SHPDraw.File.fName = filename
            #SHPDraw.File.lModified = time.ctime(os.path.getmtime(self.dirLocation+'/'+filename))
            #SHPDraw.File.cTime = time.ctime(os.path.getctime(self.dirLocation+'/'+filename))
            outFileList.append(fileObj)
        return outFileList