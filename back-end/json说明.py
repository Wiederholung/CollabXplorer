# 最后返回的json文件（字典）
# 包含三大列表：
#           1.学者：nodes
#           2：合作关系：links
#           3.学者学院：categories
fianaljson = {'nodes': [], 'links': [], 'categories': []}

# 学者（nodes）是一个列表，列表每一项都是一个字典
# 学者id：id
# 学者姓名：name
# 学者权值（中心节点为60，其余节点依据其和中心节点合作数量从5到50）：symbolsize
# 节点x轴位置：x
# 节点y轴位置：y
# 学者署名文件总数：value
# 学者所属学院（要和下面的学院相对应，例如此学者为计算机学院下面学院栏中计算机学院是第3个，那么他的值应该为2（3-1））：category
# 表明这是一个节点：“type”：“node”
# 添加节点（学者）的字典格式,以下是范例。
# -200<=x,y<=+200
addnodes = {"id": "0", "name": "王俊翔", "symbolSize": 60, "x": 0, "y": 0, "value": 108, "category": 0, "type": "node"}
# 将节点添加志json文件，每个字典是nodes列表的一部分
fianaljson['nodes'].append(addnodes)

# 连线头：source
# 连线尾：target
# 表明这是一个合作关系：“type”：“link”
# 双方合作总数：value
# 添加合作关系的字典格式,以下是范例。
addlinks = {"source": "0", "target": "1", "type": "link", "value": 10}
# 将节点添加志json文件，每个字典是links列表的一部分
fianaljson['links'].append(addlinks)

# 学院名称：name
# 注意和上面的nodes对应
# 添加学院的字典格式,以下是范例。
addcategories = {"name": "国际学院"}
# 将节点添加志json文件，每个字典是categories列表的一部分
fianaljson['categories'].append(addcategories)

# 字典生成式，将两个列表打包成一个字典
name = ['id', 'name', 'x', 'y']
data = ['0', 'wjx', 0, 0]
testnode = dict(zip(name, data))
