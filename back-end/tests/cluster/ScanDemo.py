import numpy as np
import matplotlib.pyplot as plt
import torch
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn import metrics

UNCLASSIFIED = 0  # 点未被标记
NOISE = -1  # 噪声点标记


# 计算数据点两两之间的距离
def getDistanceMatrix(datas):  # datas 是聚类数据
    N, D = np.shape(datas)  # 读取datas的维度，维度是N x D（N指数据个数，D指特征维度）   ，shape函数用于获取矩阵的形状
    dists = np.zeros([N, N])  # zeros 函数：返回一个给定形状和类型的用0填充的数组，

    for i in range(N):
        for j in range(N):
            vi = datas[i, :]  # 切片 [开始,结束]
            vj = datas[j, :]
            dists[i, j] = np.sqrt(np.dot((vi - vj), (vi - vj)))  # 欧式距离函数,返回点与点之间距离的数组
    return dists


#  寻找以点cluster_id 为中心，eps 为半径的圆内的所有点的id
def find_points_in_eps(point_id, eps, dists):
    index = dists[point_id] <= eps  # dists[point_id] 即：point_id 与 所有点的距离
    return np.where(index)[0].tolist()  # 返回所有符合的点的集合


# 聚类扩展
# dists ： 任意数据两两之间的距离  N x N
# labs :   所有数据的标签 labs N，
# cluster_id ： 一个簇的标号
# eps ： 密度评估半径
# seeds： 用来进行簇扩展的点
# min_points： 半径内最少的点数
def expand_cluster(dists, labs, cluster_id, seeds, eps, min_points):
    i = 0
    while i < len(seeds):
        Pn = seeds[i]  # 获取一个点
        if labs[Pn] == NOISE:  # 如果是噪声点，则重新标记
            labs[Pn] = cluster_id
        elif labs[Pn] == UNCLASSIFIED:  # 如果未被标记过，则进行标记
            labs[Pn] = cluster_id
            new_seeds = find_points_in_eps(Pn, eps, dists)  # 以新点为圆心再画圈，进行扩展
            if len(new_seeds) >= min_points:  # 如果扩张的圈中数够多，则加入到seeds队列中
                seeds = seeds + new_seeds
        i += 1
        # 通过挨个标记和扩展seeds里的数字，实现聚类过程


def dbscan(datas, eps, min_points):
    dists = getDistanceMatrix(datas)  # 获取点与点之间的距离，且以二维数组的形式
    # 将所有点的标签初始化为0
    n_points = datas.shape[0]  # shape[0]指读取读取矩阵第一维的长度
    labs = [UNCLASSIFIED] * n_points

    cluster_id = 0
    # 遍历所有点
    for point_id in range(n_points):
        if labs[point_id] != UNCLASSIFIED:  # 如果被标记，则结束此次循环，表示该点已处理过
            continue  # 没有处理过，则计算寻找临近点
        seeds = find_points_in_eps(point_id, eps, dists)  # 符合条件的点存到seeds中

        if len(seeds) < min_points:  # 如果临近点过少，则标记为噪声点
            labs[point_id] = NOISE
        else:  # 否则开启新一轮扩张
            cluster_id = cluster_id + 1
            labs[point_id] = cluster_id  # 标记当前点
            expand_cluster(dists, labs, cluster_id, seeds, eps, min_points)
    return labs, cluster_id


# 绘图
# 数据  聚类结果  聚类个数
def draw_cluster(datas, labs, n_cluster):
    plt.cla()
    # 设计颜色
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, n_cluster)]  # (起点，终点，几个元素)

    # 遍历所有点的坐标
    for i, lab in enumerate(labs):
        if lab == NOISE:  # 如果是噪声点 则为黑色
            plt.scatter(datas[i, 0], datas[i, 1], s=16., color=(0, 0, 0))
        else:  # 否则，根据类别的编号，来标记颜色
            plt.scatter(datas[i, 0], datas[i, 1], s=16., color=colors[lab - 1])
    plt.show()


if __name__ == "__main__":
    ## 数据1
    # centers = [[20, 1], [-2, -1], [2, -1]]  # 三个中心点的坐标
    # # datas为样本数据集，labels_true为样本数据集的标签
    # datas, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
    #                                 random_state=0)
    # 产生一组随机数datas，中心点是centers，方差是0.4，产生750个点

    ## 数据2
    # file_name = "spiral"
    # with open(file_name+".txt","r",encoding="utf-8") as f:
    #    lines = f.read().splitlines()
    # lines = [line.split("\t")[:-1] for line in lines]
    # datas = np.array(lines).astype(np.float32)
    ###
    datas = torch.load("res/author_vec_set_2d.pt")

    # 数据正则化，让参与的数据减去均值出方差，是临均值，标准差成了1
    datas = StandardScaler().fit_transform(datas)  # 计算训练数据的均值和方差，并基于计算出来的均值和方差来转换训练数据，从而把数据转换成标准的正态分布
    eps = 0.35
    min_points = 5
    # 手动实现DBSCAN
    # dbscan算法，labs是最终结果，cluster_id是分成了多少类
    labs, cluster_id = dbscan(datas, eps=eps, min_points=min_points)
    print("labs of my dbscan")
    print(labs)

    # sklearn里的DBSCAN 算法
    # 分类器     # 半径      min_points           对datas进行聚类
    db = DBSCAN(eps=eps, min_samples=min_points).fit(datas)
    skl_labels = db.labels_
    print("labs of sk-DBSCAN")
    print(skl_labels)
    # 画出
    draw_cluster(datas, labs, cluster_id)

    # dbscan 输出，123表示聚类点，-1表示噪声点
    # sklearn 输出  012表示聚类点，-1表示噪声点

