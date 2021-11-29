import re
import openpyxl
def textcz(filename,textcount):
    list1=[]
    for i in range(len(textcount)):
        result=re.search('Free memory:   (.*)',textcount[i])
        result1=re.search('Total memory:  (.*)',textcount[i])
        if result:
            list1.append(filename)
            list1.append(result.group(1))
        elif result1:
            list1.append(result1.group(1))
            writeexcel1(list1)
            break
def writeexcel1(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/cisco-fw.xlsx')
    memory1=workbook['memory1']
    memory1.append(li1)
    workbook.save('D:/xunjian/cisco-fw.xlsx')