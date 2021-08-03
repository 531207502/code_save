import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)-1):
        result=re.search('>display memory-usage',textcount[i])
        if result:
            num = i
            break
    result1=re.search('System Total Memory Is: (.*) bytes',textcount[num+2])
    result2 = re.search('Total Memory Used Is: (.*) bytes', textcount[num + 3])
    result3 = re.search('Memory Using Percentage Is: (.*)', textcount[num + 4])
    list1=[]
    list1.append(filename)
    list1.append(result1.group(1))
    list1.append(result2.group(1))
    list1.append(result3.group(1))
    writeexcel(list1)
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/hw.xlsx')
    memory1=workbook['memory1']
    memory1.append(li1)
    workbook.save('D:/xunjian/hw.xlsx')