import db_connetor
from Utils import updateUtils
# 连接数据库
client = db_connetor.get_connection()
db = client.bupt
collection = db.Anfu_Zhou

# #TODO: 动态更改作者aid
# #TODO: 获取abstract后，将abstract写入数据库
# data1 = {
#     "id": 92,
#     "Article": {
#         "aid2": {"title": "学科推荐系统2", "author": {"王俊翔": "02/2100", "王伊哲": "02/2100"},
#                  "url": "https://doi.org/10.1109/COMPSAC54236.2022.00123", "year": 2100, "abstract": "xxxxxx"},
#         "aid1": {"title": "学科推荐系统1", "author": {"朱子炫": "02/2100", "胡逸同": "02/2100"},
#                  "url": "https://dblp.org/pid/65/9612.xml", "year": 2100, "abstract": "xxxxxx"}
#     }
# }
# collection.insert_one(data1)
# print(data1)

if __name__ == '__main__':
    updateUtils.update_pid("Anfu_Zhou", "65/9612")

