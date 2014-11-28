# coding=utf-8
__author__ = 'kasper'

# Kreiranje indeks

from Crawler import Crawler
import re
from WordsList import WordsList

class CreateIndex:

    # mode = 0 -> web, mode = 1 -> lokalno
    def __init__(self, mode=0, url='', chPart=889, offset=1, fname=''):
        self.mode = mode
        self.url = url
        self.chPart = chPart
        self.offset = offset
        self.docStore = fname
        self.crawler = Crawler(url, chPart, offset, fname)

    # Vrakjat tekst procitan lokalno od fajl
    def getTextFromFile(self, fname):
        file = open(self.docStore + fname, 'r')
        page = file.read()
        file.close()
        text = self.crawler.getText(page)
        return text

    # Vrakjat lista od site zboroj od nekoj tekst
    def getWords(self, text):
        text = text.replace(u'          ', ' ')
        text = text.lower().encode('utf-8')
        text = re.sub('(,|!|\?|\.|%|“|”|"|„|-|:|\)|\(|\[|\]|\{\})', ' ', text)
        text = re.sub('\s\s+', ' ', text)
        print text
        words = text.strip()

        return words.split(' ')

    def main(self):
        # TODO

        for i in range(self.offset):
            if self.mode == 0:
                txt = self.crawler.request(self.chPart + i)
            else:
                txt = self.getTextFromFile(str(self.chPart + i) + '.html')

            words = self.getWords(txt)
            wl = WordsList(i)
            wl.insertList(words)

            for it in wl.list():
                print it + ': ' + str(wl.list()[it])

        return 0

ci = CreateIndex(1, 'http://arhiva.plusinfo.mk/vest/', 889, 1, './documents/')
ci.main()
ci.getTextFromFile('889.html')
