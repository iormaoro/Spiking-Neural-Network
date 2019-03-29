import numpy as np
from numpy import interp
import math

# initializing spike train
train=[]

freq_anterior=0

for i in range(2000):

    temp=np.zeros([(400+1),])

    # calculating firing rate proportional to the membrane potential
    # interpolating
    freq=interp(i,[0,2000],[1,6])

    # print freq
    if freq<=0:
        print error

    freq1=int(math.ceil(400 / freq))

    if(freq1!=freq_anterior):
        freq_anterior = freq1
        # return the ceiling of 600/freq as a float, the smallest integer value greater than or equal to x.

        # generating spikes according to the firing rate
        k=freq1
        while k<(400+1):  # par.T = simulation time?
            temp[k]=1
            k=k+freq1  # temp[time] = when does it have to spike, next time will be + period.
        print temp
        train.append(temp)
        # print sum(temp)

np.savetxt('train.txt', train)

