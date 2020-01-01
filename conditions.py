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
import random
import numpy as np

class conditions():
    def __init__(self, maxPeriod, maxDrift):
        self._maxIntensity = 10
        self._maxDrift = 5
        self._maxPeriod = maxPeriod
        self._minPerPeriod = 0.25
        self._period = 0
        self._state = "Flat"
        self._time = 0
        self._loc = 0
        self._initLoc = 0
        self._switch = 0
        self._intensity = 0
        self._iRatio = 0
        self._beginCycle()

    def tick(self):
        self._time += 1
        if(self._time > self._period):
            self._beginCycle()
            self._time = 1
        self._fetchLoc()
        return(self._loc)

    def getLoc(self):
        return(self._loc)

    def statusPrint(self):
        print("Period: {}/{}".format(self._time, self._period))
        print("State: {}".format(self._state))
        print("--Switch: {}".format(self._switch))
        print("--Intensity: {}".format(self._intensity))
        print("Init Loc: {}".format(self._initLoc))
        print("Loc: {}".format(self._loc))

    def _beginCycle(self):
        allCycles = ["exp"]*2 + ["flat"]*4 + ["lin"]*1 + ["sine"]*3

        self._initLoc = self._loc
        self._period = random.randint(int(self._minPerPeriod*self._maxPeriod),self._maxPeriod)
        self._state = allCycles[random.randint(0, len(allCycles)-1)]
        self._setDefaults()
        print("NEW CYCLE!")
        print(self.statusPrint())

    def _setDefaults(self):
        self._intensity = random.randint(1,self._maxIntensity)
        self._iRatio =(self._intensity/self._maxIntensity)
        self._switch = random.randint(0, 1)

    def _fetchLoc(self):
        if(self._state == "flat"):
            self._state_flat()
        elif(self._state == "lin"):
            self._state_lin()
        elif(self._state == "sine"):
            self._state_sine()
        elif(self._state == "exp"):
            self._state_exp()

        else: #fail safe
            print("FAIL SAFE TRIGGERED")
            self._state_flat()

    def _state_flat(self):
        self._loc = self._loc

    def _state_lin(self):
        slope = (1/self._period)*self._maxDrift*self._iRatio
        if(self._switch):
            self._loc = self._initLoc + slope*self._time
        else:
            self._loc = self._initLoc - slope*self._time
    def _state_sine(self):
        self._loc = self._initLoc + (self._iRatio*self._maxDrift)*np.sin(2*np.pi*(1/self._period)*self._time)

    def _state_exp(self):
        m = self._maxDrift*self._iRatio
        x = (self._time/self._period)*np.log(m + 1)
        if(self._switch):
            self._loc = self._initLoc + np.exp(x)
        else:
            self._loc = self._initLoc - np.exp(x)









