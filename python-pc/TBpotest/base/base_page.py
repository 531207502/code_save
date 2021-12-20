from selenium import webdriver
class BasePage:
    def __init__(self,driver):
        self.driver = driver
    # 封装定位元素
    def element_loc(self,loc):
        #定位元素
        return self.driver.find_element(*loc)
    def send_keys(self,loc,value):
        #定位+输入值
        self.element_loc(loc).send_keys(value)
        #定位+点击操作
    def click(self,loc):
        self.element_loc(loc).click()