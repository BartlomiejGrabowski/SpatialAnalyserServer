'''
Created on Mar 26, 2012

@author: bartek
'''
import psycopg2
import sys
import psycopg2.extras

class PostgresBasic(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def connectToDatabase(self, _db_name, _db_user, _db_passwd):
        print("Connecting to database ->%s" % (_db_name))
        try:
            #Get a connection.
            conn = psycopg2.connect(database=_db_name, user=_db_user, password=_db_passwd)
            print("Connected!\n")
        except:
            #Get the most recent exceptions.
            exType, exValue, exTraceback = sys.exc_info()
            sys.exit("Database connection failed!\n ->%s %s" % (exType, exValue))
        return conn
    
    def createCursor(self, _conn):
        print("Creating cursor to database\n")
        try:
            cursor = _conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
        except:
            #Get the most recent exceptions.
            exType, exValue, exTraceback = sys.exc_info()
            sys.exit("Cursor creation failed!\n ->%s %s" % (exType, exValue))    
        return cursor
    
    def executeQuery(self, _cursor, _query):
        print("Executing query ->%s" % (_query))
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
        
        
        
        
        
        
        
        
        
        
        
        
        