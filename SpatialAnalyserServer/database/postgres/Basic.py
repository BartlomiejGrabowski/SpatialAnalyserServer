'''
Created on Mar 26, 2012

@author: bartek
'''
import psycopg2
import sys
import psycopg2.extras
import Queue

sys.path.append("../performance")
from FindDB import FindDB

sys.path.append("../src/logger")
from Logger import Logger

class PostgresBasic(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Initialize logging handler.
        '''
        ips = Queue.Queue()   
        times = {}
        fdb = FindDB(ips, times)
        fdb.set_conn_parameters()
        
        self.db = fdb.db
        self.user = fdb.user
        self.passwd = fdb.passwd
        
        self.logger = Logger("PostgresBasic", "postgres.log")
        
    def connectToDatabase(self):
        self.logger.log.info("Connecting to database: %s" % (self.db))

        conn = psycopg2.connect(database=self.db, user=self.user, password=self.passwd)
            
        self.logger.log.info("Connected to %s database as %s user" % (self.db, self.user))
        
        return conn
    
    def createCursor(self, _conn):
        self.logger.log.info("Creating cursor to database")
        try:
            cursor = _conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
        except:
            #Get the most recent exceptions.
            exType, exValue, exTraceback = sys.exc_info()
            sys.exit("Cursor creation failed!\n -> %s %s" % (exType, exValue))    
        return cursor
    
    def executeQuery(self, _cursor, _query):
        self.logger.log.info("Executing query: %s" % (_query))
        try:
            _cursor.execute(_query)
            row_count = 0
            for row in _cursor:
                row_count += 1
                print "row: %s    %s\r" % (row_count, row)
            return 0
        except:
            #Get the most recent exception.
            exType, exValue, exTraceback = sys.exc_info()
            #Exit and print exception.
            sys.exit("Query executing failed!\n -> %s %s" % (exType, exValue))
        
    
if __name__ == "__main__":    
    test = PostgresBasic()
    test.connectToDatabase("test_gis", "postgres", "postgres")
       
        
        
        
        
        
        
        
        
        
        