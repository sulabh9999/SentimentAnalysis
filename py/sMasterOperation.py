from py import SDataSource
from py import SConstants
from py.SWordList import SWordList
from py.sUtility import SUtility
from py.sPreprocessor import SPreprocessor

# operation on downlaoded comments and store into `android_full_comments.pkl`
class sMasterOperation:
    
    def __init__():
        self.df = pd.DataFrame()
        self.sutility = SUtility()
        self.spreprocessor = SPreprocessor()
        
    
    def setFilter(row):
        processed_doc = []
        # document preprocessing, cleaning, filtering, replacement, spliting into multiple senetnces from one
        for each in spreprocessor.docCleaning(row['comment'], False): #should split by ','
            processed_doc.append(each)
        return processed_doc
        
    def createTries():
        wordList_file = SDataSource.getDataSourcePathFor(SConstants.wordFile_path)
        trieCommon = SWordList(wordList_file)

        topic_file = SDataSource.getDataSourcePathFor(SConstants.topic_path)
        trieTopic = SWordList(topic_file)

        n_reason_file = SDataSource.getDataSourcePathFor(SConstants.p_reason_path)
        trieNReason = SWordList(n_reason_file)
        
    def getTopics(doc):
        return spreprocessor.parseToTokens(trieTopic, str(doc)
                                           
    def getReasons(doc):
        return spreprocessor.parseToTokens(trieNReason, str(doc))
                                                               
    def update_processed_doc(self, dateBetween):
        df = SDataSource.getListOfCommentsFromPkl(dateBetween)
        commentsDocument = df['comment']
        print('filtered comments: ', len(commentsDocument))
        df['processed_doc'] = df.apply(setFilter, axis=1)
        print(df.head(2)
            
    def update_topic(self):
        df['topic'] = df['processed_doc'].apply(getTopics)
              
    def update_reason(self):
        df['reason'] = df['processed_doc'].apply(getReasons)