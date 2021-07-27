import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)-1):
        result=re.search(']display cpu-usage',textcount[i])
        if result:
            num = i+1
            result1=re.search('Slot (.*) CPU',textcount[num])
            while(result1):
                result2=re.search('(.*)in last' , textcount[num + 1])
                result3 = re.search('(.*)in last',textcount[num + 2])
                result4 = re.search('(.*)in last', textcount[num + 3])
                list1=[filename,result2.group(1),result3.group(1),result4.group(1)]
                writeexcel(list1)
                num+=5
                result1=re.search('Slot (.*) CPU',textcount[num])
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('F:/h3c.xlsx')
    memory1=workbook['cpu1']
    memory1.append(li1)
    workbook.save('F:/h3c.xlsx')
