import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def test01(self):
        # 打开浏览器
        global driver
        driver = webdriver.Chrome()
        # 加载百度首页
        driver.get('http://www.baidu.com')
        # 在百度搜索栏中输入软件测试
        driver.find_element(By.ID, 'kw').send_keys('软件测试')
        # 点击百度一下按钮
        driver.find_element(By.ID, 'su').click()

    def test02(self):
        # 打开浏览器
        global driver1
        driver1 = webdriver.Chrome()
        # 加载百度首页
        driver1.get('http://www.baidu.com')
        # 在百度搜索栏中输入软件测试
        driver1.find_element(By.ID, 'kw').send_keys('硬件测试')
        # 点击百度一下按钮
        driver1.find_element(By.ID, 'su').click()