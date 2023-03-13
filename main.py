import matplotlib.pyplot as plt
import numpy as np
import statistics
import torch

from other_func import get_spectrum, define_noise
from elements import whats_the_element

# mu_array = [1, 2, 3, 4, 4, 3, 2, 1, 3, 4, 5, 5, 4, 3, 0, 1, 3, 3, 1, 1, 0]
# mu_array = [1, 2, 3, 3, 4, 4, 3, 2, 1, 3, 4, 3, 5, 5, 4, 3, 0, 1, 3, 3, 1, 1, 0]

mu_array = get_spectrum('spectrum.txt')[1] # intensity
wavelength = get_spectrum('spectrum.txt')[0]  # wavelength
wavelength = [int (x) for x in wavelength]  # float list to int

w = 0
index = 0
for wave in wavelength:
    if wave == w:
        mu_array.pop(index)
        wavelength.pop(index)
    index += 1


# print(mu_array)
mu_array_initial = mu_array

mode_ind = []
ind = 0

step = 1  # set parameters
addstep = 1
noise = 0

IH = []  # IH = interval hull
max_mu_array = []

plt.plot(mu_array)
plt.show()

n = 1
iteration = -1


def ROI_mode(mu_array):  # main func
    global n, iteration
    global ind
    global wavelength
    print(f"iteration_num_{iteration+1}")

    iteration += 1

    n += 1

    max_mu = max(mu_array)
    max_mu_array.append(max_mu)

    mode_ind = []
    ind = 0

    for i in mu_array:
        if i == max_mu:
            mode_ind.append(ind)
        ind += 1


    inowL = min(mode_ind)
    inowR = max(mode_ind)

    ROInow = [i for i in range(inowL, inowR + 1)]

    if len(ROInow) > 0:  # vanish the peak
        for i in ROInow:
            mu_array[i] = 0

    Lebesgue_lev = max(mu_array)

    # try:
    #     add_noise = define_noise(mu_array)
    #
    # except ValueError:
    #     print('Done')

    stepL = step  # set step
    stepR = step

    try:  # one step forward
        inowL -= stepL
        inowR += stepR
    except inowL < 1:
        inowL = 1
    except inowR > len(mu_array):
        inowR = len(mu_array)

    ROInow = [i for i in range(inowL, inowR + 1)]

    Lebesgue_lev = max(mu_array[inowL], mu_array[inowR])

    # [aa, aa_ind] = find(mu_arraynow(ROInow) == 0);  ????????
    # ROInow(aa_ind) = [];

    GOFW = 0  # flag

    if Lebesgue_lev > 0:
        GOFW = 1  # move forward

    while GOFW:
        Lebesgue_lev = max(mu_array[inowL], mu_array[inowR])
        if Lebesgue_lev > 0:
            GOFW = 1  # move forward
        GOFW = ((Lebesgue_lev + 0) > max(mu_array))  # check if   max(Left, Rigth) > max remain array
        # print(GOFW)

        if (mu_array[inowL - 1] < mu_array[inowL]) & (mu_array[inowR + 1] < mu_array[inowR]):
            # print(mu_array[inowL - 1], mu_array[inowL])
            # print(mu_array[inowR + 1], mu_array[inowR])
            inowL -= stepL

            if inowL < 1:
                inowL = 1
            inowR += stepR

            if inowR > len(mu_array):
                inowR = len(mu_array)

            ROInow = [i for i in range(inowL, inowR + 1)]

        else:
            stepL += addstep
            stepR += addstep
            inowL -= stepL

            if inowL < 1:
                inowL = 1
            inowR += stepR

            if inowR > len(mu_array):
                inowR = len(mu_array)
            ROInow = [i for i in range(inowL, inowR + 1)]

            stepL -= addstep
            stepR -= addstep

            print("no monotone")

        Lebesgue_lev = max(mu_array[inowL], mu_array[inowR])

    if len(ROInow) > 0:  # vanish the peak
        for i in ROInow:
            mu_array[i] = 0


    plt.plot(wavelength, mu_array)  # plot without peak
    y = [0 for i in range(len(ROInow))]
    # plt.plot(ROInow, y)
    plt.show()

    IH.append([wavelength[min(ROInow)], wavelength[max(ROInow)]])
    res = whats_the_element(IH[iteration])
    print(f'The element for wavelength {res[1]} nm is ', res[0])
    # print(IH)

    while max(mu_array) != 0:
        ROI_mode(mu_array)

    return mu_array


ROI_mode(mu_array)
# noise(mu_array)
