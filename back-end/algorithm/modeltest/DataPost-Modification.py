from typing import Any

import pandas as pd
import numpy as np
from random import *

# 将sim.csv中数据导入OriginalSimilarity中
file_name = '../../res/all_sim.csv'
OriginalSimilarity = np.array(pd.read_csv(file_name))[:, 1:]

ResultSimilarity = np.zeros((126, 126))

# 加入随机数
for i in range(0, 126):
    for j in range(i, 126):
        flage = choice([-1,0,1])
        if flage == 1:
            ResultSimilarity[i][j] = OriginalSimilarity[i][j] * uniform(1.15,1.2)
        elif flage == -1:
            ResultSimilarity[i][j] = OriginalSimilarity[i][j] * uniform(0.75,0.8)
        else:
            ResultSimilarity[i][j] = OriginalSimilarity[i][j]

for i in range(0, 126):
    ResultSimilarity[i][i] = 1

#maxnumber=1.1917427432817727
#Normalisation Number = 1.21
NormalisationNumber = 1.21
for i in range(0, 126):
    for j in range(i+1, 126):
        ResultSimilarity[i][j] = ResultSimilarity[i][j]/1.21

for i in range(0, 126):
    for j in range(i, 126):
        ResultSimilarity[j][i] = ResultSimilarity[i][j]

dataframe = pd.DataFrame(ResultSimilarity)
dataframe.to_csv('../../res/all_sim_AfterChange.csv')
