import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result=re.search('^(\s)+Used bytes (.*) Free bytes (.*) Total bytes (.*) Used percent',textcount[i])
        if result:
            result1=re.search('            (.*)        (.*)        (.*)        (.*)',textcount[i+2])
            list1 = [filename, result1.group(1), result1.group(2), result1.group(3),result1.group(4)]
            writeexcel3(list1)
            break
def writeexcel3(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/mp.xlsx')
    memory1=workbook['memory1']
    memory1.append(li1)
    workbook.save('D:/xunjian/mp.xlsx')