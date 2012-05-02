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
        self.log = logging.getLogger(myLogger)
        self.log.setLevel(logging.DEBUG)
        #creating console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        #formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        self.log.addHandler(ch)
      
    def getLogger(self):
        return self.log
