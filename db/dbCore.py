'''
    Database super class
'''
import pymysql
import re
from random import uniform
from IPython.display import display, clear_output

class DBCore:
    
    def __init__(self, db='DGIndia'):
        try:
            self.__connection = pymysql.connect(host= "localhost", user="root", passwd="", db=db, charset='utf8')
            self.__curs = self.__connection.cursor()
            self.__curs.execute('SET collation_connection = utf8mb4_bin')
            if self.__connection.open:
                print('Mysql database successfuly connected')
            else:
                print('Mysql database connection failed') 
        except pymysql.Error as err:
            print("..Exception message:", err.args)
            
   
   
    
    def storeOperation(self, table, comment_id, process_doc, topics, reasons, date, rating, platform, prouct):
#         total = len(topics) * len(reasons)
        count = 0
        for topic in topics:
            for reason in reasons:
                data = (table, comment_id, topic, reason, date, rating, platform, prouct)
                query = """INSERT INTO %s VALUES (NULL, '%s','%s','%s','%s','%s','%s','%s')""" % data
                result = self.execute(query)
#                 count = count + 1
#                 clear_output(wait=True)
#                 display('Iteration '+str(count))
        
        
        
    def execute(self, query):
        if not self.isConnected():
            raise ValueError('Mysql server not connected')
        
        try:
            self.__curs.execute(query)
            result = self.__curs.fetchall()
            self.__connection.commit()
            return result
        except pymysql.Error as err:
            print('query is: ', query)
            print("..Exception message:", err.args)
            print('--- failed --')
            self.__connection.rollback()
            
    
    def addEsapesequence(self, comment): 
        return re.sub("(['\"])", r"\\\1", comment) #re.sub("([#$%^&_{}'\"])", r"\\\1", comment)

    
    def isConnected(self):
        return self.__connection.open
    
    
    def closeConnection(self):
        if self.isConnected():
            self.__curs.close()
            self.__connection.close()
            print('Closed mysql database connection')
        else:
            print('Already mysql database connection closed')
