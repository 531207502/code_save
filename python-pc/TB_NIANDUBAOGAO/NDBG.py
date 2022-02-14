import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from openpyxl import Workbook
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
        page = int(input("请输入你要查询多少页的商品内容："))
        list_gmsj = []
        list_ddh = []
        list_spms = []
        list_gmjg = []
        list_jyzt = []
        for num1 in range(1,page+1):
            if num1 ==1:
                print("开始了")
            else:
                driver.find_element(by=By.XPATH, value='.//*[@class="pagination-item pagination-item-{}"]'.format(num1)).click()
            time.sleep(4)
            list1 = driver.find_elements(by=By.XPATH, value='.//*[@class="index-mod__order-container___1ur4- js-order-container"]')
            #print(len(list1))
            if list1==[]:
                jishu = num1
                print("出现一次没有数据")
                driver.find_element(by=By.XPATH, value='.//*[@class="pagination-item pagination-item-{}"]'.format(num1-1)).click()
                time.sleep(4)
                driver.find_element(by=By.XPATH, value='.//*[@class="pagination-item pagination-item-{}"]'.format(num1)).click()
                time.sleep(4)
                list1 = driver.find_elements(by=By.XPATH,value='.//*[@class="index-mod__order-container___1ur4- js-order-container"]')
            num = 4
            for i in list1:
                #print(i.text)
                goumaishijian = i.find_element(by=By.XPATH,value='.//*[@class="bought-wrapper-mod__create-time___yNWVS"]')
                #print("购买时间是：{}".format(goumaishijian.text))
                list_gmsj.append(goumaishijian.text)
                dingdanhao = i.find_element(by=By.XPATH,value=r'//*[@id="tp-bought-root"]/div[{}]/div/table/tbody[1]/tr/td[1]/span/span[3]'.format(num))
                #print("订单号是：{}".format(dingdanhao.text))
                list_ddh.append(dingdanhao.text)
                try:
                    shangpinmiaoshu = i.find_element(by=By.XPATH,value=r'//*[@id="tp-bought-root"]/div[{}]/div/table/tbody[2]/tr/td[1]/div/div[2]/p[1]/a[1]/span[2]'.format(num))
                    #print("商品描述是：{}".format(shangpinmiaoshu.text))
                    list_spms.append(shangpinmiaoshu.text)
                    goumaijiage = i.find_element(by=By.XPATH,value=r'//*[@id="tp-bought-root"]/div[{}]/div/table/tbody[2]/tr[1]/td[5]/div/div[1]/p/strong/span[2]'.format(num))
                    #print("购买价格是：{}".format(goumaijiage.text))
                    list_gmjg.append(float(goumaijiage.text))
                    jiaoyizhuangtai = i.find_element(by=By.XPATH,value=r'//*[@id="tp-bought-root"]/div[{}]/div/table/tbody[2]/tr[1]/td[6]/div/p/span'.format(num))
                    #print("交易状态是：{}".format(jiaoyizhuangtai.text))
                    list_jyzt.append(jiaoyizhuangtai.text)
                except:
                    shangpinmiaoshu = i.find_element(by=By.XPATH,value=r'//*[@id="tp-bought-root"]/div[{}]/div/table/tbody[2]/tr[1]/td[1]/div/div[2]/p[1]/a[1]/span[2]'.format(num))
                    #print("商品描述是：{}".format(shangpinmiaoshu.text))
                    list_spms.append(shangpinmiaoshu.text)
                    goumaijiage = i.find_element(by=By.XPATH,value=r'//*[@id="tp-bought-root"]/div[{}]/div/table/tbody[2]/tr/td[5]/div/div[1]/p/strong/span[2]'.format(num))
                    #print("购买价格是：{}".format(goumaijiage.text))
                    list_gmjg.append(float(goumaijiage.text))
                    jiaoyizhuangtai = i.find_element(by=By.XPATH,value=r'//*[@id="tp-bought-root"]/div[{}]/div/table/tbody[2]/tr/td[6]/div/p/span'.format(num))
                    #print("交易状态是：{}".format(jiaoyizhuangtai.text))
                    list_jyzt.append(jiaoyizhuangtai.text)
                finally:
                    num += 1
        wbook = Workbook()
        wsheet = wbook.active
        flag = 0
        for i in range(len(list_gmsj)):
            if flag == 0:
                title= ['购买时间','订单号','商品描述','购买价格','交易状态']
                wsheet.append(title)
                hz = [list_gmsj[i], list_ddh[i], list_spms[i], list_gmjg[i], list_jyzt[i]]
                wsheet.append(hz)
                flag = 1
            else:
                hz = [list_gmsj[i],list_ddh[i],list_spms[i],list_gmjg[i],list_jyzt[i]]
                wsheet.append(hz)
        wbook.save('cyl.xlsx')
if __name__ == '__main__':
    unittest.main()