from utils.crawler import crawler_driver
from selenium.webdriver.common.by import By
from utils.crawler.rules import AAAI, arxiv, cvpr, acm, sciencedirect, springer, IEEE


def get_abstract_by_crawler(url):
    # browser是一个webdriver对象，用于获取网页源代码
    browser = crawler_driver.init_driver(url)
    try:
        # c_url是当前网页的网址
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
        # 如果是 CVPR 网址
        elif c_url.find('thecvf.com') != -1:
            res = cvpr.get_abstract(browser)
            return res
        # 如果是 AAAI 网址
        elif c_url.find('aaai.org') != -1:
            res = AAAI.get_abstract(browser)
            return res
        # 如果是其他网址
        else:
            print('未收录网址：{}'.format(url))
            return ''
    except Exception as e:
        # 如果出现异常，打印异常信息
        print('错误：{}\n异常网址：{}'.format(e, url))
        return ''
    finally:
        # 关闭浏览器
        browser.quit()


def retrieve_citations(doi):
    """
    获取某篇论文的引用数
    :param doi:
    :return:
    """
    # Construct the URL for the given DOI
    citations = 0
    url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={doi}&btnG='

    try:
        # Create a new instance of the Firefox driver
        driver = crawler_driver.init_driver(url)

        # Navigate to the URL
        # driver.get(url)

        # Find the div element with class 'gs_fl'
        gs_fl = driver.find_elements(By.CLASS_NAME, 'gs_fl')[1]

        # Extract the number of citations from the elements
        for child in gs_fl.find_elements(By.TAG_NAME, 'a'):
            if child.text.find('Cited by') != -1:
                citations = child.text.split(' ')[2]
                break

        # Close the browser window
        driver.quit()

        return citations

    except Exception as e:
        # Handle any exceptions that occur during the request
        print(f'Error: {e}')
        return '0'


if __name__ == '__main__':
    url0 = 'https://doi.org/10.48550/arXiv.2303.09607'
    print(get_abstract_by_crawler(url0))

    # Get the DOI from the user
    # DOI = input('Enter DOI: ')
    DOI = "10.1109/MCOM.2017.1500657CM"

    # Call the retrieve_citations() function and print the result
    print(f'{DOI} has {retrieve_citations(DOI)} citations.')
