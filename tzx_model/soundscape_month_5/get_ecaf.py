# -*- coding: utf-8 -*-
# @Time : 2019/6/26 10:28 
# @Author : Zhixiang Tao 

import pandas as pd
import numpy as np
from config import *

new_source_columns = ['25s文件', 'Leq_mean', 'Leq_var', 'Leq_std', 'Leq_max', 'Leq_10', 'Leq_25',
                      'Leq_median', 'Leq_75', 'Leq_90', 'Leq_10-Leq_90', 'Loudness_mean',
                      'Loudness_var', 'Loudness_std', 'Loudness_max', 'Loudness_10', 'Loudness_25',
                      'Loudness_median', 'Loudness_75', 'Loudness_90', 'Loudness_10-Loudness_90',
                      'Roughness_mean', 'Roughness_var', 'Roughness_std', 'Roughness_max',
                      'Roughness_10', 'Roughness_25', 'Roughness_median', 'Roughness_75',
                      'Roughness_90', 'Roughness_10-Roughness_90', 'Sharpness_mean',
                      'Sharpness_var', 'Sharpness_std', 'Sharpness_max', 'Sharpness_10',
                      'Sharpness_25', 'Sharpness_median', 'Sharpness_75', 'Sharpness_90',
                      'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_var', 'Fluct_std',
                      'Fluct_max', 'Fluct_10', 'Fluct_25', 'Fluct_median', 'Fluct_75', 'Fluct_90',
                      'Fluct_10-Fluct_90', 'Tonality_mean', 'Tonality_var', 'Tonality_std',
                      'Tonality_max', 'Tonality_10', 'Tonality_25', 'Tonality_median',
                      'Tonality_75', 'Tonality_90', 'Tonality_10-Tonality_90', 'ecaf', 'pctn', 'pctu',
                      'pctm', 'level']
new_source_columns_7 = ['25s文件', 'Leq_mean_x', 'Leq_std_x', 'Leq_25_x', 'Leq_median_x', 'Leq_75_x',
                        'Leq_10-Leq_90_x', 'Loudness_mean_x', 'Loudness_std_x', 'Loudness_25_x',
                        'Loudness_median_x', 'Loudness_75_x', 'Loudness_10-Loudness_90_x',
                        'Roughness_mean_x', 'Roughness_std_x', 'Roughness_25_x',
                        'Roughness_median_x', 'Roughness_75_x', 'Roughness_10-Roughness_90_x',
                        'Sharpness_mean_x', 'Sharpness_std_x', 'Sharpness_25_x',
                        'Sharpness_median_x', 'Sharpness_75_x', 'Sharpness_10-Sharpness_90_x',
                        'Fluct_mean_x', 'Fluct_std_x', 'Fluct_25_x', 'Fluct_median_x', 'Fluct_75_x',
                        'Fluct_10-Fluct_90_x', 'Tonality_mean_x', 'Tonality_std_x', 'Tonality_25_x',
                        'Tonality_median_x', 'Tonality_75_x', 'Tonality_10-Tonality_90_x', 'pctn_x',
                        'ecaf', 'pctu_x', 'pctm_x', 'level_x']

new_source_columns_7_save = ['25s文件', 'Leq_mean', 'Leq_std', 'Leq_25', 'Leq_median', 'Leq_75',
                             'Leq_10-Leq_90', 'Loudness_mean', 'Loudness_std', 'Loudness_25',
                             'Loudness_median', 'Loudness_75', 'Loudness_10-Loudness_90',
                             'Roughness_mean', 'Roughness_std', 'Roughness_25',
                             'Roughness_median', 'Roughness_75', 'Roughness_10-Roughness_90',
                             'Sharpness_mean', 'Sharpness_std', 'Sharpness_25',
                             'Sharpness_median', 'Sharpness_75', 'Sharpness_10-Sharpness_90',
                             'Fluct_mean', 'Fluct_std', 'Fluct_25', 'Fluct_median', 'Fluct_75',
                             'Fluct_10-Fluct_90', 'Tonality_mean', 'Tonality_std', 'Tonality_25',
                             'Tonality_median', 'Tonality_75', 'Tonality_10-Tonality_90', 'pctn',
                             'ecaf', 'pctu', 'pctm', 'level']

id_name_dict = {1: '37-L-1.wav', 2: '142-L-1.wav', 3: '40-L-1.wav', 4: '32-L-1.wav', 5: '112-L-1.wav',
                6: '127-L-1.wav', 7: '47-L-1.wav', 8: '149-L-1.wav', 9: '435-L-1.wav', 10: '1-L-1.wav',
                11: '699-L-1.wav', 12: '31-L-2.wav', 13: '4-L-2.wav', 14: '14-L-1.wav', 15: '53-L-1.wav',
                16: '7-L-1.wav', 17: '338-L-3.wav', 18: '110-L-1.wav', 19: '360-L-2.wav', 20: '251-L-7.wav',
                21: '77-L-1.wav', 22: '427-L-1.wav', 23: '201-L-2.wav', 24: '365-L-1.wav', 25: '295-L-5.wav',
                26: '567-L-5.wav', 27: '303-L-3.wav', 28: '186-L-29.wav', 29: '186-L-7.wav', 30: '438-L-3.wav',
                31: '407-L-9.wav', 32: '221-L-9.wav', 33: '227-L-6.wav', 34: '555-L-5.wav', 35: '450-L-11.wav',
                36: '657-L-2.wav', 37: '409-L-3.wav', 38: '686-L-7.wav', 39: '410-L-1.wav', 40: '527-L-5.wav',
                41: '281-L-7.wav', 42: '684-L-9.wav', 43: '687-L-3.wav', 44: '615-L-7.wav'}

ecad_path = r'./data/ecaf.xls'
class_4_all_path = r'./data/new_all_source_data_4.xls'
id_label_path = r'./data/id_label.csv'
source_data_ecaf_path = r'./data/new_ecaf_source_data_4.xls'
source_data_ecaf_path = r'./data/new_ecaf_source_data_4.xls'
class_4_withoutbench_rightprebench7_ecaf_path = r'./data/source_data_withoutbench_rightprebench7_ecaf_4.xls'


def get_all_data_ecaf():
    ecaf_44 = pd.read_excel(ecad_path)
    data = pd.read_excel(class_4_all_path)
    id_label = pd.read_csv(id_label_path)

    new_data = []
    for index, row in data.iterrows():
        label44 = id_label[id_label['id'] == int(row['25s文件'].split('-')[0])]['label44'].values[0]
        l_44_702 = id_name_dict[label44]
        ecaf = ecaf_44[ecaf_44['filename'] == l_44_702]['EL'].values[0]
        # print(lenrow.values))
        row['ecaf'] = ecaf
        line = row.values
        new_data.append(line)
        # print(line)

    data = pd.DataFrame(new_data, columns=new_source_columns)
    print(data)

    data.to_excel(source_data_ecaf_path)


def get_ecaf():
    ecaf = pd.read_excel(source_data_ecaf_path)
    rightprebench7 = pd.read_excel(class_4_withoutbench_rightprebench7_path)

    new_rightprebench7 = pd.merge(rightprebench7, ecaf, how='left', on='25s文件')
    new_rightprebench7 = new_rightprebench7[new_source_columns_7]
    # rightprebench7['ecaf'] = ecaf[ecaf['25s文件'] == rightprebench7['25s文件']]['ecaf']
    new_rightprebench7.to_excel(class_4_withoutbench_rightprebench7_ecaf_path)
    # print(new_rightprebench7)


if __name__ == '__main__':
    get_ecaf()
