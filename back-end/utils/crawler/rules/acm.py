from selenium.webdriver.common.by import By
from utils.crawler import crawler_driver


def get_abstract(browser):
    try:
        res_list = browser.find_elements(by=By.CLASS_NAME, value="abstractInFull")
        result = browser.execute_script("return arguments[0].textContent", res_list[0])
    except IndexError as e:
        result = ''
        print('错误：{}，未找到摘要：{}' .format(e, browser.current_url))
    return result


if __name__ == '__main__':
    url = 'https://dl.acm.org/doi/10.1145/3550298'
    print(get_abstract(driver.init_driver(url)))
