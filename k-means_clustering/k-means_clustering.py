# _*_ coding : utf-8 _*_
# @Time : 2022/11/9 14:39
# @Author : Black
# @File : k-means_clustering
# @Project : my_noise_recognize

# import numpy as np
# import pandas as pd
# import torch
#
# pd.reset_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
#
# feature = pd.read_excel(r'./input/feature.xls')
#
# # extract effective feature
# col = feature.columns[10:-1]
# feature_use = feature[col]
#
#
# # Euclidean distance
# def distEu(x, y):
#     dist_sum = np.sqrt(np.sum((x - y) ** 2))
#     return dist_sum
#
#
# # A set of K random centers of mass
# def randCenter(dataSet, k):
#     # m represents row
#     # n represents col
#     m, n = dataSet.shape
#
#     # initialize center
#     centroid = np.zeros((k, n))
#     centroid = pd.DataFrame(centroid)
#
#     # 创建质心，列名不同不能加减计算
#     centroid = centroid.set_axis(col, axis='columns')
#
#     # # traverse
#     # for i in range(k):
#     #     # index为0-m之间的随机整数
#     #     index = int(np.random.uniform(0, m))
#     #     # calculate centroid and assign
#     #     centroid.iloc[i, :] = dataSet.iloc[index, :]
#
#     index = int(np.random.uniform(0, m))
#     centroid.iloc[0, :] = dataSet.iloc[index, :]
#     centroid_0 = centroid.iloc[0, :]
#
#     # 都初始化为centroid_0
#     centroid_1 = centroid_0
#     centroid_2 = centroid_0
#     centroid_3 = centroid_0
#     max_distance = 0
#
#     for i in range(m):
#         dataSet_i = dataSet.iloc[i, :]
#         distance = distEu(centroid_0, dataSet_i)
#         if distance > max_distance:
#             centroid_1 = dataSet_i
#             max_distance = distance
#
#     centroid.iloc[1, :] = centroid_1
#
#     max_distance = 0
#
#     for i in range(m):
#         dataSet_i = dataSet.iloc[i, :]
#         distance = distEu(centroid_1, dataSet_i) + distEu(centroid_0, dataSet_i)
#         if distance > max_distance:
#             centroid_2 = dataSet_i
#             max_distance = distance
#
#     centroid.iloc[2, :] = centroid_2
#
#     max_distance = 0
#
#     for i in range(m):
#         dataSet_i = dataSet.iloc[i, :]
#         distance = distEu(centroid_1, dataSet_i) + distEu(centroid_1, dataSet_i) + distEu(centroid_0, dataSet_i)
#         if distance > max_distance:
#             centroid_3 = dataSet_i
#             max_distance = distance
#
#     centroid.iloc[3, :] = centroid_3
#
#     return centroid
#
#
# # k-means clustering
# # k-means clustering
# def KMeans(dataSet, k):
#     m = np.shape(dataSet)[0]
#
#     # 初始化一个矩阵来储存每个点的簇分配结果
#     # clusterAssment包含两列：1列记录簇索引值，2列存储当前点到簇质心的距离（用来评价聚类的效果）
#     clusterAssment = np.mat(np.zeros((m, 2)))
#     clusterChange = True
#
#     centroid = randCenter(dataSet, k)
#
#     # 初始化标志变量，用于判断迭代是否继续，如果True，则迭代继续
#     while clusterChange:
#         clusterChange = False
#
#         # 遍历所有行
#         for i in range(m):
#             # print("i:", i)
#             minDist = 10000
#             minIndex = -1
#             # 遍历所有点找到距离每个点最近的质心
#             for j in range(k):
#                 # print("j:", j)
#                 dist = distEu(centroid.iloc[j, :], dataSet.iloc[i, :])
#                 # 如果距离小于minDist，更新minDist和index索引值
#                 if dist < minDist:
#                     minDist = dist
#                     minIndex = j
#             # 如果任意一点的簇分配结果发生改变，则更新clusterChanged标志
#             # print(clusterAssment)
#             if clusterAssment[i, 0] != minIndex:
#                 clusterChange = True
#                 # 更新簇分配结果为最小质心的index，minDist
#                 clusterAssment[i, :] = minIndex, minDist
#
#         # 遍历所有质心并更新他们的取值
#         for j in range(k):
#             # 通过数据过滤来过的给定簇的所有点
#             # .A表示把矩阵转化为array的形式
#             # pointsInCluster = dataSet[np.nonzero(clusterAssment[:, 0].A == j)[0]]
#             clusterAssment = pd.DataFrame(clusterAssment)
#             same_cluster_index = clusterAssment.iloc[:, 0].isin([j])
#             pointsInCluster = dataSet[same_cluster_index]
#             # 计算所有点的均值，axis=0表示沿着列方向进行均值
#             centroid.iloc[j, :] = np.mean(pointsInCluster, axis=0)
#             # print("*******************************************")
#         clusterAssment = np.matrix(clusterAssment)
#
#     print("Cluster complete!")
#     return centroid, clusterAssment
#
#
# k = 4
# feature_test = feature_use.iloc[:100]
# centroids, clusterAssment = KMeans(feature_test, k)
#
# clusterAssment = pd.DataFrame(clusterAssment)
# print(centroids)
# print(clusterAssment)
#
# clusterAssment.columns = ['level', 'distance']
# centroids.to_csv(r"./output/centroids.csv")
# clusterAssment.to_csv(r"./output/clusterAssment.csv")

