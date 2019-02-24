#!/usr/bin/env python
# coding: utf-8
# https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

# import file to other directory
# from topicModeling import getTopics
# print(getTopics(text))

# input: text = "Team, each time I use the app..."
# output: {'Team', 'each time', 'app'}

from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

en_stop = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

def getTopics(text):    
    # compile sample documents into a list
    doc_set = re.split('; |\.|\*|\n', text)
    
    # list for tokenized documents in loop
    texts = []

    # loop through document list
    for i in doc_set:

        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)

        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]

        # stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

        # add tokens to list
        texts.append(stemmed_tokens)

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=20)
    # print(ldamodel.print_topics(num_topics=3, num_words=4))
    topicList = ldamodel.show_topics(num_topics=10, num_words=3, formatted=False)

    topicsArray = [[x[0] for x in eachList[1]] for eachList in topicList]
    topics = set(sum(topicsArray, []))
    return topics