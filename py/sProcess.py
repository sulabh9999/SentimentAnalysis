import pandas as pd
import numpy as np
import sys
from dbConfig import *
from py.sMasterOperation import *


# process comments after downloading into pkl file 
class sProcessForDB:
    
    def __init__(self):
        self.mysqlDB = dbSQL()
        self.inputFilePath = 'android_commens_till_27_02_19.pkl'
        self.outputFilePath = 'android_commens_till_27_02_19_output.pkl'
        self.smo = sMasterOperation(self.inputFilePath)

    def showDownloadedComments():
        b = pd.read_pickle('android_commens_till_27_02_19.pkl')
        print(b)
        
    def fetchNegativeCorpus():
        path = '/home/nawaz/PycharmProjects/sentmentAnaProj/N_reasons'
        data= pd.read_csv(path, sep="\n", header=None, engine='python')
        myDict = {}
        for each in data[0]:
            myDict[each] = 0
        count = 0
        myDictList = []                       # [(token)] 
        for (k,v) in myDict.items(): #'android_commens_till_27_02_19_output.pkl'
            myDictList.append((k, count))
            count = count + 1
        return myDictList

    
    def updateNegativeCorpus(self):
        fName = 'negative_words.pkl'
        a = pd.read_pickle(fName)
        self.mydb.store_n_reasons(list(a[0]))
     
    
    def performOperationOnComments(self):
        self.smo.createTries()
        self.smo.update_processed_doc()
        self.smo.update_topic()
        self.smo.update_reason()
        
    def storeDataAfterOperationOnComment(self):
        self.smo.storeDataAfterOperationOnComments(self.outputFilePath)
        
    
    def dumpNewCommentsIntoDB(self): # [()]
        self.smo.storeIntoPickle(self.mysqlDB)
        
    def showProcessedOutput(self):
        print(pd.read_pickle(self.outputFilePath).head(5))
        
    def getRealCommentForId(self, comment_id):
        self.inputFilePath = 'android_commens_till_27_02_19.pkl'
        df = pd.read_pickle(self.inputFilePath)
        index = df[df['id']==comment_id].index
        print(df['comment'][index].values[0])