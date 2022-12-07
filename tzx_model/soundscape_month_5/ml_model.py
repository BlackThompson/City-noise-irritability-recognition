# -*- coding: utf-8 -*-
# @Time : 2019/3/30 13:27 
# @Author : Zhixiang Tao

"""
此模块为更新后常规机器学习模块
"""
import joblib

from config import *
import pickle
import numpy as np
from get_data import *
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.multiclass import OneVsRestClassifier
# from xgboost.sklearn import XGBClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.svm import SVC
import sklearn.metrics as metrics
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
# from tool_kit import LossHistory
import matplotlib.pyplot as plt
# from xgboost import plot_importance
import warnings

# import joblib
# from mlxtend.classifier import StackingClassifier

warnings.filterwarnings("ignore")


def plot_confusion_matrix(cm, labels_name, title):
    cm = cm.astype('float') / cm.sum(axis=1)[:np.newaxis]
    plt.imshow(cm)
    plt.title(title)
    plt.colorbar()
    num_local = np.array(range(len(labels_name)))
    plt.xticks(num_local, labels_name, rotation=90)
    plt.yticks(num_local, labels_name)
    plt.ylabel('True label')
    plt.xlabel('predicted label')


def classifier(nb_class):
    """
    分类器集合
    :return:分类器列表
    """
    clf = [
        KNeighborsClassifier(nb_class),  # 0.68
        DecisionTreeClassifier(max_depth=40),  # 0.69
        SVC(C=10, kernel='rbf', class_weight={1: 8, 2: 4, 3: 1, 4: 10}),  # 0.42
        ExtraTreesClassifier(n_estimators=80, max_depth=24, min_samples_split=3, max_features='auto', random_state=0),
        # 0.825
        # 'max_depth': 21, 'min_samples_split': 2, 'n_estimators': 95}
        RandomForestClassifier(n_estimators=95, max_depth=21, min_samples_split=2, random_state=0),  # 0.758
        # 'max_depth': 11, 'n_estimators': 110
        # XGBClassifier(n_estimators=110, max_depth=11, learning_rate=0.001, objective='multi:softmax', nb_class=4),
        LogisticRegression(penalty='l2', class_weight='balanced', solver='lbfgs')]  # 0.45

    return clf


def run(data_path=class_4_36_path, columns_name=column_36, train_test_rate=0.3, drop_outliers=True,
        drop_feature_n=1, n_components=2):
    """
    :param data_path: 数据路径
    :param drop_outliers: 是否去除离群点
    :param drop_feature_rate: 样本有在超过drop_feature_rate的特征上被判定为了离群点，将去去除
    :return:
    """
    x_train, x_test, y_train, y_test = get_data(data_path=data_path,
                                                columns_name=columns_name,
                                                train_test_rate=train_test_rate,
                                                drop_outliers=drop_outliers,
                                                drop_feature_n=drop_feature_n,
                                                n_components=n_components)  # 获取数据
    print('分类器中训练集的shape： ', x_train.shape)
    print('测试集的shape: ', x_test.shape)
    x = np.concatenate([x_train, x_test], axis=0)
    y = np.concatenate([y_train, y_test], axis=0)
    y = np.reshape(y, (y.shape[0],))

    y_train = np.reshape(y_train, (y_train.shape[0],))
    y_test = np.reshape(y_test, (y_test.shape[0],))

    nb_feature = x_train.shape[1]  # 特征数
    nb_class = len(list(set(i for i in y_train)))  # 类别数

    # print("***************************",nb_class)

    clf_list = classifier(nb_class)

    # 0: KNN    1: 决策树    2: SVC
    # 3: 极端树  4: 随机森林  5: LogisticRegression
    clf = clf_list[0]

    # 网格化调参，寻找最优参数
    # param_test = {'n_estimators': range(60, 120, 5), 'max_depth': range(5, 50,2)}#, 'min_samples_split': range(2, 10)
    # gsearch = GridSearchCV(estimator=clf, param_grid=param_test, scoring='accuracy')
    # gsearch.fit(x, y)
    # print(gsearch.best_params_, gsearch.best_score_)

    clf.fit(x_train, y_train)
    # joblib.dump(clf, r'./model/model_24_02.pkl')

    # 读取模型
    joblib.dump(clf, r'./model/model_0516.pkl')
    pre = clf.predict(x_test)

    # print(pre)
    # 0509 插一段val
    # data = pd.read_excel('./data/gaofei_36.xls').loc[:, column_36[:-1]]
    data = pd.read_excel('./data/add_test_45.xls').loc[:, column_36[:-1]]

    # print(pd.read_excel('./data/gaofei_36.xls').loc[:, ['level']])
    output = clf.predict(data)
    print(output)
    print("一共", len(output), "条")

    target_names = ['1', '2', '3', '4']
    met = metrics.classification_report(y_test, pre, target_names=target_names, digits=3)
    print(met)
    accuracy = clf.score(x_test, y_test)
    print('acc: ', accuracy)
    pickle.dump(met, open('met.txt', 'wb'))
    # d = pickle.load(open('met.txt', 'rb'))
    # print(d)

    # cm = confusion_matrix(y_test,pre)
    # print(cm)
    # plot_confusion_matrix(cm,target_names,'Confusion Matrix')
    # plt.show()

    # bench_data_x, bench_data = det_bench_data(columns_name)
    # pre_bench = clf.predict(bench_data_x)
    # bench_data['pre_3_36']=pre_bench
    # # d = bench_data[bench_data['level'] == bench_data['pre_class']]
    # d = pd.DataFrame(pre_bench)

    # print(bench_data)
    # bench_data.to_excel(r'./data/gaofei250_3_36.xls',index=False)
    # bench_data.to_excel(r'./data/preben_feature7.xls',index=False)
    # print(bench_data[bench_data['level'] ==bench_data['pre_class']])


if __name__ == '__main__':
    # run(data_path=data_36_4_final_path, columns_name=column_36, train_test_rate=0.1, drop_outliers=True,
    #     drop_feature_n=1, n_components=30)
    run(data_path=data_path_add_0429, columns_name=column_36, train_test_rate=0.3, drop_outliers=False,
        drop_feature_n=1, n_components=30)
# print(pd.read_excel(data_all_7_path)[column_36])
# 特征data_36_4_final_path
# column_yu_1
# 1
# column_nn
# 4 column_one_pctn_pctu_pctm_high
# 5 column_feature_4_nonezero
# 7 column_feature_4_nonezero_none_inOnePca

# 路径
# class_4_36_path
# data_all_path
# data_rightpre_7_plus_44_4_path
# 3 class_4_withoutbench_rightprebench7_path
# 2 class_4_withoutbench_rightprebench_path
# 1 class_4_withoutbench_path
# data_all_7_path
# data_rightpre_7_plus_only_44_4_path
# data_36_all_4_final_path

# 2 column_none_zero  ---------------------
# 3 column_36_none_highcor

# 5 column_one_pctn_pctu_pctm_high_none_highcor


# 6 column_feature_4_nonezero_nonehigh


# 8 column_feature_4_high
# 9 column_feature_4_high__nonehigh
# 10 column_feature_4_high_none _inOnePca
