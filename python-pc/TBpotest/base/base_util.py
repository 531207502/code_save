import unittest
from selenium import webdriver
class BaseUtil(unittest.TestCase):
    def setUp(self):
        global driver
        # webdriver实例化
        # 这个是为了跳过检测的
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=self.options)
        self.driver = driver
        driver.get('https://login.taobao.com')
        driver.maximize_window()
    def tearDown(self):
        pass