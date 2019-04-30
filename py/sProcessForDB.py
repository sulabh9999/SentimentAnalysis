import pandas as pd
import numpy as np
import sys
from db.dbQueryMaster import DBQueryMaster
from py.sMasterOperation import *
from config.sConstants import SConstants



# process comments after downloading into pkl file 
class sProcessForDB:
    
    def __init__(self, db):
        self.mysqlDB = DBQueryMaster(db)
        self.inputFilePath = SConstants.pkl.source
        self.outputFilePath = SConstants.pkl.destination
        self.storeProcessedCommIntoTable = SConstants.table.preprocessed
        # for server
        self.source = SConstants.table.preprocessed
        self.destination = SConstants.table.master
        
        between = [SConstants.date.start, SConstants.date.end]
        self.smo = sMasterOperation(self.inputFilePath, between)
    
    
    def performOperationOnComments(self):
        self.smo.createTries()
        self.smo.update_processed_doc()
        self.smo.update_topic()
        self.smo.update_reason()
        self.smo.update_id()
        
##################################### PKL ###################################   
 
    def showDownloadedCommentsPKL(self):
        return pd.read_pickle(self.inputFilePathh)
    
    def storeProcessedCommentsPKL(self):
        df = self.smo.showProcessedComments()
        return df.to_pickle(self.outputFilePath)
    
    def showProcessedCommentsPKL(self):
        return pd.read_pickle(self.outputFilePath)
    
    def showPreprocessedComments(self):
        return self.smo.showProcessedComments()
    
#####################################  Database #############################################    

    def dumpPreprocessedCommentsIntoDB(self): 
        platform = -1  # { Android: 0, iOS:1, web:2, Android+iOS: 3, all: 4 }
        product = -1   # { DGIndia: 0, DGIndonatia: 1, etc...}
        if ('dgIndia' in self.inputFilePath):
            product = 0
        if ('android' in self.inputFilePath):
            platform = 0
        if ('iOS' in self.inputFilePath):
            platform = 1
        self.smo.storeProcessedCommentIntoDB(self.mysqlDB, self.storeProcessedCommIntoTable, platform, product)
        
    def dumpToFinalTable(self):
        self.smo.storeToFinalTable(self.mysqlDB, self.source, self.destination)
        
######################################################################################

    #-----------------------------tesing trie resords --------------------------
    def test_getTopics(self, sentence):
        return self.smo.test_getTopics(sentence)
    
    def test_getPReason(self, sentence):
        return self.smo.test_getPReason(sentence)
    
    def test_getNReason(self, sentence):
        return self.smo.test_getNReason(sentence)
    
    def test_getCommon(self, sentence):
        return self.smo.test_getCommon(sentence)
    
