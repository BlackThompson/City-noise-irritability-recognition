# -*- coding: utf-8 -*-
# @Time : 2019/5/13 10:26 
# @Author : Zhixiang Tao 

from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras.optimizers import adam_v2, rmsprop_v2


def model_all_features_and_f4(nb_feature, nb_class):
    """
    输入为n个特征
    :param nb_feature:特征个数
    :param nb_class: 类别个数
    :return: 模型
    """
    model = Sequential()
    # 添加输入层
    model.add(Dense(11, activation='relu', input_shape=(nb_feature,)))
    # model.add(Dense(24, activation='relu'))
    # 添加输出层
    model.add(Dense(nb_class, activation='softmax'))
    optimizer = rmsprop_v2.RMSprop(lr=0.005, decay=1e-6)
    # optimizer = Adam(lr=0.001, decay=1e-6)
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])  # 编译模型

    return model


def model_features_2(nb_feature, nb_class):
    """
    输入为36个特征
    :param nb_feature:特征个数
    :param nb_class: 类别个数
    :return: 模型
    """
    model = Sequential()
    # 添加输入层
    model.add(Dense(52, activation='relu', input_shape=(nb_feature,)))
    model.add(Dense(18, activation='relu'))
    # 添加输出层
    model.add(Dense(nb_class, activation='softmax'))
    optimizer = rmsprop_v2.RMSprop(lr=0.005, decay=1e-6)
    # optimizer = Adam(lr=0.001, decay=1e-6)
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])  # 编译模型

    return model


def model_features_3_5_6(nb_feature, nb_class):
    """
    输入为36个特征
    :param nb_feature:特征个数
    :param nb_class: 类别个数
    :return: 模型
    """
    model = Sequential()
    # 添加输入层
    model.add(Dense(8, activation='relu', input_shape=(nb_feature,)))
    model.add(Dense(8, activation='relu'))
    # 添加输出层
    model.add(Dense(nb_class, activation='softmax'))
    optimizer = rmsprop_v2.RMSprop(lr=0.005, decay=1e-6)
    # optimizer = Adam(lr=0.001, decay=1e-6)
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])  # 编译模型

    return model
