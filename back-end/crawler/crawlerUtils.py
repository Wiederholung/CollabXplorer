from crawler import acm
from crawler import arxiv
from crawler import IEEE
from crawler import sciencedirect
from crawler import springer
from crawler import cvpr
from crawler import driver
from crawler import AAAI
import traceback


def get_abstract(url):
    try:
        browser = driver.init_driver(url)
        c_url = browser.current_url
        # 如果是 IEEE 的网址
        if c_url.find('ieee.org') != -1:
            res = IEEE.get_abstract(browser)
            return res
        # 如果是 ACM 的网址
        elif c_url.find('dl.acm.org') != -1:
            res = acm.get_abstract(browser)
            return res
        # 如果是 arxiv 的网址
        elif c_url.find('arxiv.org') != -1:
            res = arxiv.get_abstract(browser)
            return res
        # 如果是 science direct 的网址
        elif c_url.find('sciencedirect.com') != -1:
            res = sciencedirect.get_abstract(browser)
            return res
        # 如果是 springer 的网址
        elif c_url.find('springer.com') != -1:
            res = springer.get_abstract(browser)
            return res
        # 如果是 cvpr 网址
        elif c_url.find('thecvf.com') != -1:
            res = cvpr.get_abstract(browser)
            return res
        # 如果是 AAAI 网址
        elif c_url.find('aaai.org') != -1:
            res = AAAI.get_abstract(browser)
            return res
        # 如果是其他网址
        else:
            print('未收录网址:' + url)
            return ''
    except:
        # 如果出现异常，打印异常信息
        print('异常网址:' + url)
        traceback.print_exc()


if __name__ == '__main__':
    url0 = 'https://doi.org/10.1145/3447993.3483259'
    print(get_abstract(url0))
