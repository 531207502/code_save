import re
import openpyxl
from time import sleep
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result=re.search('(.*) bytes total \((.*) bytes free\)', textcount[i])
        if(result):
            list1 = [filename,result.group(1),result.group(2)]
            writeexcel(list1)
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/cisco-fw.xlsx')
    interface=workbook['dir1']
    interface.append(li1)
    workbook.save('D:/xunjian/cisco-fw.xlsx')