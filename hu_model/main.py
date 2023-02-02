# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import KFold
from scipy import stats
import xlrd


def feature_normalize(dataset):
    mu = np.mean(dataset, axis=0)
    sigma = np.std(dataset, axis=0)
    return (dataset - mu) / sigma


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    score_83 = pd.read_csv('score_83.csv')
    feature_83 = pd.read_csv('feature_83.csv')
    # on 指定表的主键
    score_83 = pd.merge(score_83, feature_83, on='声音类别')
    score1_44 = pd.read_csv('score_44.csv')
    feature1_44 = pd.read_csv('feature_44up.csv')
    score1_44 = pd.merge(score1_44, feature1_44, on='声音类别')
    score2_44 = pd.read_csv('score_44.csv')
    feature2_44 = pd.read_csv('feature_44down.csv')
    score2_44 = pd.merge(score2_44, feature2_44, on='声音类别')
    feature_test = pd.read_csv('kyllin_features.csv')
    xtr_col1 = ['leq_mean', 'leq_std', 'leq_25', 'leq_median',
                'leq_75', 'leq_10_90', 'loudness_mean', 'loudness_std',
                'loudness_25', 'loudness_median', 'loudness_75',
                'loudness_10_90', 'roughness_mean', 'roughness_std',
                'roughness_25', 'roughness_median', 'roughness_75',
                'roughness_10_90', 'sharpness_mean', 'sharpness_std',
                'sharpness_25', 'sharpness_median', 'sharpness_75',
                'sharpness_10_90', 'fluct_mean', 'fluct_std', 'fluct_25',
                'fluct_median', 'fluct_75', 'fluct_10_90', 'tonality_mean',
                'tonality_std', 'tonality_25', 'tonality_median', 'tonality_75',
                'tonality_10_90']
    col_1 = ['声音类别', '吵闹度', 'leq_mean', 'leq_std', 'leq_25', 'leq_median',
             'leq_75', 'leq_10_90', 'loudness_mean', 'loudness_std',
             'loudness_25', 'loudness_median', 'loudness_75',
             'loudness_10_90', 'roughness_mean', 'roughness_std',
             'roughness_25', 'roughness_median', 'roughness_75',
             'roughness_10_90', 'sharpness_mean', 'sharpness_std',
             'sharpness_25', 'sharpness_median', 'sharpness_75',
             'sharpness_10_90', 'fluct_mean', 'fluct_std', 'fluct_25',
             'fluct_median', 'fluct_75', 'fluct_10_90', 'tonality_mean',
             'tonality_std', 'tonality_25', 'tonality_median', 'tonality_75',
             'tonality_10_90']
    score_83 = score_83[col_1]
    score1_44 = score1_44[col_1]
    score2_44 = score2_44[col_1]
    score1_44['声音类别'] = score1_44['声音类别'] + 83
    score2_44['声音类别'] = score2_44['声音类别'] + 83 + 44
    score1_44.index = score1_44.index + score_83.shape[0]
    score2_44.index = score2_44.index + score1_44.shape[0] + score_83.shape[0]
    feature_test = feature_test[xtr_col1]
    Dataset = pd.concat([score_83, score1_44, score2_44])
    Y_P = Dataset['吵闹度']
    X_p = Dataset[xtr_col1]
    X = feature_normalize(X_p)
    Y = feature_normalize(Y_P)
    X_t = (feature_test - np.mean(X_p, axis=0)) / np.std(X_p, axis=0)
    frac_prd = DecisionTreeRegressor()
    frac_prd.fit(X, Y)
    k_y = np.std(Y_P, axis=0)
    b_y = np.mean(Y_P, axis=0)
    y_test = frac_prd.predict(X_t)
    y_test = k_y * y_test + b_y
    result = pd.DataFrame(y_test)
    writer = pd.ExcelWriter('result.xlsx')
    result.to_excel(writer, float_format='%.5f')
    writer.save()
    writer.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
