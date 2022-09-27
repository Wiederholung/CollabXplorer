from selenium.webdriver.common.by import By
from crawler import driver


def get_abstract(browser):
    res_list = browser.find_elements(by=By.CLASS_NAME, value='u-mb-1')
    result = browser.execute_script("return arguments[0].textContent", res_list[1])
    return result


if __name__ == '__main__':
    url = 'https://doi.org/10.1109/JIOT.2021.3098338'
    print(get_abstract(driver.init_driver(url)))
