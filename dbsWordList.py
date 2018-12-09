from __future__ import with_statement
from trieTree import Trie


class DBSWordList:
    
    def __init__(self, wordFilePath):
        print('..DBSWordList constructor called')
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
        
#     def show():
#         print('...this is tries..')
        
    def searchInSentence(self, sentence):
        wordList = []
        tokens = sentence.split(' ')
        for word in tokens:
            if self.trie.search(word):
                wordList.append(word)
        return wordList
        
    def searchInTokens(self, tokens):
        wordList = []
        for word in tokens:
            if self.trie.search(word):
                wordList.append(word)
        return wordList
     
    def searchInDocument(self, document):
        processed_doc = []
        for tokenList in document:
            processed_doc.append(self.searchInTokens(tokenList))
        return processed_doc
        
        