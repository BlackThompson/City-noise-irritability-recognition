# -*- coding: utf-8 -*-
# @Time : 2019/5/13 11:23 
# @Author : Zhixiang Tao 

import seaborn as sns
from config import  *
import pandas as pd
from matplotlib.pyplot import plot as plt

# data = pd.read_excel(class_4_all_path)
#
# data_40_down = data[data['Leq_mean']<40]
# data_70_up =  data[data['Leq_mean']>70]
# data_40_70 = data[(data['Leq_mean'] <= 70) & (data['Leq_mean'] >= 40)]
# data_40_down.to_excel(r'./new_all_source_data_40_down_4.xls',index=False)
# data_70_up.to_excel(r'./new_all_source_data_70_up_4.xls',index=False)
# data_40_70.to_excel(r'./new_all_source_data_40_70_4.xls',index=False)
# print(data_40_70)
data_4 = pd.read_excel('./data/test_file_model4.xls')
data_5 = pd.read_excel('./data/test_file_model5.xls')
data = pd.DataFrame([sound for sound in data_4[0].values if sound in data_5[0].values])
data.to_excel('./data/test_file_model4_5.xls')
print(data)
# sns.pairplot(data,hue='level',vars=['Leq_mean', 'Leq_std', 'Leq_25', 'Leq_median',
#              'Leq_75', 'Leq_10-Leq_90', 'Loudness_mean', 'Loudness_std',
#              'Loudness_25', 'Loudness_median', 'Loudness_75',
#              'Loudness_10-Loudness_90', 'Roughness_mean', 'Roughness_std',
#              'Roughness_25', 'Roughness_median', 'Roughness_75',
#              'Roughness_10-Roughness_90', 'Sharpness_mean', 'Sharpness_std',
#              'Sharpness_25', 'Sharpness_median', 'Sharpness_75',
#              'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_std', 'Fluct_25',
#              'Fluct_median', 'Fluct_75', 'Fluct_10-Fluct_90', 'Tonality_mean',
#              'Tonality_std', 'Tonality_25', 'Tonality_median', 'Tonality_75',
#              'Tonality_10-Tonality_90'])
#
# plt.show()


# ['Leq_mean', 'Leq_std', 'Leq_25', 'Leq_median',
#              'Leq_75', 'Leq_10-Leq_90', 'Loudness_mean', 'Loudness_std',
#              'Loudness_25', 'Loudness_median', 'Loudness_75',
#              'Loudness_10-Loudness_90', 'Roughness_mean', 'Roughness_std',
#              'Roughness_25', 'Roughness_median', 'Roughness_75',
#              'Roughness_10-Roughness_90', 'Sharpness_mean', 'Sharpness_std',
#              'Sharpness_25', 'Sharpness_median', 'Sharpness_75',
#              'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_std', 'Fluct_25',
#              'Fluct_median', 'Fluct_75', 'Fluct_10-Fluct_90', 'Tonality_mean',
#              'Tonality_std', 'Tonality_25', 'Tonality_median', 'Tonality_75',
#              'Tonality_10-Tonality_90', 'level']
