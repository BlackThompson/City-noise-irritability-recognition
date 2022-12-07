# -*- coding: utf-8 -*-
# @Time : 2019/7/26 21:35 
# @Author : Zhixiang Tao
import pandas as pd
from config import *

#
column_1 = ['Leq_mean', 'Leq_std', 'Leq_25' ]
column_2 = ['Leq_mean', 'Leq_25',  'Leq_std']
# data = pd.read_excel(data_36_4_final_path)
# 0429: add
data = pd.read_excel(data_path_add_0429)
print('每个类别的数据分布：', '\n', pd.value_counts(data.level))
print(data[:2][column_1])
print(data[:2][column_2])
