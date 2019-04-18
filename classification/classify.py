##################### README ###################################################
# This file executes the classification algorithm over input testing images.
# Winner neurons inhibit other neurons by a phenomenon called Lateral inhibition
# Spike for each output neuron at each time stamp is monitored.
################################################################################
import numpy as np
from neuron import neuron
import random
from recep_field import rf


import time

from PIL import Image

from spike_train import *
# from weight_initialization import learned_weights
import numpy as np
# Parameters
global timeeeeeee,T,dt,t_back,t_fore,w_min
T=400
time_steps=np.arange(1,T+1,1)
t_back=-20
t_fore=20
Pth=2  # Should be Pth = 6 for deterministic spike train
m=784  # Number of neurons in first layer
n=3  # Number of neurons in second layer
epoch=1
num_of_images=6
w_max=0.5
w_min=-0.5

# T = 400
time_const = 1
update_time = 0.1

layer2=[]
# creating the hidden layer of neurons
for i in range(n):
    a=neuron()
    layer2.append(a)

# synapse matrix
synapse=np.zeros((n,m))

synapse=np.load('weights_numpy.npy')
# print synapse[1]

# learned weights
# weight_matrix=learned_weights()
# for i in range(num_of_images):
#     synapse[i]=weight_matrix[i]
#
# # random initialization for rest of the synapses
# for i in range(num_of_images,n):
#     for j in range(m):
#         synapse[i][j]=random.uniform(w_min,w_max)

pruebas = 0
acertado = 0
millis = int(round(time.time() * 1000))
for k in range(0,3):
    for i in range(0,70):
        winner=10
        spike_count=np.zeros((n,1))

        # read the image to be classified
        img=np.array(Image.open("../images/0/"+str(k)+"_"+str(i)+".png"))
        print str(k)+"_"+str(i)+".png"

        # initialize the potentials of output neurons
        for x in layer2:
            x.initial()

        # calculate teh membrane potentials of input neurons
        pot=rf(img)

        # generate spike trains. Select between deterministic and stochastic
        # train = np.array(encode_deterministic(pot))
        train=np.array(encode_deterministic(pot))

        # coincidences=np.zeros(400+1)
        # howmanycoin=0
        #
        # for r in range(400+1):
        #     for x in range(28 * 28):
        #         coincidences[r]=coincidences[r]+train[x][r]
        #     if (coincidences[r]>1):
        #         # print coincidences[r]
        #         howmanycoin=howmanycoin+1
        #
        # print("There have been", howmanycoin, "coincidences out of", 400, "time frames.")
        # print coincidences


        # flag for lateral inhibition
        f_spike=0
        active_pot=np.zeros((n,1))
        for t in time_steps:
            for j,x in enumerate(layer2):
                active=[]

                # update potential if not in refractory period
                if (x.t_rest<t):
                    x.P=x.P+np.dot(synapse[j],train[:,t])
                    if (x.P>x.Prest):
                        x.P-=x.P*(update_time/time_const)
                    active_pot[j]=x.P
                # if(j==0):
                #     print "potential = " + str(active_pot[j])

            # Lateral Inhibition
            if (f_spike==0):
                high_pot=max(active_pot)
                # print high_pot
                if (high_pot>Pth):
                    # print t
                    f_spike=1
                    winner=np.argmax(active_pot)
                    print "winner is" + str(winner)
                    for s in range(n):
                        if (s!=winner):
                            layer2[s].P=layer2[s].Pmin

            # Check for spikes
            for j,x in enumerate(layer2):
                s=x.check()
                if (s==1):
                    spike_count[j]+=1
                    x.t_rest=t+x.t_ref

        #print spike_count

        if (winner==k):
            acertado+=1
        pruebas+=1
millis2 = int(round(time.time() * 1000))

print str((millis2 - millis)) + "milliseconds"
print str(acertado) + "out of" + str(pruebas) + ", =" + str(100*acertado/pruebas) + "%"

