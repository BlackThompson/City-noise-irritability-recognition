from xingchen_model.config import cfg

from collections import Counter
import numpy as np
import pandas as pd


def get_data_with_drop_outliers(label, df, drop_feature_n, features):
    """
    Tuckey算法（箱型图）
    df:数据
    drop_feature_n: 阈值，某数据有drop_feature_n个特征都是离群点，就判定该数据为离群点
    feature：数据特征
    return: 返回去除离群点的数据
    """

    # 保存包含离群点的样本索引
    outlier_indices = []

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
        # print(outlier_list_col)

        # append the found outlier indices for col to the list of outlier indices
        outlier_indices.extend(outlier_list_col)

    # select observations containing more than 2 outliers
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(k for k, v in outlier_indices.items() if v >= drop_feature_n)

    df = df.drop(multiple_outliers)

    return df


def drop_outliers(data, drop_feature_n=1, label=''):
    '''  去除离群点
    :param data: 输入数据  pandas格式
    :param drop_feature_n: 有多少个特征被判定为离群点，才将找个数据舍弃
    :param features:
    :return:
    '''
    print('去除每个类别的离群点前样本数：', len(data))

    id_list = list(set(data[label].values))

    data_without_outliers = pd.DataFrame()
    for id in id_list:
        data_id = data[data[cfg.featrue[0]] == id]
        print("去除离群点之前，ID：", id, "数据条数:", len(data_id))
        data_id = get_data_with_drop_outliers(cfg.featrue[0], data_id, drop_feature_n, cfg.featrue[1:])
        print("去除离群点后，ID：", id, "数据条数:", len(data_id))
        data_without_outliers = data_without_outliers.append(data_id)
    # data_without_outliers.to_excel(r'../../data/landscape_dropout_4.xlsx')
    print('去除每个类别的离群点后样本数：', len(data_without_outliers))
    return data_without_outliers


def get_avg(data):
    print("开始求平均值。。。")
    data_ave = pd.DataFrame()

    id_list = list(set(data[cfg.featrue[0]].values))
    for id in id_list:
        data_id = data[data[cfg.featrue[0]] == id]
        data_id = data_id.mean(axis=0)
        # print(data_id)
        data_ave = data_ave.append(data_id, ignore_index=True)
    # data_ave.to_excel(r'../../data/landscape_ave.xlsx')
    print("求平均值结束。。。。")

    return data_ave


def get_trian_test_not_avg(data, train_test_rate=0.3, label=''):
    print("开始拆分训练集和测试集，样本总数：", len(data), "。。。")

    test_index = []
    id_list = list(set(data[cfg.featrue[0]].values))
    for id in id_list:
        data_id = data[data[cfg.featrue[0]] == id]
        index_id = data_id.index
        index_id = index_id[0:int(train_test_rate * len(index_id))]
        print("ID：", id, ",总样本数:", len(data_id), ",测试样本数：", len(index_id))
        test_index.extend(index_id)  # 得到测试集索引
    train_index = [i for i in data.index if i not in test_index]  # 测试集索引
    print("結束拆分训练集和测试集。。。训练集样本总数：", len(train_index), "。。。")
    print("测试集接样本总数：", len(test_index), "。。。")

    train_data, test_data = data.loc[train_index], data.loc[test_index]
    x_train, x_test = train_data[cfg.featrue[0:]], test_data[cfg.featrue[0:]]
    y_train, y_test = train_data[label], test_data[label]

    return x_train, y_train, x_test, y_test


if __name__ == '__main__':
    data_path = r'../../data/landscape_36x11.xlsx'
    data = pd.read_excel(data_path)
    data = drop_outliers(data, drop_feature_n=1)
    # data = get_avg(data)
    # x_train, y_train, x_test, y_test = \
    get_trian_test_not_avg(data)
