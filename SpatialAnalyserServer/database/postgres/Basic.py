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
    """
    This class is is a helper class used to perform basic operations on the Postgres database.
    @author: Bartlomiej Grabowski
    @version: 1.0
    """

    def __init__(self):
        """
        Initialize basic Postgres database's parameters such as:
        -name of database,
        -database user name,
        -password to database.
        """
        
        ips = Queue.Queue()   
        times = {}
        fdb = FindDB(ips, times)
        
        #Fetch database's parameters.
        fdb.set_conn_parameters()
        
        #Set value of parameters.
        self.db = fdb.db
        self.user = fdb.user
        self.passwd = fdb.passwd
        
        #Create new logger handle. Log to file 'postger.log'.
        self.logger = Logger("PostgresBasic", "postgres.log")
        
    def connectToDatabase(self):
        """
        @brief: This function is used to create a new connection to a Postgres database.
        @see: PostgresBasic
        @param None:
        @return: handle to a Postgres database. 
        """
        
        self.logger.log.info("Connecting to database: %s" % (self.db))

        conn = psycopg2.connect(database=self.db, user=self.user, password=self.passwd)
            
        self.logger.log.info("Connected to %s database as %s user" % (self.db, self.user))
        
        return conn
    
    def createCursor(self, _conn):
        """
        @brief: This function is used to create new cursor to a Postgres connection.
        @see: PostgresBasic
        @param _conn Int: Input parameter is a handle to a Postgres database.
        @return: cursor to a new Postgres connection. 
        """
        
        self.logger.log.info("Creating cursor to database")
        try:
            cursor = _conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
        except:
            #Get the most recent exception.
            exType, exValue, exTraceback = sys.exc_info()
            sys.exit("Cursor creation failed!\n -> %s %s" % (exType, exValue)) 
               
        return cursor
    
    def executeQuery(self, _cursor, _query):
        """
        @brief: This function is used to execute a query to the Postgres database.
        @see: PostgresBasic
        @param _cursor cursor: Input parameter is a cursor to Postgres database.
        @param _query string: Input parameter is a query string.
        @return: int Returns a 0 if successful.
        """
        
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
       
        
        
        
        
        
        
        
        
        
        