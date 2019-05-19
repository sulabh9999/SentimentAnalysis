# Python program for insert and search 
# operation in a Trie 

class TrieNode: 
    def __init__(self): 
        self.children = [None]*27
        self.isEndOfWord = False
        
###########################################################################################

class TrieStatus: 
    unmatched = 'unmatched'
    matched = 'matched'
    goNext = 'goNext'

##########################################################################################

class Trie():  
    def __init__(self): 
        self.root = self.getNode() 

    def __removeSpecialChar(self, fromString):
        return ''.join(i for i in fromString if i.isalpha()) 
    
    def getNode(self): 
        return TrieNode() 

    def _charToIndex(self, ch): 
        if ch == ' ':
            return 26 # since ASCII value indicates index, so space is considered as 27th index, but actual value is 32.
        asciiChar = ord(ch)-ord('a')
        if asciiChar >= 0:
            return asciiChar
        return 0


    def insert(self, key): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
        pCrawl.isEndOfWord = True

        
    def search(self, key): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level])
            try:
                if not pCrawl.children[index]: 
                    return TrieStatus.unmatched
                pCrawl = pCrawl.children[index] 
            except IndexError:
                return TrieStatus.unmatched
            
#         print('..key is:', key)
#         if key == 'I':
#             print('..pCrawl.children..', pCrawl.children)
#             print('..pCrawl.children[26]..', pCrawl.children[26])
#             print('..is end of word.', pCrawl.isEndOfWord)
            
        if pCrawl != None: 
            if pCrawl.isEndOfWord:
                return TrieStatus.matched
            elif pCrawl.children[26] is not None:
                return TrieStatus.goNext

        return TrieStatus.unmatched
                
                
      #-------------------------------------------
    def searchBySentence(self, sentence):
        wordList = list(map(lambda word: self.__removeSpecialChar(word), sentence.split(' '))) 
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
                 
                
                result = self.search(jointWords)
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
    
                