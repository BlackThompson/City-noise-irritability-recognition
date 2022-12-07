# -*- coding: utf-8 -*-
# @Time : 2019/4/28 8:09 
# @Author : Zhixiang Tao 

import numpy as np
from collections import Counter
import os
import pandas as pd

'''

'''
path_dir = r'./data/dropfilename'
file_list = os.listdir(path_dir)

drop_infor = []

for file in file_list:
    file_path = os.path.join(path_dir, file)
    f = file.split('_')[0]
    data = np.load(file_path)
    data = data.item()
    drop = [[k, v, f] for k, v in data.items()]
    drop_infor.extend(drop)

drop_infor = sorted(drop_infor,key= lambda x:x[1],reverse=True)
drop_infor = pd.DataFrame(drop_infor,columns=['drop_file','fetures_number','class'])
drop_infor.to_excel('drop_file_name.xls',index=None)
print(drop_infor)
# data = data.item()
# drop = {k:v for k,v in data.items() }
# for i ,k in data.items():
#     print(i)
# print(type(drop))
# print(data)
# print(file_list)
