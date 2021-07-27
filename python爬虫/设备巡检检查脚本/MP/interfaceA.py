import re
import openpyxl
from time import sleep
def textcz(filename,textcount):
    for i in range(len(textcount)):
        if(re.search('(.*)show interface$',textcount[i])):
            numstart=i
            print(numstart)
            break
    for j in range(numstart+1,len(textcount)):
        if(re.search('(.*)#(show| show)',textcount[j])):
            break
        else:
            duankou=re.search('^(.*):$', textcount[j])
            list1 =[]
            if(duankou):
                dkname=duankou.group(1)
                result1=re.search('line protocol is (.*)',textcount[j+1])
                list1.append(filename)
                list1.append(dkname)
                list1.append('line protocol is')
                list1.append(result1.group(1))
                #print(list1)
            writeexcel(list1)
def writeexcel(li1):
    workbook=openpyxl.load_workbook('F:/cisco.xlsx')
    interface=workbook['interface1']
    interface.append(li1)
    workbook.save('F:/cisco.xlsx')