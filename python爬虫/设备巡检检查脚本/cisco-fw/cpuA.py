import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result=re.search('CPU utilization for 5 seconds = (.*); 1 minute: (.*); 5 minutes: (.*)',textcount[i])
        if result:
            list1=[filename,result.group(1),result.group(2),result.group(3)]
            writeexcel(list1)
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/cisco-fw.xlsx')
    memory1=workbook['cpu1']
    memory1.append(li1)
    workbook.save('D:/xunjian/cisco-fw.xlsx')
