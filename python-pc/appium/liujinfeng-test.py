import time
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.common.appiumby import By
caps = {
"platformName": "Android", # 声明是ios还是Android系统
"platformVersion": "7.1.1", # Android内核版本号
"deviceName": "MI_MAX_2", # 连接的设备名称
"appPackage": "com.tencent.mm", # apk的包名
"appActivity": 'com.tencent.mm.ui.LauncherUI', # app 启动时主 Activity,界面名
"noReset": True # 在开始会话之前不要重置应用程序状态
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",caps) # 启动app
driver.implicitly_wait(10)
el1 = driver.find_element(By.ID,"com.tencent.mm:id/dt5")#点击查找
el1.click()
time.sleep(1)
el10 = driver.find_element(By.ID,"com.tencent.mm:id/bxz")#点击输入框
el10.click()
time.sleep(0.2)
el10.send_keys("微信运动")
time.sleep(0.2)
el11 = driver.find_elements(By.ID,"com.tencent.mm:id/hee")#点击微信运动
el11[1].click()
time.sleep(0.2)
el12 = driver.find_element(By.ID,"com.tencent.mm:id/d8")#点击微信运动设置
el12.click()
time.sleep(0.2)
el13 = driver.find_elements(By.ID,"android:id/title")#点击隐私及提醒设置
el13[5].click()
time.sleep(0.2)
el14 = driver.find_elements(By.ID,"com.tencent.mm:id/b0m")#取消加入排行榜
el14[0].click()
time.sleep(0.2)
el15 = driver.find_elements(By.ID,"com.tencent.mm:id/eh")#返回
el15[0].click()
time.sleep(0.2)
el16 = driver.find_elements(By.ID,"com.tencent.mm:id/eh")#返回
el16[0].click()
time.sleep(0.2)
el2 = driver.find_element(By.ID,"com.tencent.mm:id/fcw")#步数排行榜
el2.click()
time.sleep(0.2)
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
print("屏幕的高为：{}".format(width))
print("屏幕的宽为：{}".format(height))
start_x , start_y = 1/2 * width ,2/3 * height
end_x , end_y = 1/2 * width , 1/3 * height
count=2000
flag=0
driver.swipe(start_x, 3/4 * height, end_x, 1/2 * height)
time.sleep(2)
while True:
    if count<0:
        break
    else:
        el3 = driver.find_elements(By.ID, "com.tencent.mm:id/c5u")
        num=0
        for ele in el3:
            if num==0 and flag==0:
                num+=1
                count-=1
                flag=1
                continue
            else:
                ele.click()
                num+=1
                count-=1
                print(count)
        driver.swipe(start_x, start_y, end_x, end_y,duration=2)
el16 = driver.find_elements(By.ID,"com.tencent.mm:id/eh")#返回
el16[0].click()
time.sleep(0.2)
el12 = driver.find_element(By.ID,"com.tencent.mm:id/d8")#点击微信运动设置
el12.click()
time.sleep(0.2)
el13 = driver.find_elements(By.ID,"android:id/title")#点击隐私及提醒设置
el13[5].click()
time.sleep(0.2)
el14 = driver.find_elements(By.ID,"com.tencent.mm:id/b0m")#取消加入排行榜
el14[0].click()
time.sleep(0.2)

