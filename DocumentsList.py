__author__ = 'kasper'

# DISC
# TODO

class DocumentList:

    def __init__(self, did):
        self.__docList = []
        self.__docId = did
        self.__count = 0

    def addDocument(self, dId):
        self.__docList.append(dId)
        self.__count += 1

    def docList(self):
        return self.__docList

    def count(self):
        return self.__count

    def searchDocument(self, dId):
        if self.__count == 0:
            self.__docList[0] = dId
            return 1
        else:
            i = 0
            num = self.__count - 1
            while True:
                if i == num:
                    # return i
                    break
                if dId < self.__docList[(num+i)/2]:
                    num = (num+i)/2
                    num -= 1
                elif dId > self.__docList[(num+i)/2]:
                    i = (num+i-1) / 2
                    i += 1
                else:
                    # return (num+i)/2
                    i = (num+i)/2
                    break

            if dId > self.__docList[i]:
                return i



