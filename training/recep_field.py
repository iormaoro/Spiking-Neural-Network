####################################################### README #########################################################

# This file consists of function that convolves an image with a receptive field so that input to the network is 
# close to the form perceived by our eyes. 

#########################################################################################################################


import numpy as np
import cv2
from parameters import param as par


def rf(inp):
    # print inp
    #inp = inp[0]
    sca1 = 0.625
    sca2 = 0.125
    sca3 = -0.125
    sca4 = -.5

    # Receptive field kernel
    # w = [[sca4, sca3, sca2, sca3, sca4],
    #      [sca3, sca2, sca1, sca2, sca3],
    #      [sca2, sca1, 1, sca1, sca2],
    #      [sca3, sca2, sca1, sca2, sca3],
    #      [sca4, sca3, sca2, sca3, sca4]]

    w = [[-0.4, 0.5, -0.4],
         [0.5, 1, 0.5],
         [-0.4, 0.5, -0.4]]


    pot = np.zeros([par.pixel_x, par.pixel_x])
    # ran = [-2, -1, 0, 1, 2]
    ran = [-1, 0, 1]
    ox = 1
    oy = 1


    # Por cada pixel, mirar a el mismo y a los de alrededor y segun los valores darle una intensidad u otra al pixel.
    # Convolution
    for i in range(par.pixel_x):
        for j in range(par.pixel_x):
            summ = 0
            for m in ran:
                for n in ran:
                    #print w[ox + m][oy + n]
                    #print "inp"
                    #print inp[i + m][j + n]
                    if (i + m) >= 0 and (i + m) <= par.pixel_x - 1 and (j + n) >= 0 and (j + n) <= par.pixel_x - 1:
                        summ = summ + w[ox + m][oy + n] * inp[i + m][j + n] / 255
                        #print summ

            # print summ
            pot[i][j] = summ

    # print pot
    # w = 1
    # pot = np.zeros([par.pixel_x, par.pixel_x])
    # # Convolution without convolution
    # for i in range(par.pixel_x):
    #     for j in range(par.pixel_x):
    #         summ = w * inp[i][j] / 255
    #         print summ
    #         pot[i][j] = summ
    #



    return pot


if __name__ == '__main__':

    img = cv2.imread("mnist1/" + str(1) + ".png", 0)
    pot = rf(img)
    max_a = []
    min_a = []
    for i in pot:
        max_a.append(max(i))
        min_a.append(min(i))
    print "max", max(max_a)
    print "min", min(min_a)
