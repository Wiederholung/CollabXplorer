from selenium.webdriver.common.by import By
from utils.crawler import crawler_driver as driver


def get_abstract(browser):
    try:
        res_list = browser.find_elements(by=By.ID, value='Abs1-content')
        result = browser.execute_script("return arguments[0].textContent", res_list[0])
        return result
    except IndexError as e:
        result = ''
        print('错误：{}，未找到摘要：{}' .format(e, browser.current_url))

    return result


if __name__ == '__main__':
    url = 'https://link.springer.com/article/10.1007/s42486-021-00067-1'
    print(get_abstract(driver.init_driver(url)))
