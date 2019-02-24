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
        qry = """INSERT INTO `android_full_comments`  VALUES (NULL, '%s','%s','%s','%s')"""
        #data = ('sulabh shukla', '2019-02-05', 'nice work ...', '3')
        #query = """INSERT INTO `android_full_comments`  VALUES (NULL, 'sulabh shukla', '2019-02-05', 'nice work ...', '3');"""
        print('query:', qry % data)
        self.__execute(qry % data)
    
    def show(self):
        query = """SELECT * FROM `android_full_comments`;"""
        results = self.__execute(query)
        for each in results:
            print(each)
    
    def __execute(self, query):
        try:
            self.curs.execute(query)
            result = self.curs.fetchall()
            self.connection.commit()
            print('-- successful --')
            return result
        except:
            print('--- failed --')
            self.connection.rollback()
        self.connection.close()
        
    def addEsapesequence(self, comment): 
#         return re.sub("([#$%^&_{}'\"])", r"\\\1", comment)
        return re.sub("(['\"])", r"\\\1", comment)