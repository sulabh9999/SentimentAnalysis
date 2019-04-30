import pandas as pd
from config.sConstants import SConstants
from datetime import datetime


def getDataSourcePathFor(keyForFilePath):
    import json
    import os
    
    config_file_path = '/home/nawaz/.virtualenvs/AWSComp/config.json' #os.environ[SConstants.virtual_env] + '/config.json'
    with open(config_file_path) as f:
        config = json.load(f)
        if keyForFilePath in config:# ['comments_path', 'output_path']
            return config[keyForFilePath] 
    return None


# return dataframe between given dates
def getComments(file_Path, start_date=None, end_date=None):
    df = pd.read_csv(file_Path, sep='\t', usecols=['comments', 'ratings', 'dates']) 
    if (start_date and end_date) is not None:
        df['formatedDate']=pd.to_datetime(df['dates'])
        df.sort_values(by=['formatedDate'], ascending=True, inplace=True)
        dateField = df['formatedDate']
        start = datetime.strptime(start_date, '%d-%m-%Y') 
        end = datetime.strptime(end_date, '%d-%m-%Y')
        df = df.loc[(dateField>=start) & (dateField<=end)]
    return df


# return dataframe between given dates
def getEmojis(file_Path):
    df = pd.read_csv(file_Path, usecols=['Emoji', 'Final_Result']) #, 
    return  df #pd.read_csv(file_Path) 


from gensim.corpora import Dictionary
def toDict(document):
    dictionary = Dictionary(document)
    corpus = [dictionary.doc2bow(sent) for sent in document]
    vocab = list(dictionary.values()) #list of terms in the dictionary
    vocab_tf = [dict(i) for i in corpus]
    vocab_tf = list(pd.DataFrame(vocab_tf).sum(axis=0)) #list of term frequencies
    doct = dict(zip(vocab, vocab_tf))
    sortedDict = sorted(doct.items() , reverse=True, key=lambda x: x[1])
    return sortedDict

def get_Positive(kv):
    v = kv[1]
    return (v[1]-v[0])

def get_Negitive(kv):
    v = kv[1]
    return (v[0]-v[1]) 


def sortedMostNeg(dictionay):
    from operator import itemgetter
    return sorted(dictionay.items(), key=get_Negitive, reverse=True)

def sortedMostPos(dictionay):
    from operator import itemgetter
    return sorted(dictionay.items(), key=get_Positive, reverse=True)

def sortedMostFreq(dictionay):
    from operator import itemgetter
    return sorted(dictionay.items(), key=lambda kv: kv[1][2], reverse=True)

def getListOfComments(betweenDates): # ['start_date', 'end_date']
    ### This is to get csv rows between given dates
    comments_file_path = getDataSourcePathFor(SConstants.comments_path)
    commentsList = []
    if betweenDates is None:
        commentsList = getComments(comments_file_path, None, None) #['comments'] 
    elif len(betweenDates) == 2:
        commentsList = getComments(comments_file_path, betweenDates[0], betweenDates[1]) #['comments']
        print('Total number of comments: %s between %s and %s' % (len(commentsList), betweenDates[0], betweenDates[1]))
        
    #commentsList = commentsList.query("ratings > 0 and ratings < 3")#['comments'] 
    commentsList = commentsList.sort_values(by='ratings', ascending=True)
    return commentsList.query("ratings > 0 and ratings < 3")['comments'] 


def getListOfCommentsFromPkl(betweenDates, ascending=False, fromFile=SConstants.pkl.source): # ['start_date', 'end_date']
    print('Input comments from file: [%s]' % fromFile)
    print('Between dates: ', betweenDates)
    ### This is to get csv rows between given date.pkls
    comments_file_path = fromFile
    df = pd.read_pickle(comments_file_path)
    print('file shape: ', df.shape)
    commentsList = []
    if len(betweenDates) == 2:
        start_date = betweenDates[0]
        end_date = betweenDates[1]
        df['formatedDate']=pd.to_datetime(df['date'])
        df.sort_values(by=['formatedDate'], ascending=True, inplace=True)
        dateField = df['formatedDate']
        start = datetime.strptime(start_date, '%d-%m-%Y') 
        end = datetime.strptime(end_date, '%d-%m-%Y')
        df = df.loc[(dateField>=start) & (dateField<=end)]
    else:
        df['formatedDate']=pd.to_datetime(df['date'])
        df.sort_values(by=['formatedDate'], ascending=ascending, inplace=True)
#     df = df.loc[(dateField>=start) & (dateField<=end)]
#     df = df.loc[(df['rating'].astype(int) >= 0) & (df['rating'].astype(int) <= 2)] 
#     commentsList = df.sort_values(by='rating', ascending=True)
#     result = commentsList.query("rating > 0 and rating < 3")['comments'] 
#     print(df)
    return df

