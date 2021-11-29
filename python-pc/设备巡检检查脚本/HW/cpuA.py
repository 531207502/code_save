import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)-1):
        result=re.search('>display cpu-usage',textcount[i])
        if result:
            num = i
            break
    recycle=1
    while(recycle):
        list1=[]
        result1=re.search('CPU Usage: (.*)   Max: (.*)',textcount[num])
        result5 = re.search('CPU Usage            : (.*) Max: (.*)', textcount[num])
        if result1:
            result2=re.search('CPU utilization for ten seconds: (.*)  one minute:  (.*)  five minutes:  (.*)',
                              textcount[num+2])
            list1.append(filename)
            list1.append(result2.group(1))
            list1.append(result2.group(2))
            list1.append(result2.group(3))
            list1.append(result1.group(2))
            writeexcel(list1)
            list1=[]
            result3 = re.search('CPU Usage:  (.*)   Max:  (.*) ', textcount[num + 4])
            result4 = re.search('CPU utilization for ten seconds: (.*)  one minute:  (.*)  five minutes:  (.*)',
                                textcount[num + 5])
            list1.append(filename)
            list1.append(result4.group(1))
            list1.append(result4.group(2))
            list1.append(result4.group(3))
            list1.append(result3.group(2))
            writeexcel(list1)
            break
        elif result5:
            list2 = []
            result6=re.search('CPU utilization for five seconds: (.*): one minute: (.*): five minutes: (.*)',textcount[num+2])
            list2.append(filename)
            list2.append(result6.group(1))
            list2.append(result6.group(2))
            list2.append(result6.group(3))
            list2.append(result5.group(2))
            writeexcel(list2)
            break
        num += 1
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/hw.xlsx')
    memory1=workbook['cpu1']
    memory1.append(li1)
    workbook.save('D:/xunjian/hw.xlsx')
