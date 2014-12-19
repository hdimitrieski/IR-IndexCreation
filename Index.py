__author__ = 'kasper'

# Index
# TODO

from DocumentsList import DocumentList
import math

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

        val = 0
        for key in wordsList.list():
            tf = round(1 + math.log10(wordsList.getWord(key)), 2)
            wordsList.tf(key, tf)
            val += tf * tf

        length = round(math.sqrt(val), 2)

        for key in wordsList.list():
            if key in self.__index:
                self.__index[key].addDocument(dId, round(wordsList.getWord(key)/length, 2))
            else:
                dl = DocumentList(key)
                dl.addDocument(dId, round(wordsList.getWord(key)/length, 2))
                self.__index[key] = dl
                self.__distinctWords += 1

    def createFromCursor(self, cursor):
        for data in cursor:
            self.__index[data] = cursor[data]
        return 1

    def find(self, word):
        word = word.decode('utf-8')
        if word in self.__index:
            result = []
            try:
                result = self.__index[word].docList()
            except AttributeError, e:
                result = self.__index[word]
            return result
        else:
            return None

# from WordsList import WordsList
# w = WordsList(1)
# lst = ['kasper', 'jabolko', 'krusa']
# w.insertList(lst)
# w.tf('kasper', 115)
# w.tf('jabolko', 10)
# w.tf('krusa', 2)
# print w.list()
# i = Index()
# i.mergeWL(w, 1)
# for key in i.index():
#     print i.index()[key].docList()