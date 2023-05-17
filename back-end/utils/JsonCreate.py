import random

#导入fake.json
import json

for i in range(0, 30):
    # with open('../../front-end/frontPage/fake.json', 'r', encoding='utf-8') as f:
    #     json_data = json.load(f)
    # for node in json_data['nodes']:
    #     if random.uniform(0, 1.0) > 0.3:
    #         continue
    #     node["name"] = "Scholar" + str(node["id"])
    #     if int(node["id"]) == 11:
    #         node["symbolSize"] =  76.66666666666667
    #         node['x'] = 0
    #         node['y'] = 0
    #         node['value'] = 100
    #         node['category'] = 1
    #         continue
    #     node["symbolSize"] = random.uniform(2.0,29.0)
    #     node['x'] = random.uniform(-400, 800.0)
    #     node['y'] = random.uniform(-400, 800.0)
    #     node['value'] = node["symbolSize"] + 2
    #
    # #导出fake.json
    # with open('../../front-end/frontPage/result'+str(i)+'.json','w',encoding='utf-8') as f:
    #     json.dump(json_data,f,ensure_ascii=False)

    with open('../../front-end/frontPage/picture/result'+str(i)+'.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    for node in json_data['nodes']:
        node["name"] = "Scholar" + str(node["id"])
    with open('../../front-end/frontPage/picture/result' + str(i) + '.json', 'w', encoding='utf-8') as f:
        json.dump(json_data,f,ensure_ascii=False)

