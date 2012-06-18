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
        
        osmDirConf = doc.find('OSMFilesDirectory')
        #Fetch location of downloads folder.
        self.confOSMDirLocation = osmDirConf.find('Location').text


        
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
        try:
            #Convert file content to the list of strings.
            fileContent = open(absPath, 'r').read()
        except IOError as ex:
            self.logger.error("%s exception occurred during opening shp file" % (ex))
            raise SHPDraw.FileNotFound("Error occurred during openinf shp file", absPath)
            sys.exit(1)
<<<<<<< HEAD
        return fileContent
    
    def get_osm_file_list(self):
        self.logger.log.info("get_osm_file_list method invocation.")
        outFileList = list()
        try:
            for filename in sorted(os.listdir(self.confOSMDirLocation)):
                #Creating new file object.
                fileObj = SHPDraw.File(filename, time.ctime(os.path.getmtime(self.confOSMDirLocation+'/'+filename)),
                time.ctime(os.path.getctime(self.confOSMDirLocation+'/'+filename)))
                #Append file object to the result list.   
                outFileList.append(fileObj)
        except OSError as ex:
            self.logger.log.error("%s exception occurred during creating osm file list" % (ex))
            raise SHPDraw.UnknownInternalError("Error occurred during creating osm file list")
            sys.exit(1)
        return outFileList
    
    def get_osm_file_content(self, osmFileName):
        self.logger.log.info("get_osm_file_content method invocation.")
        absPath = self.confOSMDirLocation+'/'+osmFileName
        try:
            #Convert file content to the list of strings.
            fileContent = open(absPath, 'r').read()
        except IOError as ex:
            self.logger.error("%s exception occurred during opening osm file" % (ex))
            raise SHPDraw.FileNotFound("Error occurred during openinf osm file", absPath)
            sys.exit(1)
=======
>>>>>>> e4c450059ebc9624d89d515d50ca172e65a57b46
        return fileContent