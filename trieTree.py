# Python program for insert and search 
# operation in a Trie 

class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
        
###########################################################################################

# class TrieStatus(enum.Enum): 
#     unmatched = 0
#     metched = 1
#     goNext = 2

##########################################################################################

class Trie:  
    def __init__(self): 
        self.root = self.getNode() 

    def getNode(self): 
        return TrieNode() 

    def _charToIndex(self,ch): 
        asciiChar = ord(ch)-ord('a')
        if asciiChar >= 0:
            return asciiChar
        return  0


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
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 
        
        return pCrawl != None and pCrawl.isEndOfWord
        # TODO: need to set Enum
#             return TrieStatus.matched
#         elif pCrawl != None and pCrawl.isEndOfWord::
            

# # driver function 
# def main(): 

# 	# Input keys (use only 'a' through 'z' and lower case) 
# 	keys = ["the","a","there","anaswe","any", 
# 			"by","their"] 
# 	output = ["Not present in trie", "Present in tire"] 

# 	# Trie object 
# 	t = Trie() 

# 	# Construct trie 
# 	for key in keys: 
# 		t.insert(key) 

# 	# Search for different keys 
# 	print("{} ---- {}".format("the",output[t.search("the")])) 
# 	print("{} ---- {}".format("these",output[t.search("these")])) 
# 	print("{} ---- {}".format("their",output[t.search("their")])) 
# 	print("{} ---- {}".format("thaw",output[t.search("thaw")])) 

# if __name__ == '__main__': 
# 	main() 
