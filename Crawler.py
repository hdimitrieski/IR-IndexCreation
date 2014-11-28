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

        except IndexError, e:
            page = None
            print e.message

        return page.content

    def crawl(self):
        for i in range(self.offset):
            self.request(self.chPart + i)
