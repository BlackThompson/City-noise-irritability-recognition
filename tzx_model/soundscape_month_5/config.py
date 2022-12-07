# -*- coding: utf-8 -*-
# @Time : 2019/4/24 15:43 
# @Author : Zhixiang Tao 

# feature
"""
根据相关性选择特征
显著性均小于0.01
"""
column_nn = ['Leq_mean', 'Leq_std', 'Leq_25', 'Leq_median',
             'Leq_75', 'Leq_10-Leq_90', 'Loudness_mean', 'Loudness_std',
             'Loudness_25', 'Loudness_median', 'Loudness_75',
             'Loudness_10-Loudness_90', 'Roughness_mean', 'Roughness_std',
             'Roughness_25', 'Roughness_median', 'Roughness_75',
             'Roughness_10-Roughness_90', 'Sharpness_mean', 'Sharpness_std',
             'Sharpness_25', 'Sharpness_median', 'Sharpness_75',
             'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_std', 'Fluct_25',
             'Fluct_median', 'Fluct_75', 'Fluct_10-Fluct_90', 'Tonality_mean',
             'Tonality_std', 'Tonality_25', 'Tonality_median', 'Tonality_75',
             'Tonality_10-Tonality_90', 'level']

# 所有特征，共36维度
column_36 = ['Leq_mean', 'Leq_std', 'Leq_25', 'Leq_median',
             'Leq_75', 'Leq_10-Leq_90', 'Loudness_mean', 'Loudness_std',
             'Loudness_25', 'Loudness_median', 'Loudness_75',
             'Loudness_10-Loudness_90', 'Roughness_mean', 'Roughness_std',
             'Roughness_25', 'Roughness_median', 'Roughness_75',
             'Roughness_10-Roughness_90', 'Sharpness_mean', 'Sharpness_std',
             'Sharpness_25', 'Sharpness_median', 'Sharpness_75',
             'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_std', 'Fluct_25',
             'Fluct_median', 'Fluct_75', 'Fluct_10-Fluct_90', 'Tonality_mean',
             'Tonality_std', 'Tonality_25', 'Tonality_median', 'Tonality_75',
             'Tonality_10-Tonality_90', 'level']
column_pct = ['pctn', 'pctu', 'pctm']
# 'leq_w', 'leq_esm', 'sharpness_slop2', 'tonality_esm', 'tonality_phimax','crz',
# ,'tel','crz','leq_w', 'leq_esm', 'sharpness_slop2', 'tonality_esm', 'tonality_phimax','crz',
#

column_all = ['Leq_mean', 'Leq_var', 'Leq_std', 'Leq_max', 'Leq_10', 'Leq_25',
              'Leq_median', 'Leq_75', 'Leq_90', 'Leq_10-Leq_90', 'Loudness_mean',
              'Loudness_var', 'Loudness_std', 'Loudness_max', 'Loudness_10',
              'Loudness_25', 'Loudness_median', 'Loudness_75', 'Loudness_90',
              'Loudness_10-Loudness_90', 'Roughness_mean', 'Roughness_var',
              'Roughness_std', 'Roughness_max', 'Roughness_10', 'Roughness_25',
              'Roughness_median', 'Roughness_75', 'Roughness_90',
              'Roughness_10-Roughness_90', 'Sharpness_mean', 'Sharpness_var',
              'Sharpness_std', 'Sharpness_max', 'Sharpness_10', 'Sharpness_25',
              'Sharpness_median', 'Sharpness_75', 'Sharpness_90',
              'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_var',
              'Fluct_std', 'Fluct_max', 'Fluct_10', 'Fluct_25', 'Fluct_median',
              'Fluct_75', 'Fluct_90', 'Fluct_10-Fluct_90', 'Tonality_mean',
              'Tonality_var', 'Tonality_std', 'Tonality_max', 'Tonality_10',
              'Tonality_25', 'Tonality_median', 'Tonality_75', 'Tonality_90',
              'Tonality_10-Tonality_90', 'level']
