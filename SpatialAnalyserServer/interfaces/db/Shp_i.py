'''
Created on Apr 22, 2012

@author: bartek
'''

import DB__POA

class Shp_i(DB__POA.Shp):
    '''
    classdocs
    '''
    def getShp(self, fileName):
        print("Calling getShp() function test \n")
        fileName = "test"
        return fileName

    def __init__(self):
        '''
        Constructor
        '''
        