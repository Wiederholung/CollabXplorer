# 一次性文件
import torch

from utils.dao import db_utils
import preproccess

# TODO: 获取所有人的名字
allName = db_utils.get_all_name_en()


# 计算两个人的相似度并写入文件：allSim.txt
def writeFileSim():
    tensor = torch.zeros(len(allName), len(allName))
    count_i = 0
    count_j = 0
    for i in allName:
        for j in allName:
            tensor[count_i][count_j] = preproccess.get_similarity(i, j)
            count_j += 1
        count_i += 1
    # 将tensor写入文件
    torch.save(tensor, 'res/allSim.pt')


if __name__ == '__main__':
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    writeFileSim()
