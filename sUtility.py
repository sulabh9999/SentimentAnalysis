
class SUtility:
    
    def __init__(self):
        self.topicWithCountDict = {}
        self.topicWithReasonsDict = {}
        self.sortedTopicsDict = []
    
    
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
#         self.sortedTopicsDict = self.__getSorted(self.topicWithCountDict)  
     

    
    def getFamousTopics(self):
        return self.__getSorted(self.topicWithCountDict) 
    
    
    def getReasonDict(self):
        result = []
        sortedDict = self.getFamousTopics()
        for each in sortedDict:
            if each[0] in self.topicWithReasonsDict:
                result.append((each[0], self.__getSorted(self.topicWithReasonsDict[each[0]])))
        return result
    
    def showTopicCounts(self):
        print(self.getFamousTopics())
    
    def showReasonDict(self):
        for each in self.getReasonDict():
            print(each[0])
            print(each[1])
            print()
    
    def __getSorted(self, dicti):
        return sorted(dicti.items(), key=lambda x: x[1], reverse=True)
    
    
    def clean():
        self.topicWithCountDict = None
        self.topicWithReasonsDict = None
        
        
        
        
        
        