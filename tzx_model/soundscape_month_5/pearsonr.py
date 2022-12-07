# -*- coding: utf-8 -*-
# @Time : 2019/1/7 19:02 
# @Author : Zhixiang Tao 

import numpy as np
from scipy.stats import pearsonr
import random
import pandas as pd
import pickle
import time
from sklearn.preprocessing import MultiLabelBinarizer, normalize
import os
from collections import Counter


def get_correlation(data, feature):
    '''
    计算data上feature之间的相关性（pearson）
    :param data: pd 数据
    :param feature: 特征
    :return: 相关性
    '''
    corrCoeff = np.zeros((len(feature), len(feature)))
    for i, f_i in enumerate(feature):
        for j, f_j in enumerate(feature):
            if i > j:
                r, p_value = pearsonr(data[f_i].values.tolist(), data[f_j].values.tolist())
                if p_value < 0.01:
                    corrCoeff[i][j] = round(r, 2)

    return corrCoeff


def getdata():
    n_class = 3
    column = ['25s文件', '源文件', '切割后时长', '源文件时长', 'Leq_mean', 'Leq_var', 'Leq_std',
              'Leq_max', 'Leq_10', 'Leq_25', 'Leq_median', 'Leq_75', 'Leq_90', 'Loudness_mean', 'Loudness_var',
              'Loudness_std', 'Loudness_max', 'Loudness_10', 'Loudness_25',
              'Loudness_median', 'Loudness_75', 'Loudness_90', 'Roughness_mean',
              'Roughness_var', 'Roughness_std', 'Roughness_max', 'Roughness_10',
              'Roughness_25', 'Roughness_median', 'Roughness_75', 'Roughness_90',
              'Sharpness_mean', 'Sharpness_var', 'Sharpness_std', 'Sharpness_max',
              'Sharpness_10', 'Sharpness_25', 'Sharpness_median', 'Sharpness_75',
              'Sharpness_90', 'Fluct_mean', 'Fluct_var', 'Fluct_std', 'Fluct_max',
              'Fluct_10', 'Fluct_25', 'Fluct_median', 'Fluct_75', 'Fluct_90',
              'Tonality_mean', 'Tonality_var', 'Tonality_std', 'Tonality_max',
              'Tonality_10', 'Tonality_25', 'Tonality_median', 'Tonality_75',
              'Tonality_90', 'level']

    use_features = column[4:-1]
    use_column = [column[0]]
    use_column.extend(column[4:])
    # print(use_column)

    # 统计特征
    data_all_path = r'F:\tao_data\feature_soundscape/特征提取表leq_level.xls'
    data = pd.read_excel(data_all_path, index_col=[0])
    data = data[use_column]
    data = data.values
    # print(data)
    # d = data.groupby('level')
    # print(d)

    # data = data[data['25s文件'] == '1-L-1.wav']
    # print(data)
    # d = ['name1','name2','correlation','p_value']
    d = []

    for i in range(len(data)):
        first = data[i, 0]
        name_1 = first.split('-')[0]
        for j in range(1, 13):
            if i + j < len(data):
                next = data[i + j, 0]
                name_2 = next.split('-')[0]
                if name_2 == name_1:
                    r, p_value = pearsonr(data[i, 1:-1], data[i + j, 1:-1])
                    if (r < 0.95) | (p_value > 0.05):
                        r = round(r, 4)
                        p_value = '%.3g' % p_value
                        line = [data[i, 0], data[i + j, 0], r, p_value]
                        d.append(line)
                    # print([data[i,0],data[i+j, 0],r, p_value])
                    # print(line)

    d = pd.DataFrame(d, columns=['name1', 'name2', 'correlation', 'p_value'])

    # print(d)
    p = r'F:\tao_data\feature_soundscape/pearsonr_correlation_95_down.xls'
    d.to_excel(p)


