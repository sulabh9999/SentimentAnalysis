''' 
  - This files inherits base db query from its super class 'DBCore'.
  - Used to write query to minor operations in db.
''' 

import pymysql
import re
from .dbCore import DBCore
from config.sConstants import SConstants
    
class DBQueryUtills(DBCore):
    
    def __init__(self, db='DGIndia'): 
        super().__init__(db)
    
#     class fetch:
    def getTopic(self, table=SConstants.table.topic):        
        query = """select topic from %s""" % (table)
        return [each[0] for each in self.__execute(query)] 

    
    def getNReasons(self, table=SConstants.table.nReason):
        query = """select n_reason from %s""" % (table)
        return [each[0] for each in self.__execute(query)] 

    
    def getPReasons(self, table=SConstants.table.pReason):
        query = """select p_reason from %s""" % (table)
        return [each[0] for each in self.__execute(query)]
    
    
    def getAllKeys(self, table=SConstants.table.allKeyword):
        query = """select keyword from %s""" % (table)
        return [each[0] for each in self.__execute(query) if each is not None]

    
    # store token array into table `dbs_combined_corpus`      
    def storeWordList(self, table, wList):
        for token in wList:
            token = self.addEsapesequence(token)
            query = """SELECT * FROM `dbs_combined_corpus` where words='%s';""" % token
            result = self.__execute(query)
            maxValue = 0
            if len(result) == 0:
                query = """SELECT MAX(hashValue) FROM `dbs_combined_corpus`"""
                result = self.__execute(query)
                if result[0][0] != None:
                    maxValue = result[0][0] + 1
                query = """INSERT INTO `dbs_combined_corpus`  VALUES (NULL, '%s', '%s')""" % (token, maxValue)
                result = self.__execute(query)
            
            
    # add data into `dbs_attributes`
    def store_n_reasons(self, table, n_reasons):
        for each in n_reasons:
            query = """ SELECT hashValue  FROM dbs_combined_corpus WHERE words = '%s'""" % each
            hashValue = self.__execute(query)[0][0]
            query = """INSERT INTO `dbs_n_reasons` (id) VALUES ('%s')""" % (hashValue)
            result = self.__execute(query)
            print(each)
        
        
    
    def __execute(self, query):
        return self.execute(query)
    
    
    
    