import config
from xingchen_model.config import cfg
import pandas as pd
from sklearn.preprocessing import normalize

import numpy as np
from collections import Counter
from config import *
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.multiclass import OneVsRestClassifier
from xgboost.sklearn import XGBClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.svm import SVC
import sklearn.metrics as metrics
from sklearn.linear_model import LogisticRegression
# from tool_kit import LossHistory
# import matplotlib.pyplot as plt
# from xgboost import plot_importance
import warnings
from xingchen_model.config import cfg
# from mlxtend.classifier import StackingClassifier

from model.pre_dadta.prepeocess_data import drop_outliers, get_data_with_drop_outliers, get_trian_test_not_avg
import pandas as pd


def normal_label(label, n_class):
    labels = np.zeros((label.shape[0], n_class), dtype=np.int)

    for i in range(label.shape[0]):
        labels[i][int(label[i] - 1)] = 1

    return labels


def classifier(nb_class):
    '''
    分类器集合
    :return:分类器列表
    '''
    clf = [
        KNeighborsClassifier(nb_class),
        DecisionTreeClassifier(max_depth=40),
        SVC(kernel='poly', degree=5),
        ExtraTreesClassifier(n_estimators=80, max_depth=15, min_samples_split=3, max_features='auto',
                             random_state=0),
        RandomForestClassifier(n_estimators=80, max_depth=20, min_samples_split=2, random_state=0),
        # XGBClassifier(n_estimators=80, max_depth=20, learning_rate=0.01, objective='multi:softmax', nb_class=4),
        LogisticRegression(penalty='l2', class_weight='balanced', solver='lbfgs')]

    return clf


def train(train_x, train_y, test_x, test_y):
    print("训练集样本数：", len(train_x), "---测试集样本数：", len(test_x))

    train_x, train_y = np.array(train_x), np.array(train_y)
    test_x, test_y = np.array(test_x), np.array(test_y)
    # 规范化
    # train_x = normalize(train_x, norm='l2')
    # test_x = normalize(test_x, norm='l2')

    nb_feature = train_x.shape[1]  # 特征数
    nb_class = len(list(set(i for i in train_y)))  # 类别数
    print("特征数", nb_feature, "类别数", nb_class)
    clf_list = classifier(nb_class)
    # clf = clf_list[3]
    param_test = {'n_estimators': range(50, 150, 10), 'max_depth': range(10, 30), 'min_samples_split': range(2, 10)}
    clf_list = classifier(nb_class)
    clf = clf_list[4]
    # clf = StackingClassifier(classifiers=[clf_list[2],clf_list[4],clf_list[5]],meta_classifier=clf_list[3])
    # gsearch = GridSearchCV(estimator=clf,param_grid=param_test,scoring='accuracy')
    # gsearch.fit(x,y)
    # print(gsearch.best_params_,gsearch.best_score_)

    clf.fit(train_x, train_y)

    pre = clf.predict(test_x)
    # print(pre)

    target_names = [str(i) for i in set(test_y)]
    print(pre)
    print(test_y)
    print([str(i) for i in set(train_y)])

    target_names = [str(i) for i in set(train_y)]
    met = metrics.classification_report(test_y, pre, target_names=target_names)
    print(met)
    #
    # accuracy = clf.score(x_test, y_test)
    # print(accuracy)


#
#    param_test = {'n_estimators': range(50, 150, 10), 'max_depth': range(10, 30), 'min_samples_split': range(2, 10)}
#    # clf = clf_list[3]
#    clf = StackingClassifier(classifiers=[clf_list[2],clf_list[4],clf_list[5]],meta_classifier=clf_list[3])
#    # gsearch = GridSearchCV(estimator=clf,param_grid=param_test,scoring='accuracy')
#    # gsearch.fit(x,y)
#    # print(gsearch.best_params_,gsearch.best_score_)
#
#


if __name__ == '__main__':
    # data_path = r'../../data/landscape_36x11.xlsx'
    data_path = r'../../data/landscape_36x11_category.xlsx'
    data = pd.read_excel(data_path)
    data = drop_outliers(data, drop_feature_n=1, label=cfg.featrue[0])
    # data = get_avg(data)
    x_train, y_train, x_test, y_test = get_trian_test_not_avg(data, train_test_rate=0.4, label=cfg.label.CATEGORY)
    # 1:1-6
    # 2:7-14
    # 3:15-19
    # 4:20-28
    # 5:29-33
    # 6:34-36
    # x_train, y_train = x_train[(x_train[cfg.featrue[0]] <= 6)], y_train[x_train[cfg.featrue[0]] <= 6]
    # x_test, y_test = x_test[(x_test[cfg.featrue[0]] <= 6)], y_test[x_test[cfg.featrue[0]] <= 6]
    # print(x_train)
    # print(x_test)
    # print(y_train)
    train(x_train, y_train, x_test, y_test)

    # print(x_train)
    # print(x_train[cfg.featrue[0]])
    #
    # ll = 6
    # print(x_train[x_train[cfg.featrue[0]] == ll])
    # print(y_train[x_train[cfg.featrue[0]] == ll])

    # print(set(y_test))
    # train(x_train, y_train, x_test, y_test)
    # train(train_x, train_y, test_x, test_y)

    # print(data)
    # print(cfg.featrue[0])
