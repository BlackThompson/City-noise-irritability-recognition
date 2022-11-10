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
col = feature.columns[10:-1]
feature_use = feature[col]
k = 4

feature_use = feature_use.to_numpy()


# 计算两点的欧氏距离
def Euclidean_distance(x, y):
    distance = np.sqrt(np.sum((x - y) ** 2))
    return distance


# 聚类取平均值，用于计算更新聚类点
def cluster_mean(cluster):
    return np.mean(cluster, axis=0)


# 找到初始聚类点
def init_centroid(dataset):
    # 特征总数，即列数
    feature_num = dataset.shape[1]
    # 声音片段总数，即行数
    voice_num = dataset.shape[0]

    # 第一个聚类点随机选取
    # 之后每个聚类点取到之前距离最大的点
    centroid = np.zeros((4, feature_num))

    index = int(np.random.uniform(0, voice_num))
    centroid[0, :] = dataset[index, :]
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
    feature_use = np.delete(feature_use, [4074, 4076, 5223, 4071, 4075, 4080, 653, 4073, 5217, 5221, 14, 3108, 187,
                                          5689, 5312], axis=0)
    centroids, clusterAssment = Kmeans(feature_use)

    # print(centroids)
    # print("*******************************************************")
    # print(clusterAssment)

    clusterAssment = pd.DataFrame(clusterAssment)
    centroids = pd.DataFrame(centroids)

    clusterAssment.columns = ['level', 'distance']
    col = feature.columns[10:-1]
    centroids.columns = col
    centroids.to_csv(r"./output/centroids.csv")
    clusterAssment.to_csv(r"./output/clusterAssment.csv")
