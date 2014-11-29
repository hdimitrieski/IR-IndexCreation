__author__ = 'kasper'

# da zapisvam koga pocnalo nesto koga zavrsilo
# kolku fajloj se spustile
# za kolku vreme koj fajl
# kolku tekst imam
# kolku se golemi fajlojte so se kreirale i sl...

class Log:

    def __init__(self, logfile):
        self.logfile = logfile

    def console(self, message):
        print message

    def log(self, message):
        a = 1
        # vo fajl