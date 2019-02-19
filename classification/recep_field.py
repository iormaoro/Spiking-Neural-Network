############################ README ############################################
# This file is used to apply receptive field to the image to imitate how
# retinal ganglion cells perceive in real world scenario. Here 'w' is the filter
# that need to be convoluted with the image. Sophisticated python libraries for
# convolution can be used for optimization.
################################################################################

import numpy as np


def rf(inp):
    w=[[-0.5,-0.25,0.25,-0.25,-0.5],
       [-0.25,0.25,0.625,0.25,-0.25],
       [0.25,0.625,1.,0.625,0.25],
       [-0.25,0.25,0.625,0.25,-0.25],
       [-0.5,-0.25,0.25,-0.25,-0.5]]
    pot=np.zeros([28,28])
    ran=[-2,-1,0,1,2]
    ox=2
    oy=2

    z=0

    summ_of_summs = 0
    # Convolution
    for i in range(28):
        for j in range(28):
            summ=0
            for m in ran:
                for n in ran:
                    if (i+m)>=0 and (i+m)<=28-1 and (j+n)>=0 and (j+n)<=28-1:
                        # if(z>12):
                        summ=summ+w[ox+m][oy+n] * inp[i+m][j+n] / 255
                    # else:
                    #     summ=summ+w[ox+m][oy+n] * inp[i+m][j+n] / 255
                    # print summ
            summ_of_summs=summ_of_summs+summ

            # With this z we will control that if there is an image with many white, it won't outpeform the
            # rest because of it's intensity, it will somehow normalize it for every image.
            # print summ
            # if (summ>1.1):
            #     z=z+1
            pot[i][j]=summ

    for i in range(28):
        for j in range(28):
            # print pot[i][j]
            pot[i][j] = pot[i][j] + (pot[i][j] * (((50.0 - summ_of_summs)/(summ_of_summs*2))))

    return pot

# if __name__ == '__main__':

# 	maxx = -1000
# 	minn = 1000

# 	for j in range(1,1500):
# 		img = cv2.imread("images/" + str(j) + ".png", 0)
# 		pot = rf(img)
# 		for c in pot:
# 			if max(c)>maxx:
# 				maxx=  max(c)
# 			if min(c)<minn:
# 				minn = min(c)

# 	print maxx, minn
