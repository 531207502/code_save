from selenium.po测试.base.base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    #主要包含页面元素和动作
    # 元素定位，
    baidu_text_loc = (By.ID, 'kw')
    baidu_submit_loc = (By.ID, 'su')