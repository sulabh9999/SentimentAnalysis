# contains queries for web cupport
from .dbCore import DBCore
from config.sConstants import SConstants
import json

class DBWebQuery(DBCore):
    
    def __init__(self, db='DGIndia'):
        super().__init__(db)
        self.table = SConstants.table.master

    def __execute(self, query, isJson=True):
        if isJson:
            rows = self.execute(query) 
            return json.dumps(dict(list(rows)))
        else:
            return self.execute(query)
     


    # get Top n frequen element from table
    def __getTopFrequent(self, column, total, table=SConstants.table.master, isJson=True):
    	parm = (column, column, table, column, total)
    	#SELECT `topic`, COUNT(`topic`) AS `value_occurrence` FROM `dbs_master_2` GROUP BY topic ORDER BY `value_occurrence` DESC LIMIT 5
    	query = """SELECT %s, COUNT(%s) AS `value_occurrence` FROM %s GROUP BY %s ORDER BY `value_occurrence` DESC LIMIT %d"""
    	return self.__execute(query % parm, isJson)




        # get Top n frequen element from table
    def __getReasonForTopic(self, topic, total, isJson=True):
        table=SConstants.table.master
        reasonColumn = 'reason'
        topicColumn = 'topic'
        parm = (reasonColumn, reasonColumn, table, topicColumn, topic, reasonColumn, total)
        # SELECT `reason`, COUNT(`reason`) AS `value_occurrence` FROM `dbs_master_2` WHERE `topic`= "app" GROUP BY reason ORDER BY `value_occurrence` DESC LIMIT 5
        query = """SELECT %s, COUNT(%s) AS `value_occurrence` FROM %s WHERE %s = '%s' and rating < 3 GROUP BY %s ORDER BY `value_occurrence` DESC LIMIT %d"""
        return self.__execute(query % parm, isJson)



    def getData(self, start, end, country, platform, top):
        print('start: ', start)
        print('end: ', end)
        print('country: ', country)
        print('platform: ', platform)
        finalResult = {}
        topicJson = self.__getTopFrequent('topic', top, self.table, isJson=True)
        topicDict = json.loads(topicJson) 

        for topic, frequency in topicDict.items():
                reasonResult = self.__getReasonForTopic(topic, 6)
                finalResult[topic] = [frequency, json.loads(reasonResult)]
        return finalResult
        