'''
Created on Apr 22, 2012

@author: bartek
'''

import DB__POA

class Shp_i(DB__POA.Shp):
    '''
    classdocs
    '''
    def getShp(self, file_name):
        print("Calling getShp() function test \n")
        file_name = "kupa"
        return file_name

    def __init__(self):
        '''
        Constructor
        '''
        