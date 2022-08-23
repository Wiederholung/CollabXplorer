from pymongo import MongoClient

client = MongoClient('mongodb://rwAll:ARS 5111-rwAll'
                     '@dev.metattri.com:27017')
db = client.bupt
collection = db.丰雷
x = collection.find_one()

print(x)

finalJson = {'nodes': [], 'links': [], 'categories': []}
nodes = ['id', 'name', 'symbolSize', 'x', 'y', 'value', 'category', 'type']
links = ['source', 'target', 'value']
categories = ['name']
