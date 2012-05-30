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

# Import interface implementation.
from Shp_i import Shp_i
from ShpToDB_i import ShpToDB_i
from SHPDraw_i import SHPDraw_i



class Server(object):
    
    def __init__(self):
        self.logger = Logger("Server")
        self.objContext = ''
        self.logger.log.info("Starting the server")
        self.logger.log.info("Activating CORBA ORB")
        self.orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        self.poa = self.orb.resolve_initial_references("RootPOA")
        
        obj = self.orb.resolve_initial_references("NameService")
        self.logger.log.info("Narrowing root context to naming context")
        rootContext = obj._narrow(CosNaming.NamingContext)
        
        if rootContext is None:
                self.logger.log.critical("Failed to narrow to root naming context")
                sys.exit(1)
                
        #Bind a context named "shp.my_context" to the roor context
        name = [CosNaming.NameComponent("Server", "Context")]
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
    
    server.bind_new_context("DBShp", "Object", dbObj)
    
    server.bind_new_context("SHPShpToDB", "Object", shpObj)
    
    server.bind_new_context("SHPDrawBasic", "Object", shpDrawObj)
    server.activate_POA()