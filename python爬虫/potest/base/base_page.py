from selenium import webdriver
class BasePage:
    def __init__(self):
        global driver1
        self.driver=webdriver.chrome()
        self.driver.get('http://www.baidu.com')
        driver1 = self.driver
    # 封装定位元素
    def find_ele(self, *args):
        ele = self.driver.find_element(*args)
        return ele