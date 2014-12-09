__author__ = 'kasper'

import sys
import pymongo

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
            # print e.message
            return 0
        return 1

    def find(self, word):
        data = self.collection.find({'_id': word})
        if data.count() > 0:
            return data[0]['list']
        else:
            return None

    def findAll(self):
        data = self.collection.find()
        return data
