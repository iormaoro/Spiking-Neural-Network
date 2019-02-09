import numpy as np
from PIL import Image
from spike_train import encode
from spike_tbformat import print_spikes
from recep_field import rf


# img = np.array(Image.open("../images/LR" + str(0) + ".png"))
img = np.array(Image.open("../images/training_images/" + str(0) + ".png"))
pot = rf(img)
train = np.array(encode(pot))
print_spikes(train)