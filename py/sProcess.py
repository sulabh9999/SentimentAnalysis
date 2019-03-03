import pandas as pd
import numpy as np
import sys
from dbConfig import *


# process comments after downloading into pkl file 
class sProcessForDB:
    
    def __init__(self):
        self.mydb = dbSQL()

    def showDownloadedComments():
        b = pd.read_pickle('android_commens_till_27_02_19.pkl')
        print(b)
        
    def fetchNegativeCorpus():
        path = '/home/nawaz/PycharmProjects/sentmentAnaProj/N_reasons'
        fName = 'negative_words.pkl'
        data= pd.read_csv(path, sep="\n", header=None, engine='python')
        myDict = {}
        for each in data[0]:
            myDict[each] = 0

        count = 0
        myDictList = []
        for (k,v) in myDict.items():
            myDictList.append((k, count))
            count = count + 1

        df = pd.DataFrame(myDictList)
        df.to_pickle(fName)
        a = pd.read_pickle(fName)
        print(a)
    
    def updateNegativeCorpus():
        fName = 'negative_words.pkl'
        a = pd.read_pickle(fName)
        self.mydb.store_n_reasons(list(a[0]))
        
        
    def dumpNewComments(commentsList):
        pass