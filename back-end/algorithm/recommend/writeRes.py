# 一次性文件
from utils.dao import db_utils
import preproccess

#TODO: 获取所有人的名字
allName =db_utils.get_all_name_en()

# 计算两个人的相似度并写入文件：allSim.txt
def writeFileSim(user1, user2):
    with open('res/allSim.txt', 'a', encoding='utf-8') as f:
        f.write(user1 + ' ' + user2 + ' ' + str(preproccess.get_similarity(user1, user2)) + '')
        f.close()

# 计算两个人的相似度并写入数据库
def writeDBSim(user1, user2):
    db_utils.write_similarity(user1, user2, preproccess.get_similarity(user1, user2))
