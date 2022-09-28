from selenium.webdriver.common.by import By
from crawler import driver


def get_abstract(browser):
    try:
        res_list = browser.find_elements(by=By.CSS_SELECTOR, value="[class='item abstract']")
        result = browser.execute_script("return arguments[0].textContent", res_list[0])
        # 删除 result 中的前缀
        return result[20:]
    except IndexError as e:
        print('错误：{}，未找到摘要：{}' .format(e, browser.current_url))
        return ''


if __name__ == '__main__':
    url = 'https://doi.org/10.1145/3447993.3483259'
    print(get_abstract(driver.init_driver(url)))
