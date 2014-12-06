__author__ = 'kasper'
from Index import Index
import re

class QueryManager:

    def __init__(self, db, cdb):
        self.cacheIndex = Index()
        self.cacheIndex.createFromCursor(cdb.findAll())

    def toArray(self, query):
        result = re.sub('\s+', '', query)
        return result.split('AND')

    def execute(self, query):
        return self.toArray(query)
        result = self.cacheIndex.find(query)


        if result:
            return result
        else:
            return None


