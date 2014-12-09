# coding=utf-8
__author__ = 'kasper'
from Index import Index
import Tree
import re

class QueryManager:

    def __init__(self, db, cdb):
        self.cacheIndex = Index()
        self.cacheIndex.createFromCursor(cdb.findAll())
        self.db = db

    def toArray(self, query):
        strArr = []
        tmpStr = ''
        j = 0
        level = 0
        for i in range(len(query)):
            if query[i] == '(' and i < len(query):
                if tmpStr != '':
                    strArr.append(tmpStr)
                    tmpStr = ''
                strArr.append('(')
            elif query[i] == ')' and i < len(query):
                if tmpStr != '':
                    strArr.append(tmpStr)
                    tmpStr = ''
                strArr.append(')')
            elif query[i] == ' ':
                if tmpStr != '':
                    strArr.append(tmpStr)
                    tmpStr = ''
            else:
                tmpStr += query[i]
        if tmpStr != '':
            strArr.append(tmpStr)
        return strArr


    def andQ(self, A, B):
        # A ke e zbor ili lista
        # Ako ne e lista ke zejme lista od kes ili baza
        lstA = A
        lstB = B

        if not A or not B:
            raise Exception('Грешка.' )
            return None

        if not isinstance(A, list):
            lstA = self.cacheIndex.find(A)
            if not lstA:
                lstA = self.db.find(A)
            if not lstA:
                raise Exception('Зборот "' + A + '" не постои.' )
                return None

        if not isinstance(B, list):
            lstB = self.cacheIndex.find(B)
            if not lstB:
                lstB = self.db.find(A)
            if not lstB:
                raise Exception('Зборот "' + B + '" не постои.' )
                return None

        result = []
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

        return result

    def orQ(self, A, B):
        lstA = A
        lstB = B
        if not isinstance(A, list):
            lstA = self.cacheIndex.find(A)
            if not lstA:
                lstA = self.db.find(A)
            if not lstA:
                raise Exception('Зборот "' + A + '" не постои.')
                return None

        if not isinstance(B, list):
            lstB = self.cacheIndex.find(B)
            if not lstB:
                lstB = self.db.find(A)
            if not lstB:
                raise Exception('Зборот "' + B + '" не постои.')
                return None

        return list(set(lstA + lstB))

    def buildTree(self, query):
        tree = Tree.buildOrTree(query)
        return tree

    def execute(self, query):
        qArr = self.toArray(query)
        if len(qArr) == 1:
            lst = self.cacheIndex.find(qArr[0])
            if not lst:
                lst = self.db.find(qArr[0])
            return lst
        qTree = self.buildTree(qArr)
        result = self.executeQuery(qTree)
        return result

    def executeQuery(self, tree):
        lnode = tree.left
        rnode = tree.right

        if lnode and rnode:
            if tree.value == 'OR':
                try:
                    a = self.executeQuery(lnode)
                    b = self.executeQuery(rnode)
                    return self.orQ(a, b)
                except Exception, e:
                    print e.message
                    return None
            elif tree.value == 'AND':
                try:
                    a = self.executeQuery(lnode)
                    b = self.executeQuery(rnode)
                    return self.andQ(a, b)
                except Exception, e:
                    print e.message
                    return None
        else:
            return tree.value