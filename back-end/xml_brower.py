from xml.dom.minidom import parse

def getfundinfor(xml):

    # 范例
    # data1 = {
    #     "id": 92,
    #     "Article": {
    #         "aid2": {"title": "学科推荐系统2", "author": {"王俊翔": "02/2100", "王伊哲": "02/2100"},
    #                  "url": "https://doi.org/10.1109/COMPSAC54236.2022.00123", "year": 2100, "abstract": "xxxxxx"},
    #         "aid1": {"title": "学科推荐系统1", "author": {"朱子炫": "02/2100", "胡逸同": "02/2100"},
    #                  "url": "https://dblp.org/pid/65/9612.xml", "year": 2100, "abstract": "xxxxxx"}
    #     }
    # }

    # 获取根节点
    domTree = parse(xml)
    root = domTree.documentElement

    # 最终返回的字典
    result = {}
    result['Article'] = {}

    # 获取查询对象基本信息
    result['id'] = root.getAttribute('pid')
    result['name'] = root.getAttribute('name')

    # 获取合作者信息
    # 遍历每个合作文章
    pappers = root.getElementsByTagName('inproceedings')
    for papper in pappers:
        # 获取key值
        articlename = papper.getAttribute('key')
        result['Article'][articlename] = {}
        # 获取title
        result['Article'][articlename]['title'] = papper.getElementsByTagName('title')[0].childNodes[0].data
        # 获取url
        result['Article'][articlename]['url'] = papper.getElementsByTagName('ee')[0].childNodes[0].data
        # 获取year
        result['Article'][articlename]['year'] = papper.getElementsByTagName('year')[0].childNodes[0].data
        # 获取合作者
        result['Article'][articlename]['author'] = {}
        for i in range(0,len(papper.getElementsByTagName('author'))):
            result['Article'][articlename]['author'][papper.getElementsByTagName('author')[i].childNodes[0].data] = papper.getElementsByTagName('author')[i].getAttribute('pid')

    return result
