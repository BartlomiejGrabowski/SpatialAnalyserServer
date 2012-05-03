'''
Created on May 2, 2012

@author: bartek
'''

import logging

class Logger(object):
    '''
    Class Logger provides methods to write log informations.
    '''

    def __init__(self, myLogger):
        '''
        Set Logger environment and define log handlers.
        '''
        fName = "/home/bartek/git/SpatialAnalyserServer/SpatialAnalyserServer/src/server/main/server.log"
        self.log = logging.getLogger(myLogger)
        self.log.setLevel(logging.DEBUG)
        #creating console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        #create file handler
        fh = logging.FileHandler(fName)
        fh.setLevel(logging.DEBUG)
        
        #formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.log.addHandler(ch)
        self.log.addHandler(fh)
      
    def getLogger(self):
        return self.log
