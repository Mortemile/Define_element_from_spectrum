dict_elem = {'Cr 2': [333, 334, 335, 336, 337, 338, 339, 340], 'B 2': [341, 342, 343, 344, 345],
             'N IV': [347, 348, 349], 'C V': [350, 352, 353, 761, ],
             'Fe I': [675, 676, 354, 355, 356, 357, 358, 359, 360, 361, 362, 444, 445, 446, 404, 405, 406, 407, 512,
                      513, 514],
             'O III': [370, 371, 372, 375, 376, 377, 378, 379], 'O IV': [373, 374],
             'Mo I': [386], 'H I': [388, 389, 390, 866], 'F II': [401, 403, 383, 384, 385],
             'C II': [387, 392, 425, 426, 503, 504, 587, 588, 589, 614, 615, 616, 658, 659, 706, 677, 678, 679, 680,
                      711, 712, 723],
             'O II': [391, 394, 395, 397, 398, 406, 408, 407, 435, 439, 440, 441, 442, 459, 466, 663, 664, 665, 671,
                      672, 690, 691, 710], 'C I': [396, 476, 477, 478, 537, 538, 539, 599, 600, 601],
             'N II': [399, 400, 460, 461, 462, 500],
             'H_alpha': [408, 655, 656, 657], 'N III': [409, 410], 'B II': [412, 493, 494, 495],
             'B III': [423, 424, 463], 'H_gamma': [431, 432, 433, 434],
             'Cr I': [457, 458],
             'C III': [464, 465, 673, 674, 748, 759], 'He II': [467, 468],
             'H_beta': [484, 485, 486], 'Cu II': [724, 725, 726, 489, 490, 491],
             'He I': [501, 502, 585, 586, 587, 666, 667],
             ' C VI': [528, 529, 530], 'N VII': [566, 567, 568, 792], 'C IV': [579, 580, 581, 772],
             'O VIII': [605, 606, 607], 'Cu I': [648, 649, 650], 'W I': [705],
             'Cr II': [708, 709], 'Fe II': [730], 'O I ': [776], }

wavelength = [654, 656]


def whats_the_element(wavelength):
    wl = [i for i in range(wavelength[0], (wavelength[1] + 1))]

    for wave in wl:
        for check_elem in dict_elem.values():  # check_elem = [333, 334, 335, 336, 337, 338, 339]
            if wave in check_elem:
                keys = dict_elem.keys()
                for key in keys:
                    if dict_elem[key] == check_elem:
                        return key, wave
    return 'Undefined element!!'


if __name__ == '__main__':
    print(whats_the_element(wavelength))
