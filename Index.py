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
        self.__wordsCount += wordsList.count()
        for key in wordsList.list():
            if key in self.__index:
                self.__index[key].addDocument(dId)
            else:
                dl = DocumentList(key)
                dl.addDocument(dId)
                self.__index[key] = dl
                self.__distinctWords += 1

    def createFromCursor(self, cursor):
        for data in cursor:
            self.__index[data['_id']] = data['list']
        return 1

    def find(self, word):
        return self.__index[word.decode('utf-8')]