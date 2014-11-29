# coding=utf-8
__author__ = 'kasper'

# Kreiranje indeks

from Crawler import Crawler
import re
import bs4
from WordsList import WordsList
from Index import Index

class CreateIndex:

    # mode = 0 -> web, mode = 1 -> lokalno
    # vo konstruktorov samo cfg mozam da stavam
    # Rabota so tekst mojt da e vo druga klasa
    def __init__(self, mode=0, url='', chPart=889, offset=1, fname='', elements=[]):
        self.mode = mode
        self.url = url
        self.chPart = chPart
        self.offset = offset
        self.docStore = fname
        self.crawler = Crawler(url, chPart, offset, fname)
        self.elements = elements
        self.index = Index()

    # Obrabotvit strana i vrakjat tekst
    def getText(self, page):
        page = bs4.BeautifulSoup(page)
        text = page.select(self.elements[0])[0].get_text()
        title = page.select(self.elements[1])[0].get_text()
        fullText = '\n'.join((title, text))
        return fullText

    # Vrakjat html strana procitana lokalno od fajl
    def getPageFromFile(self, fname):
        file = open(self.docStore + fname, 'r')
        page = file.read()
        file.close()
        return page

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
                page = self.crawler.request(self.chPart + i)
            else:
                page = self.getPageFromFile(str(self.chPart + i) + '.html')

            if not page:
                continue

            txt = self.getText(page)
            words = self.getWords(txt)
            wl = WordsList(i)
            wl.insertList(words)

            self.index.mergeWL(wl.list(), self.chPart + i)

        ind = self.index.index()
        fil = open('index.txt', 'w')
        for it in ind:
            fil.write(it + ': ')
            fil.write(str(ind[it].docList()) + '\n')
            # print it + ': ' + str(ind[it].docList())
        fil.close()
        return 0

el = ['.glavenText', '.vestgoretext h1']
ci = CreateIndex(1, 'http://arhiva.plusinfo.mk/vest/', 889, 500, './documents/', el)
ci.main()