column_all_noVar = ['Leq_mean', 'Leq_std', 'Leq_10', 'Leq_25',
                    'Leq_median', 'Leq_75', 'Leq_90', 'Leq_10-Leq_90', 'Loudness_mean',
                    'Loudness_std', 'Loudness_10',
                    'Loudness_25', 'Loudness_median', 'Loudness_75', 'Loudness_90',
                    'Loudness_10-Loudness_90', 'Roughness_mean',
                    'Roughness_std', 'Roughness_10', 'Roughness_25',
                    'Roughness_median', 'Roughness_75', 'Roughness_90',
                    'Roughness_10-Roughness_90', 'Sharpness_mean',
                    'Sharpness_std', 'Sharpness_10', 'Sharpness_25',
                    'Sharpness_median', 'Sharpness_75', 'Sharpness_90',
                    'Sharpness_10-Sharpness_90', 'Fluct_mean',
                    'Fluct_std', 'Fluct_10', 'Fluct_25', 'Fluct_median',
                    'Fluct_75', 'Fluct_90', 'Fluct_10-Fluct_90', 'Tonality_mean',
                    'Tonality_std', 'Tonality_10',
                    'Tonality_25', 'Tonality_median', 'Tonality_75', 'Tonality_90',
                    'Tonality_10-Tonality_90', 'level']

# 特征与4类相关性非零,且不再同一主成分中,同一主成分保留，同一类特征保留两个
# 16 维度
column_feature_4_nonezero_none_inOnePca = ['Leq_mean', 'Leq_25', 'Loudness_mean', 'Loudness_25', 'Roughness_25',
                                           'Roughness_75', 'Fluct_mean', 'Fluct_75', 'Tonality_mean', 'Tonality_75',
                                           'Sharpness_mean', 'Sharpness_75', 'Roughness_std',
                                           'Loudness_std', 'Leq_10-Leq_90', 'Roughness_10-Roughness_90', 'leq_w',
                                           'leq_esm', 'sharpness_slop2', 'tonality_esm', 'tonality_phimax', 'crz',
                                           'level']
# ,'tel','cross_zero',


# 余老师商定特征
# 25
column_yu_1 = ['Leq_std', 'Leq_median', 'Leq_75', 'Leq_10-Leq_90', 'Loudness_mean',
               'Loudness_std', 'Roughness_mean', 'Roughness_75', 'Roughness_10-Roughness_90', 'Sharpness_std',
               'Sharpness_25', 'Sharpness_median', 'Sharpness_75', 'Fluct_mean', 'Fluct_std',
               'Fluct_25', 'Fluct_median', 'Fluct_10-Fluct_90', 'Tonality_mean', 'Tonality_std',
               'Tonality_25', 'Tonality_median', 'Tonality_10-Tonality_90', 'crz', 'level']
c_1 = ['crz', 'level']

# 'leq_w', 'leq_esm', 'sharpness_slop2', 'tonality_esm', 'tonality_phimax',
# 23
column_yu_2 = ['Leq_std', 'Leq_median', 'Leq_75', 'Leq_10-Leq_90', 'Loudness_mean',
               'Loudness_std', 'Roughness_mean', 'Roughness_75', 'Roughness_10-Roughness_90', 'Sharpness_std',
               'Sharpness_25', 'Sharpness_median', 'Fluct_mean', 'Fluct_std',
               'Fluct_25', 'Fluct_10-Fluct_90', 'Tonality_mean', 'Tonality_std',
               'Tonality_25', 'Tonality_median', 'Tonality_10-Tonality_90',
               'tel', 'cross_zero', 'tel', 'level']
# dict to class

# 四类对应标签，44对应4
dict44_4 = {3: 1, 5: 1, 6: 1, 8: 1, 2: 1, 1: 1, 4: 1,
            11: 2, 9: 2, 41: 2, 25: 2, 15: 2, 12: 2,
            19: 2, 39: 2, 18: 2, 22: 2, 27: 2, 7: 2, 28: 2,
            29: 3, 23: 3, 26: 3, 17: 3, 34: 3, 31: 3, 38: 3,
            20: 3, 10: 3, 43: 3, 14: 3, 40: 3, 33: 3, 13: 3,
            24: 3, 36: 3, 32: 3, 35: 3, 21: 3, 16: 3,
            30: 4, 44: 4, 37: 4, 42: 4,
            }

