import time
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.common.appiumby import By
import pymysql
caps = {
"platformName": "Android", # 声明是ios还是Android系统
"platformVersion": "11", # Android内核版本号
"deviceName": "Redmi_K20_Pro", # 连接的设备名称
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
start_x , start_y = 1/2 * width ,3/5 * height
end_x , end_y = 1/2 * width , 1/5 * height
count=2000
flag=0
#time.sleep(2)
#driver.swipe(start_x, 1/2 * height, end_x, 1/4 * height,duration=4000)
zd={}
errorcount=0
starttime=int(time.time())
while True:
    if count<0:
        break
    else:
        el6 = driver.find_elements(By.XPATH,".//*[@resource-id='com.tencent.mm:id/be3']")
        num=0
        number=len(el6)
        for xunhuan in range(1,number-1):
            # if num==0 and flag==0:
            #     num+=1
            #     count-=1
            #     flag=1
            #     continue
        #else:
            el21 = el6[xunhuan].find_elements(By.XPATH,".//*[@resource-id='com.tencent.mm:id/c5u']")
        #if el21 != []:
            num+=1
            count-=1
            print(count)
            step = el6[xunhuan].find_elements(By.XPATH,"//*[@resource-id='com.tencent.mm:id/c5a']")
            name = el6[xunhuan].find_elements(By.XPATH,"//*[@resource-id='com.tencent.mm:id/c6d']")
        #if name != [] and step != []:
            if int(step[0].get_attribute('text')) > 5000:
                el21[0].click()
                zd[name[0].get_attribute('text')] = step[0].get_attribute('text')
            else:
             count=-1
             break
        # else:
        #     errorcount+=1
        #     print("这次跳过了，这次是第{}次".format(errorcount))
        #     pass
        #else:
            #print("这次跳过了，这次是第{}次,这次跳过是点赞跳过".format(errorcount))
        driver.swipe(start_x, start_y, end_x, end_y)
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
print("总共耗时为：{}秒".format(int(time.time())-starttime))
conn=pymysql.connect(host='cylcrystal.top',port=12345,user='root',password='890718feng',db='ljf_wxyd',charset='utf8')
try:
    with conn.cursor() as cursor:
#里面的语句就按照mysql的操作语句来写
        nowtime=time.strftime("%Y_%m_%d", time.localtime())
        print(nowtime)
        sql_createTb = """CREATE TABLE %s  (
                         排名 INT ,
                         姓名  CHAR(20),
                         步数 INT
                         )
                         """% (nowtime)
        cursor.execute(sql_createTb)
        keys=zd.keys()
        values=zd.values()
        list_key=list(keys)
        list_value=list(values)
        for i in range(len(zd)):
            key_value=list_key[i]
            value_value=list_value[i]
            #print(key_value,value_value)
            result=cursor.execute('insert into %s values(%s,"%s",%s)'% (nowtime,i+1,key_value,value_value))
#这里的返回值是操作后影响的行，这里就添加了一行所以返回的是1
        if result==1:
            print("添加数据成功")
#使用游标进行数据更改时必须确认提交才生效
            conn.commit()
#如果添加失败或者操作有误，要进行回滚
except pymysql.MySQLError as error:
    print(error)
    conn.rollback()
finally:
    conn.close()