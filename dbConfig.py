# Server Connection to MySQL:


import pymysql
import re
    
class dbSQL:
    
    def __init__(self):        
        self.connection = pymysql.connect(host= "localhost", user="root", passwd="1234", db='DGIndia', charset='utf8')
        self.curs = self.connection.cursor()
        self.curs.execute('SET collation_connection = utf8mb4_bin')

    def insert(self, rawData):
        name = self.addEsapesequence(rawData[0])
        date = '2019-02-10'
        comment = self.addEsapesequence(rawData[2])
        rating = rawData[3]
        
        data = (name, date, comment, rating)
        qry = """INSERT INTO `dbs_master_table`  VALUES (NULL, '%s','%s','%s','%s')"""
        #data = ('sulabh shukla', '2019-02-05', 'nice work ...', '3')
        #query = """INSERT INTO `dbs_master_table`  VALUES (NULL, 'sulabh shukla', '2019-02-05', 'nice work ...', '3');"""
        print('query:', qry % data)
        self.__execute(qry % data)
    
    def insertInMaster(self, data):        
        data = (name, date, comment, rating)
        qry = """INSERT INTO `dbs_master_table`  VALUES (NULL, '%s','%s','%s','%s')"""
        print('query:', qry % data)
        self.__execute(qry % data)
    
    def show(self):
        query = """SELECT * FROM `dbs_master_table`;"""
        results = self.__execute(query)
        for each in results:
            print(each)
            
    # store token array into table `dbs_combined_corpus`      
    def storeWordList(self, wList):
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
                query = """INSERT INTO `dbs_combined_corpus`  VALUES (NULL, '%s', '%s')""" % (token,maxValue)
                result = self.__execute(query)
            
    # add data into `dbs_attributes`
    def store_n_reasons(self, n_reasons):
        for each in n_reasons:
            query = """ SELECT hashValue  FROM dbs_combined_corpus WHERE words = '%s'""" % each
            hashValue = self.__execute(query)[0][0]
            query = """INSERT INTO `dbs_n_reasons` (id) VALUES ('%s')""" % (hashValue)
            result = self.__execute(query)
            print(each)
        
    # commentRow: [name, date, commnt]
    def storeOperation(self, comment_id, process_doc, topics, reasons, date, rating, platform, prouct):
        for topic in topics:
            for reason in reasons:
                data = (comment_id, topic, reason, date, rating, platform, prouct)
                query = """INSERT INTO `dbs_master` VALUES (NULL, '%s','%s','%s','%s','%s','%s','%s')"""  % (data)
                result = self.__execute(query)
                
                
    def __execute(self, query):
        try:
            self.curs.execute(query)
            result = self.curs.fetchall()
            self.connection.commit()
            return result
        except:
            print('query is: ', query)
            print('--- failed --')
            self.connection.rollback()
        self.connection.close()
        
    def addEsapesequence(self, comment): 
#         return re.sub("([#$%^&_{}'\"])", r"\\\1", comment)
        return re.sub("(['\"])", r"\\\1", comment)