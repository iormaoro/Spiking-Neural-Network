####################################################### README ####################################################################

# This is the main file which calls all the functions and trains the network by updating weights


#####################################################################################################################################

# pip install -r requirements.txt
import numpy as np
from neuron import neuron
import random
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

from recep_field import rf
import cv2
from spike_train import encode
from spike_train import encode_stochastic
from rl import rl
from rl import update
from reconstruct import reconst_weights
from parameters import param as par
from var_th import threshold
from spike_tbformat import print_spikes
import os

from PIL import Image

# potentials of output neurons
pot_arrays = []
for i in range(par.n):
    pot_arrays.append([])

# time series
time = np.arange(1, par.T + 1, 1)

layer2 = []

# creating the hidden layer of neurons
for i in range(par.n):
    a = neuron()
    layer2.append(a)

# synapse matrix	initialization
synapse = np.zeros((par.n, par.m))

for i in range(par.n):
    for j in range(par.m):
        synapse[i][j] = random.uniform(0, 0.4 * par.scale)

for k in range(par.epoch):
    # for i in range (1, 7):
    # for i in range(322, 323):
    for i in range (0,2):

        print i, "  ", k
        # img = cv2.imread(mnist1/" + str(i) + ".png", 0)
        # img = np.array(Image.open("../classification/training_images/" + str(i) + ".png"))
        img = np.array(Image.open("../images/LR" + str(i) + ".png"))
        # img = np.array(Image.open("../images/10" + str(i) + ".png"))
        # print img
        # img = img[0]
        # print img

        # img_numb = np.zeros((par.pixel_x, par.pixel_x))

        # RGB to GrayScale convert Prueba1.png - type Grayscale Prueba0_Gray_1.png
        # print img
        # for x in range(0,par.pixel_x) :
        #     for y in range(0,par.pixel_x) :
        #         if (img[x][y] == True) :
        #             img_numb[x][y] = 255
        #         else :
        #             img_numb[x][y] = 0

        # print img_numb


        # Convolving image with receptive field
        # Kernel (image processing)
        pot = rf(img)

        # Generating spike train
        train = np.array(encode(pot))

        # calculating threshold value for the image
        var_threshold = threshold(train)

        # print var_threshold
        # synapse_act = np.zeros((par.n,par.m))
        # var_threshold = 9
        # print var_threshold
        # var_D = (var_threshold*3)*0.07

        var_D = 0.15 * par.scale

        # initialize threshold for hidden neurons
        for x in layer2:
            x.initial(var_threshold)

        # flag for lateral inhibition
        f_spike = 0

        img_win = 100

        active_pot = []
        for index1 in range(par.n):
            active_pot.append(0)

        # Leaky integrate and fire neuron dynamics
        for t in time:
            for j, x in enumerate(layer2):
                active = []
                if (x.t_rest < t):
                    x.P = x.P + np.dot(synapse[j], train[:, t])
                    # print "diferencia"
                    # print x.P - (x.P - np.dot(synapse[j], train[:, t]))
                    # print train[:, t]
                    # print synapse[j]
                    if (x.P > par.Prest):
                        x.P -= var_D        # Aqui iria la ecuacion diferencial.
                    active_pot[j] = x.P

                pot_arrays[j].append(x.P)

            # Lateral Inhibition
            if (f_spike == 0):
                high_pot = max(active_pot)
                if (high_pot > var_threshold):
                    f_spike = 1
                    winner = np.argmax(active_pot)
                    img_win = winner
                    print "winner is " + str(winner)
                    for s in range(par.n):
                        if (s != winner):
                            layer2[s].P = par.Pmin

            # Check for spikes and update weights
            for j, x in enumerate(layer2):
                s = x.check()
                if (s == 1):
                    x.t_rest = t + x.t_ref
                    x.P = par.Prest
                    for h in range(par.m):
                        for t1 in range(-2, par.t_back - 1, -1):
                            if 0 <= t + t1 < par.T + 1:
                                if train[h][t + t1] == 1:
                                    # print "weight change by" + str(update(synapse[j][h], rl(t1)))
                                    synapse[j][h] = update(synapse[j][h], rl(t1))

                        for t1 in range(2, par.t_fore + 1, 1):
                            if 0 <= t + t1 < par.T + 1:
                                if train[h][t + t1] == 1:
                                    # print "weight change by" + str(update(synapse[j][h], rl(t1)))
                                    synapse[j][h] = update(synapse[j][h], rl(t1))
                                    #print synapse[j][h]
        if (img_win != 100):
            for p in range(par.m):
                if sum(train[p]) == 0:
                    synapse[img_win][p] -= 0.06 * par.scale
                    if (synapse[img_win][p] < par.w_min):
                        synapse[img_win][p] = par.w_min

ttt = np.arange(0, len(pot_arrays[0]), 1)
Pth = []
for i in range(len(ttt)):
    Pth.append(layer2[0].Pth)

# Check if different pixels have spikes in same time

coincidences = np.zeros(par.T+1)
howmanycoin = 0

for l in range(par.T+1):
    for x in range(par.pixel_x * 2):
        coincidences[l] = coincidences[l] + train[x][l]
    if(coincidences[l]>1):
        howmanycoin=howmanycoin+1

print("There have been", howmanycoin, "coincidences out of", par.T, "time frames.")
print coincidences

np.savetxt('spiketrain.txt', train, fmt = '%d')
# file_object  = open("SpikeTrain.txt", "w")
# file.write("str(train)")
# file.close()
np.savetxt('weights.txt', synapse)
# file_object  = open("Weigths.txt", "w")
# file.write(str(synapse))
# file.close()
# matlab --> rot90....dec2q



# plotting
for i in range(par.n):
    axes = plt.gca()
    axes.set_ylim([-20, 50])
    plt.plot(ttt, Pth, 'r')
    plt.plot(ttt, pot_arrays[i])
    plt.show()


# print spiketrain

print_spikes(train)

# Reconstructing weights to analyse training
for i in range(par.n):
    reconst_weights(synapse[i], i + 1)
print "Donde pone winner is X, en la reconstruccion es la Neuron(X+1)."
print "Y la imagen, 1 -> Simbolo 0, 2 -> Simpolo 1..."
#print weights -> synapse[x][y], x es la neurona a la que entran los synapses, e y de la neurona de donde salen.
print synapse[0][0]

