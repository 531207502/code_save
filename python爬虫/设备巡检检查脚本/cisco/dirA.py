import re
import openpyxl
from time import sleep
def textcz(filename,textcount):
    for i in range(len(textcount)):
        if(re.search('(.*)dir$',textcount[i])):
            numstart=i
            break
    for j in range(numstart+1,len(textcount)):
        if(re.search('(.*)#show',textcount[j])):
            break
        else:
            result=re.search('(.*) bytes total \((.*) bytes free\)', textcount[j])
            result1=re.search('Usage for bootflash:',textcount[j])
            if(result):
                list1 = [filename,result.group(1),result.group(2)]
                writeexcel(list1)
                break
            elif(result1):
                num=j
                result2=re.search('(.*) bytes used',textcount[num+1])
                result3=re.search('(.*) bytes free',textcount[num+2])
                result4=re.search('(.*) bytes total',textcount[num+3])
                list1=[filename,result4.group(1),result3.group(1)]
                writeexcel(list1)
                break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('F:/cisco.xlsx')
    interface=workbook['dir1']
    interface.append(li1)
    workbook.save('F:/cisco.xlsx')