import numpy as np
from numpy.core import numeric
from numpy.lib.index_tricks import c_

dataIn = []
while True:
    lineIn = input()
    if (lineIn == ""):
        break
    dataIn.append(list([int(c) for c in lineIn]))
dataIn = np.array(dataIn)
o_arr = np.copy(dataIn)
c_arr = np.copy(dataIn)

for i in range(len(dataIn[0])):
    # number of ones and zeroes in col 'i' 
    ones_in_o = np.sum(o_arr[:,i])
    ones_in_c = np.sum(c_arr[:,i])

    if len(o_arr) > 1:
        if (2 * ones_in_o >= len(o_arr)):
            # more ones than 0 in i-th index 
            # keep ones
            o_arr = o_arr[o_arr[:, i] == 1, :]
        else:
            # more zero than 1 in i-th index 
            # keep zeros
            o_arr = o_arr[o_arr[:, i] == 0, :]

    if len(c_arr) > 1:
        if (2 * ones_in_c < len(c_arr)):
            # more zero than 1 in i-th index
            # keep ones
            c_arr = c_arr[c_arr[:, i] == 1, :]

        else:
            # more ones than 0 in i-th index
            # keep zeros
            c_arr = c_arr[c_arr[:, i] == 0, :]

retval = int(''.join(str(x) for x in o_arr[0]), 2) * int(''.join(str(x) for x in c_arr[0]), 2)
print(retval)