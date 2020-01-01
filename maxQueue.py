#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TimRo
#
# Created:     31/12/2019
# Copyright:   (c) TimRo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class maxQueue():
    def __init__(self, maxSize):
        self._maxSize = maxSize
        self._q = []

    def add(self, item):
        self._q.insert(0, item)
        if(len(self._q) > self._maxSize):
            self._q.pop()
            return(True)
        return(False)

    def output(self):
        q = self._q.copy()
        q.reverse()
        return(q)

    def getSize(self):
        return(len(self._q))

    def updateSize(maxSize):
        self._maxSize = maxSize