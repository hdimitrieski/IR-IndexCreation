# coding=utf-8
__author__ = 'kasper'

from CreateIndex import CreateIndex
from Index import Index
from DBManager import DbManager
from QueryManager import QueryManager

indexCreated = 1
cacheIndex = Index()

if not indexCreated:
    el = ['.glavenText', '.vestgoretext h1']
    ci = CreateIndex(1, 'http://arhiva.plusinfo.mk/vest/', 4000, 10, './documents/', el)
    data = ci.create()
    qManager = QueryManager(data['wordsdb'], data['cachedb'])
else:
    db = DbManager()
    cdb = DbManager(collectionName='cachewordscol')
    qManager = QueryManager(db, cdb)

print qManager.execute('(еден AND каде) OR оваа')


