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
        #driver = webdriver.Chrome()
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
        #driver.switch_to.frame('baxia-dialog-content')
        #huakuai=driver.find_elements(by=By.XPATH, value='//*[@id="nc_1_n1z"]')[0]
        # ActionChains(driver).click_and_hold(huakuai).perform()
        # tracks=258
        # for x in range(0,tracks,43):
        #     ActionChains(driver).move_by_offset(xoffset=0, yoffset=0).perform()
        #     time.sleep(0.5)
        # ActionChains(driver).release().perform()
# if __name__ == '__main__':
#     print('11111111111111')
#     unittest.main()



