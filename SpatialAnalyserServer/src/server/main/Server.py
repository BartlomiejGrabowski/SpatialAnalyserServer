'''
Created on Mar 31, 2012

@author: bartek
'''
import sys
from omniORB import CORBA, PortableServer
import CosNaming

sys.path.append("../../logger")
from Logger import Logger

sys.path.append("../../../database/performance")
from FindDB import FindDB

sys.path.append("../../../database/postgres")
from Basic import PostgresBasic

sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")
sys.path.append("../../../interfaces/projections")
sys.path.append("../../../interfaces/info")
sys.path.append("../../../interfaces/geo")
sys.path.append("../../../interfaces/raster")

# Import interface implementation.
from Shp_i import Shp_i
from ShpToDB_i import ShpToDB_i
from SHPDraw_i import SHPDraw_i
from GeodeticComputation_i import GeodeticComputation_i
from RasterInfo_i import RasterInfo_i
from Geo_i import Geo_i
from RasterProcessing_i import RasterProcessing_i


import xml.etree.ElementTree as ET


class Server(object):
    
    def __init__(self):
        self.logger = Logger("Server", "server.log")
        self.objContext = ''
        
        #Open xml configuration file.
        configurationFile = ET.parse('../conf/serverConf.xml')
        doc = configurationFile.getroot()
        #NamingContext XML TAG.
        namingContextConf = doc.find('NamingContext')
        #Fetch name of server context.
        self.confServerContext = namingContextConf.find('ServerContext').text
        #Fetch name of object context.
        self.confObjectContext = namingContextConf.find('ObjectContext').text
        #Fetch name of name service.
        self.confNameService = namingContextConf.find('NameService').text
        
        #POA XML TAG.
        POAConf = doc.find('POA')
        #Fetch POA name.
        self.confPOAName = POAConf.find('Name').text
        
        #Contexts XML TAG.
        confContexts = doc.find('Contexts')
        
        #Interface Shp context.
        confShpContext = confContexts.find('Shp')
        #Fetch ID of Shp context.
        self.confShpContextID = confShpContext.find('ID').text
        #Fetch kind of Shp context.
        self.confShpContextKind = confShpContext.find('Kind').text
        
        #Interface ShpToDB context.
        confShpToDBContext = confContexts.find('ShpToDB')
        #Fetch ID of ShpToDB context.
        self.confShpToDBContextID = confShpToDBContext.find('ID').text
        #Fetch kind of ShpToDB context.
        self.confShpToDBContextKind = confShpToDBContext.find('Kind').text
        
        #Interface SHPDraw context.
        confSHPDrawContext = confContexts.find('SHPDraw')
        #Fetch ID of SHPDraw context.
        self.confSHPDrawContextID = confSHPDrawContext.find('ID').text
        #Fetch kind of SHPdraw context.
        self.confSHPDrawContextKind = confSHPDrawContext.find('Kind').text
        
        #Interface Geodetic context.
        confGeodeticContext = confContexts.find('Geodetic')
        #Fetch ID of Geodetic context.
        self.confGeodeticContextID = confGeodeticContext.find('ID').text
        #Fetch kind of Geodetic context.
        self.confGeodeticContextKind = confGeodeticContext.find('Kind').text
        
        #Interface Raster context.
        confRasterContext = confContexts.find('Raster')
        #Fetch ID of Raster context.
        self.confRasterContextID = confRasterContext.find('ID').text
        #Fetch kind of Raster context.
        self.confRasterContextKind = confRasterContext.find('Kind').text
        
        #Interface Basic context.
        confBasicContext = confContexts.find('Basic')
        #Fetch ID of Basic context.
        self.confBasicContextID = confBasicContext.find('ID').text
        #Fetch kind of Basic context.
        self.confBasicContextKind = confBasicContext.find('Kind').text

        #Interface Processing context.
        confProcessingContext = confContexts.find('Processing')
        #Fetch ID of Processing context.
        self.confProcessingContextID = confProcessingContext.find('ID').text
        #Fetch kind of Processing context.
        self.confProcessingContextKind = confProcessingContext.find('Kind').text
        
        
        self.logger.log.info("Starting the server")
        self.logger.log.info("Activating CORBA ORB")
        self.orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        self.poa = self.orb.resolve_initial_references(self.confPOAName)
        
        obj = self.orb.resolve_initial_references(self.confNameService)
        self.logger.log.info("Narrowing root context to naming context")
        rootContext = obj._narrow(CosNaming.NamingContext)
        
        if rootContext is None:
                self.logger.log.critical("Failed to narrow to root naming context")
                sys.exit(1)
                
        #Bind a context named "shp.my_context" to the roor context
        name = [CosNaming.NameComponent(self.confServerContext, self.confObjectContext)]
        try:
            self.objContext = rootContext.bind_new_context(name)
            self.logger.log.info("Bounding new context")
            
        except CosNaming.NamingContext.AlreadyBound, ex:
            self.logger.log.warn("Context already exists")
            obj = rootContext.resolve(name)
            self.objContext = obj._narrow(CosNaming.NamingContext)
            if self.objContext is None:
                self.logger.log.critical("Server.Context exists but is not a NamingContext")
                sys.exit(1)       
        
    def bind_new_context(self, prefix, postfix, newObj):
        # Fetch a reference to object.
        objRef = newObj._this()
        # Bind new context.
        newContext = [CosNaming.NameComponent(prefix, postfix)]
        try:
            self.logger.log.info("Binding new %s.%s context" % (prefix, postfix))
            self.objContext.bind(newContext, objRef)
            self.logger.log.info("New %s.%s object bound" % (prefix, postfix))           
        
        except CosNaming.NamingContext.AlreadyBound:
            self.objContext.rebind(newContext, objRef)
            self.logger.log.warn("%s.%s binding already existed -- rebound" % (prefix, postfix))
            
    def activate_POA(self):
        #Activate the POA
        self.logger.log.info("Activating POA Manager")
        poaManager = self.poa._get_the_POAManager()
        poaManager.activate()
        
        #Block for ever (or until the ORB is shut down
        self.logger.log.info("ORB is running")
        self.orb.run();
        
if __name__ == "__main__":        
    server = Server()
    
    #Create DB object.
    dbObj = Shp_i()    
    #Create SHP object.
    shpObj = ShpToDB_i()
    #Create SHPDraw object.
    shpDrawObj = SHPDraw_i()
    #Create Geodetic object.
    geodeticObj = GeodeticComputation_i()
    #Create Raster object.
    rasterObj = RasterInfo_i()
    #Create Basic object.
    basicObj = Geo_i()
    #Create Processing object.
    processingObj = RasterProcessing_i()
    
    server.bind_new_context(server.confShpContextID, server.confShpContextKind, dbObj)
    
    server.bind_new_context(server.confShpToDBContextID, server.confShpToDBContextKind, shpObj)
    
    server.bind_new_context(server.confSHPDrawContextID, server.confSHPDrawContextKind, shpDrawObj)
    
    server.bind_new_context(server.confGeodeticContextID, server.confGeodeticContextKind, geodeticObj)
    
    server.bind_new_context(server.confRasterContextID, server.confRasterContextKind, rasterObj)
    
    server.bind_new_context(server.confBasicContextID, server.confBasicContextKind, basicObj)
    
    server.bind_new_context(server.confProcessingContextID, server.confProcessingContextKind, processingObj)
    server.activate_POA()