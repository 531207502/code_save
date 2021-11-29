import re
import openpyxl
from time import sleep
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result = re.search('(.*) total available \((.*) free\)', textcount[i])
        result1 = re.search('(.*) total \((.*) free\)',textcount[i])
        if result:
            list1 = [filename, result.group(1), result.group(2)]
            writeexcel(list1)
            break
        elif result1:
            list1 = [filename, result1.group(1), result1.group(2)]
            writeexcel(list1)
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/hw.xlsx')
    interface=workbook['dir1']
    interface.append(li1)
    workbook.save('D:/xunjian/hw.xlsx')