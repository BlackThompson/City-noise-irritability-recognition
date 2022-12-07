# -*- coding: utf-8 -*-
# @Time : 2018/12/8 11:26 
# @Author : Zhixiang Tao 
import random
import pandas as pd
import numpy as np
from config import *
from sklearn.preprocessing import MultiLabelBinarizer, normalize
from collections import Counter
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as lda


def det_bench_data(column):
    # class_4_bench_withoutpreben_equ_ben7_path
    bench_data = pd.read_excel(gaofei_path)
    # print(bench_data)
    data_X = normalize(bench_data[column[:-1]], norm='l2')
    return data_X, bench_data


def normal_label(label, n_class):
    labels = np.zeros((label.shape[0], n_class), dtype=np.int)

    for i in range(label.shape[0]):
        labels[i][int(label[i] - 1)] = 1

    return labels


def get_data_with_drop_outliers(label, df, drop_feature_n, features):
    """
    Tuckey算法
    df:数据
    drop_feature_n: 阈值，某数据有drop_feature_n个特征都是离群点，就判定该数据为离群点
    feature：数据特征
    return: 返回去除离群点的数据
    """
    # print(df['25s文件'])

    # 保存包含离群点的样本索引
    outlier_indices = []
    feature_sample_list = {}

    # iterate over features(columns)
    for col in features:
        # 1st quartile (25%)
        Q1 = np.percentile(df[col], 25)
        # 3rd quartile (75%)
        Q3 = np.percentile(df[col], 75)
        # Interquartile range (IQR)
        IQR = Q3 - Q1

        # outlier step
        outlier_step = 1.5 * IQR

        # Determine a list of indices of outliers for feature col
        outlier_list_col = df[(df[col] < Q1 - outlier_step) | (df[col] > Q3 + outlier_step)].index

        # append the found outlier indices for col to the list of outlier indices
        outlier_indices.extend(outlier_list_col)
        feature_sample_list[col] = len(outlier_list_col)
    # print(feature_sample_list)

    # select observations containing more than 2 outliers
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(k for k, v in outlier_indices.items() if v >= drop_feature_n)

    df = df.drop(multiple_outliers)

    return df


def get_data_with_drop_outliers_by_class(data, drop_feature_n, features, label_column):
    """
    按类别去除离群点
    :param data: 数据
    :param drop_feature_n: 一个样本有大于等于 drop_feature_n 的特征为离群点，删除该样本
    :param features: 数据特征
    :param label_column: 类别标签
    :return: 去除；离群点后的数据
    """
    label_list = list(set(data[label_column].values))
    label_list = [1, 2, 3, 4]
    # 2_6 4_7
    # drop_feature_n = {1: 7, 2: 4, 3: 4, 4: 7}
    drop_feature_n = {1: 6, 2: 2, 3: 2, 4: 6}
    # drop_feature_n = {1: 8, 2: 7, 3: 1, 4: 3}
    # drop_feature_n = {1: 1, 2: 1, 3: 1, 4: 1}
    data_without_outliers = pd.DataFrame()
    for label in label_list:
        data_label = data[data[label_column] == label]
        data_label = get_data_with_drop_outliers(label, data_label, drop_feature_n[label], features)
        data_without_outliers = data_without_outliers.append(data_label)

    print('去除每个类别的离群点后样本数：', len(data_without_outliers), '/', len(data))
    print('每个类别的数据分布：', '\n', pd.value_counts(data_without_outliers[label_column]))

    return data_without_outliers


def train_test_split_by_class(file_name, x, y, rate):
    """
    划分测试集训练集
    :param x: 数据
    :param y: 标签
    :param rate: 抽样比例
    :return: x_train, x_test, y_train, y_test
    """

    x = np.array(x)
    y = np.asarray(y)
    file_name = np.array(file_name)

    # 获取标签种类
    # label = list(set([i[0] for i in y]))
    label = list(set(y))

    # 获取各标签索引
    index = []
    for l in label:
        index.append([inde for inde, x in enumerate(y) if x == l])

    test_index = []
    for index_i in index:
        index_i_index = list(range(len(index_i)))  # 索引的索引
        random.shuffle(index_i_index)  # 打乱生成的索引的索引
        index_i_index = index_i_index[0:int(rate * len(index_i))]
        index_i = np.asarray(index_i)
        test_index.extend(index_i[index_i_index])  # 得到测试集索引

    train_index = [i for i in range(len(y)) if i not in test_index]  # 测试集索引
    random.shuffle(train_index)
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    test_file = file_name[test_index]
    test_file = pd.DataFrame(test_file)
    # print(test_file)
    test_file.to_excel('./data/0429_test_file_model_1.xls')
    #     test_file.to_excel('./data/test_file_model_1.xls')
    return x_train, x_test, y_train, y_test


def get_data(data_path=class_4_36_path,
             columns_name=column_36,
             train_test_rate=0.3,
             drop_outliers=True,
             drop_feature_n=1,
             n_components=2):
    """
    处理数据，返回训练集，测试集
    :param data_path: 数据文件路径
    :param columns_name: 数据所需列名
    :param train_test_rate: 测试集占比
    :param drop_outliers: 布尔值，是否去除离群点
    :param drop_feature_n:  一个样本有大于等于 drop_feature_n 的特征为离群点，就删除该样本
    :return: 训练数据，测试数据，特征个数   x_train, x_test, y_train, y_test, nb_features
    """

    data = pd.read_excel(data_path)
    # data = data[columns_name]

    print('原样本总数：', len(data))
    print('每个类别的数据分布：', '\n', pd.value_counts(data[columns_name[-1]]))
    # data = data[(data['Leq_mean'] <= 70) & (data['Leq_mean'] >= 40)]
    # print('40到70之内：', len(data))
    # print('每个类别的数据分布：', '\n', pd.value_counts(data[columns_name[-1]]))

    # print(data[columns_name])
    # 对每个类别的数据做去除离群点处理
    if drop_outliers:
        features = columns_name[0:-1]
        label_column = columns_name[-1]
        data = get_data_with_drop_outliers_by_class(data, drop_feature_n, features, label_column)

    # 去除离群点后重新定义索引
    data.index = range(0, data.shape[0])
    # print(data)
    file_name = data['25s文件']
    # file_name = data['25s_file_name']
    # '25s_file_name''25s文件'
    data_X = data[columns_name[:-1]]
    data_Y = data[columns_name[-1]]

    # 规范化
    data_X = normalize(data_X, norm='l2')
    # print(data_X.shape)

    x_train, x_test, y_train, y_test = train_test_split_by_class(file_name, data_X, data_Y, train_test_rate)

    return x_train, x_test, y_train, y_test


if __name__ == '__main__':
    # # x_train, x_test, y_train, y_test, nb_features = \
    get_data(data_path=data_all_7_path,
             columns_name=column_36,
             train_test_rate=0.3,
             drop_outliers=True,
             drop_feature_n=1)
    #
    # d = pd.read_excel(class_4_all_path)
    #
    # print(d.columns.values.tolist())
    # det_bench_data(column_36)
