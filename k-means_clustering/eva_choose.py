# @Author : Hu

import pandas as pd
import numpy as np
from sklearn.preprocessing import scale


def ind2ij(a_ii, shape):
    ii = 0
    tempp = np.arange(shape - 1, 0, -1)
    while tempp[0:ii].sum() < a_ii:
        ii = ii + 1
    jj = a_ii - tempp[0:ii - 1].sum() + ii
    return ii, jj


def ij2ind(i2, j2, shape2):
    ai2 = 0
    if i2 == 1:
        ai2 = j2 - i2
    else:
        for i22 in range(0, i2 - 1):
            ai2 = ai2 + shape2 - i22 - 1
        ai2 = ai2 + j2 - i2
    return ai2


if __name__ == '__main__':
    feature = pd.read_excel(r'./data/feature.xls')
    dis_4 = pd.read_excel('dis_1_1.xls')
    feature_4 = feature[feature['level'] == 1]
    data_4 = feature[feature['level'] == 1]
    # data_4 = data_4.drop([2339, 3466, 6330, 6329, 6328, 6331, 6332, 6333, 6334, 6335, 6336, 6338, 6337])
    # feature_4 = feature_4.drop([3466, 6330, 2339, 6329, 6331, 6332, 6333, 6334, 6335, 6336, 6337, 6338, 6328])
    xtr_col4 = ['Leq_mean', 'Leq_std', 'Leq_25', 'Leq_median',
                'Leq_75', 'Leq_10-Leq_90', 'Loudness_mean', 'Loudness_std',
                'Loudness_25', 'Loudness_median', 'Loudness_75',
                'Loudness_10-Loudness_90', 'Roughness_mean', 'Roughness_std',
                'Roughness_25', 'Roughness_median', 'Roughness_75',
                'Roughness_10-Roughness_90', 'Sharpness_mean', 'Sharpness_std',
                'Sharpness_25', 'Sharpness_median', 'Sharpness_75',
                'Sharpness_10-Sharpness_90', 'Fluct_mean', 'Fluct_std', 'Fluct_25',
                'Fluct_median', 'Fluct_75', 'Fluct_10-Fluct_90', 'Tonality_mean',
                'Tonality_std', 'Tonality_25', 'Tonality_median', 'Tonality_75',
                'Tonality_10-Tonality_90', 'leq_w', 'leq_esm', 'sharpness_slop2', 'tonality_esm',
                'tonality_phimax', 'crz']
    dis_m = dis_4[dis_4['value'] > 44000]
    dis_m = dis_m[dis_m['value'] < 70000]
    feature_4 = feature_4[xtr_col4]
    feature_4 = feature_4.iloc[dis_m['serial'].tolist(), :]
    feature_4 = scale(feature_4)
    feature_4 = pd.DataFrame(feature_4)
    a = 0
    for i in range(0, feature_4.shape[0] - 1):
        for j in range(i + 1, feature_4.shape[0]):
            x = feature_4.iloc[i, :].values
            y = feature_4.iloc[j, :].values
            temp = np.sum((x - y) ** 2)
            a = np.hstack((a, temp))
    a_i = np.argmax(a)
    a_m = np.max(a)
    [i, j] = ind2ij(a_i, feature_4.shape[0])

    data_4.iloc[dis_m.iloc[i - 1, 0], :]
    data_4.iloc[dis_m.iloc[j - 1, 0], :]

    a = 0
    for i in range(0, feature_4.shape[0]):
        x = feature_4.iloc[i, :].values
        y = feature_4.iloc[4, :].values
        z = feature_4.iloc[39, :].values
        # yy = feature_4.iloc[21, :].values
        # zz = feature_4.iloc[16, :].values
        # y_3 = feature_4.iloc[17, :].values
        # z_3 = feature_4.iloc[25, :].values
        temp = np.sum((x - y) ** 2 + (x - z) ** 2)
        a = np.hstack((a, temp))
    a[35] = 0
    # a[20] = 0
    # a[12] = 0
    # a[17] = 0
    a_i = np.argmax(a)
    a_m = np.max(a)
    data_4.iloc[dis_m.iloc[a_i - 1, 0], :]

    data_4 = data_4.iloc[dis_4.iloc[:, 0].tolist(), :]
