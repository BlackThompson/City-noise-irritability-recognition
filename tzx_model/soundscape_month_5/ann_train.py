# -*- coding: utf-8 -*-
# @Time : 2019/3/24 23:29 
# @Author : Zhixiang Tao 
"""
 此模块为ANN模块
"""
from get_data import *
from config import *
import numpy as np
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import GridSearchCV
import sklearn.metrics as metrics
from sklearn.preprocessing import OneHotEncoder
from matplotlib import pyplot as plt
from tool_kit import LossHistory
from ann_models import *


def plot_history(history):
    # 绘制acc - loss曲线
    plt.figure(1)
    tran_loss = history['loss']
    val_loss = history['val_loss']
    train_acc = history['acc']
    val_acc = history['val_acc']
    epochs = range(1, len(tran_loss) + 1)

    plt.plot(epochs, tran_loss, 'r', label='Training loss')
    plt.plot(epochs, val_loss, 'g', label='Validation loss')
    plt.plot(epochs, train_acc, 'b', label='Training acc')
    plt.plot(epochs, val_acc, 'k', label='Validation acc')
    plt.grid(True)
    plt.title('Training and validation loss_acc')
    plt.xlabel('Epochs')
    plt.ylabel('Loss_acc')
    plt.legend()
    plt.show()


def run(data_path=class_4_36_path, columns_name=column_36, train_test_rate=0.3, drop_outliers=True,
        drop_feature_n=1, n_components=30):
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
                                                drop_feature_n=drop_feature_n, n_components=n_components)  # 获取数据
    print('分类器中训练集的shape： ', x_train.shape)
    print(y_train.shape)

    y_train = np.reshape(y_train, (-1, 1))
    y_test = np.reshape(y_test, (-1, 1))

    one_hot = OneHotEncoder(sparse=False)
    one_hot.fit(y_train)
    y_train = one_hot.transform(y_train)
    y_test = one_hot.transform(y_test)
    nb_feature = x_train.shape[1]  # 特征数
    nb_class = len(y_train[0])  # 类别数

    # 定义模型并打印出模型结构
    model = model_features_3_5_6(nb_feature, nb_class)
    print(model.summary())
    # 创建一个history实例
    # 训练模型
    history = model.fit(x_train, y_train, epochs=2000, batch_size=64, verbose=1, validation_data=[x_test, y_test])
    pre = model.predict(x_test)  # 模型预测
    pre = np.argmax(pre, 1) + 1  # 样本标签从1开始，二预测结果下标从0开始
    loss, acc = model.evaluate(x_test, y_test)
    print('acc:  ', acc)
    # 混淆矩阵

    y_test = np.argmax(y_test, 1) + 1
    target_names = ['1', '2', '3', '4', '5', '6']
    met = metrics.classification_report(y_test, pre, target_names=target_names)
    print(met)

    # 绘制acc - loss曲线
    plot_history(history.history)


if __name__ == '__main__':
    run(data_path=class_4_withoutbench_path, columns_name=column_36, train_test_rate=0.4, drop_outliers=False,
        drop_feature_n=1, n_components=30)
# up_class_4_36_path
# class_4_36_path   no_bench_10class_4_36_path

# 特征
# 1 column_36
# 2 column_none_zero
# 3 column_36_none_highcor
# 4 column_one_pctn_pctu_pctm_high
# 5 column_one_pctn_pctu_pctm_high_none_highcor
