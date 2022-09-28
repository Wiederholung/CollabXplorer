from selenium.webdriver.common.by import By
from crawler import driver


def get_abstract(browser):
    try:
        res_list = browser.find_elements(by=By.CSS_SELECTOR, value="[class='abstract mathjax']")
        result = browser.execute_script("return arguments[0].textContent", res_list[0])
    except IndexError as e:
        result = ''
        print('错误：{}，未找到摘要：{}' .format(e, browser.current_url))
    return result


if __name__ == '__main__':
    url = 'https://arxiv.org/abs/2209.12891'
    print(get_abstract(driver.init_driver(url)))
