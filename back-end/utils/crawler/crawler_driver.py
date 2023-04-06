from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


try:
    # selenium 4
    from selenium.webdriver.chrome.service import Service as ChromeService
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
except TypeError:
    # selenium 3
    driver = webdriver.Chrome(ChromeDriverManager().install())

def init_driver(url):
    driver.implicitly_wait(30)  # 这是延时等待。由于网速时快时慢，
    driver.get(url)  # 而 get 方法会在网页框架加载结束后停止执行，这就会导致有些时候我们打算获取的内容还没被加载进来便结束了获取页面数据，最后报错，拿不到想要的数据。
    # 遇到class name中的复合情况（即有多个class name中间是空格隔开的）
    # 选取其中一个具有全局唯一性的class name即可准确定位所要查找的结点内容
    return driver