# 五类对应标签，44对应5
dict44_5 = {3: 1, 5: 1, 6: 1, 8: 1, 2: 1, 1: 1, 4: 1,
            11: 2, 9: 2, 41: 2, 25: 2, 15: 2, 12: 2,
            19: 2, 39: 2, 18: 2, 22: 2, 27: 2, 7: 2, 28: 2,
            29: 3, 23: 3, 26: 3, 17: 3, 34: 3, 31: 3, 38: 3,
            20: 3, 10: 3, 43: 3, 14: 3, 40: 3,
            33: 4, 13: 4, 24: 4, 36: 4, 32: 4, 35: 4, 21: 4, 16: 4,
            30: 5, 44: 5, 37: 5, 42: 5,
            }
# dict_soundsource_44 = {'海浪声风声流水声'：3, '鸟鸣虫叫流水声'：6 ,'海浪声鸟鸣虫叫'：5,
#                        '雨声'：8,'雨声鸟鸣虫叫'：2, 1: ['海浪声'],
#                        4: ['鸟鸣虫叫'], 11: ['鸟鸣虫叫', '飞机声'], 9: ['鸟鸣虫叫', '生活声'],
#                        41: ['雨声', '汽车声'], 25: ['音乐声', '生活声', '鸟鸣虫叫', '汽车声'], 15: ['风声'],
#                        12: ['鸟鸣虫叫', '渔艇声'], 19: ['虫鸣蛙叫', '飞机声'], 18: ['虫鸣蛙叫'],
#                        7: ['流水声', '风声'], 28: ['汽车声', '鸟鸣虫叫'], 27: ['生活声', '汽车声'],
#                        22: ['生活声', '鸟鸣虫叫'], : 39['歌声', '活动声（打球）'], ['鸟鸣虫叫', '生活声', '汽车声']: 29,
#                        26: ['生活声(广播)', '鸟鸣虫叫', '汽车声'], ['活动声（打球）']: 23, ['雨声', '鸟鸣虫叫', '生活声', '机器声']: 17,
# :['活动声(打球声)', '汽车声']
# 31, ['音乐声', '生活声', '汽车声']: 34, ['鸟鸣虫叫', '生活声', '渔艇声']: 10,
# 38: ['飞机声', '鸟鸣虫叫'], ['风声', '鸟鸣虫叫']: 14, ['音乐声', '鸟鸣虫叫']: 20,
# 43: ['飞机声', '机器声', '鸟鸣虫叫', '生活声']:, ['鸟鸣虫叫', '海浪声', '渔艇声']: 13, ['渔艇', '水声', '鸟鸣虫叫']: 16,
# 21: ['虫鸣'], ['歌声', '生活声']: 4, ['汽车声', '生活声']: 32, ['汽车声']: 33,
# 35: ['机器声', '生活声'], ['施工声', '鸟鸣虫叫']: 36, ['生活声（商业活动）']: 40,
# 30: ['施工声', '鸟鸣虫叫', '生活声'], ['施工声', '生活声', '鸟鸣虫叫']: 37, ['机器声']: 42, ['施工声']: 44}


# path
data_all_path = r'./data/data_all_4.xls'
class_4_36_path = r'./data/new_source_data_4.xls'
class_5_36_path = r'./data/new_source_data_5.xls'
up_class_4_36_path = r'./data/updata_new_source_data_4.xls'
up_10class_4_36_path = r'./data/updata_10_new_source_data_4.xls'
no_bench_10class_4_36_path = r'./data/no_bench_new_source_data_4.xls'
class_4_all_path = r'./data/new_all_source_data_4.xls'

# class_4_withoutbench_path = r'./data/new_source_data_withoutbench_4.xls'


