import statistics

import numpy as np
import pandas as pd
import torch
from matplotlib import pyplot as plt


def get_spectrum(file):
    new_data = []

    with open(file, 'r') as f:
        data = f.read().splitlines()
        for elem in data:
            dot = list(map(float, elem.split()))
            new_data.append(dot)

    test = pd.DataFrame(new_data, columns=['x', 'y'])
    x = test['x'].tolist()  # lambda
    y = test['y'].tolist()  # counts

    return x, y


def define_noise(mu_array, level=0.3, NBins=20):
    diffSpectrum = np.diff(np.array(mu_array))
    EdgesMed = statistics.median(diffSpectrum)
    EdgeStd = np.std(np.array(mu_array))

    # find outliers and zero it #

    for elem in range(len(diffSpectrum)):
        if abs(diffSpectrum[elem]) > 3 * EdgeStd:
            diffSpectrum[elem] = 0

    EdgesMin = min(diffSpectrum)
    EdgesMax = max(diffSpectrum)
    StepBins = (EdgesMax - EdgesMin) / NBins

    Edges = np.arange(EdgesMin, EdgesMax, StepBins)

    num, val, patches = plt.hist(diffSpectrum)
    val_max = np.where(num == num.max())

    # print(val_max[0], val[int(val_max[0])+1])  # (array([4], dtype=int64),)
    # print('maxbin', val[val_max][0])

    midEdges = (val[val_max][0] + val[int(val_max[0]) + 1]) / 2
    midEdges = max(val[val_max][0], val[int(val_max[0]) + 1])  # ??
    # plt.show()

    if (val[val_max][0] / (torch.numel(torch.FloatTensor(diffSpectrum)))) > level:  # sum hist
        noise = abs(midEdges)
    else:
        noise = 0

    print(noise)
    return noise


if __name__ == '__main__':
    pass

