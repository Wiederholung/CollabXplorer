# 模拟数据
import math
import random

testjson = {'nodes': [
    {"id": "0", "name": "王俊翔", "symbolSize": 60, "x": 0, "y": 0, "value": 108, "category": 0, "type": "node"},
    {"id": "0", "name": "wyz", "symbolSize": 60, "x": 0, "y": 0, "value": 108, "category": 1, "type": "node"},
    {"id": "0", "name": "wyz", "symbolSize": 60, "x": 0, "y": 0, "value": 108, "category": 2, "type": "node"}],
    'links': [],
    'categories': [{"name": "计算机学院"}, {"name": "信通学院"}, {"name": "国际学院"}]}

# 代码功能

# 静态变量
r = 200  # 半径
angle = 360  # 角度
interval = []  # 存储角度数组
range = []  # 存储xy数据
numCategory = len(testjson['categories'])  # 获取总共种类数
numData = len(testjson['nodes'])  # 获取数据个数

# 计算平均角度，放入interval中
average = angle / numCategory  # 计算平均角度
i = 0  # 进行循环赋值
while i < numCategory:
    angleNow = int(i * average)
    interval.append(angleNow)
    i += 1
print(interval)

# 计算x与y的具体值
i = 0  # 进行循环赋值
while i < numData:
    category = testjson['nodes'][i]["category"]  # 学院是哪个
    randomNum = random.randint(interval[category], interval[category] + 119)  # 生成随机数
    x = r * math.cos(randomNum * 2 * math.pi / 360)
    y = r * math.sin(randomNum * 2 * math.pi / 360)
    temp = {'x': x, 'y': y}
    range.append(temp)
    i += 1
print(range)
