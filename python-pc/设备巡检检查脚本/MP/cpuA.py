import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result=re.search('CPU utilization for five seconds: (.*); one minute: (.*); five minutes: (.*)',textcount[i])
        if result:
            list1=[filename,result.group(1),result.group(2),result.group(3)]
            writeexcel(list1)
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/mp.xlsx')
    memory1=workbook['cpu1']
    memory1.append(li1)
    workbook.save('D:/xunjian/mp.xlsx')