# 通过主观评测对标到4类，去除差异性较大数据
class_4_withoutbench_path = r'./data/source_data_withoutbench_4.xls'
# 差异性较大数据
class_4_bench_path = r'./data/bench_data.xls'
# class_4_withoutbench_path预测class_4_bench_path，和原标签一致，保留,2为第二次预测
class_4_bench_rightprebench_path = r'./data/preben_equ_ben.xls'
class_4_bench_rightprebench2_path = r'./data/preben_equ_ben2.xls'
class_4_bench_rightprebench3_path = r'./data/preben_equ_ben3.xls'
class_4_bench_rightprebench4_path = r'./data/preben_equ_ben4.xls'
class_4_bench_rightprebench5_path = r'./data/preben_equ_ben5.xls'
class_4_bench_rightprebench6_path = r'./data/preben_equ_ben6.xls'
# class_4_bench_rightprebench_path 加上 class_4_withoutbench_path，2为添加在预测
class_4_withoutbench_rightprebench_path = r'./data/source_data_withoutbench_rightprebench_4.xls'
class_4_withoutbench_rightprebench2_path = r'./data/source_data_withoutbench_rightprebench2_4.xls'
class_4_withoutbench_rightprebench3_path = r'./data/source_data_withoutbench_rightprebench3_4.xls'
class_4_withoutbench_rightprebench4_path = r'./data/source_data_withoutbench_rightprebench4_4.xls'
class_4_withoutbench_rightprebench5_path = r'./data/source_data_withoutbench_rightprebench5_4.xls'
class_4_withoutbench_rightprebench6_path = r'./data/source_data_withoutbench_rightprebench6_4.xls'
class_4_withoutbench_rightprebench7_path = r'./data/source_data_withoutbench_rightprebench7_4.xls'

# class_4_bench_path 减去 class_4_bench_rightprebench_path
class_4_bench_withoutpreben_equ_ben_path = r'./data/bench_data_withoutpreben_equ_ben_4.xls'
class_4_bench_withoutpreben_equ_ben2_path = r'./data/bench_data_withoutpreben_equ_ben2_4.xls'
class_4_bench_withoutpreben_equ_ben3_path = r'./data/bench_data_withoutpreben_equ_ben3_4.xls'
class_4_bench_withoutpreben_equ_ben4_path = r'./data/bench_data_withoutpreben_equ_ben4_4.xls'
class_4_bench_withoutpreben_equ_ben5_path = r'./data/bench_data_withoutpreben_equ_ben5_4.xls'
class_4_bench_withoutpreben_equ_ben6_path = r'./data/bench_data_withoutpreben_equ_ben6_4.xls'
class_4_bench_withoutpreben_equ_ben7_path = r'./data/bench_data_withoutpreben_equ_ben7_4.xls'

gaofei_path = r'./data/c2_2pl_params_with_pct_rename.xls'

source_data_ecaf_path = r'./data/new_ecaf_source_data_4.xls'

class_4_withoutbench_rightprebench7_ecaf_path = r'./data/source_data_withoutbench_rightprebench7_ecaf_4.xls'

data_all_7_path = r'./data/data_tel_crozero_7_4.xls'

# 抽回七次，并添加44段主观评测的结果
data_rightpre_7_plus_44_4_path = r'./data/source_data_rightprebench7_44_4.xls'

data_rightpre_7_plus_only_44_4_path = r'./data/source_data_rightprebench7_only44_4.xls'
data_36_4_final_path = r'./data/source_data_4_final.xls'
data_36_all_4_final_path = r'./data/source_data_all_4_final.xls'

data_path_final = r'./data/data_allfeatures_6747.xls'

###########################################################################################

## 0429 add
# 说明: 36个特征
# data_path_add_0429 = r'./data/add_0429.xls'           # 6747+45, 变化不大

## 0430 random get
# data_path_add_0429 = r'./data/add_0430_origin.xls'    # 450
# data_path_add_0429 = r'./data/add_0430_new.xls'       # 450+45

data_path_add_0429 = r'./data/add_0429.xls'  # 6700+45

# 0509 250(GaoFei) + 495
# data_path_add_0509 = r'data/add_0509_new_745.xls'  # 250+495 = 745    (read_files中处理)
# data_path_add_0509 = r'data/add_0509_new_700.xls'  # 250+450 = 700    (read_files中处理)
# data_path_add_0509 = r'data/add_0509_new_7000.xls'  # 250+6700 = 7000    (read_files中处理)
# data_path_39_250 = r'data/add_0509_39_250.xls'  # 250条 [36+pct]   # todo: 少数据
