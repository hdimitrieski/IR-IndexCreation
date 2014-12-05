# coding=utf-8
__author__ = 'kasper'

from CreateIndex import CreateIndex
from Index import Index
from DBManager import DbManager

indexCreated = 1
cacheIndex = Index()

if not indexCreated:
    el = ['.glavenText', '.vestgoretext h1']
    ci = CreateIndex(1, 'http://arhiva.plusinfo.mk/vest/', 4000, 10, './documents/', el)
    data = ci.create()
    db = data['wordsdb']
    cdb = data['cachedb']
    cacheIndex.createFromCursor(cdb.findAll())
else:
    db = DbManager()
    cdb = DbManager(collectionName='cachewordscol')
    cacheIndex.createFromCursor(cdb.findAll())



print cacheIndex.find('вмро')

data = db.find('очекува')
if data:
    print data[0]['_id']
else:
    print 'Nema podatoci'