import nltk
from py.getSentiment import getSentiment
import py.SDataSource
import py.SConstants
from py.SWordList import SWordList
from py.sUtility import SUtility
from py.sPreprocessor import SPreprocessor



def main(dateBetween):
    sutility = SUtility()
    spreprocessor = SPreprocessor()

    commentsDocument = SDataSource.getListOfComments(dateBetween)#.head(1000)
    print('filtered comments: ', len(commentsDocument))
    # document preprocessing, cleaning, filtering, replacement, spliting into multiple senetnces from one
    processed_doc = []
    for sentence in commentsDocument:
        for each in spreprocessor.docCleaning(sentence, False): #should split by ','
            processed_doc.append(each)
    
    
    
if '__name__' == '__main__':
    start_date = '01-11-2018' #  09-Sep-2018 
    end_date = '30-12-2018' # 01-Oct-201
    main([start_date, end_date])

