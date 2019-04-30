# from __future__ import with_statement
# from itertools import cycle
from .trieTree import Trie
from .trieTree import TrieStatus
from config.sConstants import SConstants
from db.dbQueryUtills import DBQueryUtills

class SWordList:
    
    def __init__(self, table, db='DGIndia'):        
        self.trie = Trie()
        self.words = self.getDataFromDB(db, table)
        for word in self.words:
            self.trie.insert(word)
        
        
    def getDataFromDB(self, db, table):
        db = DBQueryUtills(db)
        
        def topicQuery():
            return db.getTopic(table)

        def nReasonQuery():
            return db.getNReasons(table)
        
        def pReasonQuery():
            return db.getPReasons(table)
        
        def allKeywordQuery():
            return db.getAllKeys(table)

        switcher = {
            SConstants.table.topic: topicQuery,
            SConstants.table.nReason: nReasonQuery,
            SConstants.table.allKeyword: allKeywordQuery,
            SConstants .table.pReason: pReasonQuery    
        }

        func = switcher.get(table, "nothing")
        return func()
        
        
#     def searchInSentence(self, sentence):
#         return self.trie.searchBySentence(sentence)
     
        
    def searchByKey(self, key):
        return self.trie.search(key)
        
        
    def searchByTokens(self, tokens):
        wordList = []
        for word in tokens:
            if self.trie.search(word) == TrieStatus.matched:
                wordList.append(word)
        return wordList
     
        
    def searchInDocument(self, document):
        processed_doc = []
        for tokenList in document:
            processed_doc.append(self.searchInTokens(tokenList))
        return processed_doc
        
            
    def removeSpecialChar(self, fromString):
        return ''.join(i for i in fromString if i.isalpha()) 
    
    
#     def __nextValue(wordList, index):
#         nextIndex = index + 1 # next index
#         return wordList[nextIndex] if (nextIndex) < len(wordList) else None

            
    def searchBySentence(self, sentence):
        wordList = list(map(lambda word: self.removeSpecialChar(word), sentence.split(' '))) 
        resultList = []
        length = len(wordList)
        storage = [] # store matched word temproarly, to check next combine word.
#         print('words are: ', wordList)
        
        for currIndex in range(length):
            resultList = resultList + storage
            storage = []
            
            # continue if word is exist in result list, bcs repeation is not allowed.
            if any(wordList[currIndex] in r for r in resultList):
                continue

            for nextIndex in range(currIndex, length):
                if currIndex == nextIndex:
                    jointWords = wordList[currIndex]  #initialy take first word, dont  joint two words.
                    storeage = [jointWords]
                else:
                    jointWords = ' '.join([jointWords, wordList[nextIndex]]) 
                 
                
                result = self.trie.search(jointWords)
#                 print('join words: %s status; %s' % (jointWords, result))
                if result is TrieStatus.matched:
                    storage = [jointWords]
                    continue
                if result in TrieStatus.goNext:
                    continue
                if result in TrieStatus.unmatched:
                    break
                    
        resultList = resultList + storage
        return resultList  
    
    
    