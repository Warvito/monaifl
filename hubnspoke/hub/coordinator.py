import copy
import numpy as np

def FedAvg(w):
    w_avg = copy.deepcopy(w[0])
    for k in w_avg.keys():
        #print(k['features.conv0.weight'])
        for i in range(1, len(w)):
            w_avg[k] += w[i][k]
        w_avg[k] = np.divide(w_avg[k], len(w))
    return w_avg