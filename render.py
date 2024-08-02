import os
import numpy as np
from matplotlib import image as mpimg


def one(string):
    result = np.array([0, 0, 0, 0, 0, 0])
    if 'circle' in string:
        result[0] = 1
    if 'triangle' in string:
        result[1] = 1
    if 'square' in string:
        result[2] = 1
    if 'pentagon' in string:
        result[3] = 1
    if 'hexagon' in string:
        result[4] = 1
    if 'heptagon' in string:
        result[5] = 1
    return result


def load_data(path):
    file_list = os.listdir(path)
    length = len(file_list)
    train_shape = mpimg.imread(path + file_list[0]).shape
    train_data = np.ndarray(shape=(length,) + train_shape, dtype=float)
    train_answer = np.ndarray(shape=(length,) + (6,))
    l = 0
    for file in file_list:
        train_data[l] = mpimg.imread(path + file)
        train_answer[l] = one(file)
        l = l + 1
    return train_data, train_answer