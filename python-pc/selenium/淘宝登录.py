import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
class TestCase1(unittest.TestCase):
    def test_01(self):
        global driver
        #webdriver实例化
        #这个是为了跳过检测的
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=self.options)
        driver.get('https://login.taobao.com')
        driver.maximize_window()
        driver.find_element(by=By.XPATH,value='//*[@id="fm-login-id"]').send_keys('ccc531207502')
        driver.find_element(by=By.XPATH,value='//*[@id="fm-login-password"]').send_keys('900302han')
        driver.find_element(by=By.XPATH, value='//*[@id="login-form"]/div[4]/button').click()
        time.sleep(1)




