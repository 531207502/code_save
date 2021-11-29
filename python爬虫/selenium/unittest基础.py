from selenium import webdriver
from selenium.webdriver.common.by import By
#webdriver实例化
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.find_element(by=By.ID,value='kw').send_keys('马上学院')
driver.find_element(by=By.ID,value='su').click()