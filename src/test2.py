
from pymongo import MongoClient
client =MongoClient("metattri.com",27017)

# 创建临时的URL数据库： URL_db

db=client.URL_db#链接URL_db数据库 没有自动创建
collection = db.user#使用user集合 没有自动创建

data1 = { "age" : 24 , "userName" : "zuofanixu" }
data2 = { "age" : 26 , "userName" : "yanghang" }
collection.insert_one(data1)
collection.insert_one(data2)
# collection.delete_one({'age':24})


# db=client.drop_database('URL_db')#删库