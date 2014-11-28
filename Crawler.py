# coding=utf-8
__author__ = 'kasper'

# Crawler

import requests as req
import bs4
import re

class Crawler:

    def __init__(self, url, chPart, offset, ds):
        self.url = url
        self.chPart = chPart
        self.offset = offset
        self.docStore = ds

    # Obrabotka na strana
    def getText(self, page):
        page = bs4.BeautifulSoup(page)
        text = page.select('.glavenText')[0].get_text()
        title = page.select('.vestgoretext h1')[0].get_text()
        fullText = '\n'.join((title, text))
        return fullText

    # Baranje do server za strana
    def request(self, pgid):
        print self.url + str(pgid)
        try:
            page = req.get(self.url + str(pgid) + '/')
            if page.content == 'Error':
                return None

            file = open(self.docStore + str(pgid) + '.html', 'w')
            file.write(page.content)
            file.close

            fullText = self.getText(page.content)

        except IndexError, e:
            fullText = None
            print e.message


        return fullText

    def crawl(self):
        for i in range(self.offset):
            self.request(self.chPart + i)