from numpy import random
import numpy as np
import pandas as pd

# 不用dataframe，只用ndarray
# 计算速度：ndarray > Series > list > DataFrame

pd.reset_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
feature = pd.read_excel(r'./input/feature.xls')
# col = feature.columns[10:-1]
col = ['Leq_mean', 'Leq_std', 'Leq_25', 'Leq_median',
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
name = feature.columns[1]
# col = np.insert(col, 0, name)
feature_use = feature[col]
name_list = feature[name]
k = 4

feature_use = feature_use.to_numpy()


# 计算两点的欧氏距离
def Euclidean_distance(x, y):
    distance = np.sqrt(np.sum((x - y) ** 2))
    return distance


# 聚类取平均值，用于计算更新聚类点
def cluster_mean(cluster):
    return np.mean(cluster, axis=0)


# 对数据进行正态——标准化
def feature_normalize(dataset):
    mu = np.mean(dataset, axis=0)
    sigma = np.std(dataset, axis=0)
    return (dataset - mu) / sigma


# 找到初始聚类点
def init_centroid(dataset):
    # 特征总数，即列数
    feature_num = dataset.shape[1]
    # 声音片段总数，即行数
    voice_num = dataset.shape[0]

    # 第一个聚类点随机选取
    # 之后每个聚类点取到之前距离最大的点

    # centroid = np.zeros((4, feature_num))
    #
    # index = int(np.random.uniform(0, voice_num))
    # centroid[0, :] = dataset[index, :]
    # centroid_0 = centroid[0, :]

    centroid = np.zeros((4, feature_num))

    # 找到一个比较偏远的值，离中心点的距离20左右

    # centroid[0, :] = cluster_mean(dataset)
    # centroid_0 = centroid[0, :]
    # centroid[0, :] = dataset[3036, :]
    # centroid[0, :] = dataset[4067, :]
    # centroid[0, :] = dataset[241, :]

    # 209-L-5.wav
    # centroid[0, :] = dataset[1161, :]

    # 673-L-5.wav
    centroid[0, :] = dataset[6352, :]

    centroid_0 = centroid[0, :]

    centroid_1 = centroid_0
    centroid_2 = centroid_0
    centroid_3 = centroid_0
    max_distance = 0

    for i in range(voice_num):
        dataset_i = dataset[i, :]
        distance = Euclidean_distance(centroid_0, dataset_i)
        if distance > max_distance:
            centroid_1 = dataset_i
            max_distance = distance

    centroid[1, :] = centroid_1
    max_distance = 0

    for i in range(voice_num):
        dataset_i = dataset[i, :]
        distance = Euclidean_distance(centroid_0, dataset_i) + Euclidean_distance(centroid_1, dataset_i)
        if distance > max_distance:
            centroid_2 = dataset_i
            max_distance = distance

    centroid[2, :] = centroid_2
    max_distance = 0

    for i in range(voice_num):
        dataset_i = dataset[i, :]
        distance = Euclidean_distance(centroid_0, dataset_i) \
                   + Euclidean_distance(centroid_1, dataset_i) + \
                   Euclidean_distance(centroid_2, dataset_i)
        if distance > max_distance:
            centroid_3 = dataset_i
            max_distance = distance

    centroid[3, :] = centroid_3

    return centroid


def Kmeans(dataset):
    # 特征总数，即列数
    feature_num = dataset.shape[1]
    # 声音片段总数，即行数
    voice_num = dataset.shape[0]

    # 初始化一个矩阵来储存每个点的簇分配结果
    # clusterAssment包含两列：1列记录簇索引值，2列存储当前点到簇质心的距离（用来评价聚类的效果）
    # 全部置为-1，因为有0类点
    cluster_assessment = np.ones((voice_num, 2))
    cluster_assessment = -cluster_assessment
    cluster_change = True

    centroid = init_centroid(dataset)

    # 初始化标志变量，用于判断迭代是否继续，如果True，则迭代继续
    while cluster_change:
        cluster_change = False

        # 遍历所有行
        for i in range(voice_num):
            min_distance = 10000
            # 距离最近的聚类点的索引（0,1,2,3)
            min_index = -1

            # 遍历寻找距离每个点最近的质心
            for j in range(k):
                distance = Euclidean_distance(centroid[j, :], dataset[i, :])
                # 如果距离小于minDist，更新minDist和index索引值
                if distance < min_distance:
                    min_distance = distance
                    min_index = j

            # 如果有任意一点的簇分配结果改变，则更新cluster_change为True
            if cluster_assessment[i, 0] != min_index:
                cluster_change = True
                cluster_assessment[i, :] = min_index, min_distance

        # 遍历所有质心，更新取值
        for i in range(k):
            # 获取相同簇质心的所有点，取均值更新簇质心
            same_cluster_index = (cluster_assessment[:, 0] == i)
            points_same_cluster = dataset[same_cluster_index]
            centroid[i, :] = cluster_mean(points_same_cluster)

            # print("*******************************************************")
            # print(centroid)

    print("Cluster complete!")
    return centroid, cluster_assessment


if __name__ == '__main__':
    # feature_test = feature_use[:1000]
    # outlier_index = [6, 14, 114, 115, 119, 158, 165, 177, 187, 193,
    #                  195, 197, 198, 653, 800, 1096, 1100, 1255, 1256, 1257,
    #                  1258, 1263, 1266, 1269, 1297, 1342, 1343, 1350, 1353, 2017,
    #                  2091, 2436, 3039, 3105, 3106, 3108, 4071, 4072, 4073, 4074,
    #                  4075, 4076, 4077, 4078, 4079, 4080, 4081, 5216, 5217, 5221,
    #                  5222, 5223, 5224, 5225, 5304, 5305, 5308, 5311, 5312, 5313,
    #                  5689]

    # outlier_index = [14, 16, 17, 114, 115, 137, 165, 187, 354, 653,
    #                  1577, 2427, 2428, 2434, 2436, 2772, 2793, 2841, 2978, 3108,
    #                  3848, 3849, 3850, 3851, 3852, 3854, 3855, 3856, 3857, 3858,
    #                  3859, 3878, 4071, 4073, 4074, 4075, 4076, 4080, 4501, 4551,
    #                  4717, 5217, 5221, 5223, 5224, 5304, 5311, 5312, 5313, 5692,
    #                  5694, 5695, 5696, 5699, 6598]

    outlier_index = [76, 77, 114, 115, 146, 147, 161, 162, 187, 205,
                     206, 236, 237, 244, 245, 1096, 1098, 1099, 1100, 1175,
                     1183, 1188, 1254, 1255, 1256, 1257, 1258, 1263, 1265, 1266,
                     1267, 1268, 1269, 1270, 1274, 1342, 1343, 1346, 1348, 1349,
                     1350, 1353, 2017, 3039, 4071, 4072, 4073, 4074, 4075, 4076,
                     4077, 4078, 4079, 4080, 4081, 5216, 5217, 5221, 5222, 5223,
                     5224, 5225, 5304, 5305, 5307, 5308, 5309, 5311, 5312, 5313]

    feature_use = np.delete(feature_use, outlier_index, axis=0)
    # name_list从series转化为ndarray
    name_list = name_list.values
    name_list = np.delete(name_list, outlier_index, axis=0)

    # 将feature_use进行正态标准化处理
    feature_use = feature_normalize(feature_use)

    # 进行K聚类
    centroids, clusterAssment = Kmeans(feature_use)

    # print(centroids)
    # print("*******************************************************")
    # print(clusterAssment)

    clusterAssment = pd.DataFrame(clusterAssment)
    centroids = pd.DataFrame(centroids)
    name_list = pd.DataFrame(name_list)

    name_list.columns = ['25s_file_name']
    clusterAssment.columns = ['level', 'distance']
    clusterAssment = pd.concat([name_list, clusterAssment], axis=1)
    # col = feature.columns[10:-1]
    centroids.columns = col
    centroids.to_csv(r"./output/centroids_42_features.csv")
    clusterAssment.to_csv(r"./output/clusterAssment_42_features.csv")
