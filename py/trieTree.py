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
                
                
                
                