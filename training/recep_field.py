####################################################### README #########################################################

# This file consists of function that convolves an image with a receptive field so that input to the network is 
# close to the form perceived by our eyes. 

#########################################################################################################################


import numpy as np
import cv2
from parameters import param as par
import time

def rf(inp):
    # print inp
    #inp = inp[0]
    sca1 = 0.625
    sca2 = 0.25
    sca3 = -0.25
    sca4 = -.5

    # Receptive field kernel
    w = [[sca4, sca3, sca2, sca3, sca4],
         [sca3, sca2, sca1, sca2, sca3],
         [sca2, sca1, 1, sca1, sca2],
         [sca3, sca2, sca1, sca2, sca3],
         [sca4, sca3, sca2, sca3, sca4]]

    # w = [[-0.4, 0.5, -0.4],
    #      [0.5, 1, 0.5],
    #      [-0.4, 0.5, -0.4]]


    pot = np.zeros([par.pixel_x, par.pixel_x])
    ran = [-2, -1, 0, 1, 2]
    # ran = [-1, 0, 1]
    ox = 2
    oy = 2


    # Por cada pixel, mirar a el mismo y a los de alrededor y segun los valores darle una intensidad u otra al pixel.
    # Convolution
    # start_time = time.time()

    z=0

    summ_of_summs = 0
    for i in range(par.pixel_x):
        for j in range(par.pixel_x):
            summ = 0
            for m in ran:
                for n in ran:
                    #print w[ox + m][oy + n]
                    #print "inp"
                    #print inp[i + m][j + n]


                    if (i + m) >= 0 and (i + m) <= par.pixel_x - 1 and (j + n) >= 0 and (j + n) <= par.pixel_x - 1:
                        # if(z>12):
                            summ = summ + w[ox + m][oy + n] * inp[i + m][j + n] / 255
                        # else:
                        #     summ=summ+w[ox+m][oy+n] * inp[i+m][j+n] / 255
            # print summ
            summ_of_summs = summ_of_summs + summ

            # With this z we will control that if there is an image with many white, it won't outpeform the
            # rest because of it's intensity, it will somehow normalize it for every image.
            # print summ
            # if(summ>1.1):
            #     z = z+1
                # print z
                #print summ

            # print summ
            pot[i][j] = summ
    print summ_of_summs
    # low intensity images up, and high intensity ones down
    new_total = 0 # reset it to know the new one.
    for i in range(par.pixel_x):
        for j in range(par.pixel_x):
            # print pot[i][j]
            pot[i][j] = pot[i][j] + (pot[i][j] * (((50.0 - summ_of_summs)/(summ_of_summs*2))))
            # print pot[i][j]
            new_total += pot[i][j]
    print "new " + str(new_total)

            # print sum(pot[:][:])

    # end_time = time.time()-start_time
    # print "Time for receptive field: " + str(end_time)

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
