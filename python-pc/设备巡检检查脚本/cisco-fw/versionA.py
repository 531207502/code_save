import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result1 = re.search('failover cluster up (.*)', textcount[i])
        result2 = re.search('BJ-DC-CS-ASA5525-01 up (.*)',textcount[i])
        list1=[]
        if result1:
            num=i
            result2 = re.search('(\w)+ up(.*)',textcount[num-1])
            list1 = [filename, result1.group(1),result2.group(2)]
            writeexcel(list1)
            break
        elif result2:
            list1 = [filename, result2.group(1)]
            writeexcel(list1)
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/cisco-fw.xlsx')
    memory1=workbook['version1']
    memory1.append(li1)
    workbook.save('D:/xunjian/cisco-fw.xlsx')
