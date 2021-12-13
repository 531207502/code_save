import time
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.common.appiumby import By
caps = {
"platformName": "Android", # 声明是ios还是Android系统
"platformVersion": "11", # Android内核版本号
"deviceName": "Redmi_K30_Pro", # 连接的设备名称
"appPackage": "com.tencent.mm", # apk的包名
"appActivity": 'com.tencent.mm.ui.LauncherUI', # app 启动时主 Activity,界面名
"noReset": True # 在开始会话之前不要重置应用程序状态
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",caps) # 启动app
driver.implicitly_wait(5)
el1 = driver.find_element(By.ID,"com.tencent.mm:id/dt5")
el1.click()
time.sleep(1)
el10 = driver.find_element(By.ID,"com.tencent.mm:id/bxz")
el10.click()
time.sleep(1)
el10.send_keys("微信运动")
time.sleep(1)
el11 = driver.find_elements(By.ID,"com.tencent.mm:id/hee")
el11[1].click()
time.sleep(1)
# el1 = driver.find_element(By.ID,"com.tencent.mm:id/bg1")#微信运动
# el1.click()
# time.sleep(2)
el2 = driver.find_element(By.ID,"com.tencent.mm:id/fcw")#步数排行榜
el2.click()
time.sleep(1)
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
print("屏幕的高为：{}".format(width))
print("屏幕的宽为：{}".format(height))
while True:
    start_x , start_y = 1/2 * width ,3/4 * height
    end_x , end_y = 1/2 * width , 1/4 * height
    el3 = driver.find_elements(By.ID, "com.tencent.mm:id/c5u")#获取本页面的点赞元素
    for ele in el3:
        ele.click()
        el4 = driver.find_elements(By.ID, "com.tencent.mm:id/c2g")
        if el4 != []:
            el5 = driver.find_element(By.ID, "com.tencent.mm:id/eh")
            el5.click()
            time.sleep(0.5)
            continue
        else:
            pass
    driver.swipe(start_x, start_y,end_x, end_y)