def get_corr():
    id_name_dict = {1: '37-L-1.wav', 2: '142-L-1.wav', 3: '40-L-1.wav', 4: '32-L-1.wav', 5: '112-L-1.wav',
                    6: '127-L-1.wav', 7: '47-L-1.wav', 8: '149-L-1.wav', 9: '435-L-1.wav', 10: '1-L-1.wav',
                    11: '699-L-1.wav', 12: '31-L-2.wav', 13: '4-L-2.wav', 14: '14-L-1.wav', 15: '53-L-1.wav',
                    16: '7-L-1.wav', 17: '338-L-3.wav', 18: '110-L-1.wav', 19: '360-L-2.wav', 20: '251-L-7.wav',
                    21: '77-L-1.wav', 22: '427-L-1.wav', 23: '201-L-2.wav', 24: '365-L-1.wav', 25: '295-L-5.wav',
                    26: '567-L-5.wav', 27: '303-L-3.wav', 28: '186-L-29.wav', 29: '186-L-7.wav', 30: '438-L-3.wav',
                    31: '407-L-9.wav', 32: '221-L-9.wav', 33: '227-L-6.wav', 34: '555-L-5.wav', 35: '450-L-11.wav',
                    36: '657-L-2.wav', 37: '409-L-3.wav', 38: '686-L-7.wav', 39: '410-L-1.wav', 40: '527-L-5.wav',
                    41: '281-L-7.wav', 42: '684-L-9.wav', 43: '687-L-3.wav', 44: '615-L-7.wav'}

    c = ['序号' '姓名' '实验地点' '年龄' '职业' '学历' '性别' '喜欢的声音' '讨厌的声音' '心情' '顺序' '声音类型'
         '吵闹度评价' '烦躁度评价' '舒适度评价' '安静度评价' '愉悦度评价']
    use_columns = ['顺序', '吵闹度评价', '烦躁度评价', '舒适度评价', '安静度评价', '愉悦度评价']
    feature_columns = ['Leq_mean', 'Leq_std', 'Leq_10', 'Leq_25',
                       'Leq_median', 'Leq_75', 'Leq_90', 'Leq_10-Leq_90', 'Loudness_mean',
                       'Loudness_std', 'Loudness_10', 'Loudness_25',
                       'Loudness_median', 'Loudness_75', 'Loudness_90', 'Loudness_10-Loudness_90',
                       'Roughness_mean', 'Roughness_std',
                       'Roughness_10', 'Roughness_25', 'Roughness_median', 'Roughness_75',
                       'Roughness_90', 'Roughness_10-Roughness_90', 'Sharpness_mean',
                       'Sharpness_std', 'Sharpness_10',
                       'Sharpness_25', 'Sharpness_median', 'Sharpness_75', 'Sharpness_90',
                       'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_std',
                       'Fluct_10', 'Fluct_25', 'Fluct_median', 'Fluct_75', 'Fluct_90',
                       'Fluct_10-Fluct_90', 'Tonality_mean', 'Tonality_std',
                       'Tonality_10', 'Tonality_25', 'Tonality_median',
                       'Tonality_75', 'Tonality_90', 'Tonality_10-Tonality_90']

    sub = ['吵闹度评价', '烦躁度评价', '舒适度评价', '安静度评价', '愉悦度评价', ]

    new_columns = ['吵闹度评价', '烦躁度评价', '舒适度评价', '安静度评价', '愉悦度评价',
                   'Leq_mean', 'Leq_std', 'Leq_10', 'Leq_25', 'Leq_median', 'Leq_75',
                   'Leq_90', 'Leq_10-Leq_90', 'Loudness_mean',
                   'Loudness_std', 'Loudness_10', 'Loudness_25',
                   'Loudness_median', 'Loudness_75', 'Loudness_90', 'Loudness_10-Loudness_90',
                   'Roughness_mean', 'Roughness_std',
                   'Roughness_10', 'Roughness_25', 'Roughness_median', 'Roughness_75',
                   'Roughness_90', 'Roughness_10-Roughness_90', 'Sharpness_mean',
                   'Sharpness_std', 'Sharpness_10',
                   'Sharpness_25', 'Sharpness_median', 'Sharpness_75', 'Sharpness_90',
                   'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_std',
                   'Fluct_10', 'Fluct_25', 'Fluct_median', 'Fluct_75', 'Fluct_90',
                   'Fluct_10-Fluct_90', 'Tonality_mean', 'Tonality_std',
                   'Tonality_10', 'Tonality_25', 'Tonality_median',
                   'Tonality_75', 'Tonality_90', 'Tonality_10-Tonality_90']

    subject_data_path = r'./data/数据库调整（改动版）.xls'

    # getdata()
    # weak_corre_name = [162,460,564]
    data_path = r'./data/new_all_source_data_4.xls'
    data = pd.read_excel(data_path)
    subject_data = pd.read_excel(subject_data_path)
    subject_data = subject_data[use_columns]
    # print(data['25s文件'])
    num_person = len(subject_data) / 44
    subject_data_44 = subject_data.groupby(['顺序']).sum()
    subject_data_44[use_columns[1:]] = subject_data_44[use_columns[1:]] / num_person

    print(subject_data_44)
    # new_data = []
    # for index, row in subject_data_44.iterrows():
    #     d = row.values.tolist()
    #     d.extend(data[data['25s文件'] == id_name_dict[index]][feature_columns].values.tolist()[0])
    #     new_data.append(d)
    #
    # new_data = pd.DataFrame(new_data, columns=new_columns)
    # print(new_data[new_data['Leq_mean']<40]['Leq_mean'])

    # corr = []
    #
    # for s in sub:
    #     row = []
    #     for f in feature_columns:
    #         r, p_value = pearsonr(new_data[s], new_data[f])
    #         if p_value <= 0.005:
    #             row.extend([str(round(r, 6)) + '***'])
    #         else:
    #             if p_value < 0.01:
    #                 row.extend([str(round(r, 6)) + '**'])
    #             else:
    #                 if p_value < 0.05:
    #                     row.extend([str(round(r, 6)) + '**'])
    #                 else:
    #                     row.extend([str(round(r, 6))])
    #     corr.append(row)
    #
    #
    # # print(corr)
    # corr = pd.DataFrame(corr,columns=feature_columns)
    # # print(corr)
    # corr.to_excel(r'./data/corr_48_5.xls')

    # print(r)
    # if (r < 0.95) | (p_value > 0.05):
    #     r = round(r, 4)
    #     p_value = '%.3g' % p_value
    #     line = [data[i, 0], data[i + j, 0], r, p_value]
    #     d.append(line)


