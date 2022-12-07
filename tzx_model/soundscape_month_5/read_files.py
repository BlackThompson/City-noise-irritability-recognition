import pandas as pd
import numpy as np
from config import *

"""
拼接250 + 495数据到0509_new.xls
"""

cols = ['25s文件'] + column_36 + column_pct

# data_0430 = pd.read_excel('data/add_0430_new.xls').loc[:, cols]
# data_0430 = pd.read_excel('data/add_0430_origin.xls').loc[:, cols]      # 450
# data_0430 = pd.read_excel(data_36_4_final_path).loc[:, cols]      # 6700

gaofei_39 = pd.read_excel('data/gaofei_36.xls').loc[:, cols]

print(gaofei_39.columns)
print(gaofei_39[:5])

# 250 + 495 = 295 + 450
# data_0509 = pd.concat([gaofei_39, data_0430], axis=0)
# print(len(data_0509.columns))
# print(data_0509.shape)

# print(pd.value_counts(data_0430['level']))
# print(pd.value_counts(data_0509['level']))

gaofei_39.to_excel('data/add_0509_39_250.xls', index=False)
