__author__ = 'kasper'

# MEMORY

# TODO Funkcija __add za merge....

import operator

class WordsList:

    def __init__(self, dlp):
        # lista od zboroj
        self.__wordsList = {}
        # vkupen broj na zboroj
        self.__wordsCount = 0
        # vkupno razlicni zboroj
        self.__distinctWords = 0
        # id na dokument od koj so se zemeni zborojte
        self.docPointer = dlp

    def count(self):
        return self.__wordsCount

    def distinctCount(self):
        return self.__distinctWords

    def list(self):
        return self.__wordsList

    def words(self):
        return self.__wordsList.keys()

    def addWord(self, word):
        self.__wordsCount += 1
        if word in self.__wordsList:
            self.__wordsList[word] += 1
        else:
            self.__wordsList[word] = 1
            self.__distinctWords += 1

    def insertList(self, lst):
        for word in lst:
            self.__wordsCount += 1
            if(word not in self.__wordsList):
                self.__wordsList[word] = 1
                self.__distinctWords += 1
            else:
                self.__wordsList[word] += 1


# wl = WordsList(1)
# wl.addWord('hesko')
# wl.addWord('wello')
# wl.addWord('aladin')
# wl.addWord('awadin')
# wl.addWord('ba2baroga')
# wl.addWord('bab2aroga')
# wl.addWord('babar1oga')
# wl.addWord('baba1roga')
# wl.addWord('babaqwroga')
# wl.addWord('babsaaroga')
# wl.addWord('babsaroga')
# wl.addWord('babacroga')
# wl.addWord('babarogzxa')
# wl.addWord('babaroasga')
# wl.addWord('baffsbaroga')
# wl.addWord('babqwaroga')
# wl.addWord('babarrrroga')
# wl.addWord('babarwwwoga')
# wl.addWord('babarwwwoga')
#
# niza = ['mart', 'april', 'maj', 'awadin']
# wl.insertList(niza)
# print wl.list()
# print wl.count()
# print wl.distinctCount()
# wl.addWord('kako')
# print wl.list()
# print wl.count()
#
# d = wl.list()
#
# t1 = time.time()
# print d['90213']
#
# t2 = time.time()
#
# print t2
# print t1
