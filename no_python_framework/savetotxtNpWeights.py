
import numpy as np

m=784  # Number of neurons in first layer
n=3  # Number of neurons in second layer

synapse=np.zeros((n,m))

synapse=np.load("../training/ImgPot_3dig_long_2/weights_numpy.npy")
np.savetxt("../training/ImgPot_3dig_long_2/weights.txt", synapse)