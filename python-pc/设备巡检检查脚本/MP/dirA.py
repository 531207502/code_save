import re
import openpyxl
from time import sleep
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result=re.search('total number of sectors:(\s)+(\d+),(\d+)',textcount[i])
        result1=re.search('- free space on volume:(\s)+(.*)',textcount[i])
        if result:
            result2=re.search('- bytes per sector:(\s)+(\d+)',textcount[i+1])
            list1 = [filename,int(result.group(2)+result.group(3))*int(result2.group(2))]
        elif(result1):
            list1.append(result1.group(2))
            writeexcel(list1)
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/mp.xlsx')
    interface=workbook['dir1']
    interface.append(li1)
    workbook.save('D:/xunjian/mp.xlsx')