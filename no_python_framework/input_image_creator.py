# This script is used to create testbench inputs

from PIL import Image
import numpy as np

img=np.array(Image.open("../images/0/"+"2"+"_"+"1"+".png"))

str0="0x%0.2X" % 0 # 0x00

print "@(posedge clk) 64'h"+str0 + str0 + str0 + str0 + str0 + str0 + str0 + str0 +";"
for x in range(28):
    for y in xrange(0,28,7):
        strHex0="0x%0.2X" % img[x][y]
        strHex1="0x%0.2X" % img[x][y+1]
        strHex2="0x%0.2X" % img[x][y+2]
        strHex3="0x%0.2X" % img[x][y+3]
        strHex4="0x%0.2X" % img[x][y+4]
        strHex5="0x%0.2X" % img[x][y+5]
        strHex6="0x%0.2X" % img[x][y+6]

        print "@(posedge clk) 64'h"+str0 + strHex0 + strHex1 + strHex2 + strHex3 + strHex4 + strHex5 + strHex6 +";"