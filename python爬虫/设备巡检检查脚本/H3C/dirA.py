import re
import openpyxl
from time import sleep
def textcz(filename,textcount):
    for i in range(len(textcount)-1):
        result = re.search('(.*) KB total \((.*) KB free\)', textcount[i])
        if result:
            list1 = [filename, result.group(1), result.group(2)]
            writeexcel(list1)
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/h3c.xlsx')
    interface=workbook['dir1']
    interface.append(li1)
    workbook.save('D:/xunjian/h3c.xlsx')