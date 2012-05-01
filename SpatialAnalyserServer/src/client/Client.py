'''
Created on Apr 28, 2012

@author: bartek
'''
import sys
from omniORB import CORBA
import CosNaming

sys.path.append("../../interfaces/db")
sys.path.append("../../interfaces/shp")

import DB
import SHP

class Client(object):
    '''
    classdocs
    '''

    def __init__(self):
        # Initialise the ORB
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        # Obtain a reference to the root naming context
        self.obj = orb.resolve_initial_references("NameService")
        self.rootContext = self.obj._narrow(CosNaming.NamingContext)
        if self.rootContext is None:
            print("Failed to narrow the root naming context\n")
            sys.exit(1)
        
    def get_reference_to_obj(self, prefix, postfix):
        name = [CosNaming.NameComponent("Server", "Context"), CosNaming.NameComponent(prefix, postfix)]
        try:
            self.obj = self.rootContext.resolve(name)
            
        except CosNaming.NamingContext.NotFound, ex:
            print("Name not found\n")
            sys.exit(1)       
        return self.obj
        
client = Client()

obj = client.get_reference_to_obj("SHPShpToDB", "Object")

shpRef = obj._narrow(SHP.ShpToDB)
if shpRef is None:
    print("Object reference is no an SHP::ShpToDB\n")
    sys.exit(1)

shpRef.send_shp_to_postgres("/home/bartek/git/SpatialAnalyserServer/SpatialAnalyserServer/data_files/gshhs/GSHHS_l_L4.shp", "gshhs")