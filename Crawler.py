# coding=utf-8
__author__ = 'kasper'

# Crawler

import requests as req
import time
from Log import Log

class Crawler:

    def __init__(self, url, chPart, offset, ds):
        self.url = url
        self.chPart = chPart
        self.offset = offset
        self.docStore = ds
        self.log = Log('logfile.log')

    # Baranje do server za strana, ja vrakjam sodrzinata od stranta
    def request(self, pgid):
        print self.url + str(pgid)
        try:
            page = req.get(self.url + str(pgid) + '/')
            if page.content == 'Error':
                self.log.log(str(time.time()) + ' - Request to file ' + str(pgid) + ' failed.')
                return None

            file = open(self.docStore + str(pgid) + '.html', 'w')
            file.write(page.content)
            file.close

        except IndexError, e:
            page = None
            self.log.log(str(time.time()) + ' - Request to file ' + pgid + ' failed. ' + str(e.args))

        return page.content

    def crawl(self):
        for i in range(self.offset):
            self.request(self.chPart + i)
