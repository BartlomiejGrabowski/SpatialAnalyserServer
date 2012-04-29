'''
Created on Mar 31, 2012

@author: bartek
'''
import sys
from omniORB import CORBA, PortableServer
import CosNaming

sys.path.append("../../../interfaces/db")
sys.path.append("../../../interfaces/shp")

# Import interface implementation.
from Shp_i import Shp_i
from ShpToDB_i import ShpToDB_i

class Server(object):
    
    def __init__(self):
        self.objContext = ''
        self.orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        self.poa = self.orb.resolve_initial_references("RootPOA")
        
        obj = self.orb.resolve_initial_references("NameService")
        rootContext = obj._narrow(CosNaming.NamingContext)
        
        if rootContext is None:
                print("Failed to narrow to root naming context\n")
                sys.exit(1)
                
        #Bind a context named "shp.my_context" to the roor context
        name = [CosNaming.NameComponent("Server", "Context")]
        try:
            self.objContext = rootContext.bind_new_context(name)
            print("New context bound")
            
        except CosNaming.NamingContext.AlreadyBound, ex:
            print("Context already exists")
            obj = rootContext.resolve(name)
            self.objContext = obj._narrow(CosNaming.NamingContext)
            if self.objContext is None:
                print("Server.Context exists but is not a NamingContext")
                sys.exit(1)       
        
    def bind_new_context(self, prefix, postfix, newObj):
        # Fetch a reference to object.
        objRef = newObj._this()
        # Bind new context.
        newContext = [CosNaming.NameComponent(prefix, postfix)]
        try:
            self.objContext.bind(newContext, objRef)
            print("New %s.%s object bound" % (prefix, postfix))           
        
        except CosNaming.NamingContext.AlreadyBound:
            self.objContext.rebind(newContext, objRef)
            print("%s.%s binding already existed -- rebound" % (prefix, postfix))
            
    def activate_POA(self):
        #Activate the POA
        poaManager = self.poa._get_the_POAManager()
        poaManager.activate()
        
        #Block for ever (or until the ORB is shut down
        self.orb.run();
        
if __name__ == "__main__":        
    server = Server()
    
    #Create DB object.
    dbObj = Shp_i()    
    #Create SHP object.
    shpObj = ShpToDB_i()
    
    server.bind_new_context("DBShp", "Object", dbObj)
    server.bind_new_context("SHPShpToDB", "Object", shpObj)
    server.activate_POA()