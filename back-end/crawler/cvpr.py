from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 任务：爬取2页或多页指定URL的文章摘要
def get_abstract(url):
    browser = webdriver.Chrome()
    browser.implicitly_wait(200)  # 这是延时等待。由于网速时快时慢，而get方法会在网页框架加载结束后停止执行，
    # 这就会导致有些时候我们打算获取的内容还没被加载进来便结束了获取页面数据，最后报错，拿不到想要的数据。
    browser.get(url)
    # 遇到class name中的复合情况（即有多个class name中间是空格隔开的）
    # 选取其中一个具有全局唯一性的class name即可准确定位所要查找的结点内容
    res_list = browser.find_elements(by=By.ID, value='abstract')
    result = browser.execute_script("return arguments[0].textContent", res_list[0])
    time.sleep(1)  # 有些网站有反爬虫机制，如果访问间隔时间很短则不会响应。
    return result


if __name__ == '__main__':
    url0 = 'https://openaccess.thecvf.com/content/CVPR2022/html/Chen_EPro-PnP_Generalized_End-to' \
           '-End_Probabilistic_Perspective-N-Points_for_Monocular_Object_Pose_Estimation_CVPR_2022_paper.html '
    print(get_abstract(url0))
