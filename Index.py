__author__ = 'kasper'

# Index
# TODO

from DocumentsList import DocumentList

class Index:

    def __init__(self):
        self.__index = {}
        self.__wordsCount = 0
        self.__distinctWords = 0

    def index(self):
        return self.__index
    
    def count(self):
        return self.__wordsCount

    def distinctCount(self):
        return self.__distinctWords

    def sameCount(self):
        return self.__wordsCount - self.__distinctWords

    def mergeWL(self, wordsList, dId):

        for key in wordsList:
            if key in self.__index:
                self.__index[key].addDocument(dId)
            else:
                dl = DocumentList(key)
                dl.addDocument(dId)
                self.__index[key] = dl
