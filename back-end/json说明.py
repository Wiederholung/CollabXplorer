# 最后返回的json文件 nodes links categories
fianaljson = {'nodes':[],'links':[],'categories':[]}

# 添加节点的字典格式,数据是瞎写的。id name symbolsize x y value category type
#-200<=x,y<=+200
addnodes = {"id": "0","name": "王俊翔","symbolSize": 60,"x": 0,"y": 0,"value": 108,"category": 0,"type": "node"}
# 将节点添加志json文件，每个字典是nodes列表的一部分
fianaljson['nodes'].append(addnodes)

# 添加连接的字典格式,数据是瞎写的。 source target type value
addlinks = {"source": "0","target": "1","type": "link","value": 10}
# 将节点添加志json文件，每个字典是links列表的一部分
fianaljson['links'].append(addlinks)

# 添加学院的字典格式,数据是瞎写的。name
addcategories = {"name": "国际学院"}
# 将节点添加志json文件，每个字典是categories列表的一部分
fianaljson['categories'].append(addcategories)

# 字典生成式，将两个列表打包成一个字典
name=['id','name','x','y']
data=['0','wjx',0,0]
testnode=dict(zip(name,data))



