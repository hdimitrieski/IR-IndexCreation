__author__ = 'kasper'

import os.path

class Log:

    def __init__(self, logfile):
        self.logfile = logfile

    def console(self, message):
        print message

    def log(self, message):
        if not os.path.isfile(self.logfile):
            file = open(self.logfile, 'w')
            file.write(message + '\n')
            file.close()
        else:
            file = open(self.logfile, 'a')
            file.write(message + '\n')
            file.close()