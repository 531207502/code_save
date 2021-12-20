import time
from selenium.webdriver.common.by import By
from TBpotest.base.base_page import BasePage
class LoginPage(BasePage):
    #元素定位
    DL_user_loc=(By.XPATH,'//*[@id="fm-login-id"]')
    DL_pass_loc=(By.XPATH,'//*[@id="fm-login-password"]')
    DL_press_loc=(By.XPATH,'//*[@id="login-form"]/div[4]/button')
    #元素动作
    def user_login(self,user="ccc531207502",password="900302han"):
        self.send_keys(self.DL_user_loc,user)
        self.send_keys(self.DL_pass_loc,password)
        self.click(self.DL_press_loc)
        time.sleep(1)
