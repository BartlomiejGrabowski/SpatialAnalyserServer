'''
Created on Mar 31, 2012

@author: bartek
'''
import database.postgres.Basic
from database.performance import FindDB

if __name__ == '__main__':
    p = FindDB()
    p.pingTiming()