'''
Created on Mar 31, 2012

@author: bartek
'''
import sys
from omniORB import CORBA, PortableServer
import Example, Example__POA

class Echo_i (Example__POA.Echo):
    def echoString(self, mesg):
        print("echoString() called with message:", mesg)
        return mesg

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

ei = Echo_i()
eo = ei._this()

print orb.object_to_string(eo);

poaManager = poa._get_the_POAManager()
poaManager.activate()

orb.run();