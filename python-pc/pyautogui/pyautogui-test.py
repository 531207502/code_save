import pyautogui
width, height = pyautogui.size() # 屏幕的宽度和高度
print('屏幕的宽度为：{} 高度为：{}'.format(width, height))
currentMouseX, currentMouseY = pyautogui.position() # 鼠标当前位置
print('鼠标的位置为：{}，{}'.format(currentMouseX, currentMouseY))
for i in range(2):#操作鼠标移动，绝对坐标
  pyautogui.moveTo(100, 100, duration=0.25) # 移动到 (100,100)
  pyautogui.moveTo(300, 100, duration=0.25)
  pyautogui.moveTo(300, 300, duration=0.25)
  pyautogui.moveTo(100, 300, duration=0.25)
for i in range(2):#鼠标操作移动，相对坐标
  pyautogui.moveRel(50, 0, duration=0.25) # 从当前位置右移100像素
  pyautogui.moveRel(0, 50, duration=0.25) # 向下
  pyautogui.moveRel(-50, 0, duration=0.25) # 向左
  pyautogui.moveRel(0, -50, duration=0.25) # 向上
#以下常见的操作
#pyautogui.dragTo
#pyautogui.click
#pyautogui.doubleClick
#pyautogui.mouseDown
#pyautogui.mouseup
#pyautogui.scroll
#pyautogui.scroll
import pyautogui
import time

