from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.select import Select


class TestCase1(unittest.TestCase):
    def test_01(self):
        global driver
        #webdriver实例化
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')
        driver.maximize_window()
        driver.find_element(by=By.ID,value='kw').send_keys('码尚学院')
        driver.find_element(by=By.ID,value='su').click()
        driver.switch_to.frame()
        Select

    def test_02(self):
        print("这是测试案例2")
# if __name__ == '__main__':
#     print('11111111111111')
#     unittest.main()