from selenium.webdriver.common.by import By
from utils.crawler import crawler_driver as driver


def get_abstract(browser):
    try:
        res_list = browser.find_elements(by=By.ID, value='abstract')
        result = browser.execute_script("return arguments[0].textContent", res_list[0])
    except IndexError as e:
        result = ''
        print('错误：{}，未找到摘要：{}' .format(e, browser.current_url))
    return result


if __name__ == '__main__':
    url = 'https://openaccess.thecvf.com/content/CVPR2022/html/Chen_EPro-PnP_Generalized_End-to' \
           '-End_Probabilistic_Perspective-N-Points_for_Monocular_Object_Pose_Estimation_CVPR_2022_paper.html '
    print(get_abstract(driver.init_driver(url)))
