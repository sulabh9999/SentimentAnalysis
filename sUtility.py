
class SUtility:
    
    def __init__(self):
        self.topicWithCountDict = {}
        self.topicWithReasonsDict = {}
    
    
    def __del__(self):
        self.topicWithCountDict = None
        self.topicWithReasonsDict = None
        
    
    def __merge(self, tokens, dictionary):
        for token in tokens:
            if token in dictionary:
                dictionary[token] += 1
            else:
                dictionary[token] = 1
                
                
    def __appendDictWithCount(self, tokens):
        self.__merge(tokens, self.topicWithCountDict)
     
    
    def dump(self, topics, reasons):
        self.__appendDictWithCount(topics)
        for topic in topics:
            if topic in self.topicWithReasonsDict:
                self.__merge(reasons, self.topicWithReasonsDict[topic])
            else:
                self.topicWithReasonsDict[topic] = {}
                self.__merge(reasons, self.topicWithReasonsDict[topic])
                
                
    def showTopicCounts(self):
        self.__showDict(self.topicWithCountDict)
    
    
    def showReasonDict(self):
        keys = sorted(self.topicWithCountDict.items(), key=lambda x: x[1], reverse=True)
        for each in keys:
            if each[0] in self.topicWithReasonsDict:
                print('topic: ',  each[0])
                self.__showDict( self.topicWithReasonsDict[each[0]])
                print()
#         for key, valueDict in self.topicWithReasonsDict.items():
#             print('topic: ', key),
#             self.__showDict(valueDict)
    
    
    def __showDict(self, dicti):
#         print(dicti)
#         print(sorted(dicti, key=dicti.get, reverse=True))
        s = sorted(dicti.items(), key=lambda x: x[1], reverse=True)
        print(s)
        
    
    
    def clean():
        self.topicWithCountDict = None
        self.topicWithReasonsDict = None
        
        
        
        
        
        