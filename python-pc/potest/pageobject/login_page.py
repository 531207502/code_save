from selenium.webdriver.common.by import By
from potest.base.base_page import BasePage


class LoginPage(BasePage):
    #主要包含页面元素和动作
    # 元素定位，
    baidu_text_loc = (By.ID, 'kw')
    baidu_submit_loc = (By.ID, 'su')
    # 获得元素对象
    def ysdx(self):
        self.find_ele(LoginPage.baidu_text_loc)
    def yxdl(self,value):
        self.send_keys(LoginPage.baidu_text_loc,value)
        self.click(LoginPage.baidu_submit_loc)