# -*- coding: utf-8 -*-
# @Time : 2019/5/13 16:31 
# @Author : Zhixiang Tao 
import pandas as pd
from config import *


def update_drop():
    id_label_path = r'./data/id_label.csv'
    class_4_36_path = r'./data/new_source_data_4.xls'
    drop_path = r'./drop_file_name.xls'

    drop_data = pd.read_excel(drop_path)
    id_label_data = pd.read_csv(id_label_path, usecols=['id', 'label44'])
    id_label = id_label_data.values.tolist()
    # print(drop_data)
    # drop_file  fetures_number  class   498-L-6.wav

    # print(drop_data)
    # print(id_label_data)
    # #  id  label44

    id_label_dict = dict()
    for id_l in id_label:
        id_label_dict[id_l[0]] = id_l[1]

    data = []
    for index, row in drop_data.iterrows():
        file_index = int(row['drop_file'].split('-')[0])
        r = row.values.tolist()
        r.extend([dict44_4[id_label_dict[file_index]]])
        data.append(r)

    new_drop_path = r'./drop_data_file.xls'
    data = pd.DataFrame(data, columns=['drop_file', 'fetures_number', 'class', 'new_class'])
    data.to_excel(new_drop_path, index=False)
    print(data)


def up_new_source_data_4():
    id_label_path = r'./data/id_label.csv'

    id_label_data = pd.read_csv(id_label_path, usecols=['id', 'label44'])
    id_label = id_label_data.values.tolist()
    id_label_dict = dict()
    for id_l in id_label:
        id_label_dict[id_l[0]] = id_l[1]

    class_4_36_path = r'./data/new_source_data_4.xls'
    new_drop_path = r'./drop_data_file.xls'
    source_data = pd.read_excel(class_4_36_path)

    #
    data = []
    for index, row in source_data.iterrows():
        file_index = int(row['25s文件'].split('-')[0])
        row['level'] = dict44_4[id_label_dict[file_index]]
        r = row.values.tolist()
        data.append(r)

    new_source_path = r'./data/no_bench_new_source_data_4.xls'
    data = pd.DataFrame(data, columns=source_data.columns.values.tolist())
    data.to_excel(new_source_path, index=False)
    print(data)


def updata_new_source_data_4():
    class_4_36_path = r'./data/new_source_data_4.xls'
    new_drop_path = r'./drop_data_file.xls'
    source_data = pd.read_excel(class_4_36_path)
    drop_data = pd.read_excel(new_drop_path)
    # source_data[source_data['25s文件']==drop_data['drop_file']]['level'] =drop_data[source_data['25s文件']==drop_data['drop_file']]['new_class']
    # print(source_data)
    data = []
    for index, row in source_data.iterrows():
        if row['25s文件'] in drop_data['drop_file'].values:
            # print(row['level'],end='---')
            if drop_data[row['25s文件'] == drop_data['drop_file']]['fetures_number'].values[0] > 10:
                row['level'] = drop_data[row['25s文件'] == drop_data['drop_file']]['new_class'].values[0]
            # print(row['level'])
        r = row.values.tolist()
        data.append(r)

    new_source_path = r'./data/updata_10_new_source_data_4.xls'
    data = pd.DataFrame(data, columns=source_data.columns.values.tolist())
    # data.to_excel(new_source_path, index=False)
    # print(data)


if __name__ == '__main__':
    # update_drop()
    # updata_new_source_data_4()
    up_new_source_data_4()
