import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random
import numpy as np
from maxQueue import maxQueue
from conditions import conditions

MAX_LENGTH = 200
PERIOD = int(MAX_LENGTH*0.05)
MAX_DRIFT = 5
SIGMA = int(MAX_DRIFT*0.25)
AVG_N = int(MAX_LENGTH*0.05)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

q = maxQueue(MAX_LENGTH)
c = conditions(PERIOD, MAX_DRIFT)

tQ = maxQueue(MAX_LENGTH)

xar = []
for i in range(0, MAX_LENGTH):
    xar.append(i)

def generateNoise(sigma):
    average = 0
    output = np.random.normal(average, sigma, 1)
    return(output)

def getRunningAverage(data, lastN):
    dataPoints = data[-lastN:]
    return(sum(dataPoints)/len(dataPoints))

def animate(i):
    c.tick()
    mathmatical = c.getLoc()
    noise = generateNoise(SIGMA)
    signal = mathmatical + noise
    q.add(signal)
    yar = q.output()
    newTrend = getRunningAverage(yar, AVG_N)
    tQ.add(newTrend)
    trendY = tQ.output()

    ax1.clear()
    ax1.plot(xar[:q.getSize()], yar, label='Stock')
    ax1.plot(xar[:tQ.getSize()], trendY, label='Running Average')
    ax1.legend()

ani = animation.FuncAnimation(fig, animate, interval=250)
plt.show()
