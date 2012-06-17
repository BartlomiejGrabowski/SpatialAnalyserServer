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

#sys.path.append("../../interfaces/db")
#sys.path.append("../../interfaces/shp")

import DB
import SHP
import SHPDraw
import xml.etree.ElementTree as ET

class Client(object):
    '''
    Client class implementation.
    '''

    def __init__(self):
        self.logger = Logger("Client", "../client.log")
        # Initialize the ORB
        self.logger.log.info("Initialize the ORB")
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        # Obtain a reference to the root naming context
        self.logger.log.info("Obtain a reference to the root naming context")
        self.obj = orb.resolve_initial_references("NameService")
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
        
        #SHPDraw INTERFACE.
        shpDrawConf = interfacesConf.find('ShpDraw')
        #Fetch ID from interface.
        self.confSHPDrawIntID = shpDrawConf.find('ID').text
        #Fetch kind of interface.
        self.confSHPDrawIntKind = shpDrawConf.find('Kind').text
        
        #Images XML TAG.
        iconsDirConf = doc.find('IconsDir')
        #Fetch images location directory.
        self.confIconsDir = iconsDirConf.find('Location').text
        
        
    def get_reference_to_obj(self, prefix, postfix):
        self.logger.log.info("Getting reference to %s.%s object" % (prefix, postfix))
        name = [CosNaming.NameComponent(self.confServerContext, self.confObjectContext), CosNaming.NameComponent(prefix, postfix)]
        try:
            self.obj = self.rootContext.resolve(name)            
        except CosNaming.NamingContext.NotFound, ex:
            self.logger.log.error("Name not found. Error: %s" % (ex))
            sys.exit(1)       
        return self.obj
    
    def client_send_shp_to_postgres(self, fileName, tabName):
        client = Client()
        
        obj = client.get_reference_to_obj(self.confSHPIntID, self.confSHPIntKind)
        
        client.logger.log.info("Narrowing to SHP.ShpToDB reference")
        shpRef = obj._narrow(SHP.ShpToDB)
        if shpRef is None:
            client.logger.log.error("Object reference is no an SHP::ShpToDB")
            sys.exit(1)       
        try:
            client.logger.log.info("Calling send_shp_to_postgres() function")
            shpRef.send_shp_to_postgres(fileName, tabName)
            return 0
        except SHP.FileDoesNotExist as ex:
            client.logger.log.error("%s. %s" % (ex.reason, ex.fileName))
            return 1
        except SHP.CannotConnectToDB as ex:
            client.logger.log.error("%s. %s" % (ex.reason, ex.dbName))
            return 1
            
    def client_send_wbd_to_postgres(self, fileName):
        client = Client()
        
        obj = client.get_reference_to_obj(self.confSHPIntID, self.confSHPIntKind)
        
        client.logger.log.info("Narrowing to SHP.ShpToDB reference")
        shpRef = obj._narrow(SHP.ShpToDB)
        if shpRef is None:
            client.logger.log.error("Object reference is no an SHP::ShpToDB")
            sys.exit(1)
        try:
            srcFile = os.path.join(sys.path[0], "../../data_files/TM_WORLD_BORDERS-0.3", "TM_WORLD_BORDERS-0.3.shp")
            client.logger.log.info("Calling send_wbd_to_postgres() function")
            shpRef.send_wbd_to_postgres(srcFile)
            return 0
        except SHP.FileDoesNotExist as ex:
            client.logger.log.error("%s. %s" % (ex.reason, ex.fileName))
            return 1
        except SHP.CannotConnectToDB as ex:
            client.logger.log.error("%s. %s" % (ex.reason, ex.dbName))
            return 1
        
    def client_get_shp_file_list(self):
        client = Client()
        self.outList = list()
        
        obj = client.get_reference_to_obj(self.confSHPDrawIntID, self.confSHPDrawIntKind)
        
        client.logger.log.info("Narrowing reference to SHPDraw.Basic reference")
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
        client = Client()
        
        obj = client.get_reference_to_obj(self.confSHPDrawIntID, self.confSHPDrawIntKind)
        
        client.logger.log.info("Narrowing reference to SHPDraw.Basic reference")
        shpLstObj = obj._narrow(SHPDraw.Basic)
        if shpLstObj is None:
            client.logger.log.error("Object reference is no an SHPDraw::Basic")
            sys.exit(1)
        try:
            fileContent = shpLstObj.get_shp_file_content(fileName)
            return fileContent
        except SHPDraw.FileNotFound as ex:
            client.logger.log.error("%s.File: %s" % (ex.reason, ex.fileName))
            return 1
        
    def client_get_osm_file_list(self):
        client = Client()
        self.outList = list()
        
        obj = client.get_reference_to_obj(self.confSHPDrawIntID, self.confSHPDrawIntKind)
        
        client.logger.log.info("Narrowing reference to SHPDraw.Basic reference")
        osmLstObj = obj._narrow(SHPDraw.Basic)
        if osmLstObj is None:
            client.logger.log.error("Object reference is no an SHPDraw::Basic")
            sys.exit(1)
        try:
            self.outList = osmLstObj.get_osm_file_list()
            return self.outList
        except SHPDraw.UnknownInternalError as ex:
            client.logger.log.error("%s." % (ex.reason))
            return 1
        
    def client_get_osm_file_content(self, fileName):
        client = Client()
        
        obj = client.get_reference_to_obj(self.confSHPDrawIntID, self.confSHPDrawIntKind)
        
        client.logger.log.info("Narrowing reference to SHPDraw.Basic reference")
        osmLstObj = obj._narrow(SHPDraw.Basic)
        if osmLstObj is None:
            client.logger.log.error("Object reference is no an SHPDraw::Basic")
            sys.exit(1)
        try:
            fileContent = osmLstObj.get_osm_file_content(fileName)
            return fileContent
        except SHPDraw.FileNotFound as ex:
            client.logger.log.error("%s.File: %s" % (ex.reason, ex.fileName))
            return 1

            