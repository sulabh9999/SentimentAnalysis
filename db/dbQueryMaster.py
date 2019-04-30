''' 
  - This files inherits base db query from its super class 'DBCore'.
  - Used to write query to make main db file for server usage.
''' 

import pymysql
import re
from .dbCore import DBCore
    
class DBQueryMaster(DBCore):
    
    def __init__(self, db='DGIndia'): 
        super().__init__(db)
    
    
    def insertInMaster(self, table, data):        
        data = (name, date, comment, rating)
        qry = """INSERT INTO `""" + table + """`  VALUES (NULL, '%s','%s','%s','%s')"""
        print('query:', qry % data)
        self.__execute(qry % data)
    
    
    def show(self, table):
        query = """SELECT * FROM %s""" % table
        results = self.__execute(query)
        for each in results:
            print(each)
                  
    # commentRow: [name, date, commnt]
    def storeprocessedComments(self, tableName, comment_id, processed_doc, topics, reasons, date, rating, platform, product):
        data = (tableName, comment_id, processed_doc, topics, reasons, date, rating, platform, product)
        query = """INSERT INTO %s (`comment_id`, `processed_comment`, `topic`, `reason`, `date`, `rating`, `platform`, `product`) VALUES ('%s','%s','%s','%s','%s','%s','%s', '%s')""" 
        self.__execute(query % data)
                
     
    # generate table for server to show( source: source table, destination: destination table)
    def generateTableForServer(self, source, destination):
        fetchQuery = """SELECT * FROM %s""" % source
        fetchedData = self.__execute(fetchQuery)
        storeQuery = """INSERT INTO %s (`comment_id`, `topic`, `reason`, `date`, `rating`, `platform`, `product`) 
                   VALUES ('%s','%s','%s','%s','%s','%s','%s')
                   """
        for row in fetchedData:
            #  0         1             2          3        4      5        6       7           8
            # id	comment_id  	comment 	topic	reason	date	rating	platform	product
            commentID = row[1]
            topics = [topic.strip() for topic in row[3].split(',')]
            reasons = [reason.strip() for reason in row[4].split(',')]
            date = row[5]
            rating = row[6]
            platform = row[7]
            product = row[8]
            
            for topic in topics:
                for reason in reasons:
                    data = (destination, commentID, topic, reason, date, rating, platform, product)
                    storeQuery
#                     print('%s %s %s' %(commentID, topic, reason))
                    self.__execute(storeQuery % data)
        
        
    def __execute(self, query):
        return self.execute(query)
    
    