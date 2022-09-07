import json
import math
import random

from pymongo import MongoClient

client = MongoClient('mongodb://rwAll:ARS 5111-rwAll'
                     '@dev.metattri.com:27017')
db = client.bupt


# 获取作者信息，只接受单一参数
def get_auth_info(id_s, name_ch, name_en, category):
    if id_s is not None:
        for col in db.list_collection_names():
            res = db[col].find_one({'id': id_s})
            if res is not None:
                return res
        return None
    elif name_ch is not None:
        for col in db.list_collection_names():
            res = db[col].find_one({'name': name_ch})
            if res is not None:
                return res
        return None
    elif name_en is not None:
        for col in db.list_collection_names():
            if col == name_en:
                return db[col].find_one()
        return None
    elif category is not None:
        # TODO: 按学院分类
        return None
    else:
        return None


def get_data(id_s=None, name_ch=None, name_en=None, category=None):
    final_json = {'nodes': [], 'links': [], 'categories': []}
    # TODO: demo中categories只有三种，后续需要再添加学院
    categories = [{"name": "计算机学院"}, {"name": "数字媒体与设计艺术学院"}, {"name": "其他"}]
    index = None

    # 添加固定的种类数至finalJson['categories']
    final_json['categories'].append(categories)

    # 获取中心作者个人信息
    auth_info = get_auth_info(id_s, name_ch, name_en, category)
    if auth_info is None:
        print('没有找到相关作者信息，请检查参数是否正确！')
        return None

    # 将中心作者添加至finalJson['nodes']
    final_json['nodes'].append(
        {'id': auth_info['id'], 'name': auth_info['name'], 'symbolSize': 70, 'x': 0, 'y': 0, 'value': 0,
         'category': 0, 'type': 'node'}
    )

    # 获取中心作者所在的collection
    for col in db.list_collection_names():
        if db[col].find_one({'id': auth_info['id']}) is not None:
            index = col
            break

    # 遍历中心作者的所有合作者
    res = db[index].find({}, {'_id': 0, 'realted': 1}).skip(1).limit(1)[0]['realted']
    for i in res:
        co_auth_info = get_auth_info(None, None, i[0], None)
        # TODO: 目前，如果合作者不隶属BUPT，则跳过
        if co_auth_info is not None:
            # 添加合作者信息至finalJson['nodes']
            final_json['nodes'].append(
                {'id': co_auth_info['id'], 'name': co_auth_info['name'], 'symbolSize': 60, 'x': 0, 'y': 0,
                 'value': int(i[1]), 'category': 0, 'type': 'node'})
            # 添加合作信息至finalJson['links']
            final_json['links'].append(
                {'source': auth_info['id'], 'target': co_auth_info['id'],
                 "type": "link", 'value': int(i[1])}
            )

    # 计算合作者的坐标
    # 动态赋予x y值
    # 代码功能

    # 静态变量
    r = 200  # 半径
    angle = 360  # 角度
    interval = []  # 存储角度数组
    range = []  # 存储xy数据
    numCategory = len(final_json['categories'])  # 获取总共种类数
    numData = len(final_json['nodes'])  # 获取数据个数

    # 计算平均角度，放入interval中
    average = angle / numCategory  # 计算平均角度
    i = 0  # 进行循环赋值
    while i < numCategory:
        angleNow = int(i * average)
        interval.append(angleNow)
        i += 1
    # print(interval)

    # 计算x与y的具体值
    i = 1  # 进行循环赋值（从1开始跳过自己
    while i < numData:
        symbolSize = final_json['nodes'][i]["symbolSize"]  # 点大小是多少
        category = final_json['nodes'][i]["category"]  # 学院是哪个

        # 半径加权计算
        weight = symbolSize / 70  # 权值,自身点大小为70
        randomNum = random.randint(interval[category], interval[category] + 119)  # 生成随机数
        x = r * math.cos(randomNum * 2 * math.pi / 360) * weight
        y = r * math.sin(randomNum * 2 * math.pi / 360) * weight

        # 将xy值添加至finalJson中
        final_json['nodes'][i]['x'] = x
        final_json['nodes'][i]['y'] = y

        i += 1
    return final_json


if __name__ == '__main__':
    # TODO: 目前finalJson['categories']为空
    # TODO: 判断是传入JSON文件 还是直接以JSON格式直接进行文本传递

    # 需要指定中心作者的id、name_ch、name_en中的一个，以下三种方式皆可
    finalJson = get_data(name_ch="丰雷")  # 演示：假设中心作者为“丰雷”老师
    # finalJson = get_data(id_s="101")
    # finalJson = get_data(name_en="Lei_Feng_0001")

    # 将finalJson字典转化为json，utf-8编码
    # dict_json = json.dumps(finalJson, ensure_ascii=False)
    # with open('file.json', 'w+', encoding="utf-8") as file:
    #     file.write(dict_json)

    print(finalJson['nodes'])
    print(len(finalJson['nodes']))
    print(finalJson['links'])
    print(len(finalJson['links']))