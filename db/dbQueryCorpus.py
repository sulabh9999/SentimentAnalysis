''' 
  - This files inherits base db query from its super class 'DBCore'.
  - Used to write query to perform operation for existing corpus crating/update.
''' 

import pymysql
import re
import os
import pandas as pd
from .dbCore import DBCore
# from config.sConstants import topicFilePath
# from config.sConstants import nReasonFilePath
from config.sConstants import SConstants

    
class DBQueryCorpus(DBCore):
    
    def __init__(self, db='DGIndia'):
        super().__init__(db)
        

    def updateTopicTable(self, table):
        topicRawSourcePath = SConstants.localFiles.topics #'/home/nawaz/PycharmProjects/sentmentAnaProj/topics'
        
        ## check if topic corpus with Id file exists.
        if not os.path.isfile(topicRawSourcePath):
            raise Exeception('File not found: ', topicRawSourcePath)
            
        topicsSource = pd.read_csv(topicRawSourcePath, sep="\n", header=None, engine='python')
        topicsSource = topicsSource[0]
#         print("topics are:", topicsSource)

        for topic in topicsSource:
            qry = """INSERT INTO `%s` (`topic`) VALUES ('%s')""" % (table, topic)
            self.execute(qry)
                

    def updateNegReasonTable(self, table): 
        ## check if topic corpus with Id file exists.
        nReasonFilePath = SConstants.localFiles.nReasons
        
        if not os.path.isfile(nReasonFilePath):
            raise Exeception('File not found: ', nReasonFilePath)
            
        n_reasons = pd.read_csv(nReasonFilePath, sep="\n", header=None, engine='python')
        n_reasons = n_reasons[0]
        
        for nReason in n_reasons:
            qry = """select `n_reason` from `%s` where `n_reason` = '%s' """ % (table, nReason)
            if len(self.execute(qry)) == 0:  
                qry = """INSERT INTO `%s` (`n_reason`) VALUES ('%s')""" % (table, nReason)
                self.execute(qry)
            else:
                print('N_reason: "%s" is repeated' % nReason)
  

    def updatePosReasonTable(self, table): 
        ## check if topic corpus with Id file exists.
        pReasonFilePath = SConstants.localFiles.pReasons
        
        if not os.path.isfile(pReasonFilePath):
            raise Exeception('File not found: ', pReasonFilePath)
            
        p_reasons = pd.read_csv(pReasonFilePath, sep="\n", header=None, engine='python')
        p_reasons = p_reasons[0]
        
        for pReason in p_reasons:
            qry = """select p_reason from `%s` where p_reason = '%s' """ % (table, pReason)
            if len(self.execute(qry)) == 0:  
                qry = """INSERT INTO `%s` (`p_reason`) VALUES ('%s')""" % (table, pReason)
                self.execute(qry)
            else:
                print('P_reason: "%s" is repeated' % pReason)
                
        
    def updateAllKeywordsTable(self, table): 
        ## check if topic corpus with Id file exists.
        allKeywordsFilePath = SConstants.localFiles.topics
        
        if not os.path.isfile(allKeywordsFilePath):
            raise Exeception('File not found: ', allKeywordsFilePath)
            
        words = pd.read_csv(allKeywordsFilePath, sep="\n", header=None, engine='python')
        words = words[0]
        
        for word in words:
            qry = """select `keyword` from `%s` where `keyword` = '%s' """ % (table, word)
            if len(self.execute(qry)) == 0:  
                qry = """INSERT INTO `%s` (`keyword`) VALUES ('%s')""" % (table, word)
                self.execute(qry)
            else:
                print('word: "%s" is repeated' % word)
  
      
    
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