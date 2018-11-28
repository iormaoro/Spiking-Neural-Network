
from parameters import param as par

# use ctrl + h and ' borrar' replace all with nothing.
def print_spikes(train):
    for t in range(par.T):
        for i in range(par.pixel_x*par.pixel_x):
            if(i==0):
                print ('@(posedge clk) 64\'b' + str(int(train[i,t]))),
            elif(i!= (par.pixel_x*par.pixel_x -1)):
                print ('borrar'+str(int(train[i,t]))),
            else:
                print 'borrar' + str(int(train[i,t]))+";"