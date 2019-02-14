################################################ README #########################################################

# This file contains all the parameters of the network.

#################################################################################################################

class param:

    scale = 1
    T = 400     # T*update_time = simulation time = 0.5segundo
    time_const = 10      # no 10ms
    update_time = 0.1  # 2.5 ms  # 0.1ms
    t_back = -20
    t_fore = 20

    pixel_x = 28
    Prest = 0
    m = pixel_x * pixel_x  # Number of neurons in first layer

    # en si n = 3

    n = 3  # Number of neurons in second layer
    Pmin = -500 * scale # I believe it's to potentiate the training, in inference shouldn't be this.
    # Pth = 5
    # D = 0.7
    w_max = 3 * scale
    w_min = -0.1 * scale
    sigma = 0.01  # 0.02
    A_plus = 0.1  # time difference is positive i.e negative reinforcement
    A_minus = 9.6  # 0.01 # time difference is negative i.e positive reinforcement
    tau_plus = 3.8 # en si 8 Algo que ver con que nuestra simulacion es mas corta y mas precisa? Afecta en rl
    tau_minus = 3 # ens i 3

    # izetez 12
    epoch = 5

    fr_bits = 12
    int_bits = 12
