import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result=re.search('uptime is (.*)',textcount[i])
        list1=[]
        if result!=None:
            list1=[filename,result.group(1)]
            writeexcel(list1)
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/h3c.xlsx')
    memory1=workbook['version1']
    memory1.append(li1)
    workbook.save('D:/xunjian/h3c.xlsx')
