from selenium.webdriver.common.by import By
from TBpotest.base.base_page import BasePage
from TBpotest.pageobject.login_page import LoginPage
class chaxunPage(BasePage):
    #元素定位
    bianlan_loc = (By.XPATH,'.//*[@id="bought"]')
    #输入内容
    shuru_loc = (By.XPATH,'.//*[@placeholder="输入商品标题或订单号进行搜索"]')
    #点击查询
    chaxun_loc = (By.XPATH,'.//*[@class="search-mod__order-search-button___1q3E0"]')
    #元素动作
    def user_chaxun(self,value):
        dl = LoginPage(self.driver)
        dl.user_login()
        self.click(self.bianlan_loc)
        self.send_keys(self.shuru_loc, value)
        self.click(self.chaxun_loc)


