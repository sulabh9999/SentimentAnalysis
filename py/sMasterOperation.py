from py import SDataSource
from py import SConstants
from py.SWordList import SWordList
from py.sUtility import SUtility
from py.sPreprocessor import SPreprocessor

# operation on downlaoded comments and store into `android_full_comments.pkl`
class sMasterOperation:
    
    def __init__(self, filePath):
        self.df = SDataSource.getListOfCommentsFromPkl([]) #.head(5)
        self.sutility = SUtility()
        self.spreprocessor = SPreprocessor()
        
    
    def setFilter(self, row):
        processed_doc = []
        # document preprocessing, cleaning, filtering, replacement, spliting into multiple senetnces from one
        for each in self.spreprocessor.docCleaning(row['comment'], False): #should split by ','
            processed_doc.append(each)
        return processed_doc
        
    def createTries(self):
        wordList_file = SDataSource.getDataSourcePathFor(SConstants.wordFile_path)
        self.trieCommon = SWordList(wordList_file)

        topic_file = SDataSource.getDataSourcePathFor(SConstants.topic_path)
        self.trieTopic = SWordList(topic_file)

        n_reason_file = SDataSource.getDataSourcePathFor(SConstants.p_reason_path)
        self.trieNReason = SWordList(n_reason_file)
    
    def getTopics(self, doc):
        return self.spreprocessor.parseToTokens(self.trieTopic, str(doc))
                                            
    def getReasons(self, doc):
        return self.spreprocessor.parseToTokens(self.trieNReason, str(doc))
    
    #----------------------------- main operations -----------------------------------------------------
    def update_processed_doc(self):
        self.df['processed_doc'] = self.df.apply(self.setFilter, axis=1)    
              
    def update_topic(self):
        self.df['topic'] = self.df['processed_doc'].apply(self.getTopics)
                  
    def update_reason(self):
        self.df['reason'] = self.df['processed_doc'].apply(self.getReasons)
    #-------------------------------------------------------------------------------------------
    
    def storeDataAfterOperationOnComments(self, filePath):
        self.df.to_pickle(filePath)
            
        
    def storeIntoPickle(self, mysqlDB):
        numberOfRows = self.df.shape[0]
        for i in range(numberOfRows-1, -1, -1): 
            data = self.df.iloc[i]
            comment_id = data['id']
            process_doc = data['processed_doc']
            topics = data['topic']
            reasons = data['reason']
            date = data['formatedDate']
            rating = data['rating']
            platform = 0 # { Android: 0, iOS:1, web:2, Android+iOS: 3, all: 4 }
            product = 0 # { DGIndia: 0, DGIndonatia: 1, etc...}
            mysqlDB.storeOperation(comment_id, process_doc, topics, reasons, date, rating, platform, product)
    
    
    