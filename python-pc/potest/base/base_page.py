from selenium import webdriver
class BasePage:
    def __init__(self):
        global driver1
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        driver1 = self.driver
    # 封装定位元素
    def find_ele(self, args):
        ele = self.driver.find_element(*args)
        return ele
    #输入查询数据
    def send_keys(self,args,value):
        self.find_ele(args).send_keys(value)
    #进行点击操作
    def click(self,loc):
        self.find_ele(loc).click()