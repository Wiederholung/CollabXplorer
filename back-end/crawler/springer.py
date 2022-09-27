from selenium.webdriver.common.by import By
from crawler import driver


# 任务：爬取2页或多页指定URL的文章摘要
def get_abstract(browser):
    res_list = browser.find_elements(by=By.ID, value='Abs1-content')
    result = browser.execute_script("return arguments[0].textContent", res_list[0])
    return result


if __name__ == '__main__':
    url = 'https://link.springer.com/article/10.1007/s42486-021-00067-1'
    print(get_abstract(driver.init_driver(url)))
