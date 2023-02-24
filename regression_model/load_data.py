# _*_ coding : utf-8 _*_
# @Time : 2023/2/21 14:26
# @Author : Black
# @File : load_data
# @Project : my_noise_recognize

import pandas as pd
import numpy as np
from config import *


def feature_normalize(dataset):
    mu = np.mean(dataset, axis=0)
    sigma = np.std(dataset, axis=0)
    return (dataset - mu) / sigma


def load_train(path):
    dataset = pd.read_csv(path)
    train_X = feature_normalize(dataset[column_36])
    train_y = dataset['score']
    return train_X, train_y


def load_test(path):
    dataset = pd.read_csv(path)
    test_X = feature_normalize(dataset[column_36])
    test_y = dataset['score']
    return test_X, test_y

