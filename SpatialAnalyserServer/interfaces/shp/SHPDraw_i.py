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
import xml.etree.ElementTree as ET

class SHPDraw_i(SHPDraw__POA.Basic):
    '''
    Implementation of SHPDraw servant.
    '''
    
    def __init__(self):
        self.logger = Logger("SHPDraw Basic", "../../../src/server/main/server.log")
        #Open xml configuration file.
        configurationFile = ET.parse('../conf/serverConf.xml')
        doc = configurationFile.getroot()
        shpDirConf = doc.find('SHPFilesDirectory')
        #Fetch location of downloads folder.
        self.confSHPDirLocation = shpDirConf.find('Location').text


        
    def get_shp_file_list(self):
        self.logger.log.info("get_shp_file_list method invocation.")
        outFileList = list()
        try:
            for filename in sorted(os.listdir(self.confSHPDirLocation)):
                #Creating new file object.
                fileObj = SHPDraw.File(filename, time.ctime(os.path.getmtime(self.confSHPDirLocation+'/'+filename)),
                time.ctime(os.path.getctime(self.confSHPDirLocation+'/'+filename)))
                #Append file object to the result list.   
                outFileList.append(fileObj)
        except OSError as ex:
            self.logger.log.error("%s exception occurred during creating shp file list" % (ex))
            raise SHPDraw.UnknownInternalError("Error occurred during creating shp file list")
            sys.exit(1)
        return outFileList
    
    def get_shp_file_content(self, shpFileName):
        self.logger.log.info("get_shp_file_content method invocation.")
        absPath = self.confSHPDirLocation+'/'+shpFileName
        #Convert file content to the list of strings.
        fileContent = open(absPath, 'r').read()
        return fileContent