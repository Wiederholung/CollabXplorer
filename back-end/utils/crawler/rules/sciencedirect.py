from selenium.webdriver.common.by import By
from utils.crawler import crawler_driver as driver


def get_abstract(browser):
    try:
        res_list = browser.find_elements(by=By.CSS_SELECTOR, value="[class='abstract author']")
        result = browser.execute_script("return arguments[0].textContent", res_list[0])
        # 删除 result 中的前缀 'Abstract'
        return result[8:]
    except IndexError as e:
        print('错误：{}，未找到摘要：{}' .format(e, browser.current_url))
        return ''


if __name__ == '__main__':
    url = 'https://www.sciencedirect.com/science/article/pii/S0141938222001135'
    print(get_abstract(driver.init_driver(url)))
