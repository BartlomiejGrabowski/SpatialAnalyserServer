'''
Created on Mar 31, 2012

@author: bartek
'''
import sys
from omniORB import CORBA, PortableServer
import CosNaming
sys.path.append("../../../interfaces/db")
import DB
import DB__POA

"test.my_context/ExampleEcho.Object"
sys.path.append("../../../interfaces/db")
from Shp_i import Shp_i

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

shp_obj = Shp_i()
shp_ref = shp_obj._this()

obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
        print("Failed to narrow to root naming context\n")
        sys.exit(1)
        
#Bind a context named "shp.my_context" to the roor context
name = [CosNaming.NameComponent("shp", "my_context")]
try:
    shpContext = rootContext.bind_new_context(name)
    print("New shp context bound")
    
except CosNaming.NamingContext.AlreadyBound, ex:
    print("Shp context already exists")
    obj = rootContext.resolve(name)
    shpContext = obj._narrow(CosNaming.NamingContext)
    if shpContext is None:
        print("shp.my_context exists but is not a NamingContext")
        sys.exit(1)
        
#Bind the Shp object to the Shp context
name = [CosNaming.NameComponent("DBShp", "Object")]
try:
    shpContext.bind(name, shp_ref)
    print("New DB object bound")
    
except CosNaming.NamingContext.AlreadyBound:
    shpContext.rebind(name, shp_ref)
    print("DB binding already existed -- rebound")

#Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

#Block for ever (or until the ORB is shut down
orb.run();