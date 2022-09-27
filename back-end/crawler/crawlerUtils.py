from crawler import acm
from crawler import arxiv
from crawler import IEEE
from crawler import sciencedirect
from crawler import springer


def get_abstract(url):
    try:
        while True:
            res = IEEE.get_abstract(url)
            if res != '':
                return res
            res = acm.get_abstract(url)
            if res != '':
                return res
            res = arxiv.get_abstract(url)
            if res != '':
                return res
            res = sciencedirect.get_abstract(url)
            if res != '':
                return res
            res = springer.get_abstract(url)
            if res != '':
                return res
            else:
                return ''
    except:
        print("获取摘要失败")
        pass
