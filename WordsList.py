__author__ = 'kasper'

# Lista od zboroj

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

    def getWord(self, word):
        return self.__wordsList[word]

    def tf(self, word, value):
        self.__wordsList[word] = value

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
            if word not in self.__wordsList:
                self.__wordsList[word] = 1
                self.__distinctWords += 1
            else:
                self.__wordsList[word] += 1
