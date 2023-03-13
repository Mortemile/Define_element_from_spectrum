# mu_array =[6, 5, 7, 2, 7, 5, 6]
# max_mu = max(mu_array)
# mode_ind = []
# ind = 0
#
# for i in mu_array:
#     if i == max_mu:
#         mode_ind.append(ind)
#     ind += 1
#
# inowL = min(mode_ind)
# inowR = max(mode_ind)
# out = [i for i in range(inowL, inowR+1)]
#
# print(out)
# print(mode_ind)

import matplotlib.pyplot as plt
import numpy as np
import pylab as P

mu, sigma = 200, 25
x = mu + sigma*P.randn(10000)

n, b, patches = plt.hist(x, 50, histtype='stepfilled')

bin_max = np.where(n == n.max())
plt.show()

print ('maxbin', b[bin_max][0])