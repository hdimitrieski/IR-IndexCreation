__author__ = 'kasper'

import sys
import pymongo
import re

class DbManager:

    def __init__(self, host='localhost', username='', password='', dbname='words', collectionName='wordscol', port=27017):
        self.host = host
        self.username = username
        self.password = password
        self.dbName = dbname
        self.collectionName = collectionName
        self.port = port

        client = pymongo.MongoClient(host, port)
        self.db = client[dbname]
        self.collection = self.db[collectionName]

    def setCollection(self, colName):
        self.collectionName = colName
        self.collection = self.db[colName]

    def insert(self, data):
        try:
            self.collection.insert(data)
        except pymongo.errors.DuplicateKeyError, e:
            print e.message
            return 0
        except pymongo.errors.OperationFailure, e:
            print 'Poraka'
            print e.message
            return 0
        return 1

    def find(self, word):
        data = self.collection.find({'_id': word})
        if data.count() > 0:
            lst = eval(data[0]['list'])
            # lst = lst[1:len(lst) - 1]
            # lst = re.sub('\s+', '', lst)
            # lst = lst.split(',')
            # for j in range(len(lst)):
            #     lst[j] = int(lst[j])
            return lst
        else:
            return None

    def findAll(self):
        data = self.collection.find()
        lstItems = {}
        for i in range(data.count()):
            lst = eval(data[i]['list'])
            # lst = data[i]['list']
            # lst = lst[1:len(lst) - 1]
            # lst = re.sub('\s+', '', lst)
            # lst = lst.split(',')
            # for j in range(len(lst)):
            #     lst[j] = int(lst[j])
            lstItems[data[i]['_id']] = lst
        return lstItems
