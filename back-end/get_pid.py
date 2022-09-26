import urllib.request
from xml.dom.minidom import parse
import db_connetor


# 获取 db 内所有 collection 的名字
def get_all_col():
    db = db_connetor.get_connection()
    return db.list_collection_names()


def get_xml(name_en):
    url = 'https://dblp.uni-trier.de/search/author?xauthor=' + name_en
    return parse(urllib.request.urlopen(url))


def get_pid(xml_doc):
    root = xml_doc.documentElement
    return root.getElementsByTagName('author')[0].getAttribute('pid')


if __name__ == '__main__':
    for col in get_all_col():
        xml = get_xml(col)
        pid = get_pid(xml)
        print(col, pid)
