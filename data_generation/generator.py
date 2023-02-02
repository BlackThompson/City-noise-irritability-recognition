# _*_ coding : utf-8 _*_
# @Time : 2023/2/2 22:15
# @Author : Black
# @File : generator
# @Project : my_noise_recognize

import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

s = np.random.normal(3, 1.7, 1464)

for i in range(len(s)):
    if s[i] < 1:
        s[i] = 1

    if s[i] > 9:
        s[i] = 9
    s[i] = int(s[i])

print(s)

s = pd.DataFrame(s)
s.to_csv(r'./output/normal_numbers.csv')
