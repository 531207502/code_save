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
        #定位输入用户名
        driver.find_element(by=By.XPATH,value='//*[@id="fm-login-id"]').send_keys('ccc531207502')
        #定位输入密码
        driver.find_element(by=By.XPATH,value='//*[@id="fm-login-password"]').send_keys('900302han')
        #点击登录
        driver.find_element(by=By.XPATH, value='//*[@id="login-form"]/div[4]/button').click()
        time.sleep(1)
        #driver.find_element(by=By.XPATH,value='.//*[@id="bought"]').click()
        #点击已买到的宝贝
        driver.find_element(by=By.XPATH, value='.//*[@href="//trade.taobao.com/trade/itemlist/list_bought_items.htm?nekot=1470211439694"]').click()
        time.sleep(1)
        #选择输入框，输入查找内容
        driver.find_element(by=By.XPATH, value='.//*[@placeholder="输入商品标题或订单号进行搜索"]').send_keys('汽车')
        #点击搜索按钮
        time.sleep(1)
        #driver.find_element(by=By.LINK_TEXT, value='订单搜索').click()
        #driver.find_element(by=By.XPATH, value='.//*[@class="search-mod__order-search-button___1q3E0"]').click()
if __name__ == '__main__':
    unittest.main()
    unittest.TestSuite