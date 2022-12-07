# -*- coding: utf-8 -*-
# @Time : 2019/5/14 10:49
# @Author : Zhixiang Tao 
import pandas as pd
import numpy as np
from config import *


def split_bench():
    # class_4_36_path = r'./data/no_bench_new_source_data_4.xls'
    # bench_path = r'./data/benchmarking_id_level.csv'
    # df = pd.read_excel(class_4_36_path)#6747
    # bench_df = pd.read_csv(bench_path)#2290、2281/2274
    # # print(bench_df['id'])
    # # df.drop(df[df['25s文件']==bench_df['id']])
    # bench_data= df[df['25s文件'].isin(bench_df['id'].values.tolist())]
    # no_bench_data = df[-df['25s文件'].isin(bench_df['id'].values.tolist())]
    #
    #
    # bench_data.to_excel('./data/bench_data.xls',index=False)
    # no_bench_data.to_excel('./data/source_data_withoutbench_4.xls', index=False)
    #
    # print(bench_data)

    # class_4_withoutbench_path预测class_4_bench_path，和原标签一致，保留['25s文件']
    # class_4_bench_rightprebench_path = r'./data/preben_equ_ben3.xls'
    df = pd.read_excel(class_4_bench_withoutpreben_equ_ben6_path)
    rightprebench_df2 = pd.read_excel(class_4_bench_rightprebench6_path)
    df_withou_rightprebench_df = df[-df['25s文件'].isin(rightprebench_df2['25s文件'].values.tolist())]
    df_withou_rightprebench_df.to_excel('./data/bench_data_withoutpreben_equ_ben7_4.xls', index=False)

    print(df_withou_rightprebench_df)


if __name__ == "__main__":
    pass
    # ['海浪声','流水声',, '风声', '雨声','鸟鸣虫叫': 1, '生活声': 2, '渔艇声': 3, : 4, '渔艇': 5, '水声': 6: 7, '流水声': 8
    #  '汽车声': 9, '虫鸣': 10, '生活声(狗吠声）': 11, '生活声(打球声)': 12, '虫鸣蛙叫': 13: 14
    #  '活动声（打球）': 15, '音乐声': 16, '施工声': 17, '机器声': 18, '飞机声': 19, '歌声': 20, '活动声(打球声)': 21
    #  '施工机器声'：22，'生活声(连续敲击声)'：23, '其他机器声': 24, '生活声（商业活动）': 25, '生活声（广播）': 26
    # ]
    # r'./data/preben_feature7.xls'
    # update_drop()
    # updata_new_source_data_4()
    # split_bench()

    # # pct = ['25s文件','pctn','pctu','pctm']
    # data_all = pd.read_excel('./data/bench_pct_soundsource1.xls')
    # # print(data_all)
    # preben_feature = pd.read_excel(r'./data/preben_feature5.xls')
    # data= pd.merge(preben_feature,data_all,right_on='25s文件',left_on='25s文件',copy=False)
    # data.to_excel('./data/preben_feature5_all.xls', index=False)
    #
    # print(data)
    # if 0:
    #     print('nihao')

    # r'preben_feature_1'
    # df_6747 = pd.read_excel(no_bench_10class_4_36_path)  # 6747
    # df_5639 = pd.read_excel(class_4_withoutbench_rightprebench3_path)  # 5639
    # i =1
    # df_6747 = df_6747[ -(df_6747['25s文件'] =='702-L-11.wav')]
    # df_6747 = df_6747[-( df_6747['25s文件'] == '702-L-10.wav')]
    # print(df_6747)
    # for _, row in df_5639.iterrows():
    #     if row['level'] != df_6747[df_6747['25s文件'] == row['25s文件']]['level'].values[0]:
    #         print(i,row['25s文件'])
    #         i+=1
    #     # print(df_6747[df_6747['25s文件'] == row['25s文件']]['level'].values[0])
    #
    # # print(df_5639[-df_5639['25s文件'].isin(rightprebench_df2['25s文件'].values.tolist())])

    # df = pd.read_excel(class_4_withoutbench_rightprebench2_path)
    # print(len(set(df['25s文件'].values.tolist())))
