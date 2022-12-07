# -*- coding:utf-8 -*-
# 在txt文件中随机抽取行
import random
from random import randint

import numpy as np
import pandas as pd
from config import *


data = pd.read_excel(data_path_add_0429)
data = np.array(data)
print(data[30])

indexList = random.sample(range(0, 6747), 450)  # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素
indexList = random.sample(range(0, 6791), 495)  # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素

random_data = []

for i in indexList:
    random_data.append(data[i])

print(len(random_data))

test_file = pd.DataFrame(random_data)
print(test_file)
test_file.to_excel('./data/add_0430_new.xls')
