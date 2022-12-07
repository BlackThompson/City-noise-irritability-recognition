# -*- coding: utf-8 -*-
# @Time : 2018/8/16 10:16 
# @Author : Zhixiang Tao 


from pylab import *
import keras
import os
import pandas as pd
import scipy.io.wavfile as wav
import numpy as np
import re


class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = {'batch': [], 'epoch': []}
        self.accuracy = {'batch': [], 'epoch': []}
        self.val_loss = {'batch': [], 'epoch': []}
        self.val_acc = {'batch': [], 'epoch': []}

    def on_batch_end(self, batch, logs={}):
        self.losses['batch'].append(logs.get('loss'))
        self.accuracy['batch'].append(logs.get('acc'))
        self.val_loss['batch'].append(logs.get('val_loss'))
        self.val_acc['batch'].append(logs.get('val_acc'))

    def on_epoch_end(self, batch, logs={}):
        self.losses['epoch'].append(logs.get('loss'))
        self.accuracy['epoch'].append(logs.get('acc'))
        self.val_loss['epoch'].append(logs.get('val_loss'))
        self.val_acc['epoch'].append(logs.get('val_acc'))

    def loss_plot(self, loss_type):
        iters = range(len(self.losses[loss_type]))
        plt.figure()
        # acc
        plt.plot(iters, self.accuracy[loss_type], 'r', label='train acc')
        # loss
        plt.plot(iters, self.losses[loss_type], 'g', label='train loss')
        if loss_type == 'epoch':
            # val_acc
            plt.plot(iters, self.val_acc[loss_type], 'b', label='val acc')
            # val_loss
            plt.plot(iters, self.val_loss[loss_type], 'k', label='val loss')
        plt.grid(True)
        plt.xlabel(loss_type)
        plt.ylabel('acc-loss')
        plt.legend(loc="upper right")
        plt.show()


def normal_label(label, n_class):
    labels = np.zeros((label.shape[0], n_class), dtype=np.int)
    for i in range(label.shape[0]):
        labels[i][int(label[i] - 1)] = 1
    return labels


def get_distence(dest_path, save_path):
    filelist = os.listdir(dest_path)
    dict_path = r'F:\tao_data\soundscape/44-702和剪切位置.xls'
    dict_data = pd.read_excel(dict_path)
    # print(dict_data[['剪切位置','对应名称']])
    dict = list(dict_data['对应名称'])
    # vec1 = np.array( [2,2])
    # vec2 = np.array([2,3])
    # print(vec1)
    #
    # distence  = np.linalg.norm(vec1 - vec2)
    # print(distence)
    name_dict = []
    for file in dict:
        f = file.split('-')[0]
        for file_all in filelist:
            # flag = True
            fa = file_all.split('-')[0]
            if fa == f:
                thiswav = [file]
                thiswav.extend([file_all])
                # flag = False
                name_dict.append(thiswav)
    name_dict.sort(key=lambda x: int(re.split('[-.]', x[0])[0]))
    # print(name_dict)

    distence_list = []
    for line in name_dict:
        orgin_path = os.path.join(dest_path, line[0])
        other_path = os.path.join(dest_path, line[1])
        _, orgin_wavdata = wav.read(orgin_path)
        _, other_wavdata = wav.read(other_path)
        # print(other_wavdata.shape[0])
        # if other_wavdata.shape[0] != orgin_wavdata.shape[0]:
        #     print(other_wavdata.shape,orgin_wavdata.shape)
        distence = np.linalg.norm(orgin_wavdata - other_wavdata)
        line.extend([round(distence, 2)])
        # print(distence)
        distence_list.append(line)
    distence_list = np.array(distence_list)
    print(distence_list)

    # file_path = os.path.join(dest_path,file)
    #     sample_rate, wavdata = wav.read(file_path)
    #     print(len(wavdata))
    #     print(file, file in dict)


if __name__ == '__main__':
    dest_44_path = r'F:\tao_data\data_soundscape\44-L-resample-25s'
    save_path = r'F:\tao_data\data_soundscape'
