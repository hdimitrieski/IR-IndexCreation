# coding=utf-8
__author__ = 'kasper'

from Index import Index
from WordsList import WordsList
import math
from operator import itemgetter

class QueryManagerITC:

    def __init__(self, db, cdb):
        # self.cacheIndex = Index()
        # self.cacheIndex.createFromCursor(cdb.index())
        # print self.cacheIndex.find('берзански')
        self.cacheIndex = Index()
        self.cacheIndex.createFromCursor(cdb.findAll())
        self.db = db
        self.numDocs = 127000

    def toArray(self, query):
        return query.split(' ')

    def getArray(self, word):

        arr = self.cacheIndex.find(word)
        if not arr:
            arr = self.db.find(word)
        if not arr:
            arr = []
        return arr

    def intersect(self, lstA, lstB):
        result = []

        if not lstA and not lstB:
            return []

        if not lstA:
            return lstB
        if not lstB:
            return lstA

        i = 0
        j = 0
        lstA.append(None)
        lstB.append(None)
        while lstA[i] is not None and lstB[j] is not None:
            if lstA[i] == lstB[j]:
                result.append(lstA[i])
                j += 1
                i += 1
            elif lstA[i] < lstB[j]:
                i += 1
            elif lstA[i] > lstB[j]:
                j += 1
            elif lstB is None:
                result.append(lstA[i])
                i += 1
            elif lstA is None:
                result.append(lstB[j])
                j += 1

        return result

    def execute(self, query):
        qArr = self.toArray(query)
        colRes = {}
        result = []
        wt = {}
        val = 0

        for word in qArr:
            colRes[word] = self.getArray(word)

        qw = WordsList(1)
        qw.insertList(qArr)

        for key in qw.list():
            tf = round(1 + math.log10(qw.getWord(key)), 2)
            idf = round(math.log10(self.numDocs/len(colRes[key])), 2)
            wt[key] = tf*idf
            val += tf*idf*tf*idf

        val = math.sqrt(val)

        for key in qw.list():
            wt[key] = wt[key]/val

        arrIntersect = []
        for i in range(len(qArr)):
            tmpArr = []
            for j in range(len(colRes[qArr[i]])):
                tmpArr.append(colRes[qArr[i]][j][0])

            arrIntersect = self.intersect(tmpArr, arrIntersect)

        arrIntersect.append(None)

        dictIntersect = {}
        for word in qArr:
            niza = colRes[word]
            dictIntersect[word] = []
            i = 0
            j = 0
            while arrIntersect[j] is not None:
                if niza[i][0] == arrIntersect[j]:
                    dictIntersect[word].append(niza[i])
                    i += 1
                    j += 1
                elif niza[i][0] > arrIntersect[j]:
                    j += 1
                elif niza[i][0] < arrIntersect[j]:
                    i += 1

        for i in range(len(arrIntersect) - 1):
            value = 0
            for key in dictIntersect.keys():
                value += dictIntersect[key][i][1] * wt[key]
            result.append((arrIntersect[i], round(value, 2)))



        return sorted(result, key=itemgetter(1), reverse=True)