#
# 吵闹度评价    5.677656
# 烦躁度评价    6.362637
# 舒适度评价    6.223443
# 安静度评价    5.128205
# 愉悦度评价    6.212454
# Name: 1, dtype: float64

# ['tel', 'cross_zero','25s文件']

if __name__ == '__main__':
    c = ['25s文件', 'Leq_mean', 'Leq_std', 'Leq_25', 'Leq_median', 'Leq_75',
         'Leq_10-Leq_90', 'Loudness_mean', 'Loudness_std', 'Loudness_25',
         'Loudness_median', 'Loudness_75', 'Loudness_10-Loudness_90',
         'Roughness_mean', 'Roughness_std', 'Roughness_25', 'Roughness_median',
         'Roughness_75', 'Roughness_10-Roughness_90', 'Sharpness_mean',
         'Sharpness_std', 'Sharpness_25', 'Sharpness_median', 'Sharpness_75',
         'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_std', 'Fluct_25',
         'Fluct_median', 'Fluct_75', 'Fluct_10-Fluct_90', 'Tonality_mean',
         'Tonality_std', 'Tonality_25', 'Tonality_median', 'Tonality_75',
         'Tonality_10-Tonality_90', 'Unnamed: 37', 'Leq_var', 'Leq_max',
         'Leq_10', 'Leq_90', 'Loudness_var', 'Loudness_max', 'Loudness_10',
         'Loudness_90', 'Roughness_var', 'Roughness_max', 'Roughness_10',
         'Roughness_90', 'Sharpness_var', 'Sharpness_max', 'Sharpness_10',
         'Sharpness_90', 'Fluct_var', 'Fluct_max', 'Fluct_10', 'Fluct_90',
         'Tonality_var', 'Tonality_max', 'Tonality_10', 'Tonality_90', 'tel',
         'cross_zero', 'level']

    cc = ['Leq_mean', 'Leq_std', 'Leq_25', 'Leq_median', 'Leq_75',
          'Leq_10-Leq_90', 'Loudness_mean', 'Loudness_std', 'Loudness_25',
          'Loudness_median', 'Loudness_75', 'Loudness_10-Loudness_90',
          'Roughness_mean', 'Roughness_std', 'Roughness_25', 'Roughness_median',
          'Roughness_75', 'Roughness_10-Roughness_90', 'Sharpness_mean',
          'Sharpness_std', 'Sharpness_25', 'Sharpness_median', 'Sharpness_75',
          'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_std', 'Fluct_25',
          'Fluct_median', 'Fluct_75', 'Fluct_10-Fluct_90', 'Tonality_mean',
          'Tonality_std', 'Tonality_25', 'Tonality_median', 'Tonality_75',
          'Tonality_10-Tonality_90', 'tel', 'cross_zero', 'level']

    path = r'./data/data_all_4_final.xls'
    data = pd.read_excel(path)
    corr = get_correlation(data, cc)
    corr = pd.DataFrame(corr, columns=cc, index=cc)
    corr.to_excel('./corr36_tel_croze.xls')
    print(corr)
