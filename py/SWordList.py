# from __future__ import with_statement
from .trieTree import Trie
from .trieTree import TrieStatus


class SWordList():
    
    def __init__(self, wordFilePath):
        if wordFilePath is None:
            print('file not found: ', wordFilePath)
            return
        print('..SWordList constructor called ')
        self.trie = Trie()
        self.words = []
        try:
            with open(wordFilePath) as f:
                self.words = f.read().split('\n')
        except EnvironmentError: 
            print('..file: %s not present' %(wordFilePath))
            return
        
        for word in self.words:
            self.trie.insert(word)
        
        
    def searchInSentence(self, sentence):
        return self.trie.searchBySentence(sentence)
     
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
            

    def searchBySentence(self, sentence):
        wordList = list(map(lambda word: self.removeSpecialChar(word), sentence.split(' '))) 
        outputWordList = []
        length = len(wordList)
        for i in range(length):
            currStr = wordList[i]
            result = self.trie.search(currStr)
            if result is TrieStatus.matched:
                outputWordList.append(currStr)
                
            if result in TrieStatus.goNext:
                for j in range(i+1, length):
                    currStr = currStr+' '+wordList[j]
                    result = self.trie.search(currStr)
                    if result == TrieStatus.matched:
                        outputWordList.append(currStr)
                    elif result == TrieStatus.unmatched:
                        break
        return outputWordList  
    
    
    