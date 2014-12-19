# coding=utf-8
__author__ = 'kasper'

from CreateIndex import CreateIndex
from Index import Index
from DBManager import DbManager
from QueryManager import QueryManager
import time
from QueryManagerITC import QueryManagerITC

indexCreated = 1
cacheIndex = Index()

if not indexCreated:
    el = ['.glavenText', '.vestgoretext h1']
    ci = CreateIndex(1, 'http://arhiva.plusinfo.mk/vest/', 800, 128000, '../../Desktop/documents/', el)
    t1 = time.time()
    data = ci.create()
    t2 = time.time()
    print "Vreme: "
    print t2-t1
    qManager = QueryManagerITC(data['wordsdb'], data['cachedb'])
    # qManager = QueryManagerITC('', data)
else:
    db = DbManager()
    cdb = DbManager(collectionName='cachewordscol')
    qManager = QueryManagerITC(db, cdb)


while True:
    q = raw_input('Внеси израз: ')
    if q == 'exit' or q == 'quit':
        print 'Поздрав.'
        break
    else:
        t1 = time.time()
        print 'Резултат: ' + str(qManager.execute(q))
        t2 = time.time()
        print t2-t1

# print qManager.execute('((еден AND каде) OR оваа) AND луѓе')
# print qManager.execute('еден OR каде')


