from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.select import Select
class TestCase1(unittest.TestCase):
    def test_01(self):
        global driver
        #webdriver实例化
        driver = webdriver.Chrome()
        driver.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.21814703.754894437.1.5af911d9lQFxfw&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F')
        driver.maximize_window()
        driver.find_element(by=By.XPATH,value='//*[@id="fm-login-id"]').send_keys('ccc531207502')
        driver.find_element(by=By.XPATH,value='//*[@id="fm-login-password"]').send_keys('900302han')
        driver.find_element(by=By.XPATH, value='//*[@id="login-form"]/div[4]/button').click()
# if __name__ == '__main__':
#     print('11111111111111')
#     unittest.main()



