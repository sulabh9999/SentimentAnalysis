import numpy as np
from py import SDataSource
from py.SWordList import SWordList
from py.sUtility import SUtility
from py.sPreprocessor import SPreprocessor
from config.sConstants import SConstants
from IPython.display import display, clear_output

# operation on downlaoded comments and store into `android_full_comments.pkl`
class sMasterOperation:
    
    def __init__(self, filePath, dateBetween):
        self.df = SDataSource.getListOfCommentsFromPkl(dateBetween) #.head(5)
        print('Total comments between given dates are: ', self.df.shape[0])
        self.sutility = SUtility()
        self.spreprocessor = SPreprocessor()
        
        
    def setFilter(self, row):
        processed_doc = []
        # document preprocessing, cleaning, filtering, replacement, spliting into multiple senetnces from one
        for each in self.spreprocessor.docCleaning(row['comment'], False): #should split by ','
            processed_doc.append(each)
        return processed_doc
        
        
    def createTries(self):
        self.trieCommon  = SWordList(SConstants.table.allKeyword)
        self.trieTopic   = SWordList(SConstants.table.topic)
        self.trieNReason = SWordList(SConstants.table.nReason)
        self.triePReason = SWordList(SConstants.table.pReason)
    
    
#     def getTopics(self, doc):
#         return self.trieTopic.
#         return self.spreprocessor.parseToTokens(self.trieTopic, str(doc))
    
#     def getNReasons(self, doc):
#         return self.spreprocessor.parseToTokens(self.trieNReason, str(doc))

#     def getPReasons(self, doc):
#         return self.spreprocessor.parseToTokens(self.triePReason, str(doc))
    
    def getReasons(self, dfRow):
        doc = str(dfRow['processed_doc'][0])
        if int(dfRow['rating']) < 3:
            return self.trieNReason.searchBySentence(doc)
        else:
            return self.triePReason.searchBySentence(doc)
    
   
    #----------------------------- main operations ----------------------------------------------   
    def update_processed_doc(self):
        self.df['processed_doc'] = self.df.apply(self.setFilter, axis=1)   
              
    def update_topic(self):
        self.df['topic'] = self.df['processed_doc'].apply(lambda doc: self.trieTopic.searchBySentence(doc[0]))
        # replace empty value of cell to default 'app'
        self.df['topic'] = self.df['topic'].apply(lambda cell: cell if cell else ['app'])
                  
    def update_reason(self):
        self.df['reason'] = self.df.apply(self.getReasons, axis=1)

    def update_id(self):
        self.df['id'] = range(0, 0 + len(self.df))
      
    
    #-----------------------------tesing trie resords --------------------------
    def test_getTopics(self, sentence):
        return self.trieTopic.searchBySentence(sentence)
    
    def test_getPReason(self, sentence):
        return self.triePReason.searchBySentence(sentence)
    
    def test_getNReason(self, sentence):
        return self.trieNReason.searchBySentence(sentence)
    
    def test_getCommon(self, sentence):
        return self.trieCommon.searchBySentence(sentence)
    
#-------------------------------------------------------------------------------------------    
    
    def showProcessedComments(self):
        return self.df[::-1]
    
#     def storeProcessedCommentIntoDB(self, mysqlDB, tableName, input_df,):
#         length = 20 #len(input_df)
#         for i in range(lenght): 
#             data = self.df.iloc[i]
#             comment_id = data['id']
#             processed_doc = data['processed_doc']
#             commentDate = data['formatedDate']
#             rating = data['rating']
#             mysqlDB.storePreprocessedComments(tableName, comment_id, processed_doc, commentDate, rating, platform, product)
       
    def merge(self, arr):
        return ', '.join(filter(None.__ne__, arr)) if (arr is not None) else ''
    
    
    def storeProcessedCommentIntoDB(self, mysqlDB, table, product, platform):
        count = 0
        totalRows = self.df.shape[0]
        for i in range(totalRows-1, -1, -1): 
            data = self.df.iloc[i]
            comment_id = data['id']
            processed_doc = self.merge(data['processed_doc'])
            topics = self.merge(data['topic'] if data['topic'] else ['app'])
            reasons = self.merge(data['reason'])
            date = data['formatedDate']
            rating = data['rating']
            mysqlDB.storeprocessedComments(table, comment_id, processed_doc, topics, reasons, date, rating, platform, product)

            count = count + 1
#             clear_output(wait=True)
            print('%d...%d..%d.\r' % (int(count/totalRows*100), count, totalRows), end='')
#             display('progressing: %d/%d...%d\%' % (count, totalRows, int(count/totalRows*100)))
            
    def storeToFinalTable(self, db, sourceTable, destinationTable):
        db.generateTableForServer(sourceTable, destinationTable)
        
        
        
        
        
        
        
        