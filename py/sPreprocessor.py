# import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim import parsing

from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.corpus import wordnet as wn
from nltk import pos_tag, word_tokenize
from nltk.stem import *

from textblob import TextBlob
from . import SNouns
from . import toReplace
import re 

# global object for trie WordList
# _trie = None

class SPreprocessor:
    
    def __init__(self):
        self.stemmer = SnowballStemmer('english')
    ''' Need to resolve first '''
#     def resolveDependancy(trie):
#         global _trie
#         _trie = trie
#         print('..dependancy done %s and address %s' % (type(_trie), id(_trie)))

    ''' 1. Tokenization:Split the text into sentences and the sentences into words. Lowercase the words and remove  punctuation.'''
    def tokenize(self, text):
        return simple_preprocess(text)


    ''' 2. Remove small words: Words that have fewer than 3 characters are removed.'''
    def isShortWord(self, token):
        return len(token) < 3


    ''' 3. Remove stopwords: All stopwords are removed.'''
    def isStopWord(self, token):
        return token in STOPWORDS


    ''' 4. lemmatized + Stemming:
    Words are lemmatized — words in third person are changed to first person and verbs in past and future tenses are changed 
    into present.Words are stemmed — words are reduced to their root form.'''
    def lemmatize_stemming(self, token):
        return self.stemmer.stem(token)
#         stemmer = PorterStemmer() #gensim.parsing.stem_text(tokenize) #
#         for word, tag in pos_tag(word_tokenize(token)):
#             wntag = tag[0].lower()
#             wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
#             lemma = WordNetLemmatizer().lemmatize(word, wntag) if wntag else word
#             return TextBlob(lemma).words[0].singularize()
#         return ''


    def filterWord(self, token):
        if not (self.isStopWord(token) or self.isShortWord(token)):
            lemmaWord = self.lemmatize_stemming(token)
            if not self.isShortWord(lemmaWord):
                return ("".join(re.findall("[a-zA-Z]+", lemmaWord)).lower())
        return None 


#     def filters(sentence):
#         result = []
#         #nouns = getNounList(sentence) # fetch only Nouns
#         for token in tokenize(sentence):#nouns: ###tokenize(text):
#             result.append(filterWord(token))
#         return result


    def filterWords(self, tokens):
        result = []
        for each in tokens:
            if len(each.split(' ')) > 1:
                result.append(each)
            else:
                result.append(self.filterWord(each))
        return result

    
    def splitIntoSentences(self, fullcomment):
        sentence = re.sub('[,.]', '@#@#@', fullcomment) # logging.contacted -> logging contacted
#         sentence = sentence
        splited = sentence.split('@#@#@')
        return list(filter(None, splited))
    
    
    def docCleaning(self, fullComment, splitIntoMultSentences = False):
        # tolower case
        fullComment = fullComment.lower()
        multipleSentncs = [fullComment]
        if splitIntoMultSentences:
            # break comment into multiple sentences
            multipleSentncs = self.splitIntoSentences(fullComment)
            
        result = []
        for sentence in multipleSentncs:
            # remove special chars
            temp = re.sub(r'[^a-zA-Z ]+', '', sentence)
            # replace words with compatable words
            temp = toReplace.replaceWords(temp)
            result.append(temp)
        return result

#     def preprocessCommentDocument(document):
#         return document.map()#list(map(lambda sentence: filters(sentence), document))
    

    def parseToTokens(self, trie, sentence):
        # trie implementation
        trieTopicFilteredTokens = trie.searchBySentence(sentence)
        # removeing None from token array
        trieTopicFilteredTokens = list(filter(None, trieTopicFilteredTokens)) # remove empty from string list
        # filter words by lemma, stemming
#         print('bafore filter words:', trieTopicFilteredTokens)
        filterByRulsTokens = self.filterWords(trieTopicFilteredTokens)
#         print('after filter words', filterByRulsTokens)
#         print()
        result = []
        [x for x in filterByRulsTokens if x not in result and (result.append(x) or True)]  #getNounList('', trieFilterWords)
        return result


