from typing import Any

import pandas as pd
import numpy as np
from random import *

# 将sim.csv中数据导入OriginalSimilarity中
file_name = '../../res/all_sim-50d.csv'
OriginalSimilarity = np.array(pd.read_csv(file_name))[:, 1:]

ResultSimilarity = np.zeros((126, 126))

#上下界
DownRate = 0.15
UpRate = 0.2

# 加入随机数
for i in range(0, 126):
    for j in range(i, 126):
        flage = choice([-1,0,1])
        if flage == 1:
            ResultSimilarity[i][j] = OriginalSimilarity[i][j] * uniform(1+DownRate,1+UpRate)
        elif flage == -1:
            ResultSimilarity[i][j] = OriginalSimilarity[i][j] * uniform(1-UpRate,1-DownRate)
        else:
            ResultSimilarity[i][j] = OriginalSimilarity[i][j]

#对角线归1
for i in range(0, 126):
    ResultSimilarity[i][i] = 1

#简单归一化
#maxnumber=1.1917427432817727
#Normalisation Number = 1.21
NormalisationNumber = np.max(ResultSimilarity) + 0.02
for i in range(0, 126):
    for j in range(i+1, 126):
        ResultSimilarity[i][j] = ResultSimilarity[i][j]/NormalisationNumber

#补全矩阵
for i in range(0, 126):
    for j in range(i, 126):
        ResultSimilarity[j][i] = ResultSimilarity[i][j]

#写入文件
dataframe = pd.DataFrame(ResultSimilarity)
dataframe.to_csv('../../res/all_sim_AfterChange.csv')
