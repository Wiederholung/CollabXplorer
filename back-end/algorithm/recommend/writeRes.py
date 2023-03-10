# 一次性文件
import torch

from utils.dao import db_utils
import preprocess

# TODO: 获取所有人的名字
allName = db_utils.get_all_name_en()


# 计算两个人的相似度并写入文件：allSim.txt
def writeFileSim():
    all_sim = torch.zeros(len(allName), len(allName))
    for i in range(len(allName)):
        for j in range(len(allName)):
            all_sim[i][j] = preprocess.get_similarity(allName[i], allName[j])
            print(all_sim[i][j])
    print(all_sim)
    # 将tensor写入文件
    torch.save(all_sim, 'res/all_sim.pt')


if __name__ == '__main__':
    writeFileSim()
