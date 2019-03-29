######################################################## README #############################################################

# This file generates rate based spike train from the potential map.

############################################################################################################################


import numpy as np
from numpy import interp
from neuron import neuron
import random
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from recep_field import rf
import cv2
from rl import rl
from rl import update
import math
from parameters import param as par
from sklearn.preprocessing import normalize


# Builds a probabilistic spike train
def encode_stochastic(img):
    T = 200
    train = []
    pot1 = normalize(img, norm='l2') # least squares: sum of squares on each row = 1
                                     # takes outliners in consideration in learning
    for l in range(par.pixel_x):
        for m in range(par.pixel_x):
            temp = np.random.uniform(size=(T + 1))
            # temp = (temp < pot1[l][m])
            for x in range(T+1): # if not, temp gives True and False, and we need 1 or 0
                    if(temp[x] < pot1[l][m]):
                        temp[x]=1
                        # print "temp changed!!"
                    else:
                        temp[x]=0
            # print "this is temp"
            # print temp
            train.append(temp)
    return train

def encode(pot):
    # initializing spike train
    train = []

    for l in range(par.pixel_x):
        for m in range(par.pixel_x):

            temp = np.zeros([(par.T + 1), ])

            # calculating firing rate proportional to the membrane potential
            # interpolating
            freq = interp(pot[l][m], [0, 2.781], [1, 6], right=0.1) # right means if it is upper than 2.781, take right value 0.1 = nospike


            # print freq
            if freq <= 0:
                print error

            freq1 = int(math.ceil(par.T / freq))
            # return the ceiling of 600/freq as a float, the smallest integer value greater than or equal to x.

            # generating spikes according to the firing rate
            k = freq1
            if (pot[l][m] > 0):
                while k < (par.T + 1): # par.T = simulation time?
                    temp[k] = 1
                    k = k + freq1   # temp[time] = when does it have to spike, next time will be + period.
            train.append(temp)
        # print sum(temp)
    return train


if __name__ == '__main__':
    # m = []
    # n = []
    img = cv2.imread("mnist1/6/" + str(15) + ".png", 0)

    pot = rf(img)

    # for i in pot:
    # 	m.append(max(i))
    # 	n.append(min(i))

    # print max(m), min(n)
    train = encode(pot)
    f = open('look_ups/train6.txt', 'w')
    print np.shape(train)

    for i in range(201):
        for j in range(784):
            f.write(str(int(train[j][i])))
        f.write('\n')

    f.close()
