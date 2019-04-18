# This script is used to create testbench inputs

from PIL import Image
import numpy as np




str0="0x%0.2X" % 0 # 0x00

# 64 bit frame

# for i in range(0,3): # i is the digit's number (0 means we are inputing a 0)
#     for l in range(0,10):
#         img=np.array(Image.open("../images/0/"+str(i)+"_"+str(l)+".png"))
#         strHexInfo="0x%0.2X" % i # we send info of what number is it
#         print "@(posedge clk) frame = 64'h"+str0 + str0 + str0 + str0 + str0 + str0 + str0 + strHexInfo +";"
#         print "arrived = 1'b1;"
#         for x in range(28):
#             for y in xrange(0,28,7):
#                 strHex0="0x%0.2X" % img[x][y]
#                 strHex1="0x%0.2X" % img[x][y+1]
#                 strHex2="0x%0.2X" % img[x][y+2]
#                 strHex3="0x%0.2X" % img[x][y+3]
#                 strHex4="0x%0.2X" % img[x][y+4]
#                 strHex5="0x%0.2X" % img[x][y+5]
#                 strHex6="0x%0.2X" % img[x][y+6]
#
#                 print "@(posedge clk) frame = 64'h"+str0 + strHex0 + strHex1 + strHex2 + strHex3 + strHex4 + strHex5 + strHex6 +";"
#         #once finished sending a digit:
#         print "@(posedge clk) arrived = 1'b0; #9000"

# 32 bit frame

for i in range(0,3): # i is the digit's number (0 means we are inputing a 0)
    for l in range(0,10):
        img=np.array(Image.open("../images/0/"+str(i)+"_"+str(l)+".png"))
        strHexInfo="0x%0.2X" % i # we send info of what number is it
        print "@(posedge clk) frame = 32'h"+str0 + str0 + str0 + strHexInfo +";"
        print "arrived = 1'b1;"
        for x in range(28):
            for y in xrange(0,28,4):
                strHex0="0x%0.2X" % img[x][y]
                strHex1="0x%0.2X" % img[x][y+1]
                strHex2="0x%0.2X" % img[x][y+2]
                strHex3="0x%0.2X" % img[x][y+3]
                # strHex4="0x%0.2X" % img[x][y+4]
                # strHex5="0x%0.2X" % img[x][y+5]
                # strHex6="0x%0.2X" % img[x][y+6]

                print "@(posedge clk) frame = 32'h"+ strHex0 + strHex1 + strHex2 + strHex3+";"
        #once finished sending a digit:
        print "@(posedge clk) arrived = 1'b0; #9000"