# Server Connection to MySQL:


import pymysql
    
class dbSQL:
    
    def __init__(self):        
        self.connection = pymysql.connect(host= "localhost", user="root", passwd="1234", db='DGIndia')
        self.curs = self.connection.cursor()

    def insert(self, data):
        escaped = data[2].translate(str.maketrans({"-":  r"\-",
                                          "]":  r"\]",
                                          "\\": r"\\",
                                          "^":  r"\^",
                                          "$":  r"\$",
                                          "*":  r"\*",
                                          ".":  r"\."}))
        
        qry = """INSERT INTO `android_full_comments`  VALUES (NULL,'%s','%s','%s','%s')"""
        #data = ('sulabh shukla', '2019-02-05', 'nice work ...', '3')
        #query = """INSERT INTO `android_full_comments`  VALUES (NULL, 'sulabh shukla', '2019-02-05', 'nice work ...', '3');"""
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
        
