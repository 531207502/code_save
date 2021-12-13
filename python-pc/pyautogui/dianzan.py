import time
import pyautogui
import openpyxl
time.sleep(2)
pyautogui.PAUSE = 1
#获取对应图标在屏幕上的位置的大小，返回的是一个元组
a = pyautogui.locateOnScreen(r'C:\Users\Crystal\PycharmProjects\code_save\python-pc\pyautogui\weixin.png')
print(a)
x, y = pyautogui.center(a) # 获得文件图片在现在的屏幕上面的中心坐标
print(x,y)
pyautogui.doubleClick(x=x, y=y,button='left')
b = pyautogui.locateOnScreen(r'C:\Users\Crystal\PycharmProjects\code_save\python-pc\pyautogui\pyq.png')
x, y = pyautogui.center(b) # 获得文件图片在现在的屏幕上面的中心坐标
pyautogui.click(x=x, y=y,button='left')
width, height = pyautogui.size()
pyautogui.moveTo(width/2,height/2)
while True:
    pyautogui.scroll(-800)
    b = pyautogui.locateAllOnScreen(r'C:\Users\Crystal\PycharmProjects\code_save\python-pc\pyautogui\weixinmx.png')
    if b!=None:
        for pos in b:
            x, y = pyautogui.center(pos)
            pyautogui.click(x=x, y=y, button='left')